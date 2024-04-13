from django.db import models

class ContactMessage(models.Model):
    """
    Model to store contact messages submitted by users.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f'{self.name} - {self.subject}'


class Department(models.Model):
    """
    Model to represent different departments for contact purposes.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.name


class ContactOption(models.Model):
    """
    Model to represent different contact options for users.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Contact Option'
        verbose_name_plural = 'Contact Options'

    def __str__(self):
        return self.name


class ContactForm(models.Model):
    """
    Model to define custom contact forms with specific options.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    options = models.ManyToManyField(ContactOption)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Contact Form'
        verbose_name_plural = 'Contact Forms'

    def __str__(self):
        return self.name
