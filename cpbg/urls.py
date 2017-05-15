from django.conf.urls import url
from . import views, fuzzy

urlpatterns = [url(r'^$', views.index, name='index'),
	url(r'^categories/$', views.categories, name='categories'),
	url(r'^category/(?P<num>\d+)/$', views.category, name='category'),
	url(r'^companies/$', views.companies, name='companies'),
	url(r'^company/(?P<num>\d+)/$', views.company, name='company'),
	url(r'^position/(?P<num>\d+)/$', views.position, name='position'),
	url(r'^person/(?P<num>\d+)/$', views.person, name='person'),
    url(r'^address/(?P<num>\d+)/$', views.address, name='address'),
    url(r'^search-company/$', views.search_company, name='search_company'),
    url(r'^search-person/$', views.search_person, name='search_person'),
    url(r'^search-STD/$', views.search_STD, name='search_STD'),
    url(r'^search-PIN/$', views.search_PIN, name='search_PIN'),
    url(r'^search-mobile/$', views.search_mobile, name='search_mobile'),
    url(r'^emails/$', views.emails, name='emails'),
    url(r'^alternate/$', views.alternate, name='alternate'),
    url(r'^fuzzy/$', fuzzy.meta_keyword, name='fuzzy'),
    url(r'^fuzzy-feedback/$', fuzzy.feedback, name='fuzzy_feedback'),
    url(r'^landingpage/$', views.landing, name='landing'),
]
