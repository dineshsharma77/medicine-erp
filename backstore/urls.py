from . import views
from django.urls import path

urlpatterns = [
    path('brands', views.brands, name='brands'),
    path('dealers', views.dealers, name='dealers'),
    path('medicines', views.medicines, name='medicines'),
    path('staff',views.staffs, name='staff'),
    path('user',views.user,name='user'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),

]