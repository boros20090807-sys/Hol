from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post,Cotegory,Vidi
from django.core.paginator import Paginator
from .forms import ProductForms
from apps.filter import ProductFilter
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import get_user_model



def about(request):
    return render(request, 'main/about.html')

def deteilz(request, id):
    games = Post.objects.get(isActive=True, id=id)
    context = {
        'games': games
    }
    return render(request, 'main/deteilz.html', context)

def main(request):
    game_search = Post.objects.filter(isActive=True)
    search = request.GET.get('q')
    cotegory_id=request.GET.get('vidi')

    if cotegory_id:
        game_search=game_search.filter(cotegorys=cotegory_id)
    
    if search:
        game_search = game_search.filter(title__icontains=search)

    product=ProductFilter(request.GET,queryset=game_search)
    pagindtor = Paginator(product.qs, 10)
    page = request.GET.get('page')
    page_obj = pagindtor.get_page(page)
    cotegories=Vidi.objects.all()

    context={
    'posts': page_obj,
    'product':product,
    'cotegories':cotegories
    }
    
    return render(request, 'main/index.html',context)

def games_delate(request,id):
    delet_podt=Post.objects.get(id=id)
    return render(request,'main/deteilz.html',{'delet_podt':delet_podt})

def post_delete(request,id):
    product=Post.objects.get(id=id)
    if request.method=='POST':
            product.delete()
            messages.success(request,'ваш пост удалён')
            return redirect ('main')
    return render (request,'main/modal.html',{'product':product})

def add_product(request):
    if request.method == 'POST':
        form = ProductForms(request.POST, request.FILES)
        if form.is_valid():
            product=form.save(commit=False)
            product.slug=product.title.lower().replace(' ','-')
            product.save()
            form.save_m2m()
            messages.success(request,'ваш пост сохранён')
            return redirect('main')
    else:
        form = ProductForms()

    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)

def update_deteilz(request,id):
    product=Post.objects.get(id=id)
    if request.method=='POST':
        form=ProductForms(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product=form.save(commit=False)
            product.slug=product.title.lower().replace(' ','-')
            product.save()
            form.save_m2m()
            messages.success(request,'ваш пост изменён')
        return redirect('main')
    else:
        form=ProductForms(instance=product,initial={
            'title':product.title,
            'text':product.text,
            'slug':product.slug,
            'cotegory':product.cotegory,
            'image':product.image,
            'count':product.count
        })
    contex={
        'form':form,
        'product':product,
    }
    return render(request,'updaet.html',contex)

def login_view(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(request, phone=phone, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Вы успешно вошли в аккаунт!')
            return redirect('main')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль!')
            return redirect('login')

    return render(request, 'profil/login.html')

def logout_view(request):
    logout(request) 
    
    messages.error(request, 'вы вышли из аккаунта!')
    return redirect('main')

def regist(request):
    if request.method=='POST':
        username=request.POST.get('phone')
        pasword=request.POST.get('pasword')
        pasword1=request.POST.get('pasword1')
        if pasword != pasword1:
            messages.error(request,'пороли не совпадают!')
            return redirect('regist')
        if User.objects.filter(username=username).exists():
            messages.error(request,'такой аккаунт уже существует!')
            return redirect('regist')
        
        user=User.objects.create_user(
            username=username,
            password=pasword,
        )
        login(request, user)
        messages.success(request,'вы успешно зашли в аккаунт!') 
        return redirect('main')
    return render(request, 'profil/regist.html')  
  
@login_required
def profil(request):
    user=request.user
    if request.method=='POST':
        user.email=request.POST.get('email')
        user.first_name=request.POST.get('first_name')
        user.last_name=request.POST.get('last_name')

        user.save()

        messages.success(request,'вы успешно обновили профил')

    context={
        'user':user
    }
    return render(request,'profil/profil.html',context)

@login_required
def update_password(request):
    if request.method =='POST':
        old_password=request.POST.get('old_password')
        new_password=request.POST.get('new_password')
        new_password2=request.POST.get('new_password2')

        if not request.user.check_password(old_password):

            messages.error(request,'не верный старый пороль')

            return redirect('update_password')
        
        if new_password!=new_password2:

            messages.error(request,'пороли не совпадают')
        
            return redirect('update_password')
        
        if len(new_password)<8:

            messages.error(request,'пороль меньше чем 8 символов')
                    
            return redirect('update_password')

        request.user.set_password(new_password)

        request.user.save()

        update_session_auth_hash(request,request.user)

        messages.success(request,'пароль успешно изменён')

        return redirect('profil')
    
    return render(request,'profil/update_password.html')


    
