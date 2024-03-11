from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Task, Tag
from .forms import TaskForm, TagForm


class HomeView(ListView):
    model = Task
    template_name = "home.html"
    ordering = ["-is_done", "-created_at"]


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"


class TaskDetailView(DetailView):
    model = Task
    template_name = "task_detail.html"


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "task_confirm_delete.html"
    success_url = reverse_lazy("home")


class TaskStatusView(UpdateView):
    model = Task
    template_name = "task_form.html"

    def post(self, request, *args, **kwargs):
        task = self.get_object()
        task.is_done = not task.is_done
        task.save()
        return redirect(reverse_lazy("home"))


class TagListView(ListView):
    model = Tag
    template_name = "tag_list.html"


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = "tag_form.html"


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "tag_form.html"


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "tag_confirm_delete.html"
    success_url = reverse_lazy("tag_list")