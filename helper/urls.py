from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordResetForm, MyPasswordChangeForm, MySetPasswordForm

urlpatterns = [
    path('', views.home),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('category/<slug:value>', views.CategoryView.as_view(), name="category"),
    path('category-title/<value>', views.CategoryTitle.as_view(), name="category-title"),
    path('product-detail/<int:pk>', views.ProductDetail.as_view(), name="detail"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('address/', views.address, name="address"),
    path('updateAddress/<int:pk>', views.UpdateAddress.as_view(), name="updateAddress"),
    path('add-to-cart/', views.add_to_cart, name="addtocart"),
    path('cart/', views.show_cart, name="showcart"),
    path('checkout/', views.Checkout.as_view(), name="checkout"),
    path('pluscart/', views.pluscart, name="pluscart"),
    path('minuscart/', views.minuscart, name="minuscart"),
    path('removecart/', views.removecart, name="removecart"),
    
    #Log in Authentication
    path('registration/', views.RegistrationView.as_view(), name="registrationform"),
    path('login/', auth_views.LoginView.as_view(template_name='helper/login.html',authentication_form=LoginForm), name="login"),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='helper/passwordchange.html',form_class=MyPasswordChangeForm, success_url='/passwordchangedone'), name="passwordchange"),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='helper/passwordreset.html',form_class=MyPasswordResetForm), name="passwordreset"),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='helper/passwordchangedone.html'), name="passwordchangedone"),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='helper/password_reset_done.html'), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='helper/password_reset_confirm.html',form_class=MySetPasswordForm), name='password_reset_confirm'),
    path("password-reset-complete/",auth_views.PasswordResetCompleteView.as_view(template_name='helper/password_reset_complate.html'), name='password_reset_complete'),
]
