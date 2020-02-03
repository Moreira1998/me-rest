from django import forms
from apps.staff.models import Staff, Role
from django.contrib.auth.models import User


# -------------------------------------------------------->
# Forms User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        labels = {
            'username': 'Nombre de usuario',
            'last_name': 'Nombre',
            'first_name': 'Apellido',
            'password': 'Password',
            'email': 'Correo electronico'
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


# -------------------------------------------------------->
# Forms role

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = (
            'name',
            'description',
        )
        labels = {
            'name': 'Nombre Del Rol',
            'description': 'Descripcion del rol',
        }


# -------------------------------------------------------->
# Form staff

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = [
            'idStaff',
            'name',
            'direction',
            'birthday',
            'phone',
            'phone2',
            'email',
            'user',
            'role',
            'photo',

        ]

        labels = {
            'idStaff': 'Id',
            'name': 'Name',
            'direction': 'Dirreccion',
            'birthday': 'Nacimiento',
            'phone': 'Telefono',
            'phone2': 'Celular',
            'email': 'Correo Electronico',
            'user': 'Usuario',
            'role': 'Rol',
            'photo': 'Foto',

        }

        widgets = {
            'idStaff': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Id personal',

                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre Completo',
                }
            ),
            'direction': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Dirreccion',
                }
            ),
            'birthday': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Fecha de nacimiento',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Telefono',
                }
            ),
            'phone2': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Celular',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Celular',
                }
            ),
            'user': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'role': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),

        }
