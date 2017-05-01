from django.shortcuts import render
from srs.forms import RegistrationForm
from django.http import HttpResponseRedirect
# for what?
from srs.models import User,Workshop

# Create your views here.
def startup(request):
	return render(request, "startup.html")

# def form(request):
# 	return render(request, "conferenceDetail.html")

def thank(request):
	return render(request, "thank.html")

def contact(request):
	# errors = []
	# if "first_name" in request.POST:
	# 	first_name = request.POST["first_name"]
	# 	if not first_name:
	# 		errors.append('Enter first name!')
	# if "middle_name" in request.POST:
	# 	middle_name = request.POST["middle_name"]
	# 	if not middle_name:
	# 		errors.append('Enter middle_name!')
	# if "last_name" in request.POST:
	# 	last_name = request.POST["last_name"]
	# 	if not last_name:
	# 		errors.append('Enter last_name!')
	
	# return render(request,'conferenceDetail.html',{'errors': errors})

	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			
			user = User(
				#User Information
				first_name =data['firstName'], 
				middle_name=data['middleName'], 
				last_name=data['lastName'],
				organization=data['organization'],
				job_title=data['job_title'],
				street_address=data['street_address'],
				city=data['city'],
				state=data['state'],
				zip=data['zip'],
				email=data['email'],
				work_phone=data['work_phone'],

				#Payment Information
				payment_method=data['payment_method'],
				card_number=data['card_number'],
				expiration_MM=data['expiration_MM'],
				expiration_YY=data['expiration_YY'])
			user.save()

			# workshop = Workshop(first_name =data['firstName'], 
			# 					middle_name=data['middleName'], 
			# 					last_name=data['lastName'],
			# 					FridayWorkshop=data['lastName'],
			# 					SaturdayWorkshop=data['lastName'])
			# workshop.save()
			
			return HttpResponseRedirect('/registration/thanks/')


		# else:
		# 	return HttpResponseRedirect('/registration/thanks/')
	else:
		form = RegistrationForm()
	return render(request,'conferenceDetail.html',{'form':form})

