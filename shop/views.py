from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.
def redirect_to_catalog(request):
	return redirect('product_menu',permanent=True)