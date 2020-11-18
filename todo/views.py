from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ToDo, User, Goals
from .forms import GoalForm,TodoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Website views here.




def landing(request):
	return render(request, 'todo/landing.html')

@login_required
def home(request):
	context = {'long_term_goals':Goals.objects.filter(user=request.user)}
	return render(request,'todo/home.html',context)

@login_required
def todo(request):
	context = {'entries':ToDo.objects.filter(user=request.user)}
	return render(request,'todo/todo.html',context)

@login_required
def positivity(request):
	#context = {'memes':Memes.objects.all}
	return render(request,'todo/positivity.html')

@login_required
def goalform(request):
	print("Saved")
	# if not request.user.is_authenticated:
	# 	raise Http404
	if request.method == 'POST':
		print("Post")
		form = GoalForm(request.POST)
		if form.is_valid():


			instance = form.save()
			instance.user = request.user
			instance.save()
			return redirect("todo-home")
	else:
		form = GoalForm()
	return render(request, 'todo/goalform.html', {'form': form})


@login_required
def todoform(request):
	print("Saved")
	# if not request.user.is_authenticated:
	# 	raise Http404
	if request.method == "POST":
		print("Post")
		form = TodoForm(request.POST)
		if form.is_valid():
			print("valid")
			instance = form.save()
			instance.user = request.user
			instance.save()

			return redirect("todo-list")
	else:
		form = TodoForm()
	return render(request,'todo/todoform.html',{'form':form})
