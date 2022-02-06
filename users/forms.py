from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class UserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "phone_number")