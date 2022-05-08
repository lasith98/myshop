from django.urls import path

from core.views import index, login_request, logout_request

app_name = 'core'
urlpatterns = [
    path('', index, name='index'),
    path('login', login_request, name='login'),
    path('logout', logout_request, name='logout'),

]
