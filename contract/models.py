# contract/models.py
from django.db import models
from django.contrib.auth.models import User

class Contract(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Menunggu Pembayaran'),
        ('In Progress', 'Sedang Dikerjakan'),
        ('Review', 'Tahap Review Klien'),
        ('Completed', 'Selesai'),
    )

    # Menghubungkan kontrak ini dengan User yang login
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=200)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project_name} - {self.user.username}"