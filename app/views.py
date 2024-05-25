from django.shortcuts import render

# Create your views here.
def myview(request):
    # context = {'key': 'value'}  # Optional: Add context data if needed
    return render(request, 'index.html')