from django.shortcuts import render, redirect  
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile, Post, LikePost,ContactUs
# Create your views here.

@login_required(login_url='signin')
def index(request):
    user_object = User.objects.get(username = request.user.username)
    user_profile = Profile.objects.get(user = user_object)
    posts = Post.objects.all()
    return render(request, 'index.html', {'user_profile':user_profile, 'posts':posts})

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email already exists')
                return redirect('signup')
            
            elif User.objects.filter(username = username).exists():
                messages.info(request, 'Username already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username = username, email=email, password=password)
                user.save()

                user_login  = auth.authenticate(username=username, password = password)
                auth.login(request, user_login)

                user_model = User.objects.get(username = username)
                new_profile = Profile.objects.create(user=user_model)
                new_profile.save()
                return redirect('settings')
        else:
            messages.info(request, "Passowrd not matching")
            return redirect('signup')
    else:
        return render(request, 'signup.html')

def signin(request):


    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user  = auth.authenticate(username=username, password = password)

        if user is not None:
            #User is authenticated
            auth.login(request, user)
            return redirect('/')
        else:
            print('User Authentication failed')
            messages.info(request, 'Username and/or Password is invalid')
            return redirect('signin')
    else:
        #redirect user to login page
        return render(request, 'signin.html')

@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')

@login_required(login_url='signin')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == "POST":

        if request.FILES.get('image') == None:
            image = user_profile.profileimg
        else:
            image = request.FILES.get('image')

        bio = request.POST['bio']
        location = request.POST['location']

        user_profile.profileimg = image
        user_profile.bio = bio
        user_profile.location = location
        user_profile.save()

        messages.info(request, 'Profile details updated succesfully')
        return redirect('settings')

    return render(request, 'setting.html', {'user_profile':user_profile})

@login_required(login_url='signin')
def upload(request):
    if request.method == "POST":
        user = request.user
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']

        if caption is None or caption == "":
            new_post = Post.objects.create(user=user,image=image)
        else:
            new_post = Post.objects.create(user=user,image=image, caption = caption)
        new_post.save() 

    return redirect('index')

@login_required(login_url='signin')
def like_post(request):
    username = request.user.username
    user = User.objects.get(username = request.user)
    post_id = request.GET.get('post_id')
    post = Post.objects.get(id = post_id)
    like_filter = LikePost.objects.filter(post_id=post, username = user).first()

    if like_filter == None:
        new_like = LikePost.objects.create(post_id=post, username = user)
        new_like.save()
        post.no_of_likes = post.no_of_likes + 1
        post.save()

    else:
        like_filter.delete()
        post.no_of_likes = post.no_of_likes - 1
        post.save()

    return redirect('index')

@login_required(login_url='signin')
def profile(request, pk):
    user_object = User.objects.get(username = pk)
    user_profile = Profile.objects.get(user = user_object)
    user_posts = Post.objects.filter(user = user_object)
    user_post_len = len(user_posts)

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts': user_posts,
        'user_post_length':user_post_len
        }
        
    return render(request, 'profile.html', context)
    
@login_required(login_url='signin')
def contactus(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        new_msg = ContactUs.objects.create(name=name,
                                           email=email,
                                           message=message)
        new_msg.save()
        messages.info(request, 'Thanks for contacting us we will get back to you shortly!')
        return redirect('message')

    return render(request, 'contact.html', {'user_profile':user_profile})



@login_required(login_url='signin')
def message(request):
    
    messages = ContactUs.objects.all()
    return render(request, 'message.html', { 'messages':messages})



