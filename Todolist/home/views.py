from django.http import HttpResponse
from django.shortcuts import render, redirect
from home.models import Tasklist
from django.utils.timezone import now
from django.utils.dateparse import parse_datetime  # This imports Django's tool for understanding dates

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
            try:  # This is like saying "try to do this, but if it fails, don't crash"
            # Convert the dates to a format Django understands
            # The form sends dates like "2024-01-19T10:00"
            # We replace 'T' with space to make "2024-01-19 10:00"
                start_datetime = parse_datetime(start_date.replace('T', ' '))
                finish_datetime = parse_datetime(finish_date.replace('T', ' '))
            
            # Create new task in database with the converted dates
                Tasklist.objects.create(
                title=title,
                start_date=start_datetime,
                finish_date=finish_datetime
                )
            except Exception as e:  # If anything goes wrong...
                print(f"Error: {e}")  # ...print the error (helps with debugging)
        return redirect('home')
    return redirect('add')