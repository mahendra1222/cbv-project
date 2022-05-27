from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from cbvapp.models import Student

# Create your views here.


class studentlistview(ListView):
    model = Student
    # template name by default is Student_list.html
    # default dictionary context  name is Student_list
