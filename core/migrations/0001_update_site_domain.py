from django.db import migrations
from django.conf import settings

APP_DOMAIN = 'webkan-wmnm.onrender.com'
SITE_NAME = 'Web_Kan'

def update_site_domain(apps, schema_editor):
    """
    Menggunakan update_or_create untuk memastikan Site ID=1
    memiliki domain dan nama yang benar.
    """
    Site = apps.get_model('sites', 'Site')
    
    Site.objects.update_or_create(
        # Cari Site dengan id=1 (yang diatur di settings.py)
        id=settings.SITE_ID,
        
        # Perbarui (atau buat) dengan nilai-nilai ini:
        defaults={
            'domain': APP_DOMAIN,
            'name': SITE_NAME
        }
    )
    
    print(f"\n[Migrasi Data] Berhasil mengatur Site ID=1 ke {APP_DOMAIN}")

def remove_site(apps, schema_editor):
    """ Dibiarkan kosong, tidak perlu rollback data ini """
    pass

class Migration(migrations.Migration):

    # Ini adalah file migrasi pertama di 'core', jadi tidak
    # ada dependensi ke 'core' lain.
    dependencies = [
        # Kita HANYA perlu memastikan migrasi 'sites' bawaan Django
        # sudah berjalan SEBELUM skrip ini berjalan.
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        # Menjalankan fungsi Python kustom kita
        migrations.RunPython(update_site_domain, remove_site),
    ]