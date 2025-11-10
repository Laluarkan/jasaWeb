from django.db import models
from django.urls import reverse

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # Pastikan pip install Pillow
    image = models.ImageField(upload_to='projects/') 
    url = models.URLField(blank=True, null=True, help_text="Link ke website live (opsional)")
    date_completed = models.DateField()

    class Meta:
        ordering = ['-date_completed'] # Tampilkan yang terbaru dulu

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Ini membuat URL untuk detail proyek, misal: /portfolio/3/
        return reverse('portfolio:project_detail', kwargs={'pk': self.pk})