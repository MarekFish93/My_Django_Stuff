from django.conf.urls import url
from AppTwo import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^users/', views.show_form, name = 'users')
]
