from django.db import models

class TeamMember(models.Model):
    """
    Model to represent a team member for the About Us page.
    """
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='team_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Team Members'

    def __str__(self):
        return self.name


class CompanyInfo(models.Model):
    """
    Model to represent company information for the About Us page.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    logo = models.ImageField(upload_to='company_logos/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    """
    Model to represent customer testimonials for the About Us page.
    """
    author_name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return self.author_name
