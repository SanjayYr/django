from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
	html_var = 'f strings'
	html_ = f"""<!DOCTYPE html>
	<html lang=en>
	<head>

	</head>

	<body>
	<h1>Hello World!</h1>
	<p>This is {html_var} coming through</p>
	</body>
	
	</html>
	"""

	return HttpResponse(html_)
