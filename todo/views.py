from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

def todoView(request):
	all_todo_items = TodoItem.objects.all()

	return render(request, 'todo.html', 
		{'all_items': all_todo_items})
		#passes all the items into the render template

def addTodo(request):
	#creates a new item
	new_item = TodoItem(content = request.POST['content'])
	#save
	new_item.save()
	#redirect to /todo/
	return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
	deleted = TodoItem.objects.get(id=todo_id)
	deleted.delete()
	return HttpResponseRedirect('/todo/')

