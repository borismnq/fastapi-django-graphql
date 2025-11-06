from django.db import models

# Create your models here.

class ExampleModel(models.Model):
    """
    Example model - replace with your own models
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "example_model"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
