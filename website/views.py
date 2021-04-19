from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import RegisterModel
from .forms import RegisterForm, UpdateForm


class Home(CreateView):
    model = RegisterModel
    form_class = RegisterForm
    template_name = 'website/home.html'


class StudentListView(ListView):
    model = RegisterModel
    template_name = 'website/login_view.html'
    ordering = ['enrollment_number']


class StudentDetailView(DetailView):
    model = RegisterModel
    template_name = 'website/student_view.html'

    def get_context_data(self, *args, **kwargs):
        student = get_object_or_404(RegisterModel, enrollment_number=self.kwargs['pk'])
        context = {'student': student}
        return context


class StudentUpdateView(UpdateView):
    model = RegisterModel
    form_class = UpdateForm
    template_name = 'website/student_update_view.html'


class StudentDeleteView(DeleteView):
    model = RegisterModel
    template_name = 'website/student_delete_view.html'
    success_url = reverse_lazy('student_list')

    def get_context_data(self, *args, **kwargs):
        student = get_object_or_404(RegisterModel, enrollment_number=self.kwargs['pk'])
        context = {'student': student}
        return context
