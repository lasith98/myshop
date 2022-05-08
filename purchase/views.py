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
from purchase.models import Purchase

class purchaseListView(ListView):
    model = Purchase
    template_name = "purchase/purchase-list.html"
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            stk = []
            object_list = Purchase.objects.filter(Q(invoice_no = query))
            for object in object_list:
                id = object.id
                invoice_date= object.invoice_date
                invoice_no= object.invoice_no
                from_add= object.from_add
                delivery_date = object.delivery_date
                item_id= object.item_id
                item_name= object.item_name
                model_no= object.model_no
                quantity= object.from_add
                discount = object.discount
                purchase_price = object.purchase_price
                stk.append({'id': id,'invoice_date':invoice_date,'invoice_no': invoice_no,'from_add': from_add, 'delivery_date': delivery_date,'discount':discount,'purchase_price': purchase_price,'item_name': item_name, 'item_id': item_id, 'quantity': quantity, 'model_no': model_no
                })
            return stk
        else:
            stk = []
            object_list = Purchase.objects.all()
            for object in object_list:
                id = object.id
                invoice_date= object.invoice_date
                invoice_no= object.invoice_no
                from_add= object.from_add
                delivery_date = object.delivery_date
                item_id= object.item_id
                item_name= object.item_name
                model_no= object.model_no
                quantity= object.from_add
                discount = object.discount
                purchase_price = object.purchase_price
                stk.append({'id': id,'invoice_date':invoice_date,'invoice_no': invoice_no,'from_add': from_add, 'delivery_date': delivery_date,'discount':discount,'purchase_price': purchase_price,'item_name': item_name, 'item_id': item_id, 'quantity': quantity, 'model_no': model_no
                })
            return stk
        

class purchaseCreateView(CreateView):
    model = Purchase
    template_name = "purchase/purchase-form.html"
    success_url = reverse_lazy('purchase:purchase-list')
    fields = "__all__"

class purchaseUpdateView(UpdateView):
    model = Purchase
    template_name = "purchase/purchase-form.html"
    success_url = reverse_lazy('purchase:purchase-list')
    fields = "__all__"


class purchaseDeleteView(DeleteView):
    model = Purchase
    template_name = ""
    success_url = reverse_lazy('purchase:purchase-list')

def exportcsv(request):
    model = Purchase
    Purchase_report = Purchase.objects.all()
    response = HttpResponse('')
    response['Content-Disposition'] = 'attachment; filename=Purchase.csv'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Invoice Date','Invoice No', 'From', 'Delivery Date', 'Item Id', 'Item Name', 'Model No', 'Quantity', 'Purchase Price', 'Discount'])
    for object in Purchase_report:
        id = object.id
        invoice_date= object.invoice_date
        invoice_no= object.invoice_no
        from_add= object.from_add
        delivery_date = object.delivery_date
        item_id= object.item_id
        item_name= object.item_name
        model_no= object.model_no
        quantity= object.from_add
        discount = object.discount
        purchase_price = object.purchase_price
        Purchase_report = (id,invoice_date,invoice_no,from_add,delivery_date,item_id,item_name,model_no,quantity,purchase_price,discount)
        writer.writerow(Purchase_report)
    return response