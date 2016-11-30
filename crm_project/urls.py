from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout, login


from app_crm.views import IndexView, CreateAssetView, AssetDetailView, CreateNoteView, NoteListView, NoteDetailView
from app_crm.views import CreateTagView, TagListView, TagDetailView, CreateTaskView, TaskListView, TaskDetailView, ProfilePageView
from app_crm.views import AssetUpdateView, CreateCompanyView, CompanyListView, CompanyDetailView, NoteUpdateView, TagUpdateView
from app_crm.views import DashboardPageView



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^accounts/profile/$', ProfilePageView.as_view(), name="profile_page_view"),
    url(r'^dashboard/$', login_required(DashboardPageView.as_view()), name="dashboard_page_view"),
    url(r'^create_asset$', login_required(CreateAssetView.as_view()), name="create_asset_view"),
    url(r'^update_asset/(?P<pk>\d+)/$', login_required(AssetUpdateView.as_view()), name="asset_update_view"),
    url(r'^asset_list/(?P<pk>\d+)/$', login_required(AssetDetailView.as_view()), name="asset_detail_view"),
    url(r'^create_company$', login_required(CreateCompanyView.as_view()), name="create_company_view"),
    url(r'^company_list$', login_required(CompanyListView.as_view()), name="company_list_view"),
    url(r'^company_list/(?P<pk>\d+)/$', login_required(CompanyDetailView.as_view()), name="company_detail_view"),
    url(r'^create_note$', login_required(CreateNoteView.as_view()), name="create_note_view"),
    url(r'^note_list$', login_required(NoteListView.as_view()), name="note_list_view"),
    url(r'^note_list/(?P<pk>\d+)/$', login_required(NoteDetailView.as_view()), name="note_detail_view"),
    url(r'^update_note/(?P<pk>\d+)/$', login_required(NoteUpdateView.as_view()), name="note_update_view"),
    url(r'^create_tag$', login_required(CreateTagView.as_view()), name="create_tag_view"),
    url(r'^tag_list$', login_required(TagListView.as_view()), name="tag_list_view"),
    url(r'^tag_list/(?P<pk>\d+)/$', login_required(TagDetailView.as_view()), name="tag_detail_view"),
    url(r'^update_tag/(?P<pk>\d+)/$', login_required(TagUpdateView.as_view()), name="tag_update_view"),
    url(r'^create_task$', login_required(CreateTaskView.as_view()), name="create_task_view"),
    url(r'^task_list$', login_required(TaskListView.as_view()), name="task_list_view"),
    url(r'^task_list/(?P<pk>\d+)/$', login_required(TaskDetailView.as_view()), name="task_detail_view"),
    url(r'^calendar/', include('schedule.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
