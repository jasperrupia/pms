from django.urls import path
from . import views


app_name = 'sales'
urlpatterns = [
    path('sell', views.sell, name='sell'),
    path('records', views.records, name='records'),
    path('receipt', views.receipt, name='receipt'),
    # path('receipt_view', views.receipt_view, name='receipt_view'),
] 
