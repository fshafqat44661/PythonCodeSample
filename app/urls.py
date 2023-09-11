from app.forms import *
from django.urls import path
from app import views
from django.contrib.auth import logout, views as auth_views
urlpatterns = [
# Home
    path('', views.Home.as_view(), name='home'),
 
#  Product Detail
    path('product-detail <int:pk>/', views.ProductDetailView.as_view(), name = 'product-detail'),

# Add to Cart
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
# Show Cart
    path('cart/', views.show_cart, name='show_cart'),

# Plus_Button
    path('pluscart/', views.plus_cart, name="plus-cart"),
# minus Cart
path('minuscart/', views.minus_cart, name="minus-cart"),

# minus Cart
path('removecart/', views.remove_cart, name="remove-cart"),


# Buy
    path('buy/', views.buy_now, name='buy-now'),

# Profile
    path('profile/', views.ProfileView.as_view(), name='profile'),

# Address
    path('address/', views.address, name='address'),

# Order
    path('orders/', views.orders, name='orders'),

# MObiles
    path('mobile/', views.mobile, name='mobile'),

# Mobile Details
    path('mobile<slug:data>/', views.mobile, name='mobiledata'),

# Laptops
    path('laptop/', views.laptop, name='laptop'),
 
# Laptop Detail 
    path('laptop<slug:data>/', views.laptop, name='laptopdata'),

# Login
    path('accounts/login/', auth_views.LoginView.as_view(template_name = 'app/login.html', authentication_form = LoginForm), name='login'),

# Logout
    path('logout/', auth_views.LogoutView.as_view(next_page = 'login'), name='logout'),

# Change Password
    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name = 'app/changepassword.html', form_class = MYPasswordChangeForm, success_url = '/passwordchangedone/'), name='changepassword'),

# password change Done
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name = 'app/passwordchangedone.html'), name='passwordchangedone'),

# Password Reset 
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name = 'app/password_reset.html', form_class = MyPasswordResetForm), name='password_reset'),

# Password Rest Done
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'app/password_reset_done.html'), name='password_reset_done'),

# Password Reset Confirm
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'app/password_reset_confirm.html', form_class = MySetPasswordForm), name='password_reset_confirm'),

# Password Reset Complete
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'app/password_reset_complete.html'), name='password_reset_complete'),

# Registration
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),

# Check Out
    path('checkout/', views.checkout, name='checkout'),

# Payment done
path('paymentdone/', views.payment_done, name='paymentdone'),

# Contact
    path('contact/', views.contact, name='contact_us'),
]
