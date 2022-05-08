from django.urls import path
from purchase.views import purchaseListView, purchaseCreateView, purchaseUpdateView, purchaseDeleteView , exportcsv 

app_name = 'purchase'
urlpatterns = [
    path('', purchaseListView.as_view(), name='purchase-list'),
    path('create', purchaseCreateView.as_view(), name='purchase-create'),
    path('update/<int:pk>', purchaseUpdateView.as_view(), name='purchase-update'),
    path('delete/<int:pk>', purchaseDeleteView.as_view(), name='purchase-delete'),
    path('search', purchaseListView.as_view(), name='purchase-search'),
    path('exportcsv', exportcsv, name='purchase-report'),
]