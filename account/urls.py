from django.urls import path

from account.views import AccountListView, AccountCreateView, AccountUpdateView, AccountDeleteView

app_name = 'account'

urlpatterns = [
    path('', AccountListView.as_view(), name='account-list'),
    path('create', AccountCreateView.as_view(), name='account-create'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='account-update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='account-delete'),
]
