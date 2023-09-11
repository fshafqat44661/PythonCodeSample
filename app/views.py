from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import *
from .forms import *
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
#  return render(request, 'app/home.html')
class Home(View):
    def get(self, request):
        all_products = Product.objects.all()
        asianfoods = Product.objects.filter(category = 'TAF')
        healthy_food = Product.objects.filter(category = 'Healthy_Food')
        gym_box = Product.objects.filter(category = 'Gym_Box')
        cakes = Product.objects.filter(category = 'CakesADD')
        parties = Product.objects.filter(category = 'OGP')
        breakfast = Product.objects.filter(category = 'Breakfast')
        vegan = Product.objects.filter(category = 'Vegan')
        if request.user.is_authenticated:
            user = request.user
            cart = Cart.objects.filter(user = user)
            total_quantity = 0
            amount = 0
            discount = 0
            cart_product = [p for p in Cart.objects.all() if p.user==user]
            # print(cart_product)
            if cart_product:
                for p in cart_product:
                    total_quantity += p.quantity
                    temp_amount = (p.quantity * p.product.selling_price)
                    amount += temp_amount
                    discount += (p.quantity * p.product.discounted_price)
        
            return render(request, 'app/home.html', {'asian_foods': asianfoods, 'healthy_food': healthy_food, 'gym_box': gym_box, 'cakes':cakes, 'parties': parties, 'breakfast': breakfast, 'vegan': vegan, 'amount': amount, 'quantity': total_quantity})
            
        return render(request, 'app/home.html', {'asian_foods': asianfoods, 'healthy_food': healthy_food, 'gym_box': gym_box, 'cakes':cakes, 'parties': parties, 'breakfast': breakfast, 'vegan': vegan})


class ProductDetailView(View):
    def get (self, request, pk):
        product = Product.objects.get(pk = pk)
        d_price = product.selling_price - product.discounted_price
        item_already_in_cart = False
        if request.user.is_authenticated:
            item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user = request.user)).exists()
        return render(request, 'app/productdetail.html', {'product': product, 'price':d_price, 'item_already_in_cart': item_already_in_cart} )

# Add to Cart
@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    # print(f"product id: {product_id}")
    product = Product.objects.get(id = product_id)
    Cart(user= user, product = product).save()
    return redirect('/cart')

# Show Cart
@login_required
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user = user)
        amount = 0
        discount = 0
        total_quantity = 0
        cart_product = [p for p in Cart.objects.all() if p.user==user]
        # print(cart_product)
        if cart_product:
            for p in cart_product:
                total_quantity += p.quantity
                temp_amount = (p.quantity * p.product.selling_price)
                amount += temp_amount
                discount += (p.quantity * p.product.discounted_price)
            return render(request, 'app/addtocart.html',{'carts':cart, 'amount': amount,'discount':discount, 'total_amount':amount - discount, 'quantity': total_quantity})
        else:
            return render(request, 'app/empty_cart.html')


def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product = prod_id) & Q(user = request.user))
        c.quantity += 1
        c.save()
        amount = 0
        shipping_amount = 70
        discount = 0
        cart_product = [p for p in Cart.objects.all() if p.user==request.user]
        # print(cart_product)
        if cart_product:
            for p in cart_product:
                temp_amount = (p.quantity * p.product.selling_price)
                amount += temp_amount
                discount += (p.quantity * p.product.discounted_price)
            data = {
                'quantity':c.quantity,
                'amount': amount,
                'discount': discount,
                'total_amount': amount-discount,
            }
            return JsonResponse(data)

# Minus Cart
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product = prod_id) & Q(user = request.user))
        c.quantity -= 1
        c.save()
        amount = 0
        shipping_amount = 70
        discount = 0
        cart_product = [p for p in Cart.objects.all() if p.user==request.user]
        # print(cart_product)
        if cart_product:
            for p in cart_product:
                temp_amount = (p.quantity * p.product.selling_price)
                amount += temp_amount
                discount += (p.quantity * p.product.discounted_price)
            data = {
                'quantity':c.quantity,
                'amount': amount,
                'discount': discount,
                'total_amount': amount - discount,
            }
            return JsonResponse(data)



# Minus Cart
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product = prod_id) & Q(user = request.user))
        c.delete()
        amount = 0
        cart_product = [p for p in Cart.objects.all() if p.user==request.user]
        # print(cart_product)
        if cart_product:
            for p in cart_product:
                temp_amount = (p.quantity * p.product.selling_price)
                amount += temp_amount

            data = {
                'total_amount': amount
            }
            return JsonResponse(data)


# Buy Now
def buy_now(request):
 return render(request, 'app/buynow.html')

# Address
@login_required
def address(request):
    data = Customer.objects.filter(user = request.user)
    return render(request, 'app/address.html',{'active': 'btn-primary', 'data':  data})

# Orders
@login_required
def orders(request):
    op = OrderPlaced.objects.filter(user = request.user)
    return render(request, 'app/orders.html' ,{'order_placed':op})

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request, data = None):
    if data == None:
        mobiles = Product.objects.all()
    elif data == 'Healthy_Food':
        mobiles = Product.objects.filter(category = 'Healthy_Food')
    elif data == 'Gym_Box':
        mobiles = Product.objects.filter(category = 'Gym_Box')
    elif data == 'TAF':
        mobiles = Product.objects.filter(category = 'TAF')
    elif data == 'CakesADD':
        mobiles = Product.objects.filter(category = 'CakesADD')
    elif data == 'OGP':
        mobiles = Product.objects.filter(category = 'OGP')
    elif data == 'Breakfast':
        mobiles = Product.objects.filter(category = 'Breakfast')
    elif data == 'Vegan':
        mobiles = Product.objects.filter(category = 'Vegan')
    return render(request, 'app/mobile.html', {'mobiles': mobiles})


def laptop(request, data = None):
    if data == None:
        laptops = Product.objects.filter(category = 'L')
    elif data == 'Samsung' or data == 'Apple' or data == 'Lenovo' or data == 'HP' or data == 'Dell' or data == 'Accer' or data == 'Microsoft' or data == 'Asus':
        laptops = Product.objects.filter(category = 'L').filter(brand = data)
    return render(request, 'app/laptop.html', {'laptops': laptops})

# def login(request):
#  return render(request, 'app/login.html')

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')
class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerregistraionForm
        return render(request, 'app/customerregistration.html', {'form': form})
    def post(self, request):
        form = CustomerregistraionForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations! Registered Successfully!')
            form.save()
        return render(request, 'app/customerregistration.html', {'form': form})

@login_required
def checkout(request):
    user = request.user
    add = Customer.objects.filter(user = user)
    cart_items = Cart.objects.filter(user = user)
    amount = 0
    cart_product = [p for p in Cart.objects.all() if p.user==request.user]
    if cart_product:
        for p in cart_product:
            temp_amount = (p.quantity * p.product.selling_price)
            amount += temp_amount

    return render(request, 'app/checkout.html', {'add': add, 'amount':amount, 'items':cart_items})

@login_required
def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    print(custid)
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user = user)
    for item in cart:
        OrderPlaced(user = user, customer = customer, product = item.product, quantity= item.quantity).save()
        item.delete()
    return redirect('orders')

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary'})
    
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user = usr, name = name, locality = locality, city= city, state = state, zipcode =  zipcode)
            reg.save()
            messages.success(request, 'Congratulations Your Profile Updated Successfully!')
        return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary'})

def contact(request):
    return render(request, 'app/contact.html')