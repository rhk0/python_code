from django.shortcuts import render
from home.models import Contact
from datetime import datetime
from hello.settings import RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY
import razorpay
# Create your views here.
client = razorpay.Client(auth=(RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY))
def index(request):
    order_amount = 50000
    order_currency = 'INR'
    
    payment_order = client.order.create(dict(amount =order_amount,currency = order_currency,payment_capture = 1))
    payment_order_id = payment_order['id']
    context = {
        'amount':500, 'api_key':RAZORPAY_API_KEY, 'order_id':payment_order_id,
        'variable1':"This is sent",
        'variable2':"This is send"

    }
    # return HttpResponse("this is homepage")
    return render(request,'index.html',context)
def about(request):
    return render(request,'about.html')

    # return HttpResponse("this is about")

def service(request):
    return render(request,'service.html')

    # return HttpResponse("this is server")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        desc = request.POST.get('desc')
        field1 = request.POST.get('field1')
        field2 = request.POST.get('field2')
        result = request.POST.get('result')

        contact = Contact(name = name, email = email, desc = desc,phone_number = phone_number,field1=field1,field2=field2,result=result,date = datetime.today,)
        contact.save()

    return render(request,'contact.html')


