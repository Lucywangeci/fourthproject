from django.contrib import admin
from .models import ContactMessage, Hero, About, Event, Blog, TeamMember, Testimonial, Appointment, Student

# Register your models here.

admin.site.register(ContactMessage)
admin.site.register(Hero)
admin.site.register(About)
admin.site.register(Event)
admin.site.register(Blog)
admin.site.register(TeamMember)
admin.site.register(Testimonial)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['parent_name', 'appointment_type', 'appointment_date', 'duration', 'payment_option', 'amount_to_pay']
    search_fields = ['parent_name', 'appointment_type']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email"]
