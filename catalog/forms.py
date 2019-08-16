from django import forms
from .models import *
from django.core.exceptions import ValidationError

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.png',]
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension. You need .png file.')

class UniversalForm(forms.Form):
	model=None
	title=forms.CharField(max_length=50)
	cost=forms.IntegerField()
	body=forms.CharField(max_length=5000, widget=forms.Textarea)
	file=forms.FileField(validators=[validate_file_extension,], required=False)
	title.widget.attrs.update({'class':'form-control'})
	cost.widget.attrs.update({'class':'form-control'})
	body.widget.attrs.update({'class':'form-control'})
	file.widget.attrs.update({'class':'form-control-file'})
	def save(self):
		obj=self.model.objects.create(title=self.cleaned_data['title'], cost=self.cleaned_data['cost'], body=self.cleaned_data['body'])
		return obj
	def clean_cost(self):
		s=self.cleaned_data['cost']
		if s<0:
			raise ValidationError('Цена не может быть отрицательной.')
		return s
class ComputerForm(UniversalForm):
	model=Computer
class PhoneForm(UniversalForm):
	model=Phone
