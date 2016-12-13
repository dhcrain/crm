from django.core.urlresolvers import reverse_lazy

from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView
from app_crm.models import Asset, Note, Tag, Task, Company


class IndexView(TemplateView):
    template_name = "index.html"


class DashboardPageView(ListView):
    model = Asset
    template_name = "dashboard.html"

    # def get_queryset(self):
    #     return self.model.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(DashboardPageView, self).get_context_data(**kwargs)
        context["assets"] = Asset.objects.filter(user=self.request.user)
        context["tasks"] = Task.objects.filter(creator=self.request.user)
        context["notes"] = Note.objects.filter(note_creator=self.request.user)
        context["tags"] = Tag.objects.all()
        context["companies"] = Company.objects.all()
        return context


class calendar(TemplateView):
    template_name = "calendar.html"


class ProfilePageView(UpdateView):
    fields = ["first_name", "last_name", "email"]
    success_url = reverse_lazy("dashboard_page_view")

    def get_object(self, queryset=None):
        return self.request.user


class CreateAssetView(CreateView):
    model = Asset
    fields = ['first_name', 'last_name', 'is_company', 'company',
              'phone_number', 'email', 'street', 'street2', 'city', 'state', 'zip_code',
              'country', 'website', 'twitter', 'facebook', 'linkedin', 'profile_picture',
              'tags']
    success_url = reverse_lazy("dashboard_page_view")

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
        context["tags"] = Tag.objects.all()
        context["tasks"] = Task.objects.all()
        return context


class AssetUpdateView(UpdateView):
    model = Asset
    template_name = 'app_crm/asset_update.html'
    fields = ['first_name', 'last_name', 'is_company', 'company',
              'phone_number', 'email', 'street', 'street2', 'city', 'state',
              'zip_code', 'country', 'website', 'twitter', 'facebook', 'linkedin',
              'profile_picture', 'tags']
    success_url = reverse_lazy("dashboard_page_view")

    def form_valid(self, form):
        asset = form.save(commit=False)
        asset.user = self.request.user
        return super(AssetUpdateView, self).form_valid(form)


class CreateCompanyView(CreateView):
    model = Company
    fields = ['name']
    success_url = reverse_lazy("dashboard_page_view")

    def form_valid(self, form):
        company = form.save(commit=False)
        company.user = self.request.user
        return super(CreateCompanyView, self).form_valid(form)


class CompanyListView(ListView):
    model = Company


class CompanyDetailView(DetailView):
    model = Company


class CreateNoteView(CreateView):
    model = Note
    fields = ['note_is_about', 'note', 'note_picture', 'note_file']
    success_url = reverse_lazy('dashboard_page_view')

    def form_valid(self, form):
        note = form.save(commit=False)
        note.note_creator = self.request.user
        return super(CreateNoteView, self).form_valid(form)


class NoteListView(ListView):
    model = Note

    def get_context_data(self, **kwargs):
        context = super(NoteListView, self).get_context_data(**kwargs)
        context["notes"] = Note.objects.filter(note_creator=self.request.user)
        return context


class NoteDetailView(DetailView):
    model = Note


class NoteUpdateView(UpdateView):
    model = Note
    template_name = "app_crm/note_update.html"
    fields = ['note_is_about', 'note', 'note_picture', 'note_file']
    success_url = reverse_lazy('dashboard_page_view')

    def form_valid(self, form):
        note = form.save(commit=False)
        note.note_creator = self.request.user
        return super(CreateNoteView, self).form_valid(form)


class CreateTagView(CreateView):
    model = Tag
    fields = ['tag']
    success_url = reverse_lazy('dashboard_page_view')

    def form_valid(self, form):
        tag = form.save(commit=False)
        tag.user = self.request.user
        return super(CreateTagView, self).form_valid(form)


class TagListView(ListView):
    model = Tag


class TagDetailView(DetailView):
    model = Tag


class TagUpdateView(UpdateView):
    model = Tag
    fields = ['tag']
    success_url = reverse_lazy('dashboard_page_view')


class CreateTaskView(CreateView):
    model = Task
    fields = ['assigned_to', 'task_is_about', 'task', 'due_date', 'completed']
    success_url = reverse_lazy('dashboard_page_view')

    def form_valid(self, form):
        task = form.save(commit=False)
        task.creator = self.request.user
        return super(CreateTaskView, self).form_valid(form)


class TaskListView(ListView):
    model = Task


class TaskDetailView(DetailView):
    model = Task


class TaskUpdateView(UpdateView):
    model = Task
    fields = ['assigned_to', 'task_is_about', 'task', 'due_date', 'completed']
    success_url = reverse_lazy('dashboard_page_view')

    def form_valid(self, form):
        task = form.save(commit=False)
        task.creator = self.request.user
        return super(CreateTaskView, self).form_valid(form)
