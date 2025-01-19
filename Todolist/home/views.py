from django.http import HttpResponse
from django.shortcuts import render, redirect
from home.models import Tasklist
from django.utils.timezone import now

def home_view(request):
    tasklist = Tasklist.objects.all().values()
    context = {'alltasks': tasklist}
    return render(request, 'index.html', context)

def add_view(request):
    return render(request,'add.html')

def addrecord_view(request):
    if request.method == 'POST':
        title = request.POST.get ('task_title')
        start_date = request.POST.get ('start_date')
        finish_date = request.POST.get ('finish_date', default=now)
        if title and start_date and finish_date:
            Tasklist.objects.create(
                title = title,
                start_date = start_date,
                finish_date = finish_date
            )
        return redirect('home')
    return redirect('add')