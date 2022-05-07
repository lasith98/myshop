import uuid
from datetime import datetime

from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

# Create your views here.
from balance_sheet.models import BalanceSheet


class BalanceSheetListView(ListView):
    model = BalanceSheet
    template_name = "balance_sheet/balance_sheet-list.html"

    query = ''

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        self.query = ''

        if query != '':
            self.query = query
            return super(BalanceSheetListView, self).get_queryset().filter(balance_sheet_id=query)
        return super(BalanceSheetListView, self).get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['delete_url'] = reverse('balance_sheet:balance_sheet-delete', kwargs={'pk': 1})
        context['query'] = self.query

        return context


class BalanceSheetCreateView(CreateView):
    model = BalanceSheet
    template_name = "balance_sheet/balance_sheet-form.html"
    success_url = reverse_lazy('balance_sheet:balance_sheet-list')
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["uid"] = uuid.uuid4().hex.upper()[0:6]
        return context


class BalanceSheetUpdateView(UpdateView):
    model = BalanceSheet
    template_name = "balance_sheet/balance_sheet-form.html"
    success_url = reverse_lazy('balance_sheet:balance_sheet-list')
    fields = "__all__"


class BalanceSheetDeleteView(DeleteView):
    model = BalanceSheet
    template_name = ""
    success_url = reverse_lazy('balance_sheet:balance_sheet-list')
