from ..models import *
import re

'''
import cpbg.static.pdf as p
p.gen()
'''

def start(f):
	f.write("\documentclass[a4paper, 11pt, twoside]{book}\n")
	f.write("\\title{CPBG Contacts}\n")
	f.write("\\author{Jul-2016 to Dec-2016}\n")
	f.write("\usepackage{hyperref}\n")
	f.write("\hypersetup{\n")
	f.write("colorlinks = true, % Colours links instead of ugly boxes\n")
	f.write("urlcolor = blue, % Colour for external hyperlinks\n")
	f.write("linkcolor = blue, % Colour of internal links\n")
	f.write("citecolor = red % Colour of citations\n")
	f.write("}\n")
	f.write("\\begin{document}\n")
	f.write("\maketitle\n")
	f.write("\\tableofcontents\n")
	
def san(s):
	t = re.sub('&', '\&', s)
	u = re.sub('#', '\#', t)
	v = re.sub('_', '\_', u)
	return v
	
def cats(f):
	f.write("\chapter{Categories}\n")
	cats = Comcat1.objects.all()
	if cats:
		f.write("\\begin{tabular}{|c|l|}\n")
		f.write("\hline\n")
		for cat in cats:
			f.write("\\ref{cat:%d} & {%s} \\\ \hline\n" % (cat.id, san(cat.cat_name), ))
		f.write("\end{tabular}\n")
	
def cat(f):
	f.write("\chapter{Companies under Category}\n")
	cats = Comcat1.objects.all()
	if cats:
		for cat in cats:
			f.write("\section{%s}\label{cat:%d}\n" % (san(cat.cat_name), cat.id))
			coms = Company2.objects.filter(company_categories = cat)
			if coms:
				f.write("\\begin{tabular}{|c|l|}\n")
				f.write("\hline\n")
				for com in coms:
					f.write("\\ref{com:%d} & %s \\\ \hline\n" % (com.id, san(com.company_name)))
				f.write("\end{tabular}\n")
			
def com(f):
	f.write("\chapter{Company Details}\n")
	coms = Company2.objects.all().order_by('company_name')
	if coms:
		for com in coms:
			f.write("\section{%s}\label{com:%d}\n" % (san(com.company_name), com.id))
			f.write("\\begin{description}\n")
			f.write("\item[Domain]%s\n" % (com.domain_for_company,))
			f.write("\end{description}\n")
			com_adds = Address3.objects.filter(address_of_company = com)
			f.write("\subsection*{Postal Address(s)}\n")
			if com_adds:
				for com_add in com_adds:
					address = "%s" % (com_add,)
					f.write("\\begin{description}\n")
					f.write("\item [%d]%s\n" % (com_add.id, san(address)))
					f.write("\end{description}\n")
					add_poss = Compos4.objects.filter(address_of_position = com_add)
					if add_poss:
						f.write("\\begin{tabular}{|p{4cm}|p{2cm}|p{2cm}|p{3cm}|}\n")
						f.write("\hline\n")
						for add_pos in add_poss:
							f.write("%s" % (san(add_pos.position_name), ))
							add_pos_per = Person5.objects.filter(person_for_position = add_pos)
							if add_pos_per:
								f.write(" & %s" % (san(add_pos_per[0].person_name),))
								mob = Mobile6 .objects.filter(mobile_of_person = add_pos_per[0])
								if mob:
									f.write(" & %s" % (mob[0],))
								else:
									f.write(" & ")
								email_ids = Email6.objects.filter(email_of_person = add_pos_per[0])
								if email_ids:
									email_id = "%s" % (email_ids[0].email_name,)
									f.write(" & %s" % (san(email_id),))
								else:
									f.write(" & ")
							else:
								f.write(" & & & ")
							f.write(" \\\ \hline\n")
						f.write("\end{tabular}\n")						
				
def finish(f):
	f.write("\end{document}\n")
	
def gen():
	f = open('cpbg/static/data.tex', 'w')
	start(f)
	cats(f)
	cat(f)
	com(f)
	finish(f)
	f.close()

'''
exit()
'''
