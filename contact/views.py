from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.conf import settings
import requests 
from django.core.mail import send_mail # Pertahankan impor ini untuk menghindari error jika ada kode lama yang memanggilnya

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

# --- FUNGSI NOTIFIKASI TELEGRAM ---
def send_telegram_notification(subject, name, email, whatsapp_number, message_content):
    """ Mengirim pesan ke Bot Telegram Anda. """
    
    # Kumpulkan isi pesan dalam format Markdown
    message = (
        f"🚨 *PESAN BARU DARI WEBSITE* 🚨\n\n"
        f"Subjek: *{subject}*\n"
        f"Nama: {name}\n"
        f"Email: {email}\n"
        f"WA/HP: *{whatsapp_number or 'Tidak Dicantumkan'}*\n"
        f"----------------------------\n"
        f"Isi:\n{message_content}"
    )

    token = settings.TELEGRAM_BOT_TOKEN
    chat_id = settings.TELEGRAM_CHAT_ID
    
    if not token or not chat_id:
        print("ERROR: Token atau Chat ID Telegram tidak ditemukan di settings.")
        return False

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    
    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'Markdown' 
    }

    try:
        # Kirim permintaan HTTP POST ke Telegram API
        response = requests.post(url, data=payload, timeout=5)
        response.raise_for_status()
        return True
    except requests.RequestException as e:
        # Ini akan dicetak ke log Render jika gagal, tetapi TIDAK akan menyebabkan error 500
        print(f"ERROR TELEGRAM: Gagal mengirim pesan. {e}")
        return False

# --- FUNGSI UTAMA (HANYA SATU) ---
def contact_view(request):
    
    if request.method == 'POST':
        # --- Handle data yang disubmit (POST) ---
        form = ContactForm(request.POST)
        if form.is_valid():
            
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            whatsapp_number = form.cleaned_data['whatsapp_number']
            subject = form.cleaned_data['subject']
            message_content = form.cleaned_data['message']

            # 1. Simpan pesan ke database
            form.save() 
            
            # 2. KIRIM NOTIFIKASI TELEGRAM
            send_telegram_notification(subject, name, email, whatsapp_number, message_content)
            
            # 3. Redirect ke halaman sukses
            return redirect(reverse('contact:contact_success'))
    
    else:
        # --- Handle halaman yang baru dibuka (GET) ---
        initial_data = {} # Mulai dengan data awal kosong
    
        # 1. Cek parameter 'service' (dari halaman Layanan)
        service_key = request.GET.get('service')
        if service_key in SERVICE_SUBJECTS:
            initial_data['subject'] = SERVICE_SUBJECTS.get(service_key)
            initial_data['message'] = SERVICE_MESSAGES.get(service_key)
        
        # 2. Cek apakah user sudah login (Fitur pengisian otomatis)
        if request.user.is_authenticated:
            # Isi 'name' dan 'email' dari data user yang login
            initial_data['name'] = request.user.first_name or request.user.username
            initial_data['email'] = request.user.email

        # 3. Buat form baru dengan data awal
        form = ContactForm(initial=initial_data) 

    # Tampilkan halaman dengan form
    return render(request, 'contact/contact_form.html', {'form': form})


def contact_success_view(request):
    # Halaman "terima kasih"
    return render(request, 'contact/contact_success.html')