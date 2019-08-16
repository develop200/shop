from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.core.paginator import Paginator

def handle_uploaded_file(f,s):
	s='catalog\\static\\catalog\\images\\'+s
	destination = open(s, 'wb+')
	for chunk in f.chunks():
		destination.write(chunk)
	destination.close()

class ObjectsMixin:
	model=None
	template='catalog/objs_list.html'
	is_computer=False
	is_phone=False
	searchcomp=False
	searchphone=False
	def get(self,request):
		search_query=request.GET.get('search','')
		if search_query:
			objs=self.model.objects.filter(title__icontains=search_query)
		else:
			objs=self.model.objects.all()
		context={}
		paginator=Paginator(objs,5)
		page_number=request.GET.get('page',1)
		page=paginator.get_page(page_number)
		is_paginated=page.has_other_pages()
		prev_url=''
		next_url=''
		if not search_query:
			if page.has_previous():
				prev_url='?page='+str(page.previous_page_number())
			if page.has_next():
				next_url='?page='+str(page.next_page_number())
		else:
			if page.has_previous():
				prev_url='?search='+search_query+'&page='+str(page.previous_page_number())
			if page.has_next():
				next_url='?search='+search_query+'&page='+str(page.next_page_number())
		context['page']=page
		context['is_computer']=self.is_computer
		context['is_phone']=self.is_phone
		context['searchcomp']=self.searchcomp
		context['searchphone']=self.searchphone
		context['is_paginated']=is_paginated
		context['prev_url']=prev_url
		context['next_url']=next_url
		context['search_query']=search_query
		return render(request,self.template, context)

class ObjectDetailMixin:
	model=None
	template='catalog/obj_detail.html'
	def get(self,request,slug):
		obj=get_object_or_404(self.model,slug__iexact=slug)
		return render(request,self.template,context={'obj':obj, 's':'/static/catalog/images/'+obj.title+'.png'})

class ObjectCreateMixin:
	form_model=None
	template='catalog/create_object.html'
	is_computer=False
	is_phone=False
	def get(self,request):
		form=self.form_model()
		c=form.model.__name__.lower()
		return render(request,self.template,context={'form':form, 'class':c, 'is_computer':self.is_computer, 'is_phone':self.is_phone})
	def post(self,request):
		bound_form=self.form_model(request.POST, request.FILES)
		if bound_form.is_valid():
			if request.FILES:
				s=str(bound_form.cleaned_data['title'])+'.png'
				handle_uploaded_file(request.FILES['file'],s)
			obj=bound_form.save()
			if self.is_computer:
				return redirect('computers_list',permanent=True)
			if self.is_phone:
				return redirect('phones_list',permanent=True)
		c=bound_form.model.__name__.lower()
		return render(request,self.template,context={'form':bound_form, 'class':c, 'is_computer':self.is_computer, 'is_phone':self.is_phone})

class ObjectUpdateMixin:
	form_model=None
	model=None
	template='catalog/update_object.html'
	is_computer=False
	is_phone=False
	def get(self,request,slug):
		obj=self.model.objects.get(slug__iexact=slug)
		data={'title':obj.title, 'cost':obj.cost, 'body':obj.body}
		form=self.form_model(data)
		obj.delete()
		return render(request,self.template,context={'form':form, 'slug':slug, 'is_computer':self.is_computer, 'is_phone':self.is_phone})
	def post(self,request,slug):
		bound_form=self.form_model(request.POST)
		if bound_form.is_valid():
			if request.FILES:
				s=str(bound_form.cleaned_data['title'])+'.png'
				handle_uploaded_file(request.FILES['file'],s)
			obj=bound_form.save()
			if self.is_computer:
				return redirect('computers_list',permanent=True)
			if self.is_phone:
				return redirect('phones_list',permanent=True)
		return render(request,self.template,context={'form':bound_form, 'slug':slug, 'is_computer':self.is_computer, 'is_phone':self.is_phone})

class ObjectDeleteMixin:
	model=None
	template='catalog/delete_object.html'
	is_computer=False
	is_phone=False
	def get(self,request,slug):
		obj=self.model.objects.get(slug__iexact=slug)
		return render(request,self.template,context={'is_computer':self.is_computer, 'is_phone':self.is_phone, 'obj':obj})
	def post(self,request,slug):
		obj=self.model.objects.get(slug__iexact=slug)
		obj.delete()
		if self.is_computer:
			return redirect('computers_list',permanent=True)
		if self.is_phone:
			return redirect('phones_list',permanent=True)