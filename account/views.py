import uuid
from datetime import datetime

from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

# Create your views here.
from account.models import Account


class AccountListView(ListView):
    model = Account
    template_name = "account/account-list.html"
    date_error = ''
    query = ''
    from_ = ''
    to = ''

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        self.query = ''

        if query != '':
            self.query = query
            return super(AccountListView, self).get_queryset().filter(account_no=query)
        return super(AccountListView, self).get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['delete_url'] = reverse('account:account-delete', kwargs={'pk': 1})
        context['query'] = self.query

        return context


class AccountCreateView(CreateView):
    model = Account
    template_name = "account/account-form.html"
    success_url = reverse_lazy('account:account-list')
    fields = "__all__"


class AccountUpdateView(UpdateView):
    model = Account
    template_name = "account/account-form.html"
    success_url = reverse_lazy('account:account-list')
    fields = "__all__"


class AccountDeleteView(DeleteView):
    model = Account
    template_name = ""
    success_url = reverse_lazy('account:account-list')
