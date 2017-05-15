from django.db import models

class Comcat1(models.Model):
	cat_name = models.CharField(max_length=100, unique=True)
	search_rank = models.IntegerField(default=0)
	
	def __str__(self):
		return self.cat_name

class Edomain1(models.Model):
	domain_name = models.CharField(max_length=25, unique=True)
	
	def __str__(self):
		return self.domain_name

class Stdcode1(models.Model):
	std_code = models.IntegerField(unique=True)
	std_area = models.CharField(max_length=100, blank=True, null=True)
	
	def __str__(self):
		return '%s : %s' % (self.std_code, self.std_area)

	class Admin:
		pass

class Company2(models.Model):
	company_name = models.CharField(max_length=100)
	company_categories = models.ManyToManyField(Comcat1)
	domain_for_company = models.ForeignKey(Edomain1, blank=True, null=True)
	company_description = models.TextField(blank=True, null=True)
	search_rank = models.IntegerField(default=0)
	
	def __str__(self):
		return self.company_name

class Address3(models.Model):
	address_of_company = models.ForeignKey(Company2)
	road_address = models.TextField(unique=True)
	address_pin = models.IntegerField(blank=True, null=True)
	
	def __str__(self):
		return '%s %s' % (self.road_address, self.address_pin)

class Compos4(models.Model):
	position_of_company = models.ForeignKey(Company2)
	position_name = models.CharField(max_length=100)
	address_of_position = models.ForeignKey(Address3, blank=True, null=True)
	
	def __str__(self):
		return self.position_name

class Landline5(models.Model):
	std_for_landline = models.ForeignKey(Stdcode1)
	landline_number = models.CharField(max_length=100)
	landline_of_company = models.ForeignKey(Company2)
	landline_for_position = models.ForeignKey(Compos4, blank=True, null=True)
	landline_in_address = models.ForeignKey(Address3)
	is_landline_for_fax = models.BooleanField()
	
	def __str__(self):
		return '%s - %s : STD - %s' %(self.landline_of_company, self.landline_number, self.std_for_landline)

class Person5(models.Model):
	person_name = models.CharField(max_length=100)
	person_for_position = models.ForeignKey(Compos4, blank=True, null=True)
	company_of_person = models.ForeignKey(Company2, blank=True, null=True)
	search_rank = models.IntegerField(default=0)
	
	def __str__(self):
		return self.person_name

class Mobile6(models.Model):
	mobile_number = models.CharField(max_length=40)
	mobile_of_person = models.ForeignKey(Person5)
	
	def __str__(self):
		return self.mobile_number

class Email6(models.Model):
	email_name = models.CharField(max_length=25)
	domain_of_email = models.ForeignKey(Edomain1)
	email_of_person = models.ForeignKey(Person5, blank=True, null=True)
	email_of_position = models.ForeignKey(Compos4, blank=True, null=True)
	
	def __str__(self):
		return '%s@%s' %(self.email_name, self.domain_of_email)
