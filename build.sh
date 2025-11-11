#!/usr/bin/env bash
# Keluar jika ada error
set -o errexit

# 1. Install dependencies
pip install -r requirements.txt

# 2. Kumpulkan file statis
python manage.py collectstatic --noinput

# 3. Jalankan migrasi (dengan urutan yang benar)
python manage.py migrate auth
python manage.py migrate

# 4. Buat Superuser (Hanya jika belum ada)
# Ini menjalankan kode Python singkat menggunakan 'shell'
# Ini akan membaca environment variables (DJANGO_SUPERUSER_...)
python manage.py shell -c "
from django.contrib.auth import get_user_model
import os

User = get_user_model()
username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

if not User.objects.filter(username=username).exists():
    print(f'Membuat superuser baru: {username}')
    User.objects.create_superuser(username, email, password)
else:
    print(f'Superuser {username} sudah ada.')
"