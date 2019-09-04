from django.shortcuts import render
from forth_app.models import User
from forth_app.forms import UserForm
from forth_app import forms

# Create your views here.
def index(request):
    return render(request,'forth_app/index.html')

def users(request):
    user_list = User.objects.order_by('ulast_name')
    user_dict = {'user_records':user_list}
    return render(request, 'forth_app/users.html', context=user_dict)

def form_add_user(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return users(request)
            #take use back to user list

    return render(request,'forth_app/form.html',{'new_user':form})
