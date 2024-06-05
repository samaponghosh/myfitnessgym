"""mygym URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from gymapp.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    # path('signup/',user_signup,name='signup'),
    path('about/',About,name='About'),
    path('contact/',Contact,name='Contact'),
    # path('login/',user_login,name='login'),
    # path('logout/',user_logout,name='logout'),
    path('BMI_calculator/',bmicalculator,name='BMI_calculator'),
    path('view_equipments/',viesEquip,name='view_equipments'),
    path('view_member/',viewMem,name='view_member'),
    path('view_plan/', viewPlan, name='view_plan'),
    path('view_enquiry/', viewEnq, name='view_enquiry'),
    path('add_enquiry/', addEnq, name='add_enquiry'),
    path('delete_enquiry(?p<int:pid>)/', delEnq, name='delete_enquiry'),
    
    path('cam/', showCam, name='cam'),
    path('walk/', walkcount, name='walk'),
    path('curl/', curlCount, name='curl'),
    path('squat/', squatCount, name='squat'),
    path('pushUp/', pushCount, name='pushUp'),
    path('pullUp/', pullCount, name='pullUp'),
    path('jump/', jumpCount, name='jump'),
    path('crunch/', crunchCount, name='crunch'),
    # path('chestPress/', chestCount, name='chestPress'),
    path('AIGymTrainer/', AiTrainerHome, name='AIGymTrainer'),
    
    path('chat/', include('chat.urls')),
    path('social/', include('social.urls')),
    path('blogs/', include('blogsapp.urls')),
]

urlpatterns = urlpatterns+static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)
