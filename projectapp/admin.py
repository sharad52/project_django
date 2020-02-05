from django.contrib import admin
from .models import Book
from .models import Student
from .models import Publication


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display=('title','author','price',)
	list_filter=('author','price',)
	search_fields=('title','author',)


@admin.register(Student)
class hello(admin.ModelAdmin):
	list_display=('name','address',)

@admin.register(Publication)
class pubadmin(admin.ModelAdmin):
	list_display=('name','address','active','slug',)
	search_fields=('name','address')
	list_editable=('active',)

# Register your models here.
