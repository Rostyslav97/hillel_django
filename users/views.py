from django.contrib.auth import get_user_model
from django.http.response import HttpResponse

from core.models import Post

User = get_user_model()

def users (requests):
    users = User.objects.all()
    results = ", ".join(user.username for user in users)
    return HttpResponse(results)