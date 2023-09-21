from django.urls import path
from users import views

urlpatterns = [
    path('user/', views.get_user_data, name='get_user_data'),
    path('register/', views.register_api, name='register_api'),
    path('login/', views.login_api, name='login_api'),
    path('logout/', views.logout_api, name='logout_api')
]
