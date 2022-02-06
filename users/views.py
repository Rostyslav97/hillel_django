from django.contrib.auth import get_user_model
from .forms import UserSignUpForm
from django.http.response import HttpResponse
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView

User = get_user_model()

def users (requests):
    users = User.objects.all()
    results = ", ".join(user.username for user in users)
    return HttpResponse(results)

class SignUpView(CreateView):
    form_class = UserSignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"