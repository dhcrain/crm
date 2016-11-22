from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from app_crm.views import IndexView, CreateAssetView, AssetDetailView, CreateNoteView, NoteListView, NoteDetailView
from app_crm.views import CreateTagView, TagListView, TagDetailView, CreateTaskView, TaskListView, TaskDetailView, ProfilePageView
from app_crm.views import AssetUpdateView



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^accounts/profile/$', ProfilePageView.as_view(), name="profile_page_view"),
    url(r'^create_asset$', CreateAssetView.as_view(), name="create_asset_view"),
    url(r'^update_asset/(?P<pk>\d+)/$', AssetUpdateView.as_view(), name="asset_update_view"),
    url(r'^asset_list/(?P<pk>\d+)/$', AssetDetailView.as_view(), name="asset_detail_view"),
    url(r'^create_note$', CreateNoteView.as_view(), name="create_note_view"),
    url(r'^note_list$', NoteListView.as_view(), name="note_list_view"),
    url(r'^note_list/(?P<pk>\d+)/$', NoteDetailView.as_view(), name="note_detail_view"),
    url(r'^create_tag$', CreateTagView.as_view(), name="create_tag_view"),
    url(r'^tag_list$', TagListView.as_view(), name="tag_list_view"),
    url(r'^tag_list/(?P<pk>\d+)/$', TagDetailView.as_view(), name="tag_detail_view"),
    url(r'^create_task$', CreateTaskView.as_view(), name="create_task_view"),
    url(r'^task_list$', TaskListView.as_view(), name="task_list_view"),
    url(r'^task_list/(?P<pk>\d+)/$', TaskDetailView.as_view(), name="task_detail_view"),
    url(r'^calendar/', include('schedule.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
