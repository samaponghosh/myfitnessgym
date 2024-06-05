from django.shortcuts import render

# Create your views here.
from itertools import chain
from  django . shortcuts  import  get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Followers, LikePost, Post, Profile
from django.db.models import Q
from gymapp.views import *
from gymapp.models import *
from datetime import datetime

def signup(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect('/')
	else:
		if request.method == 'POST':
			fnm=request.POST.get('fnm')
			emailid=request.POST.get('emailid')
			pwd=request.POST.get('pwd')
			acType = request.POST.get('acType')
			roomCode = request.POST.get('roomCode')
				# now = datetime.now()
				# print(fnm,emailid,pwd)
			my_user=User.objects.create_user(fnm,emailid,pwd)
			if acType == "activeUser":
				my_user.is_staff=False
			elif acType == "staffUser":
				my_user.is_staff=True
			my_user.save()
			user_model = User.objects.get(username=fnm)
			new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
			if my_user.is_staff:
				new_profile.userType = "Trainer"
				new_profile.roomCode = roomCode
			new_profile.save()
			if my_user is not None:
				login(request,my_user)
				return HttpResponseRedirect('/')
			return redirect('/social/signup_social/')
		else:
			return render(request, "signup_copy.html")
		# except:
		# 	invalid="User already exists"
		# 	return render(request, 'signup_copy.html',{'invalid':invalid})
	# return render(request, 'signup_copy.html')

def loginn(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect('/')
	else:
		if request.method == 'POST':
			unm=request.POST.get('fnm')
			pwd=request.POST.get('pwd')
			# print(fnm,pwd)
			userr=authenticate(request,username=unm,password=pwd)
			if userr is not None:
				login(request,userr)
				return redirect('/')
			invalid="Invalid Credentials"
			return render(request, 'loginn.html',{'invalid':invalid})
		else:
			return render(request, 'loginn.html')
	# return render(request, 'loginn.html')
	
@login_required(login_url='/social/login_social/')
def logoutt(request):
	logout(request)
	return redirect('/')
# @login_required(login_url='/login_social/')

def home(request):
	if request.user.is_authenticated:
		following_users = Followers.objects.filter(follower=request.user.username).values_list('user', flat=True)
		post = Post.objects.filter(Q(user=request.user.username) | Q(user__in=following_users)).order_by('-created_at')

		profile = Profile.objects.get(user=request.user)

		context = {'post': post, 'profile': profile,}
		return render(request, 'socialHome.html',context)
	else:
		messages.error(request, 'Only rigistered users are allowed')
		return HttpResponseRedirect('/social/login_social/')
	

def upload(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			user = request.user.username
			image = request.FILES.get('image_upload')
			caption = request.POST['caption']

			new_post = Post.objects.create(user=user, image=image, caption=caption)
			new_post.save()

			return redirect('/social/')
		else:
			return redirect('/social/')
	else:
		messages.error(request, 'Only rigistered users are allowed')
		return redirect('/social/login_social/')

@login_required(login_url='/social/login_social/')
def likes(request, id):
	if request.method == 'GET':
		username = request.user.username
		post = get_object_or_404(Post, id=id)

		like_filter = LikePost.objects.filter(post_id=id, username=username).first()

		if like_filter is None:
			new_like = LikePost.objects.create(post_id=id, username=username)
			post.no_of_likes = post.no_of_likes + 1
		else:
			like_filter.delete()
			post.no_of_likes = post.no_of_likes - 1

		post.save()

		# Generate the URL for the current post's detail page
		print(post.id)

		# Redirect back to the post's detail page
		return redirect('/social/#'+id+'/')
# @login_required(login_url='/login')
def explore(request):
	if request.user.is_authenticated:
		post=Post.objects.all().order_by('-created_at')
		profile = Profile.objects.get(user=request.user)

		context={
			'post':post,
			'profile':profile
			
		}
		return render(request, 'explore.html',context)
	else:
		messages.error(request, 'Only rigistered users are allowed')
		return HttpResponseRedirect("/social/login_social/")
	
# @login_required(login_url='/login')
def profile(request,id_user):
	if request.user.is_authenticated:
		user_object = User.objects.get(username=id_user)
		print(user_object)
		profile = Profile.objects.get(user=request.user)
		user_profile = Profile.objects.get(user=user_object)
		user_posts = Post.objects.filter(user=id_user).order_by('-created_at')
		user_post_length = len(user_posts)

		follower = request.user.username
		user = id_user
		
		if Followers.objects.filter(follower=follower, user=user).first():
			follow_unfollow = 'Unfollow'
		else:
			follow_unfollow = 'Follow'

		user_followers = len(Followers.objects.filter(user=id_user))
		user_following = len(Followers.objects.filter(follower=id_user))

		context = {
			'user_object': user_object,
			'user_profile': user_profile,
			'user_posts': user_posts,
			'user_post_length': user_post_length,
			'profile': profile,
			'follow_unfollow':follow_unfollow,
			'user_followers': user_followers,
			'user_following': user_following,
		}
		
		
		if request.user.username == id_user:
			if request.method == 'POST':
				if request.FILES.get('image') == None:
					image = user_profile.profileimg
					bio = request.POST['bio']
					location = request.POST['location']

					user_profile.profileimg = image
					user_profile.bio = bio
					user_profile.location = location
					user_profile.save()
				if request.FILES.get('image') != None:
					image = request.FILES.get('image')
					bio = request.POST['bio']
					location = request.POST['location']

					user_profile.profileimg = image
					user_profile.bio = bio
					user_profile.location = location
					user_profile.save()
				return redirect('/social/profile/'+id_user+"/")
			else:
				return render(request, 'profile.html', context)
		return render(request, 'profile.html', context)
	else:
		messages.error(request, 'Only rigistered users are allowed')
		return HttpResponseRedirect("/social/login_social/")

# @login_required(login_url='/login_social/')
def delete(request, id):
	if request.user.is_authenticated:
		post = Post.objects.get(id=id)
		post.delete()

		return redirect('/social/profile/'+ request.user.username+"/")
	else:
		messages.error(request, 'Only rigistered users are allowed')
		return HttpResponseRedirect("/social/login_social/")


# @login_required(login_url='/login_social/')
def search_results(request):
	if request.user.is_authenticated:
		query = request.GET.get('q')

		users = Profile.objects.filter(user__username__icontains=query)
		posts = Post.objects.filter(caption__icontains=query)

		context = {
			'query': query,
			'users': users,
			'posts': posts,
		}
		return render(request, 'search_user.html', context)
	else:
		messages.error(request, 'Only rigistered users are allowed')
		return HttpResponseRedirect("/social/login_social/")

def home_post(request,id):
	if request.user.is_authenticated:
		post=Post.objects.get(id=id)
		profile = Profile.objects.get(user=request.user)
		context={
			'post':post,
			'profile':profile
		}
		return render(request, 'socialHome.html',context)
	else:
		messages.error(request, 'Only rigistered users are allowed')
		return HttpResponseRedirect("/social/login_social/")



def follow(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			follower = request.POST['follower']
			user = request.POST['user']

			if Followers.objects.filter(follower=follower, user=user).first():
				delete_follower = Followers.objects.get(follower=follower, user=user)
				delete_follower.delete()
				return redirect('/social/profile/'+user+"/")
			else:
				new_follower = Followers.objects.create(follower=follower, user=user)
				new_follower.save()
				return redirect('/social/profile/'+user+"/")
		else:
			return redirect('/social/')
	else:
		messages.error(request, 'Only rigistered users are allowed')
		return HttpResponseRedirect("/social/login_social/")