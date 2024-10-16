from django.db.models import *
from random import randint


def random_section_color():
    return randint(0, 359)

class Section(Model):
    title = CharField(max_length=50)
    color = SmallIntegerField(default=random_section_color, blank=True)
   

# class History(Model):
# 