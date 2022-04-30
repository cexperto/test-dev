from django.db import models
from datetime import date
import math
# Create your models here.


class VehicleType(models.Model):
    name = models.CharField(max_length=32)
    max_capacity = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name


class Vehicle(models.Model):
    name = models.CharField(max_length=32)
    passengers = models.PositiveIntegerField()
    vehicle_type = models.ForeignKey(VehicleType, null=True, on_delete=models.SET_NULL)
    number_plate = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name

    def can_start(self) -> bool:
        return self.vehicle_type.max_capacity >= self.passengers

    def get_distribution(self):
        passengers = self.passengers
        matriz = []
        columns = 2        
        stop = math.ceil(passengers/2)        
        counter = 0
        for i in range(stop):
            matriz.append([])
            counter += 1
            for j in range(columns):
                matriz[i].append(True)                
                if j == 1 and counter == stop:
                    matriz[i][j] = False              
                                                
        return matriz

class Journey(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT)
    start = models.DateField()
    end = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.vehicle.name} ({self.start} - {self.end})"

    def is_finished(self):
        end = self.end
        if date.today() == end:
            return True
        else:
            return False

def validate_number_plate(number_plate):
    size = len(number_plate)
    if size !=8: return False
    if number_plate[0:2].isalpha() and number_plate[2] == '-' and number_plate[3:5].isdigit() and number_plate[5] == '-' and number_plate[6:8].isdigit():
        return True
    else:
        return False