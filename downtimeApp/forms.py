from django import forms
from .models import Machine, Downtime

class DowntimeForm(forms.ModelForm):
    class Meta:
        model = Downtime
        fields = ('id', 'machine', 'employee', 'stoppage', 'date', 'startTime', 'endTime',)


class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ('id', 'name', 'description', 'supervisor',)
