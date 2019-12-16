from django.contrib.auth.decorators import login_required
from downtimeApp.decorators import employee_required, supervisor_required
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.utils import timezone
from django.db.models import Sum
from downtimeApp.serializers import DowntimeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

now = timezone.now()
@login_required
def home(request):
    if request.user.is_employee:
        return render(request, 'downtimeApp/employee_home.html')
    if request.user.is_supervisor:
        return render(request, 'downtimeApp/supervisor_home.html')
    return render(request, 'downtimeApp/home.html')





# Create your views here.
@login_required

def machine_list(request):
    machines = Machine.objects.filter()
    return render(request, 'downtimeApp/machine_list.html', {'machines': machines})

@login_required

def machine_new(request):
    if request.method == "POST":
        form = MachineForm(request.POST)
        if form.is_valid():
            machine = form.save(commit=False)
            machine.created_date = timezone.now()
            machine.save()
            machine = Machine.objects.filter()
            return render(request, 'downtimeApp/machine_list.html',
                          {'machines': machine})
    else:
        form = MachineForm()
    return render(request, 'downtimeApp/machine_new.html', {'form': form})


@login_required

def machine_edit(request, pk):
    machine = get_object_or_404(Machine, pk=pk)
    if request.method == "POST":
        # update
        form = MachineForm(request.POST, instance=machine)
        if form.is_valid():
            machine = form.save(commit=False)
            machine.updated_date = timezone.now()
            machine.save()
            machine = Machine.objects.filter()
            return render(request, 'downtimeApp/machine_list.html',
                          {'machines': machine})
    else:
        # edit
        form = MachineForm(instance=machine)
    return render(request, 'downtimeApp/machine_edit.html', {'form': form})

@login_required

def machine_delete(request, pk):
    machine = get_object_or_404(Machine, pk=pk)
    machine.delete()
    return redirect('downtimeApp:machine_list')

@login_required

def downtime_new(request):
    if request.method == "POST":
        form = DowntimeForm(request.POST)
        if form.is_valid():
            downtime = form.save(commit=False)
            downtime.created_date = timezone.now()
            downtime.save()
            downtime = Downtime.objects.filter()
            return render(request, 'downtimeApp/downtime_list.html',
                          {'downtimes': downtime})
    else:
        form = DowntimeForm()
    return render(request, 'downtimeApp/downtime_new.html', {'form': form})

@login_required

def downtime_edit(request, pk):
    downtime = get_object_or_404(Downtime, pk=pk)
    if request.method == "POST":
        # update
        form = DowntimeForm(request.POST, instance=downtime)
        if form.is_valid():
            downtime = form.save(commit=False)
            downtime.updated_date = timezone.now()
            downtime.save()
            downtime = Downtime.objects.filter()
            return render(request, 'downtimeApp/downtime_list.html',
                          {'downtimes': downtime})
    else:
        form = DowntimeForm(instance=downtime)
    return render(request, 'downtimeApp/downtime_edit.html', {'form': form})

@login_required
def downtime_list(request):
    downtime = Downtime.objects.filter()
    return render(request, 'downtimeApp/downtime_list.html', {'downtimes': downtime})


@login_required

def summary(request, pk):
    machine = get_object_or_404(Machine, pk=pk)
    machines = Machine.objects.filter(name=pk)
    downtimes = Downtime.objects.filter(machine=pk)
    sum_stoppageHours = Downtime.objects.filter(machine=pk).aggregate(Sum('stoppageHours'))
    return render(request, 'downtimeApp/summary.html', {'machines': machines,
                                                        'downtimes': downtimes,
                                                        'sum_stoppageHours': sum_stoppageHours})

class DwontimeList(APIView):
    def get(self,request):
        downtimes_json = Downtime.objects.all()
        serializer = DowntimeSerializer(downtimes_json, many=True)
        return Response(serializer.data)