from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .forms import CustomUserCreationForm
from django.http import JsonResponse
from .forms import AppointmentForm, RegisterUserForm
import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Hero, ContactMessage, Child, Service, Program, Testimonial, TeamMember, Event, Blog, Appointment, About
from .models import Student
from django.contrib import messages
from django.db.models import Q

from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee


def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'form.html', {'form': form})


def show(request):
    employees = Employee.objects.all()
    return render(request, "show.html", {'employees': employees})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'employee': employee})


def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")

def index2(request):
    students = Student.objects.all()
    search_query = ""
    if request.method == "POST":
        if "create" in request.POST:
            name = request.POST.get("name")
            email = request.POST.get("email")
            Student.objects.create(
                name=name,
                email=email
            )
            messages.success(request, "Student added successfully")

        elif "update" in request.POST:
            id = request.POST.get("id")
            name = request.POST.get("name")
            email = request.POST.get("email")
            student = Student.objects.get(id=id)
            student.name = name
            student.email = email
            student.save()
            messages.success(request, "student updated successfully")

        elif "delete" in request.POST:
            id = request.POST.get("id")
            Student.objects.get(id=id).delete()
            messages.success(request, "student deleted successfully")

        elif "search" in request.POST:
            search_query = request.POST.get("query")
            students = Student.objects.filter(Q(name__icontains=search_query) | Q(email__icontains=search_query))

    context = {"students": students, "search_query": search_query}
    return render(request, "index2.html", context=context)


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('app:index') # Redirect to a success page.                ...
        else:
             messages.success(request, ("An error occurre please check your username and password"))# Return an 'invalid login' error message.
             return redirect('register:login')

    else:
        return render(request, 'authenticate/login.html', {'nav':'login'})

def logout_user(request):
    logout(request)
    return redirect('app:login')

def user_register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            # phone = form.cleaned_data['phone']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,'registration successfully')
            return redirect('app:index')
    else:
        form = RegisterUserForm()
    return render(request, 'authenticate/user_register.html',{'nav':'register', 'form':form})


@csrf_exempt
def create_appointment(request):
    if request.method == 'GET':
        return render(request, 'create_appointment.html')

    if request.method == 'POST':
        form = AppointmentForm(json.loads(request.body))
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Appointment created successfully'})

        else:
            errors = {field: form.errors[field][0] for field in form.errors}
            return JsonResponse({'error': errors}, status=400)


@csrf_exempt
def create_appointment(request):
    if request.method == 'GET':
        return render(request, 'create_appointment.html')

    if request.method == 'POST':
        data = json.loads(request.body)
        parent_name = data.get('parent_name')
        appointment_date = data.get('appointment_date')

        if timezone.now() >= timezone.datetime.strptime(appointment_date, '%Y-%m-%d %H:%M:%S'):
            return JsonResponse({'error': 'Appointment date must be in the future'}, status=400)

        appointment = Appointment(parent_name=parent_name, appointment_date=appointment_date)
        appointment.save()

        return redirect('appointment_list')

def get_appointments(request):
    if request.method == 'GET':
        appointments = Appointment.objects.all()
        appointments_list = [{'id': appointment.id, 'parent_name': appointment.parent_name,
                              'appointment_date': appointment.appointment_date.strftime('%Y-%m-%d %H:%M:%S')}
                             for appointment in appointments]
        return render(request, 'appointment_list.html', {'appointments': appointments_list})

@csrf_exempt
def update_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)

    if request.method == 'PUT':
        data = json.loads(request.body)
        parent_name = data.get('parent_name')
        appointment_date = data.get('appointment_date')

        if timezone.now() >= timezone.datetime.strptime(appointment_date, '%Y-%m-%d %H:%M:%S'):
            return JsonResponse({'error': 'Appointment date must be in the future'}, status=400)

        appointment.parent_name = parent_name
        appointment.appointment_date = appointment_date
        appointment.save()

        return JsonResponse({'message': 'Appointment updated successfully'})

    return render(request, 'update_appointment.html', {'appointment': appointment})

@csrf_exempt
def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)

    if request.method == 'DELETE':
        appointment.delete()
        return JsonResponse({'message': 'Appointment deleted successfully'})

    return render(request, 'cancel_appointment.html', {'appointment': appointment})



def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to your existing home page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to your login page
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})




def home(request):
    # Your existing home view logic
    return render(request, 'index.html')
def index(request):
    # Retrieve data for each section
    hero_data = Hero.objects.first() if Hero.objects.exists() else None
    about_data = About.objects.first() if About.objects.exists() else None
    events_data = Event.objects.all()[:3]
    blog_data = Blog.objects.all()[:3]
    team_data = TeamMember.objects.all()[:4]
    testimonials_data = Testimonial.objects.all()[:3]
    services_data = Service.objects.all()

    # Additional context data, if needed
    context = {
        'navbar': 'index',
        'hero_data': hero_data,
        'about_data': about_data,
        'events_data': events_data,
        'blog_data': blog_data,
        'team_data': team_data,
        'testimonials_data': testimonials_data,
    }

    return render(request, 'index.html', context)


def about(request):
    abouts = About.objects.all()
    context = {'navbar': 'about'}
    return render(request, 'about.html', context)

def blog(request):
    blogs = Blog.objects.all()
    context = {'navbar': 'blog'}
    return render(request, 'blog.html', context)

def contact(request):
    data = ContactMessage.objects.all()
    context = {'navbar': 'contact'}
    return render(request, 'contact.html', context)

def event(request):
    events = Event.objects.all()
    context = {'navbar': 'event'}
    return render(request, 'event.html', context)

def program(request):
    programs = Program.objects.all()
    context = {'navbar': 'program'}
    return render(request, 'program.html', context)

def service(request):
    services = Service.objects.all()
    context = {'navbar': 'service'}
    return render(request, 'service.html', context)



def team(request):
    teams = TeamMember.objects.all()
    context = {'navbar': 'team'}
    return render(request, 'team.html', context)

def testimonial(request):
    testimonials = Testimonial.objects.all()
    context = {'navbar': 'testimonial'}
    return render(request, 'testimonial.html', context)

