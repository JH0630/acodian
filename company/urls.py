from django.urls import path, re_path
from company import views

app_name = 'company'

urlpatterns = [

    # Example: /os/langrank
    path('langrank', views.ComlangLV.as_view(), name='com_lang'),

    # Example: /os/licerank
    path('dutyrank', views.ComdutyLV.as_view(), name='duty_rank'),

]