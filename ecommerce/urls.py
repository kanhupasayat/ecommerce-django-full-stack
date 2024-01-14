from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from authcart import views 
from django.conf import settings






urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("ecommerceapp.urls")),

    path('signup/', views.signup, name='signup'),
    path('login/', views.handlelogin, name='handlelogin'),
    path('logout/', views.handlelogout, name='handlelogout'),
     

    path('activate/<uidb64>/<token>/', views.ActivateAccountView.as_view(), name='activate_account'),




   
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
