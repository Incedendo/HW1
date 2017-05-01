from django import forms

class RegistrationForm(forms.Form):

	# State
	Alabama ="AL"
	Alaska ="AK"
	Arizona ="AZ"
	Arkansas ="AR"
	California ="CA"
	Colorado ="CO"
	Connecticut ="CT"
	Delaware ="DE"
	DistrictOfColumbia ="DC"
	Florida ="FL"
	Georgia ="GA"
	Hawaii ="HI"
	Idaho ="ID"
	Illinois ="IL"
	Indiana= "IN"
	Iowa ="IA"
	Kansas ="KS"
	Kentucky ="KY"
	Louisiana ="LA"
	Maine ="ME"
	Maryland ="MD"
	Massachusetts ="MA"
	Michigan ="MI"
	Mississippi ="MS"
	Missouri ="MO"
	Montana ="MT"
	Nebraska ="NE"
	Nevada ="NV"
	New_Hampshire ="NH"
	New_Jersey ="NJ"
	New_Mexico ="NM"
	New_York ="NY"
	North_Carolina ="NC"
	North_Dakota ="ND"
	Ohio ="OH"
	Oklahoma ="OK"
	Oregon ="OR"
	Pennsylvania ="PA"
	Rhode_Island ="RI"
	South_Carolina ="SC"
	South_Dakota ="SD"
	Tennessee ="TN"
	Texas ="TX"
	Utah ="UT"
	Vermont ="VT"
	Virginia ="VA"
	Washington ="WA"
	West_Virginia ="WV"
	Wisconsin ="WI"
	Wyoming ="WY"

	state_choices=(
    	(Alabama ,"AL"  ),
    	(Alaska ,"AK" ),
    	(Arizona ,"AZ" ),
	    (Arkansas ,"AR" ),
	    (California ,"CA" ),
	    (Colorado ,"CO" ),
	    (Connecticut ,"CT" ),
	    (Delaware ,"DE" ),
	    (DistrictOfColumbia ,"DC" ),
	    (Florida ,"FL" ),
	    (Georgia ,"GA" ),
	    (Hawaii ,"HI" ),
	    (Idaho ,"ID" ),
	    (Illinois ,"IL"  ),
	    (Indiana ,"IN" ),
	    (Iowa ,"IA" ),
	    (Kansas ,"KS" ),
	    (Kentucky ,"KY" ),
	    (Louisiana ,"LA" ),
	    (Maine ,"ME" ),
	    (Maryland ,"MD" ),
	    (Massachusetts ,"MA" ),
	    (Michigan ,"MI" ),
	    (Mississippi ,"MS" ),
	    (Missouri ,"MO" ),
	    (Montana ,"MT" ),
	    (Nebraska ,"NE" ),
	    (Nevada ,"NV" ),
	    (New_Hampshire ,"NH" ),
	    (New_Jersey ,"NJ" ),
	    (New_Mexico ,"NM" ),
	    (New_York ,"NY" ),
	    (North_Carolina ,"NC" ),
	    (North_Dakota ,"ND" ),
	    (Ohio ,"OH" ),
	    (Oklahoma ,"OK" ),
	    (Oregon ,"OR" ),
	    (Pennsylvania ,"PA" ),
	    (Rhode_Island ,"RI" ),
	    (South_Carolina ,"SC" ),
	    (South_Dakota ,"SD" ),
	    (Tennessee ,"TN" ),
	    (Texas ,"TX" ),
	    (Utah ,"UT" ),
	    (Vermont ,"VT" ),
	    (Virginia ,"VA" ),
	    (Washington ,"WA" ),
	    (West_Virginia ,"WV"),
	    (Wisconsin ,"WI" ),
	    (Wyoming ,"WY" )
    )

	# Month
	January 	= 'January'
	February	= 'February'
	March   	= 'March'
	April   	= 'April'
	May 		= 'May'
	June 		= 'June'
	July 		= 'July'
	August 		= 'August'
	September	= 'September'
	October 	= 'October'
	November	= 'November'
	December	= 'December'

	month_choices = (
		(January,'January'),
		(February,'February'),
		(March ,'March'),
		(April,'April'),
		(May,'May'),
		(June,'June'),
		(July ,'July'),
		(August ,'August'),
		(September,'September'),
		(October,'October'),
		(November,'November'),
		(December,'December')
	)

	#Card 
	MasterCard= "Master Card"
	Visa="Visa"
	Discover= "Discover"

	card_choices = (
		(MasterCard, "Master Card"),
		(Visa, "Visa"),
		(Discover, "Discover")
	)

	#Registration Fee
	mem = "Member"
	non_mem = "Non Member"
	stu = "Student"
	non_mem_stu = "Non-member Student"

	reg_choices = (
		(mem, "Member"),
		(non_mem, "Non Member"),
		(stu, "Student"),
		(non_mem_stu, "Non-member Student")
	)

	#Friday Courses
	fri_first = "C# and .NET: $100"
	fri_second = "Issues in wireless security: $75"
	fri_third = "Scenario-based Requirement Engineering: $50"

	fri_choices = (
		(fri_first,"C# and .NET: $100"),
		(fri_second,"Issues in wireless security: $75"),
		(fri_third,"Scenario-based Requirement Engineering: $50")
	)

	#Saturday Courses
	sat_first = "Algorithms to Applications: $50"
	sat_second = "Cloud Computing: $75"

	sat_choices = (
		(sat_first, "Algorithms to Applications: $50"),
		(sat_second, "Cloud Computing: $75")
	)

   	#User Information
	firstName = forms.CharField(max_length=30)
	middleName = forms.CharField(max_length=30, required=False)
	lastName = forms.CharField(max_length=30)
	organization = forms.CharField(max_length=30)
	job_title = forms.CharField(max_length=30, required=False)
	street_address = forms.CharField(max_length=30)
	city = forms.CharField(max_length=30)
	state = forms.ChoiceField(choices=state_choices)
	zip = forms.CharField(max_length=5)
	email = forms.EmailField()
	work_phone = forms.CharField(max_length=10)

	# RADIO SELECT
	reg = forms.ChoiceField(choices=reg_choices, widget=forms.RadioSelect())
	friday = forms.ChoiceField(choices=fri_choices, widget=forms.RadioSelect())
	saturday = forms.ChoiceField(choices=sat_choices, widget=forms.RadioSelect())
	
	#Payment Information
	payment_method = forms.ChoiceField(choices=card_choices)
	card_number = forms.CharField(max_length=16)
	expiration_MM = forms.ChoiceField(choices=month_choices)
	expiration_YY = forms.ChoiceField(choices=[(x, x) for x in range(2017, 2023)])


	def clean_zip(self):
		zip = self.cleaned_data['zip']
		if(len(zip) != 5):
			raise forms.ValidationError("Enter valid 5-digit ZIP ")
		return zip

	def clean_work_phone(self):
		work_phone = self.cleaned_data['work_phone']
		if(len(work_phone) != 10):
			raise forms.ValidationError("Enter valid 10-digit phone number")
		return work_phone

	def clean_card_number(self):
		card_number = self.cleaned_data['card_number']
		if(len(card_number) != 16):
			raise forms.ValidationError("Enter valid 16-digit Credit Card Number")
		return card_number