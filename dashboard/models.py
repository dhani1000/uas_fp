from django.db import models

#create
class Jenis(models.Model):
    nama=models.CharField(max_length=50)
    ket=models.TextField()

    def __str__(self):
        return self.nama

class Barang(models.Model):
    kodebrg=models.CharField(max_length=8, default="BRG" )
    nama=models.CharField(max_length=50)
    stok=models.IntegerField()
    harga=models.BigIntegerField()
    link_gbr=models.CharField(max_length=50, blank=True)
    waktu_posting=models.DateTimeField(auto_now_add=True)
    jenis_id=models.ForeignKey(Jenis, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return "{}. {}. {}. {}. {}".format(self.kodebrg,self.nama,self.stok,self.harga,self.link_gbr)

class Pinjam(models.Model):
    id_buku=models.CharField(max_length=10)
    nama=models.CharField(max_length=10)
    tglpinjam=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "{}. {}".format(self.id_buku,self.nama)
    
class Kembali(models.Model):
    id_buku=models.CharField(max_length=10)
    nama=models.CharField(max_length=10)
    tglkembali=models.DateTimeField(auto_now_add=True)
    kondisi=models.CharField(max_length=10)

    def __str__(self):
        return "{}. {}. {}".format(self.id_buku,self.nama,self.kondisi)

class Detailtrans(models.Model):
    kodetrans=models.CharField(max_length=10)
    kodebrg=models.CharField(max_length=8)
    qty=models.IntegerField()
    subtotal=models.BigIntegerField()

    def __str__(self):
        return "{}. {}".format(self.kodetrans,self.kodebrg)

class Member(models.Model):
    idmbr=models.CharField(max_length=25)
    nama=models.CharField(max_length=25)
    alamat=models.CharField(max_length=30)
    

    def __str__(self):
        return "{}. {}".format(self.idmbr,self.nama,self.alamat)
