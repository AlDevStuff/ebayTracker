from .models import Item

def updatingData():
    qs = Item.objects.all()
    for link in qs:
        link.save()

    print('Running cronjob updatingData')
