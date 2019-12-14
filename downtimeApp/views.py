from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *

from django.utils import timezone

now = timezone.now()

def home(request):
   return render(request, 'downtimeApp/employee_home.html',
                 {'downtimeApp': home})

# Create your views here.
@login_required
def machine_list(request):
    machine = Machine.objects.filter()
    return render(request, 'downtimeApp/machine_list.html', {'machines': machine})

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
        # edit
       form = DowntimeForm(instance=downtime)

@login_required
def downtime_list(request):
    downtime = Downtime.objects.filter()
    return render(request, 'downtimeApp/downtime_list.html', {'downtimes': downtime})