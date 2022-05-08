from django.shortcuts import render

# Create your views here.
from unittest import result
from attr import fields
from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
import xlwt
import csv
from django.http import HttpResponse
from json import dumps

# Create your views here.
from sales.models import Sales


class salesListView(ListView):
    model = Sales
    template_name = "sales/sales-list.html"
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            stk = []
            query = query[3:]
            object_list = Sales.objects.filter(Q(id = int(query)))
            for object in object_list:
                id = object.id
                customer= object.customer
                date= object.date
                due_date = object.due_date
                address = object.address
                item_name = object.item_name
                unit_price = object.unit_price
                quantity = object.quantity
                amount = object.amount
                sales_id = "S00" + str(id)
                stk.append({'id':id,'sales_id': sales_id,'customer': customer, 'date': date, 'due_date': due_date, 'address': address, 'item_name':item_name, 'unit_price':unit_price, 'quantity':quantity, 'amount':amount
                })
            return stk
        else:
            stk = []
            object_list = Sales.objects.all()
            for object in object_list:
                id = object.id
                customer= object.customer
                date= object.date
                due_date = object.due_date
                address = object.address
                item_name = object.item_name
                unit_price = object.unit_price
                quantity = object.quantity
                amount = object.amount
                sales_id = "S00" + str(id)
                stk.append({'id':id,'sales_id': sales_id,'customer': customer, 'date': date, 'due_date': due_date, 'address': address, 'item_name':item_name, 'unit_price':unit_price, 'quantity':quantity, 'amount':amount
                })
            return stk
        

class salesCreateView(CreateView):
    model = Sales
    template_name = "sales/sales-form.html"
    success_url = reverse_lazy('sales:sales-list')
    fields = "__all__"

class salesUpdateView(UpdateView):
    model = Sales
    template_name = "sales/sales-form.html"
    success_url = reverse_lazy('sales:sales-list')
    fields = "__all__"


class salesDeleteView(DeleteView):
    model = Sales
    template_name = ""
    success_url = reverse_lazy('sales:sales-list')

def exportcsv(request):
    model = Sales
    Sales_report = Sales.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=Sales.csv'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Customer', 'Date', 'Due Date', 'Address', 'Item Name','Unit price','Quantity','Amount'])
    for object in Sales_report:
        id = object.id
        customer= object.customer
        date= object.date
        due_date = object.due_date
        address = object.address
        item_name = object.item_name
        unit_price = object.unit_price
        quantity = object.quantity
        amount = object.amount
        sales_id = "S00" + str(id)
        Sales_report = (sales_id,customer,date,due_date,address,item_name,unit_price,quantity,amount)
        writer.writerow(Sales_report)
    return response