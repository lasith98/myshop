from django.urls import path
from items.views import itemsListView, itemsCreateView, itemsUpdateView, itemsDeleteView , exportcsv 

app_name = 'items'
urlpatterns = [
    path('', itemsListView.as_view(), name='items-list'),
    path('create', itemsCreateView.as_view(), name='items-create'),
    path('update/<int:pk>', itemsUpdateView.as_view(), name='items-update'),
    path('delete/<int:pk>', itemsDeleteView.as_view(), name='items-delete'),
    path('search', itemsListView.as_view(), name='items-search'),
    path('exportcsv', exportcsv, name='items-report'),
]