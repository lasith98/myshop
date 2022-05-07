from django.urls import path

from balance_sheet.views import BalanceSheetListView, BalanceSheetCreateView, BalanceSheetUpdateView, BalanceSheetDeleteView

app_name = 'balance_sheet'

urlpatterns = [
    path('', BalanceSheetListView.as_view(), name='balance_sheet-list'),
    path('create', BalanceSheetCreateView.as_view(), name='balance_sheet-create'),
    path('update/<int:pk>', BalanceSheetUpdateView.as_view(), name='balance_sheet-update'),
    path('delete/<int:pk>', BalanceSheetDeleteView.as_view(), name='balance_sheet-delete'),
]
