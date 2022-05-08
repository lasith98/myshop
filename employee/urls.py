from django.urls import path
from employee.views import employeeListView, employeeCreateView, employeeUpdateView, employeeDeleteView , exportcsv 

app_name = 'employee'
urlpatterns = [
    path('', employeeListView.as_view(), name='employee-list'),
    path('create', employeeCreateView.as_view(), name='employee-create'),
    path('update/<int:pk>', employeeUpdateView.as_view(), name='employee-update'),
    path('delete/<int:pk>', employeeDeleteView.as_view(), name='employee-delete'),
    path('search', employeeListView.as_view(), name='employee-search'),
    path('exportcsv', exportcsv, name='employee-report'),
]