from django.contrib.auth.tokens import default_token_generator   
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site

def send_confirmation_email(request, user):
    token = default_token_generator.make_token(user)
    uid = user.pk 
    domain = get_current_site(request)

    subject = 'sdsd'
    message = render_to_string('registration/account_activation_email.html',
    {
        'user':user,
        'domain':domain,
        'uid':uid,
        'token':token
    })
    user.email_user(subject, message)