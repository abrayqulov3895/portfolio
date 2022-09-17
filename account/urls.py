from django.urls import path

from account.views import blog, contact, home, portfolio, resume

urlpatterns = [
    path('',home,name='home'),
    path('resume/',resume,name='resume'),
    path('portfolio/',portfolio,name='portfolio'),
    path('blog/',blog,name='blog'),
    path('contact/',contact,name='contact'),
]
