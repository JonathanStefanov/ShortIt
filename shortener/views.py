from django.shortcuts import render
from django.contrib.auth import logout as django_logout
from django.http import HttpResponseRedirect, Http404
from .forms import ShortUrlGuestForm, SignUpForm, SignInForm, ShortUrlAuthForm
from .models import ShortUrlGuest, ShortUrlAuth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import random
import string

def home(request):
    '''Home Page'''
    Valid = False
    shortUrlRandomString = ""
    form = ShortUrlGuestForm(request.POST or None) # Getting the form

    if form.is_valid():  # If the form is valid
        shorturlguest = ShortUrlGuest()
        shorturlguest.longUrl = form.cleaned_data["longUrl"] # Setting the value of the long url
        shortUrlRandomString = generate(5) # Generationg a random string for the sort url
        try: # Creating another short url if the short url already exists
            ShortUrlGuest.objects.get(shortUrl=shortUrlRandomString)
            shortUrlRandomString = generate(5)
        except ShortUrlGuest.DoesNotExist:
            pass

        shorturlguest.shortUrl = shortUrlRandomString # Giving to shorturl the value of the unique generated random string
        shorturlguest.save()
        Valid = True

    return render(request, 'shortener/home.html', {'Valid' : Valid, 'url' : shortUrlRandomString, 'form' : form})



def redirect_guest(request, shortUrl):
    '''Redirect Funtion'''
    try: # Testing if the link exists
        ShortUrlGuest.objects.get(shortUrl=shortUrl)
    except ShortUrlGuest.DoesNotExist:
        raise Http404
    longUrl = ShortUrlGuest.objects.get(shortUrl=shortUrl).longUrl
    return HttpResponseRedirect(longUrl)

def redirect_auth(request, shortUrl):
    '''Redirect Funtion'''
    try: # Testing if the link exists
        shorturlauth = ShortUrlAuth.objects.get(shortUrl=shortUrl)
    except ShortUrlGuest.DoesNotExist:
        raise Http404
    longUrl = shorturlauth.longUrl
    shorturlauth.timesClicked += 1
    shorturlauth.save()

    return HttpResponseRedirect(longUrl)


def signup(request):
    '''SignUp fucntion'''
    form = SignUpForm(request.POST or None)
    Success = False

    if form.is_valid():
        username = form.cleaned_data["username"] # Getting the data from the form
        email = form.cleaned_data["email"]
        passw = form.cleaned_data["passw"]

        user = User.objects.create_user(username, email, passw) # Creating the User
        profile = Profile(user=user)
        profile.save()
        Success = True

    return render(request, 'shortener/signup.html', {'Success' : Success, 'form' : form})


def signin(request):
    form = SignInForm(request.POST or None)
    error = False

    if form.is_valid():
        username = form.cleaned_data["username"] # Getting the data from the form
        passw = form.cleaned_data["passw"]
        user = authenticate(username=username, password=passw) # Verifies the data
        if user: # If the Object isn't none
            login(request, user) # We log him in
            return HttpResponseRedirect("/dashboard")
        else: # Else we display an error message
            error = True

    return render(request, 'shortener/signin.html', locals())


def logout(request):
    django_logout(request)
    return HttpResponseRedirect("/signin")


def dashboard(request):
    return render(request, 'shortener/dashboard_home.html')


def dashboard_new_link(request):
    form = ShortUrlAuthForm(request.POST or None)
    Valid = False

    if form.is_valid():
        longUrl = form.cleaned_data["longUrl"]
        customText = form.cleaned_data["customText"]

        if customText == "":  # If there is no custom text
            shortUrl = generate(5)
        else:
            shortUrl = customText
            # TODO: say to the user that the URL is already taken

        shorturlauth = ShortUrlAuth() # Creating the instance
        shorturlauth.shortUrl = shortUrl
        shorturlauth.longUrl = longUrl
        shorturlauth.author = request.user.username
        shorturlauth.save()
        Valid=True



    return render(request, 'shortener/dashboard_new_link.html', locals())


def dashboard_my_links(request):
    empty = False
    try:
        urls = ShortUrlAuth.objects.filter(author=request.user.username)
        if not urls:
            empty = True
    except:
        pass

    return render(request, 'shortener/dashboard_my_links.html', locals())

def generate(nb):
    '''Fct that generates the random char string for the links'''
    char = string.ascii_letters + string.digits
    randm = [random.choice(char) for _ in range(nb)]

    return ''.join(randm)
