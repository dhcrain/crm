from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

from django.views.generic import TemplateView, CreateView, ListView, DetailView
from app_crm.models import Asset, Note


class IndexView(ListView):
    model = Asset
    template_name = "index.html"

    def get_queryset(self):
        return Asset.objects.all()


class CreateAssetView(CreateView):
    model = Asset
    fields = ['first_name', 'last_name', 'is_company', 'company', 'phone_number', 'email', 'street', 'street2', 'city', 'state', 'zip_code', 'country', 'website', 'twitter', 'facebook', 'linkedin', 'profile_picture']
    success_url = reverse_lazy("index_view")

    def form_valid(self, form):
        asset = form.save(commit=False)
        asset.user = self.request.user
        return super(CreateAssetView, self).form_valid(form)


class AssetDetailView(DetailView):
    model = Asset

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(AssetDetailView, self).get_context_data(**kwargs)
        context["notes"] = Note.objects.all()
        return context


class CreateNoteView(CreateView):
    model = Note
    fields = ['note_is_about', 'note', 'note_picture', 'note_file']
    success_url = reverse_lazy('note_list_view')


class NoteListView(ListView):
    model = Note


class NoteDetailView(DetailView):
    model = Note


class CreateTagView(CreateView):
    model = Tag
    fields = ['user', 'tag']
    success_url = reverse_lazy('tag_list_view')


class TagListView(ListView):
    model = Tag


class TagDetailView(DetailView):
    model = Tag


class CreateTaskView(CreateView):
    model = Task
    fields = ['creator', 'assigned_to', 'task_is_about', 'task', 'due_date', 'completed', 'created']
    success_url = reverse_lazy('task_list_view')


class TagListView(ListView):
    model = Task


class TagDetailView(DetailView):
    model = Task
