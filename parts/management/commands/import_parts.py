from csv import DictReader

from unipath import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from parts.models import Part, Type
from vin_charts.models import Chassis, Engine, Transmission


PARTS_DIR = Path(settings.BASE_DIR.parent, "data/parts")


class Command(BaseCommand):

    help = "Import all parts in data/parts/"

    def handle(self, *args, **options):
        for part_file in PARTS_DIR.listdir():
            with open(part_file) as open_file:
                reader = DictReader(open_file)

                for row in reader:
                    type_obj, c = Type.objects.get_or_create(
                        description=row["type"]
                    )
                    part, c = Part.objects.get_or_create(
                        sku=row["sku"], defaults={"type": type_obj}
                    )

                    if row["chassis"]:
                        chassis, c = Chassis.objects.get_or_create(
                            number=row["chassis"]
                        )
                        parts.chassis.add(part)

                    if row["engine"]:
                        engine, c = Engine.objects.get_or_create(
                            number=row["engine"]
                        )
                        part.engines.add(engine)

                    if row["transmission"]:
                        transmission, c = Transmission.objects.get_or_create(
                            number=row["transmission"]
                        )
                        part.transmissions.add(transmission)
