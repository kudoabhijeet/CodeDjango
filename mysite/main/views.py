from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
my_name = "Abhijeet"
my_list = ['Item 1', 'Item 2']
context = {
    "name" : my_name,
    "lists" : my_list,
}
def homepage(request):
    return render(request, 'main/index.html', context)