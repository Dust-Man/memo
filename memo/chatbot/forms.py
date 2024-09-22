from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile  # Asegúrate de importar tu modelo Profile

class CreateUserForm(UserCreationForm):
    full_name = forms.CharField(
        max_length=255, 
        required=True, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Full name',
            'class': 'form-control',
        })
    )
    emergency_phone = forms.CharField(
        max_length=15, 
        required=True, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Emergency contact',
            'class': 'form-control',
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'full_name', 'emergency_phone']

    # Sobrescribir el método save() para guardar los datos en el modelo Profile
    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.save()  # Guardar el usuario primero

        # Guardar los datos adicionales en Profile
        full_name = self.cleaned_data['full_name']
        emergency_phone = self.cleaned_data['emergency_phone']

        # Crear o actualizar el perfil del usuario
        profile, created = Profile.objects.get_or_create(user=user)
        profile.full_name = full_name
        profile.emergency_phone = emergency_phone
        profile.save()

        return user
