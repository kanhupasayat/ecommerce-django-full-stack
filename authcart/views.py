from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from .utils import TokenGenerator,generate_token
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse







def signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        confirm_password = request.POST.get('pass2')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, 'signup.html')

        try:
            if User.objects.get(username=email):
                messages.error(request, "Email already exists")
                return render(request, 'signup.html')
        except User.DoesNotExist:
            user = User.objects.create_user(email, email, password)
            user.is_active = False
            user.save()
            
            email_subject = "Activate Your Account"
            activation_link = f"kanhupasayatweb/activate/{urlsafe_base64_encode(force_bytes(user.pk))}/{generate_token.make_token(user)}/"
            
            message = render_to_string('activate.html', {
                'user': user,
                'domain': 'kanhupasayatweb',
                'activation_link': activation_link,
            })

            email_message = EmailMessage(
                email_subject,
                message,
                settings.EMAIL_HOST_USER,
                [email],
            )
            email_message.send()
            
            messages.success(request, "Activate Your Account By Clicking The Link In Your Email")
            return redirect('/signup')

    return render(request, 'signup.html')


class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and generate_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.info(request, "Account Activated Successfully")
            return redirect('handlelogin')
        return render(request, 'activatefail.html')
    






def handlelogin(request):
    if request.method == "POST":
        username = request.POST.get('username')  # Match the name attribute in your HTML form
        password = request.POST.get('password')  # Match the name attribute in your HTML form

        myuser = authenticate(username=username, password=password)

        if myuser is not None:
            login(request, myuser)
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('handlelogin')

    return render(request, 'login.html')





def handlelogout(request):
    logout(request)
    messages.info(request, "Logout Success")
    return redirect('/')







