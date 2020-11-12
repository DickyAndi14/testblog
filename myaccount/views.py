from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .filters import ImageFilter
from .forms import PostForm

# Create your views here.

def home(request):
    pics=Image.objects.all()
    post_form = PostForm()
    posts = PostModel.objects.all()
 
    context = {
    'page_title':'Semua Komentar',
    'posts':posts,

    }

    if request.method == 'POST':
        PostModel.objects.create(
        Nama = request.POST['Nama'],
        Komentar = request.POST['Komentar'],
    )

    pics = ImageFilter(
        request.GET,
        queryset=Image.objects.all()
    )

    context['pics'] = pics

    return render(request, 'account/dashboard.html', context=context)  

def posting(request):
    return render(request, 'account/posting.html')
def accoustic(request):
    return render(request, 'account/accoustic.html')
def classic(request):
    return render(request, 'account/classic.html')
def elektrik(request):
    return render(request, 'account/elektrik.html') 

def upload(request):
    pics=Image.objects.all()

    context = {'pics':pics}

    pics = ImageFilter(
        request.GET,
        queryset=Image.objects.all()
    )

    context['pics'] = pics

    return render(request, 'account/readmore.html', context=context)

def cate(request):
    pics=Image.objects.all()

    context = {'pics':pics}

    pics = ImageFilter(
        request.GET,
        queryset=Image.objects.all()
    )

    context['pics'] = pics

    return render(request, 'account/cate.html', context=context)      
