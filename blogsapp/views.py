from django.shortcuts import render
from django.views import generic
from  django . shortcuts  import render, redirect
from django.http import HttpResponseRedirect
from .models import *
from django.contrib import messages

# Create your views here.

class PostList(generic.ListView):
	queryset = Post.objects.filter(status=1).order_by('-created_on')
	template_name = 'bloghome.html'
	
class PostDetail(generic.DetailView):
	model = Post
	template_name = 'post_detail.html'

def uploadPost(request):
	if request.user.is_authenticated and request.user.is_staff:
		if request.method == 'POST':
			title = request.POST.get('title')
			slug = request.POST.get('slug')
			content = request.POST.get('content')
			
			check_slug = Post.objects.filter(slug = slug)
			if not check_slug:
				uname = request.user.username
				new_post = Post.objects.create(author=uname, title = title, slug = slug, content = content)
				new_post.save()
				messages.success(request, 'Blog uploaded seccessfully')
				return HttpResponseRedirect('/blogs/')
			else:
				messages.error(request, "Slug is already used")
				return HttpResponseRedirect('/blogs/upload_blog/')
		else:
			return render(request, 'blogUpload.html')
	else:
		messages.error(request, 'You have to login as trainer to post blogs')
		return HttpResponseRedirect('/social/login_social/')

def deleteBlog(request, slug):
	if request.user.is_authenticated:
		usr = request.user.username
		post = Post.objects.get(slug = slug)
		if usr == post.author:
			post.delete()
			return redirect('/blogs/')
		else:
			# sl = Post.objects.get(slug = slug)
			messages.error(request, 'Only author can delete blog')
			return HttpResponseRedirect('/blogs/')
	else:
		messages.error(request,'You have to login first')
		return HttpResponseRedirect('/social/login_social/')