from django.contrib import admin
from .models import *

class Comcat1Admin(admin.ModelAdmin):
		list_display = ('cat_name', 'search_rank')
		ordering = ('-search_rank',)
		search_fields = ('cat_name',)
		
admin.site.register(Comcat1, Comcat1Admin)

class Edomain1Admin(admin.ModelAdmin):
	search_fields = ('domain_name',)

admin.site.register(Edomain1, Edomain1Admin)

class Stdcode1Admin(admin.ModelAdmin):
	search_fields = ('std_code','std_area')

admin.site.register(Stdcode1, Stdcode1Admin)

class Company2Admin(admin.ModelAdmin):
	list_display = ('company_name', 'domain_for_company')
	list_filter = ('company_categories',)
	search_fields = ('company_name', )

admin.site.register(Company2, Company2Admin)

class Address3Admin(admin.ModelAdmin):
	list_display = ('address_of_company', 'address_pin')
	list_filter = ('address_of_company',)
	search_fields = ('address_of_company',)
	
admin.site.register(Address3, Address3Admin)

class Compos4Admin(admin.ModelAdmin):
	list_display = ('id', 'position_of_company', 'position_name')
	list_filter = ('position_of_company',)
	search_fields = ('position_name',)

admin.site.register(Compos4, Compos4Admin)

class Landline5Admin(admin.ModelAdmin):
	list_display = ('landline_of_company', 'std_for_landline', 'landline_number', 'landline_for_position')
	list_filter = ('landline_of_company', 'is_landline_for_fax')

admin.site.register(Landline5, Landline5Admin)

class Person5Admin(admin.ModelAdmin):
	list_display = ('company_of_person', 'person_name', 'company_of_person')
	list_filter = ('company_of_person', 'person_for_position')
	search_fields = ('person_name',)

admin.site.register(Person5, Person5Admin)

class Mobile6Admin(admin.ModelAdmin):
	list_display = ('mobile_of_person', 'mobile_number')
	list_filter = ('mobile_of_person',)
	search_fields = ('mobile_of_person', 'mobile_number')

admin.site.register(Mobile6, Mobile6Admin)

class Email6Admin(admin.ModelAdmin):
	list_display = ('email_of_person', 'email_name', 'domain_of_email')
	list_filter = ('domain_of_email', 'email_of_position', 'email_of_person')
	search_fields = ('email_of_person', 'email_name')

admin.site.register(Email6, Email6Admin)
