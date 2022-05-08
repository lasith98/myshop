
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
import xlwt
import csv
from django.http import HttpResponse
from json import dumps

# Create your views here.
from supplier.models import Supplier


class supplierListView(ListView):
    model = Supplier
    template_name = "supplier/supplier-list.html"
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            stk = []
            query = query[3:]
            object_list = Supplier.objects.filter(Q(id = int(query)))
            for object in object_list:
                id = object.id
                supplier_name= object.supplier_name
                contact = object.contact
                item_name= object.item_name
                date = object.date
                supplier_id = "SU0" + str(id)
                stk.append({'id':id,'supplier_id': supplier_id,'supplier_name': supplier_name, 'contact': contact, 'item_name': item_name, 'date': date
                })
            return stk
        else:
            stk = []
            object_list = Supplier.objects.all()
            for object in object_list:
                id = object.id
                supplier_name= object.supplier_name
                contact = object.contact
                item_name= object.item_name
                date = object.date
                supplier_id = "SU0" + str(id)
                stk.append({'id':id,'supplier_id': supplier_id,'supplier_name': supplier_name, 'contact': contact, 'item_name': item_name, 'date': date
                })
            return stk
        

class supplierCreateView(CreateView):
    model = Supplier
    template_name = "supplier/supplier-form.html"
    success_url = reverse_lazy('supplier:supplier-list')
    fields = "__all__"

class supplierUpdateView(UpdateView):
    model = Supplier
    template_name = "supplier/supplier-form.html"
    success_url = reverse_lazy('supplier:supplier-list')
    fields = "__all__"


class supplierDeleteView(DeleteView):
    model = Supplier
    template_name = ""
    success_url = reverse_lazy('supplier:supplier-list')

def exportcsv(request):
    model = Supplier
    Supplier_report = Supplier.objects.all()
    response = HttpResponse('')
    response['Content-Disposition'] = 'attachment; filename=Supplier.csv'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Supplier Name', 'Contact', 'Item Name', 'Date'])
    for object in Supplier_report:
        id = object.id
        supplier_name= object.supplier_name
        contact = object.contact
        item_name= object.item_name
        date = object.date
        supplier_id = "SU0" + str(id)
        Supplier_report = (supplier_id,supplier_name,contact,item_name,date)
        writer.writerow(Supplier_report)
    return response