from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import *
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.views.generic import FormView
from django.contrib.auth.views import LoginView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUpView(FormView):
    template_name = "base/signup.html"
    form_class = SignupForm
    success_url = reverse_lazy('candidate_list')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    
class LoginView(LoginView):
    template_name = "base/login.html"
    form_class = LoginForm

    
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse_lazy('login'))


class CandidateDirectoryListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = CandidateDirectory
    template_name = 'base/candidate_list.html' 
    context_object_name = 'candidates'
    ordering = ['-created_date'] 

class CandidateDirectoryDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = CandidateDirectory
    template_name = 'base/candidate_detail.html'  
    context_object_name = 'candidate'

class CandidateDirectoryCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = CandidateDirectory
    form_class = CandidateDirectoryForm
    template_name = 'base/candidate_form.html'  
    def form_valid(self, form):
        candidate = form.save()
        return HttpResponseRedirect(reverse('candidate_detail', args=[candidate.pk]))

class CandidateEditView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = CandidateDirectory
    form_class = CandidateDirectoryForm
    template_name = 'base/candidate_edit.html'
    success_url = reverse_lazy('candidate_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['candidate'] = self.object
        return context
    
class CandidateDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = CandidateDirectory
    template_name = 'base/delete_candidate.html'
    success_url = reverse_lazy('candidate_list')