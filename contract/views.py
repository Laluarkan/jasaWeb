# contract/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required # <-- KUNCI KEAMANAN
from .models import Contract

@login_required # <-- Memaksa user login sebelum bisa akses
def contract_list_view(request):
    # Ambil HANYA kontrak milik user yang sedang login
    contracts = Contract.objects.filter(user=request.user)

    context = {
        'contracts': contracts
    }
    return render(request, 'contract/contract_list.html', context)