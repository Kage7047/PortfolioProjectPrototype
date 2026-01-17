from django.db import models


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('branding', 'Branding'),
        ('ui-ux', 'UI/UX Design'),
        ('print', 'Print Design'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    main_image = models.ImageField(upload_to='projects/')  # Main thumbnail
    client = models.CharField(max_length=200, blank=True)  # NEW: Client name
    project_url = models.URLField(blank=True)  # NEW: Live project link
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class ProjectImage(models.Model):
    """Additional images for a project (gallery)"""
    project = models.ForeignKey(Project, related_name='gallery_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/gallery/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)  # For sorting images

    def __str__(self):
        return f"Image for {self.project.title}"

    class Meta:
        ordering = ['order']


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

    class Meta:
        ordering = ['-created_at']