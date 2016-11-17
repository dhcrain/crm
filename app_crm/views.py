from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

from django.views.generic import TemplateView, CreateView, ListView
from app_crm.models import Asset


class IndexView(TemplateView):
    template_name = "index.html"

class CreateAssetView(CreateView):
    model = Asset
    fields = ['user', 'is_company', 'first_name', 'last_name', 'company', 'phone_number', 'email', 'street', 'street2', 'city', 'state', 'zip_code', 'country', 'website', 'twitter', 'facebook', 'linkedin', 'profile_picture']
    success_url = reverse_lazy("index_view")

    def form_valid(self, form):
        customer = form.save(commit=False)
        customer.user = self.request.user
        return super(CreateCustomerView, self).form_valid(form)

class AssetListView(ListView):
    model = Asset

    def get_queryset(self):
        return Asset.objects.all()
