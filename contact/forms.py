from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        # Tampilkan semua field KECUALI 'created_at'
        exclude = ('created_at',) 
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nama Anda'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Anda'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subjek Pesan'}),
            'message': forms.Textarea(attrs={'placeholder': 'Isi Pesan Anda...', 'rows': 5}),
        }