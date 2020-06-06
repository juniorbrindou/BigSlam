from django.shortcuts import render

# Create your views here.


def index(request):
	return render(request,'pages/blog-2-columns.html')

def single(request):
	return render(request,'pages/standard-post-type.html')