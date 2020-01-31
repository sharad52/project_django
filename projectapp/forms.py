from django import forms
from .models import Publication,Book

# class PublicationForm(forms.Form):
# 	name=forms.CharField()
# 	contact=forms.CharField()
# 	address=forms.CharField()

#if foreign_key is available we need dropdown so we need choice fields 
''' so defining form be like
class BookForm(forms.Form):
	name=forms.CharField()
	publication=forms.ModelChoiceField(queryset=Publication.objects.all())

'''
class PublicationForm(forms.ModelForm):
	class Meta:
		model= Publication
		fields=('name','contact','address',)

class BookForm(forms.ModelForm):
	class Meta:
		model=Book
		#fields='__all__'
		exclude=('created','updated',)