/* static/js/main.js */

document.addEventListener('DOMContentLoaded', () => {
    
    // --- LOGIKA UNTUK LINK NAVIGASI AKTIF ---
    const currentLocation = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-links a');

    navLinks.forEach(link => {
        if (link.pathname === currentLocation) {
            link.classList.add('active');
        }
    });

    // --- LOGIKA BARU UNTUK HAMBURGER MENU ---
    const navToggle = document.getElementById('nav-toggle');
    const navMenu = document.getElementById('nav-menu');

    // Pastikan elemennya ada
    if (navToggle && navMenu) {
        // Tambahkan event listener 'click'
        navToggle.addEventListener('click', () => {
            // Toggle class 'active' pada menu
            navMenu.classList.toggle('active');
        });
    }

    const profileToggle = document.getElementById('profile-toggle');
    const profileMenu = document.getElementById('profile-menu');
    const profileDropdown = document.getElementById('profile-dropdown');

    if (profileToggle && profileMenu) {
        
        // 1. Klik tombol profil untuk buka/tutup
        profileToggle.addEventListener('click', (e) => {
            // Hentikan 'event bubbling' agar tidak memicu 'click outside'
            e.stopPropagation(); 
            profileMenu.classList.toggle('active');
        });

        // 2. Klik di dalam menu tidak boleh menutup menu
        profileMenu.addEventListener('click', (e) => {
            e.stopPropagation();
        });

        // 3. Klik di mana saja di luar menu akan menutupnya
        document.addEventListener('click', (e) => {
            if (profileMenu.classList.contains('active')) {
                profileMenu.classList.remove('active');
            }
        });
    }

});