from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import DeleteView
from .models import Widget
from .forms import WidgetForm

# Create your views here.

def home(request):
    widgets = Widget.objects.all()
    w_form = WidgetForm()
    return render(request, 'index.html', { 'widgets': widgets, 'w_form': w_form })

def add_widget(request):
    if request.method == 'POST':
        w_form = WidgetForm(request.POST)
        if w_form.is_valid():
            new_widget = w_form.save()
            return redirect('home')

class WidgetDelete(DeleteView):
    model = Widget
    success_url = '/'
