from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm


class UserRegisterView(generic.CreateView):
    # form_class = UserCreationForm
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    pass


class UserEditView(generic.UpdateView):
    # form_class = UserCreationForm
    form_class = EditProfileForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
        pass
    pass
