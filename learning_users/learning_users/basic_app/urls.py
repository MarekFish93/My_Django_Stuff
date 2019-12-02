from django.urls import path, include
from basic_app import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'app_interface', views.app_interface)

app_name = 'basic_app'

urlpatterns = [
    # path('', include(router.urls)),
    path('register/', views.register, name = 'register'),
    path('user_login/', views.user_login, name = 'user_login'),
    path('api_auth/', include('rest_framework.urls', namespace = 'rest_framework'))
]
