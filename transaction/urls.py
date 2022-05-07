"""
 * author: Lasith Hansana
 * email : lasithhansana9@gmail.com
 * web   : https://lasithhansana.com
 * date  : 2022-03-27
 * time  : 10:58
"""
from django.urls import path

from transaction.views import TransactionListView, TransactionCreateView, TransactionUpdateView, TransactionDeleteView

app_name = 'transaction'

urlpatterns = [
    path('', TransactionListView.as_view(), name='transaction-list'),
    path('create', TransactionCreateView.as_view(), name='transaction-create'),
    path('update/<int:pk>', TransactionUpdateView.as_view(), name='transaction-update'),
    path('delete/<int:pk>', TransactionDeleteView.as_view(), name='transaction-delete'),
]