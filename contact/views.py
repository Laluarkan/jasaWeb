from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Definisikan "kamus" untuk subjek dan pesan Anda
SERVICE_SUBJECTS = {
    'profil': 'Pertanyaan tentang Website Profil Perusahaan',
    'ecommerce': 'Pertanyaan tentang Toko Online (E-commerce)',
    'maintenance': 'Pertanyaan tentang Jasa Maintenance',
    'uiux': 'Pertanyaan tentang Desain UI/UX',
    'custom_app': 'Pertanyaan tentang Web Aplikasi Kustom (AI/IoT)',
    'blog': 'Pertanyaan tentang Blog & Portofolio'
}

SERVICE_MESSAGES = {
    'profil': 'Halo, saya tertarik dengan layanan pembuatan Website Profil Perusahaan Anda. Bisakah kita diskusikan lebih lanjut?',
    'ecommerce': 'Halo, saya tertarik dengan layanan pembuatan Toko Online. Bisakah Anda jelaskan fiturnya dan estimasi biayanya?',
    'maintenance': 'Halo, saya ingin bertanya tentang paket Jasa Maintenance Website Anda.',
    'uiux': 'Halo, saya tertarik dengan layanan Desain UI/UX untuk proyek saya.',
    'custom_app': 'Halo, saya punya ide untuk Web Aplikasi Kustom (AI/IoT) dan ingin berkonsultasi dengan Anda.',
    'blog': 'Halo, saya ingin membuat Blog/Portofolio pribadi. Apa saja yang perlu saya siapkan?'
}


# --- HANYA ADA SATU FUNGSI INI ---
def contact_view(request):
    
    if request.method == 'POST':
        # --- Handle data yang disubmit (POST) ---
        form = ContactForm(request.POST)
        if form.is_valid():
            
            # 1. Ambil data bersih dari form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message_content = form.cleaned_data['message']

            # 2. Simpan pesan ke database
            form.save() 

            # 3. Siapkan isi email yang akan Anda terima
            email_subject = f"Pesan Baru dari Website: {subject}"
            email_body = f"""
            Anda menerima pesan baru dari:
            
            Nama: {name}
            Email: {email}
            
            Isi Pesan:
            {message_content}
            """
            
            # 4. Tentukan pengirim dan penerima
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [settings.EMAIL_HOST_USER] # Kirim ke email Anda sendiri

            # 5. Kirim email!
            try:
                send_mail(email_subject, email_body, from_email, recipient_list)
            except Exception as e:
                # Jika gagal, cetak error di terminal (untuk debugging)
                print(f"Error saat mengirim email: {e}") 
            
            # 6. Redirect ke halaman sukses
            return redirect(reverse('contact:contact_success'))
    
    else:
        # --- Handle halaman yang baru dibuka (GET) ---
        initial_data = {} # Mulai dengan data awal kosong
    
        # 1. Cek parameter 'service' dari URL (dari halaman Layanan)
        service_key = request.GET.get('service')
        if service_key in SERVICE_SUBJECTS:
            initial_data['subject'] = SERVICE_SUBJECTS.get(service_key)
            initial_data['message'] = SERVICE_MESSAGES.get(service_key)
        
        # 2. === INI LOGIKA YANG HILANG ===
        # Cek apakah user sudah login
        if request.user.is_authenticated:
            initial_data['email'] = request.user.email

        # 3. Buat form baru dengan data awal yang sudah kita siapkan
        form = ContactForm(initial=initial_data) 

    # Tampilkan halaman dengan form (bisa kosong, bisa terisi)
    return render(request, 'contact/contact_form.html', {'form': form})


def contact_success_view(request):
    # Halaman "terima kasih" (tanda kurung berlebih sudah dihapus)
    return render(request, 'contact/contact_success.html')