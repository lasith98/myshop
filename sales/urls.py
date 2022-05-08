from django.urls import path
from sales.views import salesListView, salesCreateView, salesUpdateView, salesDeleteView , exportcsv 

app_name = 'sales'
urlpatterns = [
    path('', salesListView.as_view(), name='sales-list'),
    path('create', salesCreateView.as_view(), name='sales-create'),
    path('update/<int:pk>', salesUpdateView.as_view(), name='sales-update'),
    path('delete/<int:pk>', salesDeleteView.as_view(), name='sales-delete'),
    path('search', salesListView.as_view(), name='sales-search'),
    path('exportcsv', exportcsv, name='sales-report'),
]