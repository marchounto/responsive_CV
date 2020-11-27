from django.shortcuts import render

# Create your views here.
def show_CV(request):
    return render(request, 'CV.html',{})
