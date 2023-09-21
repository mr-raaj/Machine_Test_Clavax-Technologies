from django.shortcuts import *
from .models import Student ,Class
# Create your views here.
def home(Request):
    data = Student.objects.all()
    return render(Request,'index.html',{'data':data})

def register(Request):
    if(Request.method=="POST"):
        S = Student()
        S.first_name = Request.POST.get("first_name")
        S.last_name = Request.POST.get("last_name")
        S.phone = Request.POST.get("phone")
        S.email = Request.POST.get("email")
        S.status_choices = Request.POST.get("status_choices")
        S.date_of_birth = Request.POST.get("date_of_birth")
        S.image = Request.FILES.get("image")
        S.selected_class = Request.FILES.get("selected_class")
        S.save()
        return redirect("/")
    return render(Request,'register.html')