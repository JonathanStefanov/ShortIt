from django.urls import path
from shortener import views

urlpatterns = [
    path('', views.home),
    path('g/<shortUrl>', views.redirect_guest),
    path('a/<shortUrl>', views.redirect_auth),
    path('signup', views.signup),
    path('signin', views.signin),
    path('logout', views.logout),
    path('dashboard', views.dashboard),
    path('dashboard/new_link', views.dashboard_new_link),
    path('dashboard/my_links', views.dashboard_my_links),
    ]
