from django.db import migrations

# GANTI INI DENGAN DOMAIN RENDER ANDA YANG SEBENARNYA
# Pastikan ini nama domain Anda yang benar (misal: webkan-wmnm.onrender.com)
RENDER_DOMAIN = 'webkan-wmnm.onrender.com' 
SITE_NAME = 'Web_Kan'


def update_site_domain(apps, schema_editor):
    """
    Mengambil Site default (ID=1) dan memperbaruinya
    dari 'example.com' menjadi domain Render kita.
    """
    Site = apps.get_model('sites', 'Site')
    
    try:
        # Cari site ID=1 (yang default-nya example.com)
        default_site = Site.objects.get(pk=1)
        
        # Perbarui field-nya
        default_site.domain = RENDER_DOMAIN
        default_site.name = SITE_NAME
        default_site.save()
        
        print(f"\nBerhasil memperbarui Site ID=1 ke {RENDER_DOMAIN}")
        
    except Site.DoesNotExist:
        # Jika (karena alasan aneh) tidak ada, buat baru
        print(f"\nSite ID=1 tidak ditemukan. Membuat site baru: {RENDER_DOMAIN}")
        Site.objects.create(pk=1, domain=RENDER_DOMAIN, name=SITE_NAME)


class Migration(migrations.Migration):

    # Kita harus pastikan migrasi 'sites' bawaan Django
    # sudah berjalan SEBELUM skrip ini berjalan.
    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        # Menjalankan fungsi Python kustom kita
        migrations.RunPython(update_site_domain),
    ]