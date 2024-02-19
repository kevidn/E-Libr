from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from app.models import *

# Form penambahan data buku.
class FormBuku(ModelForm):
    class Meta:
        model = Buku
        exclude = ('jumlah', 'pendata', 'koleksi', )
        
        widgets = { 
            'judul' : forms.TextInput({'class':'form-control'}),
            'penulis' : forms.TextInput({'class':'form-control'}),
            'penerbit' : forms.TextInput({'class':'form-control'}),
            'kelompok_buku' : forms.Select({'class':'form-control'}),
            'cover' : forms.FileInput({'class':'form-control'}),
        }

# Form meminjam salah satu buku.
class PinjamBuku(ModelForm):
    class Meta:
        model = Pinjam
        exclude = ('user', )
        
        widgets = {
            'buku' : forms.Select(choices=[(buku.id, buku.judul) for buku in Buku.objects.all()]),
            'tanggal_peminjaman' : forms.DateInput(attrs={'type':'date'}),
            'tanggal_pengembalian' : forms.DateInput(attrs={'type':'date'}),
            'status': forms.Select(choices=[('Dipinjam', 'Dipinjam'), ('Dikembalikan', 'Dikembalikan'), ('Terlambat','Terlambat')]),
        }

# Form mengedit salah satu buku.
class EditPinjam(ModelForm):
    class Meta:
        model = Pinjam
        exclude = ('user', 'buku', 'status', ) 
        
        widgets = {
            'tanggal_peminjaman' : forms.DateInput(attrs={'type':'date'}),
            'tanggal_pengembalian' : forms.DateInput(attrs={'type':'date'}),
        }
        
# Form memberikan ulasan mengenai salah satu buku.
class TambahUlasan(ModelForm):
    class Meta:
        model = Ulasan
        exclude = ('user', )
        
        widgets = {
            'buku': forms.Select(choices=[(buku.id, buku.judul) for buku in Buku.objects.all()]),
            'ulasan': forms.TextInput({'class':'form-control'}),
            'rating': forms.NumberInput({'class':'form-control','type':'number'}),
        }
        
# Form mengedit ulasan mengenai salah satu buku.
class EditUlasan(ModelForm):
    class Meta:
        model = Ulasan
        exclude = ('user', 'buku', )
        
        widgets = {
            'ulasan': forms.TextInput({'class':'form-control'}),
            'rating': forms.NumberInput({'class':'form-control','type':'number'}),
        }
        
# Form menambahkan koleksi untuk user.
class TambahKoleksi(ModelForm):
    class Meta:
        model = Koleksi
        fields = ['buku']
        
        widgets = {
            'buku': forms.Select(choices=[(buku.id, buku.judul) for buku in Buku.objects.all()]),
        }
       
    
# Form menambahkan kategori buku.
class TambahKategori(ModelForm):
    class Meta:
        model = Kelompok
        fields = ['nama', 'keterangan']
        
        widgets = {
            'nama' : forms.TextInput({'class':'form-control'}),
            'keterangan' : forms.TextInput({'class':'form-control'}),
        }

# Form melakukan registrasi user.
class SignUp(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'groups']
        
        widgets = {
            'groups': forms.Select(choices=[('administrator', 'administrator'), ('peminjam', 'peminjam')]),
        }