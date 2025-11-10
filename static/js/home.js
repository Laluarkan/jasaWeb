/* static/js/home.js */

document.addEventListener('DOMContentLoaded', () => {
    
    console.log('Home.js dimuat, animasi scroll berulang aktif.');

    // 1. Pilih semua elemen yang ingin dianimasikan
    const sectionsToFade = document.querySelectorAll('.fade-in-section');

    // 2. Opsi untuk IntersectionObserver
    const observerOptions = {
        root: null, 
        rootMargin: '0px',
        threshold: 0.1 // 10% dari elemen harus terlihat
    };

    // 3. Buat observer-nya
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            
            // --- INI PERUBAHAN LOGIKANYA ---
            
            if (entry.isIntersecting) {
                // Saat elemen MASUK layar, tambahkan class
                entry.target.classList.add('is-visible');
            } else {
                // Saat elemen KELUAR layar, hapus class (untuk reset)
                entry.target.classList.remove('is-visible');
            }
            
            // Kita HAPUS baris 'observer.unobserve(entry.target);'
            // agar browser terus mengamati
        });
    }, observerOptions);

    // 4. Minta observer untuk mengamati setiap section
    sectionsToFade.forEach(section => {
        observer.observe(section);
    });

    const typingElement = document.getElementById('typing-effect');
    
    if (typingElement) {
        // 2. Opsi untuk Typed.js
        const options = {
            strings: [
                'Website Profesional',
                'Web Prediksi AI',
                'Toko Online Cepat',
                'Web Apapun yang Anda Butuhkan'
            ],
            typeSpeed: 50,     // Mengetik sedikit lebih cepat
            backSpeed: 30,     // Menghapus sedikit lebih cepat
            backDelay: 1800,   // Berpikir sedikit lebih LAMA sebelum menghapus
            startDelay: 500,   // Waktu tunggu sebelum mulai
            loop: true,
            smartBackspace: true 
        };

        // 3. Inisialisasi Typed.js
        new Typed('#typing-effect', options);
    }

});