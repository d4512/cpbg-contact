from django.shortcuts import render_to_response
import mysql.connector
from models import *
from django.db.models import Q

def meta_keyword(request,):
	query = request.GET.get('q', '')
	if query:
		qset_company = (Q(company_description__icontains=query))
		results_company = Company2.objects.filter(qset_company).distinct()

		qset_person = (Q(person_for_position__position_name__icontains=query))
		results_person = Person5.objects.filter(qset_person).distinct()

		qset_address = (Q(road_address__icontains=query))
		results_address = Address3.objects.filter(qset_address).distinct()

		qset_position = (Q(position_name__icontains=query)
			|
				Q(address_of_position__road_address__icontains=query))
		results_position = Compos4.objects.filter(qset_position).distinct()
	else:
		results_company = []
		results_person = []
		results_address = []
		results_position = []
	return render_to_response("fuzzy.html",
		{
			"results_company": results_company,
			"results_person": results_person,
			"results_address": results_address,
			"results_position": results_position,
			"query": query
		})

def get_client_ip(request, ):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def feedback(request, ):
    query = request.GET.get('q', '')
    reason = request.GET.get('r', '')
    if query:
        cnx = mysql.connector.connect(user='cpbgit2', password='cpbgit2',
                                      host='10.40.3.123',
                                      database='cpbgit2')
        cursor = cnx.cursor()
        register_request = ("INSERT INTO fuzzyreq "
                            "(search_term, ip, reason)"
                            "VALUES (%s, %s, %s)")
        data_request = (query, get_client_ip(request), reason)
        cursor.execute(register_request, data_request)
        cnx.commit()
        cnx.close()
        dr = {'query': query, 'reason': reason}
        return render_to_response('feedback.html',
                                  {'data_request': dr,})
    else:
        return render_to_response('error.html', )
