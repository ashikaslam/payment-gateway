from django.shortcuts import render,redirect
from django.http import HttpResponse
import random
import string
from sslcommerz_lib import SSLCOMMERZ 
from django.views.decorators.csrf import csrf_exempt

def generate_transaction_id(length=15):
    characters = string.ascii_letters + string.digits
    transaction_id = ''.join(random.choice(characters) for _ in range(length))
    return transaction_id

def home(request):
    return render(request,'index.html')
@csrf_exempt
def f(request):
    return render(request,'fail.html')
@csrf_exempt
def s(request):
    return render(request,'success.html')



def pay(request):
      
    settings = {'store_id':'djang6694103d32b98','store_pass':'djang6694103d32b98@ssl','issandbox':True}
    sslcz = SSLCOMMERZ(settings)
    post_body = {}
    post_body['total_amount'] = 100.26
    post_body['currency'] = "BDT"
    post_body['tran_id'] = "12345"
    post_body['success_url'] = "http://127.0.0.1:8000/s/"
    post_body['fail_url'] = "http://127.0.0.1:8000/f"
    post_body['cancel_url'] = "http://127.0.0.1:8000/f"
    post_body['emi_option'] = 0
    post_body['cus_name'] = "aslam"
    post_body['cus_email'] = "test@test.com"
    post_body['cus_phone'] = "01700000000"
    post_body['cus_add1'] = "customer address"
    post_body['cus_city'] = "Dhaka"
    post_body['cus_country'] = "Bangladesh"
    post_body['shipping_method'] = "NO"
    post_body['multi_card_name'] = ""
    post_body['num_of_item'] = 1
    post_body['product_name'] = "Test"
    post_body['product_category'] = "Test Category"
    post_body['product_profile'] = "general"


    response = sslcz.createSession(post_body) # API response
    print(response)
    # Need to redirect user to response['GatewayPageURL']
    return redirect(response['GatewayPageURL'])


