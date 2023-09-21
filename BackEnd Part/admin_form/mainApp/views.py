from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import ClassDetailForm

def add_class(request):
    if request.method == 'POST':
        form = ClassDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_list')  # Redirect to a class list view
    else:
        form = ClassDetailForm()
    return render(request, 'add_clas.html', {'form': form})
