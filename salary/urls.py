from django.urls import path
from salary.views import salaryListView, salaryCreateView, salaryUpdateView, salaryDeleteView , exportcsv , send_ids, sav_data

app_name = 'salary'
urlpatterns = [
    path('', salaryListView.as_view(), name='salary-list'),
    path('create', salaryCreateView.as_view(), name='salary-create'),
    path('update/<int:pk>', salaryUpdateView.as_view(), name='salary-update'),
    path('delete/<int:pk>', salaryDeleteView.as_view(), name='salary-delete'),
    path('search', salaryListView.as_view(), name='salary-search'),
    path('exportcsv', exportcsv, name='salary-report'),
    path('send_ids', send_ids, name='salary-send_ids'),
    path('sav_data', sav_data, name='salary-sav_data'),
]