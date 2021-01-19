from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import TaskForm
from .models import Task
from .tasks import exec1
import pytz
import datetime


@login_required
def taskView(request, id):

    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})

@login_required
def newTask(request):
    if request.method == 'POST':
        print("opa")
        form = TaskForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.user = request.user
            task.save()
            print(request.user.id)
            data = {
                'user_email': request.user.email,
            }
            exec1.apply_async(
                (data, ),
                eta=(datetime.datetime.strptime(request.POST['schedule_date'], "%Y-%m-%dT%H:%M"))
            )

            return redirect('/')

    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form': form})

@login_required
def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)
    
    if (request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)
        
        if(form.is_valid()):
            task.save()
            return redirect('/')
        else:
            
            return render(request, 'tasks/edittask.html', {'form': form, 'task': task})
        
    else:
        return render(request, 'tasks/edittask.html', {'form': form, 'task': task})

@login_required
def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso!')
    return redirect('/',{'del': True})

@login_required
def changeStatus(request, id):
    task = get_object_or_404(Task, pk=id)
    url = request.META['HTTP_REFERER']

    if(task.done == 'doing'):
        task.done = 'done'
    else:
        task.done = 'doing'
    
    task.save()

    return redirect(url)

@login_required
def changeStatusTask(request, id):
    task = get_object_or_404(Task, pk=id)
    
    if(task.done == 'doing'):
        task.done = 'done'
        messages.info(request, 'Tarefa finalizada!')
    else:
        task.done = 'doing'
    
    
    task.save()
    
    return redirect('/task/'+ str(id))


@login_required
def dashboard(request):
    search = request.GET.get('search')
    
    all_tasks = Task.objects.filter(user=request.user).count()

    tasksDoneRecently = Task.objects.filter(done='done', user=request.user, updated_at__gt=datetime.datetime.now() - datetime.timedelta(days=30))
    tasksDoneRecentlyCount = tasksDoneRecently.count()
    
    tasksDone = Task.objects.filter(done='done', user=request.user).count()
    tasksDoing = Task.objects.filter(done='doing', user=request.user).count()
    
    if search:
        tasks = Task.objects.filter(title__icontains=search, user=request.user)

    else:
        tasks = Task.objects.all().order_by('-created_at').filter(user=request.user)

        paginator = Paginator(tasks, 8)
        
        page = request.GET.get('page')
        
        tasks = paginator.get_page(page)

    return render(request, 'tasks/doing.html', {'tasks': tasks, 'tasksdonerecently': tasksDoneRecently, 'tasksdone': tasksDone, 'tasksdoing': tasksDoing, 'tasksdonerecentlycount': tasksDoneRecentlyCount, 'all_tasks': all_tasks})


@login_required
def tasksDone(request):
    search = request.GET.get('search')
    
    all_tasks = Task.objects.filter(user=request.user).count()

    tasksDoneRecently = Task.objects.filter(done='done', user=request.user, updated_at__gt=datetime.datetime.now() - datetime.timedelta(days=30))
    tasksDoneRecentlyCount = tasksDoneRecently.count()
    
    tasksDone = Task.objects.filter(done='done', user=request.user).count()
    tasksDoing = Task.objects.filter(done='doing', user=request.user).count()
    
    if search:
        tasks = Task.objects.filter(title__icontains=search, user=request.user)

    else:
        tasks = Task.objects.all().order_by('-created_at').filter(done='done',user=request.user)

        paginator = Paginator(tasks, 8)
        
        page = request.GET.get('page')
        
        tasks = paginator.get_page(page)

    return render(request, 'tasks/done.html', {'tasks': tasks, 'tasksdonerecently': tasksDoneRecently, 'tasksdone': tasksDone, 'tasksdoing': tasksDoing, 'tasksdonerecentlycount': tasksDoneRecentlyCount, 'all_tasks': all_tasks})

@login_required
def tasksDoing(request):
    search = request.GET.get('search')
    
    all_tasks = Task.objects.filter(user=request.user).count()

    tasksDoneRecently = Task.objects.filter(done='done', user=request.user, updated_at__gt=datetime.datetime.now() - datetime.timedelta(days=30))
    tasksDoneRecentlyCount = tasksDoneRecently.count()
    
    tasksDone = Task.objects.filter(done='done', user=request.user).count()
    tasksDoing = Task.objects.filter(done='doing', user=request.user).count()
    
    if search:
        tasks = Task.objects.filter(title__icontains=search, user=request.user)

    else:
        tasks = Task.objects.all().order_by('-created_at').filter(done='doing',user=request.user)

        paginator = Paginator(tasks, 8)
        
        page = request.GET.get('page')
        
        tasks = paginator.get_page(page)

    return render(request, 'tasks/doing.html', {'tasks': tasks, 'tasksdonerecently': tasksDoneRecently, 'tasksdone': tasksDone, 'tasksdoing': tasksDoing, 'tasksdonerecentlycount': tasksDoneRecentlyCount, 'all_tasks': all_tasks})

@login_required
def lastDays(request):
    search = request.GET.get('search')
    
    all_tasks = Task.objects.filter(user=request.user).count()

    tasksDoneRecently = Task.objects.all().order_by('-created_at').filter(done='done', user=request.user, updated_at__gt=datetime.datetime.now() - datetime.timedelta(days=7))
    tasksDoneRecentlyCount = tasksDoneRecently.count()
    
    tasksDone = Task.objects.filter(done='done', user=request.user).count()
    tasksDoing = Task.objects.filter(done='doing', user=request.user).count()
    
    if search:
        tasks = Task.objects.filter(title__icontains=search, user=request.user)

    else:
        tasks = tasksDoneRecently

        paginator = Paginator(tasks, 8)
        
        page = request.GET.get('page')
        
        tasks = paginator.get_page(page)

    return render(request, 'tasks/lastdays.html', {'tasks': tasks, 'tasksdonerecently': tasksDoneRecently, 'tasksdone': tasksDone, 'tasksdoing': tasksDoing, 'tasksdonerecentlycount': tasksDoneRecentlyCount, 'all_tasks': all_tasks})

