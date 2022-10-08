from django.http.response import HttpResponseBadRequest
from django.contrib.auth.tokens import default_token_generator  
from django.shortcuts import render, redirect, get_object_or_404
 
from .forms import SignUpForm, User
from .utils import send_confirmation_email

# Create your views here.
def signup(request):
    if request.method == 'POST':

        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            send_confirmation_email(request, user)

            return render(request, 'registration/signup_success.html')

    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html',{'form':form})

def activate_email(request, pk, token):
    user = get_object_or_404(User, pk=pk)
    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()

        return redirect('login')

    else:
        return HttpResponseBadRequest('Bad Token')


# def show_token(request, pk):
#      if request.user.is_authenticated:
#         user = get_object_or_404(User, pk=pk)
#         return render(request, 'registration/showtoken.html',{'user':user})
