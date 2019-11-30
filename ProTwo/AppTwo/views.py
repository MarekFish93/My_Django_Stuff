from django.shortcuts import render
from AppTwo.forms import MyNewForm

# Create your views here.

def index(request):
    welcome_string = {'welcome':'Hello on my site. To se all users go to /users'}
    return render(request, 'AppTwo/index.html', context = welcome_string)

# def users(request):
#     users_list = User.objects.order_by('first_name')
#     user_dict = {'user':users_list}
#
#     return render(request, 'AppTwo/users.html', context = user_dict)

def show_form(request):
    form = MyNewForm()

    if request.method == 'POST':
        form = MyNewForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print('Error for invalid')

    return render(request, 'AppTwo/users.html', {'form': form})
