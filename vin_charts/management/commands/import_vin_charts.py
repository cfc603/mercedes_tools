from csv import DictReader

from unipath import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

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
                    chassis, created = Chassis.objects.get_or_create(
                        number=row["chassis"]
                    )
                    engine, created = Engine.objects.get_or_create(
                        number=row["engine"]
                    )
                    transmission, created = Transmission.objects.get_or_create(
                        number=row["transmission"]
                    )
                    Vehicle.objects.update_or_create(
                        vin_prefix=row["vin_prefix"], defaults={
                            "model_year": model_year,
                            "sales_designation": row["sales_designation"],
                            "chassis": chassis,
                            "engine": engine,
                            "transmission": transmission,
                        }
                    )
