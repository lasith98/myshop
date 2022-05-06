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
from items.models import Items


class itemsListView(ListView):
    model = Items
    template_name = "items/items-list.html"
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            stk = []
            query = query[3:]
            object_list = Items.objects.filter(Q(id = int(query)))
            for object in object_list:
                id = object.id
                item_name= object.item_name
                category= object.category
                quantity = object.quantity
                unit_price = object.unit_price
                item_id = "#00" + str(id)
                stk.append({'id':id,'item_id': item_id,'item_name': item_name, 'category': category, 'quantity': quantity, 'unit_price': unit_price
                })
            return stk
        else:
            stk = []
            object_list = Items.objects.all()
            for object in object_list:
                id = object.id
                item_name= object.item_name
                category= object.category
                quantity = object.quantity
                unit_price = object.unit_price
                item_id = "#00" + str(id)
                stk.append({'id':id,'item_id': item_id,'item_name': item_name, 'category': category, 'quantity': quantity, 'unit_price': unit_price
                })
            return stk
        

class itemsCreateView(CreateView):
    model = Items
    template_name = "items/items-form.html"
    success_url = reverse_lazy('items:items-list')
    fields = "__all__"

class itemsUpdateView(UpdateView):
    model = Items
    template_name = "items/items-form.html"
    success_url = reverse_lazy('items:items-list')
    fields = "__all__"


class itemsDeleteView(DeleteView):
    model = Items
    template_name = ""
    success_url = reverse_lazy('items:items-list')

def exportcsv(request):
    model = Items
    Items_report = Items.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=Items.csv'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Item Name', 'Category', 'Quantity', 'Unit Price'])
    for object in Items_report:
        id = object.id
        item_name= object.item_name
        category= object.category
        quantity = object.quantity
        unit_price = object.unit_price
        item_id = "#00" + str(id)
        Items_report = (item_id,item_name,category,quantity,unit_price)
        writer.writerow(Items_report)
    return response