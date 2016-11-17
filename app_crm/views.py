from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

from django.views.generic import TemplateView, CreateView
# from app_crm.models import Customer


class IndexView(TemplateView):
    template_name = "index.html"

class CreateCustomerView(CreateView):
    # model = Customer
    fields = ['asset', 'notes']
    success_url = reverse_lazy("index_view")

    def form_valid(self, form):
        customer = form.save(commit=False)
        customer.user = self.request.user
        return super(CreateCustomerView, self).form_valid(form)

#'first_name', 'last_name', 'phone_number', 'email', 'website', 'street', 'street2', 'city', 'state', 'country',
