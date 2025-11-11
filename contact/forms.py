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
            'whatsapp_number': forms.TextInput(attrs={'placeholder': 'Nomor WhatsApp (Contoh: 0812xxxxxx)', 'required': 'True'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subjek Pesan'}),
            'message': forms.Textarea(attrs={'placeholder': 'Isi Pesan Anda...', 'rows': 5}),
        }