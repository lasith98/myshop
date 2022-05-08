from django.urls import path
from supplier.views import supplierListView, supplierCreateView, supplierUpdateView, supplierDeleteView , exportcsv 

app_name = 'supplier'
urlpatterns = [
    path('', supplierListView.as_view(), name='supplier-list'),
    path('create', supplierCreateView.as_view(), name='supplier-create'),
    path('update/<int:pk>', supplierUpdateView.as_view(), name='supplier-update'),
    path('delete/<int:pk>', supplierDeleteView.as_view(), name='supplier-delete'),
    path('search', supplierListView.as_view(), name='supplier-search'),
    path('exportcsv', exportcsv, name='supplier-report'),
]