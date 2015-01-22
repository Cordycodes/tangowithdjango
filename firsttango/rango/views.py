from django.shortcuts import render

from django.http import HttpResponse	

def index(request):
	return HttpResponse("Rango says I love you, world! \
                        <br> <a href ='/rango/about'> About</a>")

def about(request):
    return HttpResponse("This page brought to you by Cordelia Schmid (2038363s)."\
                        "<br> <img src='http://i.imgur.com/NzHBDjO.jpg' style='width:350px;height:467px'>"\
                        "<br> Back to index:<a href='/rango/'> Index</a>")
	
