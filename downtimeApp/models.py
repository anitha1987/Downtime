from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

stoppage = (
    ('OilChange', 'OilChange'),
    ('BreakDown', 'BreakDown '),
    ('ProcessChange', 'ProcessChange'),
    ('Washing', 'Washing'),
    ('LightChange', 'LightChange'),
    ('PlannedStoppage', 'PlannedStoppage'),
    ('ElectricalFailure', 'ElectricalFailure'),
)


class User(AbstractUser):
    @property
    def is_supervisor(self):
        if hasattr(self, 'supervisor'):
            return True
        return False

    @property
    def is_employee(self):
        if hasattr(self, 'employee'):
            return True
        return False



class Supervisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name

class Machine(models.Model):
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    id = models.CharField(primary_key='True', max_length=100)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank='True')

    def __str__(self):
        return self.name

class Downtime(models.Model):
    id = models.CharField(primary_key='True', max_length=100)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    stoppage = models.CharField(max_length=50, choices=stoppage, blank=False)
    date = models.DateField(db_index=True)
    startTime = models.TimeField()
    endTime = models.TimeField(blank=False)

    def __str__(self):
        return "Stoppage on %s by %s for %s" % (self.date, self.employee, self.stoppage)