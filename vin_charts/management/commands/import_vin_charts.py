from csv import DictReader
from time import sleep

from unipath import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import DataError

from vin_charts.models import (
    Chassis,
    Engine,
    ModelYear,
    Note,
    Transmission,
    Vehicle
)


VIN_CHART_DIR = Path(settings.BASE_DIR.parent, "data/vin_charts")


def split_note_from_value(data):
    start = data.find("(")
    if start >= 0:
        value = data[:start]
        message = data[start+1:-1]
        return value, message
    return data, None


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
                        # get Chassis
                        chassis_number, chassis_note = split_note_from_value(
                            row["chassis"]
                        )
                        chassis, created = Chassis.objects.get_or_create(
                            number=chassis_number
                        )
                        Note.create_from_import(chassis, chassis_note)

                        # get Engine
                        engine_number, engine_note = split_note_from_value(
                            row["engine"]
                        )
                        engine, created = Engine.objects.get_or_create(
                            number=engine_number
                        )
                        Note.create_from_import(engine, engine_note)

                        # get Vehicle
                        vin_prefix, vehicle_note = split_note_from_value(
                            row["vin_prefix"]
                        )

                        # format sales_designation
                        sales_designation = row["sales_designation"]
                        if "AMG" == sales_designation[:3]:
                            sales_designation = sales_designation[3:]
                            sales_designation = f"{sales_designation} AMG"
                        sales_designation = sales_designation.strip()

                        vehicle, created = Vehicle.objects.update_or_create(
                            vin_prefix=vin_prefix, defaults={
                                "model_year": model_year,
                                "sales_designation": sales_designation,
                                "chassis": chassis,
                                "engine": engine,
                            }
                        )
                        Note.create_from_import(vehicle, vehicle_note)

                        # add transmissions
                        for trans_number in row["transmission"].split("/"):
                            trans_number, trans_note = split_note_from_value(
                                trans_number
                            )
                            trans, c = Transmission.objects.get_or_create(
                                number=trans_number
                            )
                            vehicle.transmissions.add(trans)
                            Note.create_from_import(trans, trans_note)

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
