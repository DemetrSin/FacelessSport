from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login as django_login
from django.views import View
from .models import CustomUser

oauth = OAuth()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)


def index(request):
    return redirect('home')


def home(request):
    return render(request, 'home.html')


class CallbackView(View):
    def get(self, request):
        token = oauth.auth0.authorize_access_token(request)
        user_info = oauth.auth0.userinfo(token=token)
        user = self.get_or_create_user(user_info)
        django_login(request, user)
        request.session["user"] = token
        return redirect(request.build_absolute_uri(reverse("index")))

    @staticmethod
    def get_or_create_user(user_info):
        name = user_info.get('name')
        locale = user_info.get('locale')
        picture = user_info.get('picture')
        email = user_info.get('email')
        auth0_id = user_info.get('sub')
        try:
            user = CustomUser.objects.get(email=email)
            user.name = name
            user.locale = locale
            user.picture = picture
            user.save()
        except CustomUser.DoesNotExist:
            user = CustomUser.objects.create(
                name=name,
                locale=locale,
                picture=picture,
                email=email,
                auth0_id=auth0_id
            )
        return user


def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("callback"))
    )


def logout(request):
    request.session.clear()
    return redirect('home')
