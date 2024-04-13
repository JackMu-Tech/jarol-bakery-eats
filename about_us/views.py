from django.shortcuts import render, get_object_or_404, redirect
from .models import TeamMember, CompanyInfo, Testimonial
from .forms import TeamMemberForm, CompanyInfoForm, TestimonialForm

def team_member_list(request):
    team_members = TeamMember.objects.all()
    return render(request, 'about_us/team_member_list.html', {'team_members': team_members})

def team_member_detail(request, pk):
    team_member = get_object_or_404(TeamMember, pk=pk)
    return render(request, 'about_us/team_member_detail.html', {'team_member': team_member})

def add_team_member(request):
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('team_member_list')
    else:
        form = TeamMemberForm()
    return render(request, 'about_us/team_member_form.html', {'form': form})

def edit_team_member(request, pk):
    team_member = get_object_or_404(TeamMember, pk=pk)
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, request.FILES, instance=team_member)
        if form.is_valid():
            form.save()
            return redirect('team_member_list')
    else:
        form = TeamMemberForm(instance=team_member)
    return render(request, 'about_us/team_member_form.html', {'form': form})

def delete_team_member(request, pk):
    team_member = get_object_or_404(TeamMember, pk=pk)
    if request.method == 'POST':
        team_member.delete()
        return redirect('team_member_list')
    return render(request, 'about_us/team_member_confirm_delete.html', {'team_member': team_member})

def company_info_detail(request):
    company_info = CompanyInfo.objects.first()
    return render(request, 'about_us/company_info_detail.html', {'company_info': company_info})

def edit_company_info(request):
    company_info = CompanyInfo.objects.first()
    if request.method == 'POST':
        form = CompanyInfoForm(request.POST, instance=company_info)
        if form.is_valid():
            form.save()
            return redirect('company_info_detail')
    else:
        form = CompanyInfoForm(instance=company_info)
    return render(request, 'about_us/edit_company_info.html', {'form': form})

def testimonial_list(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'about_us/testimonial_list.html', {'testimonials': testimonials})

def add_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimonial_list')
    else:
        form = TestimonialForm()
    return render(request, 'about_us/testimonial_form.html', {'form': form})

def edit_testimonial(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)
    if request.method == 'POST':
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            form.save()
            return redirect('testimonial_list')
    else:
        form = TestimonialForm(instance=testimonial)
    return render(request, 'about_us/testimonial_form.html', {'form': form})

def delete_testimonial(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)
    if request.method == 'POST':
        testimonial.delete()
        return redirect('testimonial_list')
    return render(request, 'about_us/testimonial_confirm_delete.html', {'testimonial': testimonial})
