from django.conf.urls import url
from django.contrib import admin

from app_crm.views import IndexView, CreateCustomerView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^create_customer$', CreateCustomerView.as_view(), name="create_customer_view")
]
