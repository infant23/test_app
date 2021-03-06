from django.urls import path


from . import views


urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('profile/', views.RestrictedUserDetail.as_view()),
    path('register/', views.UserRegisterView.as_view()),
    path('confirm/', views.UserConfirmView.as_view()),
]
