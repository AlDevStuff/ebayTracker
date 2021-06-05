from django.core.management import BaseCommand
from base.models import Item

class Command(BaseCommand):
    help = 'Fetches the data from the Ebay URL'


    def handle(self, *args, **options):
        qs = Item.objects.all()
        for link in qs:
         link.save()

        print('Running cronjob updatingData')