
from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
import csv
from django.http import HttpResponse
import json
from json import dumps
from django.http import JsonResponse

# Create your views here.
from salary.models import Salary
from employee.models import Employee


class salaryListView(ListView):
    model = Salary
    template_name = "salary/salary-list.html"
    def get_queryset(self):
        query = self.request.GET.get('search')
        try:
            if query:
                stk = []
                object_list = Salary.objects.filter(Q(emp_id = query))
                for object in object_list:
                    id = object.id
                    emp_id = object.emp_id
                    first_name= object.first_name
                    last_name= object.last_name
                    net_salary = object.net_salary
                    stk.append({'id':id,'emp_id': emp_id,'first_name': first_name, 'last_name': last_name, 'net_salary': net_salary
                    })
                return stk
            else:
                stk = []
                object_list = Salary.objects.all()
                for object in object_list:
                    id = object.id
                    emp_id = object.emp_id
                    first_name= object.first_name
                    last_name= object.last_name
                    net_salary = object.net_salary
                    stk.append({'id':id,'emp_id': emp_id,'first_name': first_name, 'last_name': last_name, 'net_salary': net_salary
                    })
                return stk
        except:
            stk = []
            object_list = Salary.objects.all()
            for object in object_list:
                id = object.id
                emp_id = object.emp_id
                first_name= object.first_name
                last_name= object.last_name
                net_salary = object.net_salary
                stk.append({'id':id,'emp_id': emp_id,'first_name': first_name, 'last_name': last_name, 'net_salary': net_salary
                })
            return stk
        

class salaryCreateView(CreateView):
    model = Salary
    template_name = "salary/salary-form.html"
    success_url = reverse_lazy('salary:salary-list')
    fields = "__all__"
    

class salaryUpdateView(UpdateView):
    model = Salary
    template_name = "salary/salary-update.html"
    success_url = reverse_lazy('salary:salary-list')
    fields = "__all__"


class salaryDeleteView(DeleteView):
    model = Salary
    template_name = ""
    success_url = reverse_lazy('salary:salary-list')

def exportcsv(request):
    model = Salary
    Salary_report = Salary.objects.all()
    response = HttpResponse('')
    response['Content-Disposition'] = 'attachment; filename=Salaries.csv'
    writer = csv.writer(response)
    writer.writerow(['ID', 'First Name', 'Last Name', 'Net Salary'])
    for object in Salary_report:
        id = object.id
        emp_id = object.emp_id
        first_name= object.first_name
        last_name= object.last_name
        net_salary = object.net_salary
        Salary_report = (emp_id,first_name,last_name,net_salary)
        writer.writerow(Salary_report)
    return response

def send_ids(request):
    # create data dictionary
        stk = []
        object_list = Employee.objects.all()
        for object in object_list:
            id = object.id
            emp_id = "E00" + str(id)
            first_name = object.first_name
            last_name = object.last_name
            stk.append({'emp_id': emp_id,'last_name':last_name,'first_name':first_name
            })
        return render(request, 'salary/salary-form.html', {'df_json': stk})

def sav_data(request):
    emp_id = request.POST.get('emp_id')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    nic = request.POST.get('nic')
    bank = request.POST.get('bank')
    pay_period = request.POST.get('pay_period')
    tax_no = request.POST.get('tax_no')
    basic_salary = request.POST.get('basic_salary')
    dedcutions = request.POST.get('dedcutions')
    net_salary = request.POST.get('net_salary')
    s = Salary(emp_id=emp_id, first_name=first_name, last_name=last_name, nic=nic, bank=bank, pay_period=pay_period, tax_no=tax_no, basic_salary=basic_salary, dedcutions=dedcutions, net_salary=net_salary)
    s.save()
    return render(request, 'salary/salary-form.html')