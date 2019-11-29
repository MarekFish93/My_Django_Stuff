from django.shortcuts import render
from AppTwo.models import User

# Create your views here.

def index(request):
    welcome_string = {'welcome':'Hello on my site. To se all users go to /users'}
    return render(request, 'AppTwo/index.html', context = welcome_string)

def users(request):
    users_list = User.objects.order_by('first_name')
    user_dict = {'user':users_list}

    return render(request, 'AppTwo/users.html', context = user_dict)
