from csv import DictReader
from time import sleep

from unipath import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import DataError

from vin_charts.models import Chassis, Engine, ModelYear, Transmission, Vehicle


VIN_CHART_DIR = Path(settings.BASE_DIR.parent, "data/vin_charts")


class Command(BaseCommand):

    help = "Import all vin charts in data/vin_charts/"

    def handle(self, *args, **options):
        for vin_chart in VIN_CHART_DIR.listdir():
            year = int(vin_chart.name[:vin_chart.name.find("csv") - 1])
            model_year, create = ModelYear.objects.get_or_create(year=year)

            with open(vin_chart) as open_file:
                reader = DictReader(open_file)

                for row in reader:
                    try:
                        chassis, created = Chassis.objects.get_or_create(
                            number=row["chassis"]
                        )
                        engine, created = Engine.objects.get_or_create(
                            number=row["engine"]
                        )
                        vehicle, created = Vehicle.objects.update_or_create(
                            vin_prefix=row["vin_prefix"], defaults={
                                "model_year": model_year,
                                "sales_designation": row["sales_designation"],
                                "chassis": chassis,
                                "engine": engine,
                            }
                        )

                        # add transmissions
                        for trans_number in row["transmission"].split("/"):
                            trans, c = Transmission.objects.get_or_create(
                                number=trans_number
                            )
                            vehicle.transmissions.add(trans)

                        self.stdout.write(
                            self.style.SUCCESS(
                                f"{year} {vehicle.sales_designation} added!"
                            )
                        )
                    except DataError:
                        self.stdout.write(
                            self.style.WARNING(
                                f"Problem with importing row: {row}"
                            )
                        )
                        sleep(5)
