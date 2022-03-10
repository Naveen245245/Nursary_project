from django.db.models.signals import post_save
from . models import Nursary, Bed


def create_beds(sender, instance, created, **kwargs):
    print("**************** in post signal create bed")
    l = []
    rows = instance.rows
    cols = instance.columns
    name = instance.name
    if created == True:
        for i in range(rows):
            for j in range(cols):
                print(instance.name)
                l.append(Bed(nursary=instance))
        # print(l)
        Bed.objects.bulk_create(l)


post_save.connect(create_beds, sender=Nursary)
