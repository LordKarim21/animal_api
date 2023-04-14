from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(blank=True)
    weight = models.IntegerField(blank=True)
    height = models.IntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    omens = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    def add_animal(self, name: str, age: int, weight: int, height: int, omens: str = ' '):
        Animal.objects.create(name=name, age=age, weight=weight, height=height, omens=omens)

    def delete_animal(self, id):
        Animal.objects.delete(id)
