from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .utils import *
from .forms import *
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def menu(request):
	return render(request,'catalog/home_page.html')

class ShowComputers(ObjectsMixin,View):
	model=Computer
	is_computer=True
	searchcomp=True
class ShowPhones(ObjectsMixin,View):
	model=Phone
	is_phone=True
	searchphone=True

class ShowComputer(ObjectDetailMixin,View):
	model=Computer
class ShowPhone(ObjectDetailMixin,View):
	model=Phone

class CreateComputer(LoginRequiredMixin,ObjectCreateMixin,View):
	is_computer=True
	form_model=ComputerForm
class CreatePhone(LoginRequiredMixin,ObjectCreateMixin,View):
	is_phone=True
	form_model=PhoneForm

class UpdateComputer(LoginRequiredMixin,ObjectUpdateMixin,View):
	is_computer=True
	form_model=ComputerForm
	model=Computer
class UpdatePhone(LoginRequiredMixin,ObjectUpdateMixin,View):
	is_phone=True
	form_model=PhoneForm
	model=Phone

class DeleteComputer(LoginRequiredMixin,ObjectDeleteMixin,View):
	is_computer=True
	model=Computer
class DeletePhone(LoginRequiredMixin,ObjectDeleteMixin,View):
	is_phone=True
	model=Phone
