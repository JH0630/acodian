from django.urls import path, re_path
from all import views

app_name = 'all'

urlpatterns = [

    # Example: /os/langrank
    path('', views.AllLV.as_view(), name='all'),
]