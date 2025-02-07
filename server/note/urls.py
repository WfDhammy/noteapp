from django.urls import path
from . import views 


urlpatterns = [
    path('',views.main, name='main'),
    path('detail/<int:note_id>', views.detail, name='detail'),
    path("signup", views.signup, name="signup"),
    path("logout", views.logout_user, name="logout"),
    path("login", views.login_user, name="login"),
    path('create_note', views.create_note, name='create_note'),
    path('note_list', views.note_list, name='note_list'),
    path('edit/<int:note_id>', views.edit, name='edit'),
    path('delete/<int:note_id>', views.delete, name='delete'),
]