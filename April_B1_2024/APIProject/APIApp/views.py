from django.shortcuts import render
import requests


def Productpage(request):
    api_url="https://fakestoreapi.com/products"
    data=requests.get(api_url)
    if data.status_code==200:
        products=data.json()
    else:
        products=[]
    return render(request,"Product.html",{'products':products})
