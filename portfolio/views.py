from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, ContactMessage
from django.contrib import messages


def home(request):
    """Homepage with project grid"""
    projects = Project.objects.all()

    category = request.GET.get('category')
    if category:
        projects = projects.filter(category=category)

    return render(request, 'portfolio/home.html', {
        'projects': projects,
        'selected_category': category
    })


def project_detail(request, project_id):
    """Individual project page with all images"""
    project = get_object_or_404(Project, id=project_id)

    # Get all gallery images for this project
    gallery_images = project.gallery_images.all()

    return render(request, 'portfolio/project_detail.html', {
        'project': project,
        'gallery_images': gallery_images
    })


def about(request):
    """About page"""
    return render(request, 'portfolio/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # Show success message
        messages.success(request, 'Thanks! Your message has been sent. I\'ll get back to you soon.')
        return redirect('contact')

    return render(request, 'portfolio/contact.html')