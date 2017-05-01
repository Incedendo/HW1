from django.db import models

# Create your models here.
class User(models.Model):

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

	first_name 		= models.CharField(max_length=30)
	middle_name 	= models.CharField(max_length=30, blank=True)
	last_name 		= models.CharField(max_length=30)
	organization 	= models.CharField(max_length=30)
	job_title 		= models.CharField(max_length=30, blank=True)
	street_address 	= models.CharField(max_length=30)
	city 			= models.CharField(max_length=30)
	state 			= models.CharField(max_length=2, choices=state_choices)
	zip 			= models.CharField(max_length=5)
	email 			= models.EmailField()
	work_phone 		= models.CharField(max_length=10)
	payment_method 	= models.CharField(max_length=30)
	card_number 	= models.CharField(max_length=16)
	expiration_MM 	= models.CharField(max_length=10)
	expiration_YY 	= models.CharField(max_length=4)

class Workshop(models.Model):
	first_name 			= models.CharField(max_length=30)
	middle_name 		= models.CharField(max_length=30)
	last_name 			= models.CharField(max_length=30)
	FridayWorkshop 		= models.CharField(max_length=30)
	SaturdayWorkshop 	= models.CharField(max_length=30)
