from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render,HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from .forms import LoginForm, UserRegistration,ArticleRegistrationForm,ArticleUpdateForm
from .models import Article
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required

# Create your views here.
def articles_list(request):

    article_list = Article.objects.all().order_by('-published')
    #PAGINATIONS

    paginator = Paginator(article_list, 6)
    page = request.GET.get('page')

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)


    return render(request,'Articles/sample.html',{'article_list':articles, 'page':page})


def article_details(request, slug):
    article = get_object_or_404(Article, slug=slug)

    return render(request,'Articles/details.html',{'article':article}) 

def user_login(request):
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user= authenticate(request,username=cd['Username'], password=cd['Password'])
        if user is not None:
            login(request,user)
            return render(redirect('Articles/sample.html'))
        else:
            return HttpResponse("INVALID LOGIN PARAMETERS")
    else:
        form=LoginForm()
        return render(request,'registration/login.html', {'form':form})

# REGISTRATION FORM

def register(request):
    if request.method == "POST":
        userform = UserRegistration(request.POST)

        if userform.is_valid():

            new_user = userform.save(commit=False)
            new_user.set_password(userform.cleaned_data['password1'])
            new_user.save()
            return render(request,'registration/donereg.html',{'new_user':new_user})
    else:
        userform = UserRegistration
        return render(request,'registration/register.html',{'userform':userform})


#adding article views
@login_required
def add_article(request):
    if request.method == "POST":

        add_form =  ArticleRegistrationForm(request.POST)

        if add_form.is_valid():

            article = add_form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('articles:articles_list')
 
    else:
        add_form =  ArticleRegistrationForm()

        return render(request, 'Articles/add_article.html', {'add_form':add_form} )


def update_article(request,slug):
    article = get_object_or_404(Article, slug=slug)
    form = ArticleUpdateForm(request.POST or None, instance=article)

    if form.is_valid():
        form.save()
        return redirect('articles:articles_list')
   
    return render(request,'Articles/update.html',{'form':form})


def delete_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article.delete()
    return redirect('articles:articles_list')