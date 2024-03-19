from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.user_register, name='register'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('event/', views.event, name='event'),
    path('program/', views.program, name='program'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('index2/', views.index2, name="index2"),
    path('appointments/', views.create_appointment, name='create_appointment'),
    path('appointment_lists/', views.get_appointments, name='get_appointments'),
    path('appointments/<int:appointment_id>/', views.update_appointment, name='update_appointment'),
    path('appointments/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),
    path('emp', views.emp, name='emp'),
    path('show', views.show, name='show'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]
