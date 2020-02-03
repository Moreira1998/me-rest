from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404

from apps.staff.models import Staff, User
from apps.staff.forms import StaffForm, UserForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# ------------------------------------------------------------------------------------>
# view Staff

class StaffList(ListView):
    model = Staff
    template_name = 'staff/staff_list.html'
    context_object_name = 'staff_list'
    queryset = Staff.objects.all()


class StaffNew(CreateView):
    model = Staff
    form_class = StaffForm
    template_name = 'staff/staff_form.html'
    success_url = reverse_lazy('#')


# ------------------------------------------------------------------------------------>
# view User

class UserList(ListView):
    Model = User
    template_name = 'staff/user/user_list.html'
    context_object_name = 'user_list'
    queryset = User.objects.all()


class UserCreate(CreateView):
    model = User
    form_class = UserForm
    template_name = 'staff/user/user_form.html'
    success_url = reverse_lazy('staff:user_list')


class UserUpdate(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'staff/user/user_form.html'
    success_url = reverse_lazy('staff:user_list')


class UserDelete(DeleteView):
    model = User
    form_class = UserForm
    template_name = 'staff/user/user_confirm_delete.html'
    success_url = reverse_lazy('staff:user_list')
