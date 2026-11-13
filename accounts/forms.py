from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User


def style_fields(form):
    """Добавляем Bootstrap-классы, чтобы формы выглядели нормально."""
    for field in form.fields.values():
        css = "form-select" if isinstance(field.widget, forms.Select) else "form-control"
        field.widget.attrs["class"] = css


class RegisterForm(UserCreationForm):
    role = forms.ChoiceField(label="Кто вы?", choices=User.Role.choices)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "role", "city", "phone")
        labels = {
            "username": "Имя пользователя (для входа)",
            "email": "Email",
            "city": "Город",
            "phone": "Телефон",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style_fields(self)


class StyledAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style_fields(self)
