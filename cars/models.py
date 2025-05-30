from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField()
    model_year = models.IntegerField()
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField()
    photo = models.ImageField(upload_to='cars_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.factory_year})"
    
    