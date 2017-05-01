from django import template

#Django template custom math filters
#Ref : https://code.djangoproject.com/ticket/361
register = template.Library()

def add3(value, arg1, arg2):
	return int(value) + int(arg1) + int(arg2)

register.filter('add3', add3)
