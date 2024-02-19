from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User, Group, Permission, AbstractUser

class CustomUser(AbstractUser):
    alamat = models.TextField()
    groups = models.ForeignKey(Group, on_delete=models.CASCADE)
    
    user_permissions = models.ForeignKey(
        Permission, on_delete=models.CASCADE, related_name='custom_user_permissions'
    )
    
    def __str__(self):
        return self.alamat

class Kelompok(models.Model):
    nama = models.CharField(max_length=255)
    keterangan = models.TextField()

    def __str__(self):
        return self.nama
    
class Pinjam(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    buku = models.ForeignKey('Buku', on_delete=models.CASCADE)
    tanggal_peminjaman = models.DateField()
    tanggal_pengembalian = models.DateField()
    status = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.user.username} - {self.buku.judul}"


class Buku(models.Model):
    judul = models.CharField(max_length=255)
    penulis = models.CharField(max_length=255)
    penerbit = models.CharField(max_length=255)
    pendata = models.ForeignKey(User, on_delete=models.CASCADE)
    kelompok_buku = models.ForeignKey('Kelompok', on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='cover/', null=True)
    tahun_terbit = models.IntegerField(null=True)
    slug = models.SlugField(blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.judul)
        return super(Buku, self).save(*args, **kwargs)

    def __str__(self):
        return self.judul

class Koleksi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    buku = models.ForeignKey('Buku', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username} - {self.bukus.judul}"
    
class Ulasan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    buku = models.ForeignKey('Buku', on_delete=models.CASCADE)
    ulasan = models.TextField()
    rating = models.IntegerField()
    
    def __str__(self):
        return f"{self.user.username} - {self.buku.judul}"