from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

from django.conf import settings

from .models import *
from .forms import *

from django.http import FileResponse
import io
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def index(request):
    buku = Buku.objects.all()
    
    kumpulan = {
        'buku': buku,
    }
    return render(request, 'content/index.html', kumpulan)
    
def detail(request, slugField):
    buku = Buku.objects.get(slug=slugField)
    
    kumpulan = {
        'title':'Detail Buku',
        'buku': buku,
    }
    
    return render(request, 'content/detail.html', kumpulan)

def laporan_peminjaman(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont('Helvetica', 14)
    
    datas = Pinjam.objects.all()
    
    lines = []
    
    for data in datas:
        lines.append(data.buku.judul)
        lines.append(data.user.username)
        lines.append(f"data.tanggal_peminjaman")
        lines.append(f"data.tanggal_pengembalian")
        lines.append(data.status)
        lines.append(" ")
    
    for line in lines:
        textob.textLine(line)
        
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    
    return FileResponse(buf, as_attachment=True, filename='laporan_peminjaman.pdf')

@permission_required('app.view_kelompok', login_url='/login', raise_exception=True)
@login_required(login_url='/login')
def kategori(request):
    kategori = Kelompok.objects.all()
    
    kumpulan = {
        'title':'Data Kategori',
        'kategori':kategori,
    }
    
    return render(request, 'content/kategori.html', kumpulan)

@permission_required('app.add_kategori', login_url='/login', raise_exception=True)
@login_required(login_url='/login')
def tambah_kategori(request):
    if request.POST:
        form = TambahKategori(request.POST)
        if form.is_valid:
            form.save()
            
            messages.success(request, 'Kategori berhasil ditambah!')
            form = TambahKategori()
            
            kumpulan = {
                'title':'Form Tambah Kategori',
                'form':form,
            }
            
            return render(request, 'content/tambah_kategori.html', kumpulan)
    else:
        form = TambahKategori()
        
    kumpulan = {
        'title':'Form Tambah Kategori',
        'form':form,
    }
    
    return render(request, 'content/tambah_kategori.html', kumpulan)

@permission_required('app.view_koleksi', login_url='/login', raise_exception=True)
@login_required(login_url='/login')
def koleksi(request):
    koleksi = Koleksi.objects.filter(user=request.user)

    kumpulan = {
        'title':'Koleksi Buku',
        'koleksi':koleksi,
    }
    
    return render(request, 'content/koleksi.html', kumpulan)

@permission_required('app.add_koleksi', login_url='/login', raise_exception=True)
@login_required(login_url='/login')
def tambah_koleksi(request):
    if request.POST:
        form = TambahKoleksi(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            
            messages.success(request, 'Koleksi berhasil ditambahkan!')
            form = TambahKoleksi()
            
            kumpulan = {
                'title':'Form Tambah Koleksi',
                'form':form,
            }
            return render(request, 'content/tambah_koleksi.html', kumpulan)
    else:
        form = TambahKoleksi()
        
    kumpulan = {
        'title':'Form Tambah Koleksi',
        'form':form,
    }
    return render(request, 'content/tambah_koleksi.html', kumpulan)
        
@permission_required('app.delete_koleksi', login_url='/login', raise_exception=True)
@login_required(login_url='/login')
def hapus_koleksi(id_koleksi):
    koleksi = Koleksi.objects.filter(id=id_koleksi)
    koleksi.delete()
    
    redirect('koleksi.html')

@permission_required('app.add_ulasan', login_url='/login', raise_exception=True)
@login_required(login_url='/login')
def tambah_ulasan(request):
    if request.POST:
        form = TambahUlasan(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            
            messages.success(request, 'Terima kasih ulasannya!')
            form = TambahUlasan()
            
            kumpulan = {
                'title':'Form Ulasan Buku',
                'form':form,
            }
            
            return render(request, 'content/ulasan.html', kumpulan)
    else:
        form = TambahUlasan()
    
    kumpulan = {
        'title':'Form Ulasan Buku',
        'form':form,
    }
    
    return render(request, 'content/ulasan.html', kumpulan)

@permission_required('app.view_ulasan', login_url='/login', raise_exception=True)
@login_required(login_url='/login')
def data_ulasan(request):
    ulasan = Ulasan.objects.all()
    
    kumpulan = {
        'title':'Ulasan Buku',
        'ulasan':ulasan,
    }
    
    return render(request, 'content/data_ulasan_buku.html', kumpulan)

@permission_required('app.edit_ulasan', login_url='/login', raise_exception=True)
@login_required(login_url='/login')
def edit_ulasan(request, id_ulasan):
    ulasan = Ulasan.objects.get(id=id_ulasan)
    if request.POST:
        form = EditUlasan(request.POST, instance=ulasan)
        if form.is_valid:
            form.save()
            
            messages.success(request, 'Ulasan berhasil diperbaharui!')
            
            return redirect('edit_ulasan', id_ulasan=id_ulasan)
    else:
        form = EditUlasan(instance=ulasan)
    
    kumpulan = {
        'title':'Form Edit Ulasan Buku',
        'form':form,
        'ulasan':ulasan,
    }
    return render(request, 'content/edit_ulasan.html', kumpulan)

@permission_required('app.delete_ulasan', login_url='/login', raise_exception=True)
@login_required(login_url='/login')
def hapus_ulasan(request, id_ulasan):
    ulasan = Ulasan.objects.filter(id=id_ulasan)
    ulasan.delete()
    
    return redirect('data_ulasan_buku')

@permission_required('app.add_buku', login_url='/login', raise_exception=True)
@login_required(login_url='/login')
def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.pendata = request.user
            form.save()
            
            messages.success(request, 'Data buku berhasil ditambah!')
            form = FormBuku()
            
            kumpulan = {
                'form': form,
                'title':'Form Tambah Buku',
            }
            return render(request, 'content/form.html', kumpulan)
    else:
        form = FormBuku()
        
    kumpulan = {
        'form': form,
        'title':'Form Tambah Buku',
    }
    
    return render(request, 'content/form.html', kumpulan)

@permission_required('app.edit_buku', login_url='/login', raise_exception=True)
@login_required(login_url='/login')
def edit_buku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    if request.POST:
        form = FormBuku(request.POST, request.FILES, instance=buku)
        if form.is_valid():
            form = form.save(commit=False)
            form.pendata = request.user
            form.save()
            messages.success(request, 'Data berhasil diperbaharui!')
            
            return redirect('edit_buku', id_buku=id_buku)
    else:
        form = FormBuku(instance=buku)
    
    kumpulan = {
        'title':'Form Edit Buku',
        'form': form,
        'buku': buku,
    } 
    return render(request, 'content/edit.html', kumpulan)

@permission_required('app.add_pinjam', login_url='/login', raise_exception=True)
@login_required(login_url='/login')
def pinjam_buku(request):
    if request.POST:
        form = PinjamBuku(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            
            messages.success(request, 'Buku Berhasil Dipinjam!')
            form = PinjamBuku()
            
            kumpulan = {
                'title':'Form Pinjam Buku',
                'form':form,
            }
            
            return render(request, 'content/pinjam.html', kumpulan)
    else:
        form = PinjamBuku()
    
    kumpulan = {
        'title':'Form Pinjam Buku',
        'form':form,
    }
    return render(request, 'content/pinjam.html', kumpulan)

@permission_required('app.edit_pinjam', login_url='/login', raise_exception=True)
@login_required(login_url='/login')
def edit_pinjam(request, id_pinjam):
    pinjam = Pinjam.objects.get(id=id_pinjam)
    if request.POST:
        form = EditPinjam(request.POST, instance=pinjam)
        if form.is_valid:
            form.save()
            
            messages.success(request, 'Data peminjaman berhasil diperbaharui!')
            
            return redirect('edit_pinjam', id_pinjam=id_pinjam)
    else:
        form = EditPinjam(instance=pinjam)
    
    kumpulan = {
        'title':'Form Edit Peminjaman Buku',
        'form':form,
        'pinjam':pinjam,
    }
    return render(request, 'content/edit_pinjam.html', kumpulan)

@permission_required('app.delete_pinjam', login_url='/login', raise_exception=True)
@login_required(login_url='/login')
def hapus_pinjam(request, id_pinjam):
    pinjam = Pinjam.objects.filter(id=id_pinjam)
    pinjam.delete()
    
    return redirect('data_peminjaman')

@permission_required('app.edit_pinjam', login_url='/login', raise_exception=True)
@login_required(login_url='/login')
def dikembalikan_pinjam(request, id_pinjam):
    pinjam = Pinjam.objects.get(id=id_pinjam)
    pinjam.status = "Dikembalikan"
    pinjam.save()
    
    return redirect('data_peminjaman')

@permission_required('app.edit_pinjam', login_url='/login', raise_exception=True)
@login_required(login_url='/login')
def terlambat_pinjam(request, id_pinjam):
    pinjam = Pinjam.objects.get(id=id_pinjam)
    pinjam.status = "Terlambat"
    pinjam.save()
    
    return redirect('data_peminjaman')

@permission_required('app.edit_pinjam', login_url='/login', raise_exception=True)
@login_required(login_url='/login')
def dipinjam_pinjam(request, id_pinjam):
    pinjam = Pinjam.objects.get(id=id_pinjam)
    pinjam.status = "Dipinjam"
    pinjam.save()
    
    return redirect('data_peminjaman')

@permission_required('app.view_pinjam', login_url='/login', raise_exception=True)
@login_required(login_url='/login')
def data_peminjaman(request):
    data = Pinjam.objects.all()
    
    kumpulan = {
        'title':'Data Peminjaman Buku',
        'data':data,
    }
    
    return render(request, 'content/data_peminjaman.html', kumpulan)

@permission_required('app.delete_buku', login_url='/login', raise_exception=True)
@login_required(login_url='/login')
def hapus_buku(request, id_buku):
    buku = Buku.objects.filter(id=id_buku)
    buku.delete()
    
    return redirect('index')

def signup(request):
    if request.POST:
        form = SignUp(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('login')
        else:
            messages.error(request, 'Terjadi kesalahan!')
            return redirect('signup')
    else:
        form = SignUp()
        
    kumpulan = {
        'form': form,
        'title':'Sign Up',
    }
    return render(request, 'registration/signup.html', kumpulan)