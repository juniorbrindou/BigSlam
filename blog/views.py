from django.shortcuts import render

# Create your views here.


def index(request):
	return render(request,'pages/blog-grid-3-columns.html')