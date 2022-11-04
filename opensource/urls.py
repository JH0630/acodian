from django.urls import path, re_path
from opensource import views

app_name = 'opensoource'

urlpatterns = [

    # Example: /os/
    path('', views.OsLV.as_view(), name='index'),

    # Example: /os/langrank
    path('langrank', views.OslangLV.as_view(), name='os_lang'),

    # Example: /os/licerank
    path('licerank', views.OsliceLV.as_view(), name='os_lice'),

]