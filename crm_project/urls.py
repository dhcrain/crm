from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


from app_crm.views import IndexView, CreateAssetView, AssetListView, AssetDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', AssetListView.as_view(), name="asset_list_view"),
    url(r'^create_asset$', CreateAssetView.as_view(), name="create_asset_view"),
    # url(r'^asset_list$', AssetListView.as_view(), name="asset_list_view"),
    url(r'^asset_list/(?P<pk>\d+)/$', AssetDetailView.as_view(), name="asset_detail_view")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
