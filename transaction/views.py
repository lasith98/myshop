import uuid
from datetime import datetime

from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

# Create your views here.
from account.models import Account
from transaction.models import Transaction


class TransactionListView(ListView):
    model = Transaction
    template_name = "transaction/transaction-list.html"
    date_error = ''
    query = ''
    from_ = ''
    to = ''

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        self.date_error = ''
        self.query = ''
        self.from_ = ''
        self.to = ''
        if query != '':
            self.query = query
            return super(TransactionListView, self).get_queryset().filter(transaction_id=query)
        form = self.request.GET.get('from', '')
        to = self.request.GET.get('to', '')

        if form != '' and to != '':
            self.from_ = form
            self.to = to

            if datetime.strptime(form, '%Y-%m-%d') >= datetime.strptime(to, '%Y-%m-%d'):
                self.date_error = "To date cannot be earlier than from date!"
                return None
            else:
                return super(TransactionListView, self).get_queryset().filter(date__range=(form, to))

        return super(TransactionListView, self).get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['delete_url'] = reverse('transaction:transaction-delete', kwargs={'pk': 1})
        context['date_error'] = self.date_error
        context['query'] = self.query
        context['from'] = self.from_
        context['to'] = self.to
        return context


class TransactionCreateView(CreateView):
    model = Transaction
    template_name = "transaction/transaction-form.html"
    success_url = reverse_lazy('transaction:transaction-list')
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["uid"] = uuid.uuid4().hex.upper()[0:6]
        context["accounts"] = Account.objects.all()

        return context


class TransactionUpdateView(UpdateView):
    model = Transaction
    template_name = "transaction/transaction-form.html"
    success_url = reverse_lazy('transaction:transaction-list')
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["accounts"] = Account.objects.all()

        return context


class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = ""
    success_url = reverse_lazy('transaction:transaction-list')
