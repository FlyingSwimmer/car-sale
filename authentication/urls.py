from django.urls import path

from authentication.views import login, signup

urlpatterns = [
    path('login/', login),
    path('signup/', signup),

]
