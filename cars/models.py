from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=25)
    company = models.CharField(max_length=20)
    model = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def details(self):
        return self.name