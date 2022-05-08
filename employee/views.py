
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
import xlwt
import csv
from django.http import HttpResponse
from json import dumps

# Create your views here.
from employee.models import Employee


class employeeListView(ListView):
    model = Employee
    template_name = "employee/employee-list.html"
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            stk = []
            query = query[3:]
            object_list = Employee.objects.filter(Q(id = int(query)))
            for object in object_list:
                id = object.id
                first_name= object.first_name
                last_name= object.last_name
                email = object.email
                contact = object.contact
                occupation = object.occupation
                emp_id = "E00" + str(id)
                stk.append({'id':id,'emp_id': emp_id,'first_name': first_name, 'last_name': last_name, 'email': email, 'contact': contact, 'occupation':occupation
                })
            return stk
        else:
            stk = []
            object_list = Employee.objects.all()
            for object in object_list:
                id = object.id
                first_name= object.first_name
                last_name= object.last_name
                email = object.email
                contact = object.contact
                occupation = object.occupation
                emp_id = "E00" + str(id)
                stk.append({'id':id,'emp_id': emp_id,'first_name': first_name, 'last_name': last_name, 'email': email, 'contact': contact, 'occupation':occupation
                })
            return stk
        

class employeeCreateView(CreateView):
    model = Employee
    template_name = "employee/employee-form.html"
    success_url = reverse_lazy('employee:employee-list')
    fields = "__all__"

class employeeUpdateView(UpdateView):
    model = Employee
    template_name = "employee/employee-form.html"
    success_url = reverse_lazy('employee:employee-list')
    fields = "__all__"


class employeeDeleteView(DeleteView):
    model = Employee
    template_name = ""
    success_url = reverse_lazy('employee:employee-list')

def exportcsv(request):
    model = Employee
    Employee_report = Employee.objects.all()
    response = HttpResponse('')
    response['Content-Disposition'] = 'attachment; filename=Employees.csv'
    writer = csv.writer(response)
    writer.writerow(['ID', 'First Name', 'Last Name', 'Email', 'Contact', 'Occupation'])
    for object in Employee_report:
        id = object.id
        first_name= object.first_name
        last_name= object.last_name
        email = object.email
        contact = object.contact
        occupation = object.occupation
        emp_id = "E00" + str(id)
        Employee_report = (emp_id,first_name,last_name,email,contact,occupation)
        writer.writerow(Employee_report)
    return response