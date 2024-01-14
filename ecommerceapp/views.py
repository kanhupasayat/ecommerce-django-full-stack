
from django.shortcuts import render
from flask import redirect
from ecommerceapp.models import Contact,Product,Product2,Orders,OrderUpdate
from django.contrib import messages
from math import ceil
from django.conf import settings
import json
from authcart import views
from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from ecommerceapp.models import Orders, OrderUpdate
from django.http import HttpResponse  



from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse

from ecommerceapp.models import Orders, OrderUpdate
from django.conf import settings












def index(request):
    # Fetch all products from the database
    products = Product.objects.all()
    products2= Product2.objects.all()
    
    return render(request, 'index.html', {'products': products,'products2': products2})


 # Replace 'contact.html' with your actual contact page template



def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phumber = request.POST.get("pnumber")
        desc = request.POST.get("desc")

        myquery = Contact(name=name, email=email, phonenumber=phumber, desc=desc)
        myquery.save()

        # Redirect to a success page or show a success message
        return render(request, 'index.html')  # Replace 'success.html' with your success template

    return render(request, 'contact.html',)


def shop(request):
    products = Product.objects.all()

    return render(request, 'shop.html', {'products': products})






import razorpay
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse

from ecommerceapp.models import Orders, OrderUpdate
from django.conf import settings




def checkout(request):
    context = {'payment': None}  # Default value for payment

    if not request.user.is_authenticated:
        messages.warning(request, "Please log in and try again.")
        return render(request, 'login.html', context)

    if request.method == "POST":
        try:
            items_json = request.POST.get('cart', '')
            name = request.POST.get('name', '')
            amount = float(request.POST.get('amt', '0'))
            email = request.POST.get('email', '')
            address1 = request.POST.get('address1', '')
            city = request.POST.get('city', '')  
            state = request.POST.get('state', '')
            zip_code = request.POST.get('zip_code', '')
            oid = request.POST.get('oid', '')
            phone = request.POST.get('phone', '')

            order = Orders(
            items_json=items_json, name=name, amount=amount, email=email, address1=address1, city=city, state=state,zip_code=zip_code,oid=oid, phone=phone)
            print(order)
            order.save()

            update = OrderUpdate(order_id=order.order_id, update_desc="Order has been placed")
            update.save()

            if amount < 1.00:
                messages.error(request, "The amount must be at least INR 1.00.")
                return render(request, 'checkout.html', context)

            client = razorpay.Client(auth=(settings.KEY, settings.SECRET))
            payment = client.order.create({'amount':float(amount * 100), 'currency': 'INR', 'payment_capture': 1, 'receipt': str(oid)})
            context['payment'] = payment
            print(payment)

        except Exception as e:
            messages.error(request, f"Error processing payment: {str(e)}")

    return render(request, 'checkout.html', context)





    


