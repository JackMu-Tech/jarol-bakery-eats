from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import ContactMessage, Department, ContactForm
from .forms import ContactMessageForm, DepartmentForm, ContactFormForm
from django.views.generic import ListView,DetailView,CreateView

def contact_form(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactMessageForm()
    return render(request, 'contact_us/contact_form.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_us/contact_success.html')

class DepartmentListView(ListView):
    model = Department
    template_name = 'contact_us/department_list.html'
    context_object_name = 'departments'

class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'contact_us/department_detail.html'
    context_object_name = 'department'

class DepartmentCreateView(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'contact_us/department_form.html'
    success_url = reverse_lazy('department_list')

class ContactFormCreateView(CreateView):
    model = ContactForm
    form_class = ContactFormForm
    template_name = 'contact_us/contact_form_form.html'
    success_url = reverse_lazy('contact_success')
