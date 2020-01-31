from django.shortcuts import render,reverse,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Book,Publication
from .forms import PublicationForm ,BookForm


def home_view(request):
	context={'name':'Sharad','age':'24','address':'Pyuthan',}
	book=Book.objects.all()
	publication=Publication.objects.all()


	return render(request,'home.html',{'booklist':book,'context':context,'publicationlist':publication})

def add_publication(request):
	form=PublicationForm(request.POST or None)
	# print(request.POST)
	if form.is_valid():
		form.save() #this is used to save or create data
		form=PublicationForm() #this will create empty instances(fields) after saving data
		# Publication.objects.create(**form.cleaned_data)
		# print(form.cleaned_data) #cleaned_data is built in in form

	return render(request,'form.html',{'form':form,'model_name':'Publication'})

def edit_publication(request,p_id):
	publication=get_object_or_404(Publication,pk=p_id)
	form=PublicationForm(request.POST or None,instance=publication)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('baseapp:home'))

	return render(request,'form.html',{'form':form,'model_name':'Publication'})


def add_book(request):

	form=BookForm(request.POST or None)
	if form.is_valid():
		form.save()
		# form=BookForm() it will redirect empty form 
		return HttpResponseRedirect(reverse('baseapp:home')) #it will redirect the home page

	return render(request,'form.html',{'form':form,'model_name':'Book'})


def edit_book(request,book_id):
	book=get_object_or_404(Book,pk=book_id)
	form=BookForm(request.POST or None,instance=book)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('baseapp:home'))
	return render(request,'form.html',{'form':form,'model_name':'Book'})
