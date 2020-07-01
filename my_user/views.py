from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model


def home(request):
	user_model = get_user_model()
	all_users = user_model.objects.all()
	return render(request, 'home.html', {'all_users': all_users})


def create_new_user(request):
	if request.method == 'POST':
		email = request.POST['email']
		name = request.POST['name']
		password = request.POST['password']
		blog_title = request.POST['blog_title']
		user_model = get_user_model()
		user_obj = user_model.objects.create_user(email=email, name=name)
		user_obj.set_password(password)
		user_obj.blogpost.title = blog_title
		user_obj.save()
		return redirect('home')
	else:
		return render(request, 'create_new_user.html')








