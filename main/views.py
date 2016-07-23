from django.shortcuts import render, HttpResponse
from django.views.generic import View

class Sabado(View):
	def get(self,request):
		#return HttpResponse('Hola que haces!!')
		return render(request,'hola.html')

class hola(View):
	def get(self,request):
		return HttpResponse('Khe miras prro >:v!!')