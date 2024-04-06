from django.shortcuts import render

# Create your views here.
def products_sell(request):
    return render(request,'customer/products_sell.html')