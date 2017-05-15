from django.shortcuts import render_to_response, redirect
from models import *
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request, ):
	cats = Comcat1.objects.all().order_by('-search_rank')[:3]
	coms = Company2.objects.all().order_by('-search_rank')[:3]
	pers = Person5.objects.all().order_by('-search_rank')[:3]
	return render_to_response('index.html',
		{
			"categories" : cats,
			"companies" : coms,
			"persons" : pers
		})

def search_company(request,):
	query = request.GET.get('q', '')
	if query:
		qset = (Q(company_name__icontains=query))
		results = Company2.objects.filter(qset).distinct()
	else:
		results = []
	return render_to_response("search-company.html",
		{
			"results": results,
			"query": query
		})

def search_person(request,):
	query = request.GET.get('q', '')
	if query:
		qset = (Q(person_name__icontains=query))
		results = Person5.objects.filter(qset).distinct()
	else:
		results = []
	return render_to_response("search-person.html",
		{
			"results": results,
			"query": query
		})

def search_PIN(request,):
	query = request.GET.get('q', '')
	if query:
		qset = (Q(address_pin__icontains=query))
		results = Address3.objects.filter(qset).distinct()
	else:
		results = []
	return render_to_response("search-PIN.html",
		{
			"results": results,
			"query": query
		})

def search_mobile(request,):
	query = request.GET.get('q', '')
	if query:
		qset = (Q(mobile_number__icontains=query))
		results = Mobile6.objects.filter(qset).distinct()
	else:
		results = []
	return render_to_response("search-mobile.html",
		{
			"results": results,
			"query": query
		})
	
def search_STD(request,):
	query = request.GET.get('q', '')
	if query:
		qset = (Q(std_code__icontains=query))
		s = Stdcode1.objects.filter(qset).distinct()
		results = Landline5.objects.filter(std_for_landline = s).distinct().order_by('landline_of_company')
	else:
		results = []
	return render_to_response("search-STD.html",
		{
			"results": results,
			"query": query
		})	

def categories(request,):
	cats = Comcat1.objects.all().order_by('-search_rank')
	return render_to_response('categories.html',
		{
			"categories": cats
		})

def emails(request,):
	emails = Email6.objects.all().order_by('domain_of_email', 'email_name')
	return render_to_response('emails.html',
		{
			"emails" : emails
		})

def category(request,num):
	cat = Comcat1.objects.filter(id=num)
	if cat:
		cat[0].search_rank = cat[0].search_rank + 1
		cat[0].save()
		comps = Company2.objects.filter(company_categories = cat)
		return render_to_response('category.html',
			{
				"companies": comps,
				"category":Comcat1.objects.get(id=num)
			})
	else:
		return render_to_response('error.html',)

def companies(request,):
	coms = Company2.objects.all().order_by('company_name')
	paginator = Paginator(coms, 5)
	page = request.GET.get('page')
	try:
		companies = paginator.page(page)
	except PageNotAnInteger:
		companies = paginator.page(1)
	except EmptyPage:
		companies = paginator.page(paginator.num_pages)
	return render_to_response( 'companies.html',
		{
			"page" : page,
			"companies": companies
		})

def company(request,num):
	com = Company2.objects.filter(id=num)
	if com:
		company = Company2.objects.get(id=num)
		company.search_rank = company.search_rank + 1
		company.save()
		cats = Comcat1.objects.filter(company2__id=num)
		addresses = Address3.objects.filter(address_of_company=company)
		positions = Compos4.objects.filter(position_of_company=company)
		persons = Person5.objects.filter(company_of_person=company)
		return render_to_response('company.html',
			{
				"company" : company,
				"categories": cats,
				"addresses" : addresses,
				"positions" : positions,
				"persons" : persons
			})
	else:
		return render_to_response('error.html',)

def position(request,num):
	pos = Compos4.objects.filter(id=num)
	if pos:
		position = Compos4.objects.get(id=num)
		landlines = Landline5.objects.filter(landline_for_position=pos)
		persons = Person5.objects.filter(person_for_position=pos)
		emails = Email6.objects.filter(email_of_position=pos)
		return render_to_response('position.html',
			{
				"position" : position,
				"landlines" : landlines,
				"persons" : persons,
				"emails" : emails
			})
	else:
		return render_to_response('error.html',)

def person(request,num):
	p = Person5.objects.filter(id=num)
	if p:
		person = Person5.objects.get(id=num)
		person.search_rank = person.search_rank + 1
		person.save()
		mobiles = Mobile6.objects.filter(mobile_of_person=person)
		emails = Email6.objects.filter(email_of_person=person)
		return render_to_response('person.html',
			{
				"person" : person,
				"mobiles" : mobiles,
				"emails" : emails
			})
	else:
		return render_to_response('error.html',)

def address(request,num):
	a = Address3.objects.filter(id=num)
	if a:
		address = Address3.objects.get(id=num)
		pos = Compos4.objects.filter(address_of_position=address)
		landlines = Landline5.objects.filter(landline_in_address=address)
		return render_to_response('address.html',
			{
				"address" : address,
				"positions": pos,
				"landlines" : landlines
			})
	else:
		return render_to_response('error.html',)

def alternate(request,):
	cats = Comcat1.objects.all()
	coms_all = Company2.objects.all().order_by('-search_rank')
	coms = coms_all[:10]
	pers_all = Person5.objects.all().order_by('-search_rank')
	pers = pers_all[:10]	
	return render_to_response('alternate.html',
		{
			"categories": cats,
			"top_10_companies": coms,
			"number_of_companies": coms_all.count,
			"top_10_persons": pers,
			"number_of_persons": pers_all.count
		})

def landing(request,):
	return render_to_response('landing-page.html',)
