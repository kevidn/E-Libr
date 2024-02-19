from django.urls import path
from django.contrib.auth.views import *
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('buku/tambah/', tambah_buku, name='tambah_buku'),
    path('edit/<int:id_buku>', edit_buku, name='edit_buku'),
    path('buku/hapus/<int:id_buku>', hapus_buku, name='hapus_buku'),
    path('detail/<slug:slugField>', detail, name='detail_buku'),
    
    path('kategori/', kategori, name='kategori_buku'),
    path('kategori/tambah', tambah_kategori, name='tambah_kategori'),
    
    path('koleksi/', koleksi, name='koleksi_buku'),
    path('koleksi/tambah', tambah_koleksi, name='tambah_koleksi'),
    
    path('ulasan/', data_ulasan, name='data_ulasan_buku'),
    path('ulasan/tambah', tambah_ulasan, name='tambah_ulasan'),
    path('ulasan/edit/<int:id_ulasan>', edit_ulasan, name='edit_ulasan'),
    path('ulasan/hapus/<int:id_ulasan>', hapus_ulasan, name='hapus_ulasan'),
    
    path('buku/pinjam', pinjam_buku, name='pinjam_buku'),
    path('pinjam/data', data_peminjaman, name='data_peminjaman'),
    path('pinjam/laporan', laporan_peminjaman, name='laporan_peminjaman'),
    path('pinjam/edit/<int:id_pinjam>', edit_pinjam, name='edit_pinjam'),
    path('pinjam/hapus/<int:id_pinjam>', hapus_pinjam, name='hapus_pinjam'),
    path('pinjam/dikembalikan/<int:id_pinjam>', dikembalikan_pinjam, name='dikembalikan_pinjam'),
    path('pinjam/terlambat/<int:id_pinjam>', terlambat_pinjam, name='terlambat_pinjam'),
    path('pinjam/dipinjam/<int:id_pinjam>', dipinjam_pinjam, name='dipinjam_pinjam'),
    
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('accounts/signup/', signup, name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)