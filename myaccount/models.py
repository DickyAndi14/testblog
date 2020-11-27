from django.db import models


# Create your models here.
class Tag(models.Model):
    Nama=models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.Nama

class Image(models.Model):
    CATEGORY = (
        ('Gitar Akustik', 'Gitar Akustik'),
        ('Gitar Elektrik', 'Gitar Elektrik'),
        ('Gitar Classic', 'Gitar Classic'),
        )
    nama = models.TextField(max_length=1000) 
    deskripsi = models.TextField(max_length=3000)
    Tags= models.ManyToManyField(Tag)
    Category = models.CharField(max_length= 1000, null=True, choices=CATEGORY)
    image = models.ImageField(upload_to='static/%y')
    button = models.CharField(max_length=200)
    des = models.TextField(max_length= 5000)

    def __str__(self):
        return self.nama

class PostModel(models.Model):
    Nama = models.CharField(max_length=100)
    Komentar = models.TextField()

    def __str__(self):
        return self.Nama
