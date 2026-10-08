import csv

from django.core.management.base import BaseCommand

from waitlist.models import WaitlistEntry


class Command(BaseCommand):
    help = "Bulk import waitlist entries from a CSV with name,email columns."

    def add_arguments(self, parser):
        parser.add_argument("csv_path")

    def handle(self, *args, **options):
        created = skipped = 0
        with open(options["csv_path"], newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                email = (row.get("email") or "").strip().lower()
                name = (row.get("name") or "").strip()
                if not email:
                    continue
                _, was_created = WaitlistEntry.objects.get_or_create(
                    email=email, defaults={"name": name}
                )
                if was_created:
                    created += 1
                else:
                    skipped += 1
        self.stdout.write(self.style.SUCCESS(f"Added {created}, skipped {skipped} already on the list."))