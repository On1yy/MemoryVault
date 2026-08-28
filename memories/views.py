from pyexpat.errors import messages
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import  MemoryForm
from .models import Memory
from django.contrib.auth.decorators  import login_required
from django.db.models import Q


@login_required
def create_memory(request):
    if request.method == 'POST':
        form = MemoryForm(request.POST)

        if form.is_valid():
            memory = form.save(commit=False)
            memory.user = request.user
            memory.save()
            messages.success(request,'Воспоминание создано')
            return redirect('/memory/list')

    else:
        form = MemoryForm()

    return render(request, 'memories/create_memory_page.html',{'form':form})

@login_required
def edit_memory(request,id):
    memory = get_object_or_404(Memory, id=id,user=request.user)

    if request.method == 'POST':
        form = MemoryForm(request.POST,instance=memory)
        if form.is_valid():
            memory = form.save(commit=False)
            memory.edited = True
            form.save()
            messages.success(request,'Изменения внесены')
            return redirect('/memory/list')

    else:
        form = MemoryForm(instance=memory)

    return render(request, 'memories/edit_memory_page.html', {'form': form})

@login_required
def delete_memory(request,id):
    memory = get_object_or_404(Memory,id=id,user=request.user)
    memories = Memory.objects.filter(user=request.user)

    memory.delete()
    messages.success(request,'Воспоминание удалено')
    return redirect('/memory/list')

@login_required
def memory_list(request):

    sort = request.GET.get('sort','newest')

    q = request.GET.get("q")

    memories = Memory.objects.filter(user=request.user,is_archived=False)

    if q:
        memories = memories.filter(
            Q(title__icontains=q) |
            Q(text__icontains=q)
        )

    if sort == 'newest':
        memories = memories.order_by('-created_at')

    elif sort == 'oldest':
        memories = memories.order_by('created_at')

    elif sort == 'title':
        memories = memories.order_by('title')

    return render(
        request,
        "memories/memories_list_page.html",
        {"memories": memories}
    )


@login_required
def toggle_favorite(request,id):
    memory = get_object_or_404(Memory,id=id,user=request.user)
    memory.is_favorite = not memory.is_favorite
    memory.save()
    messages.success(request, 'Добавлено в избранные')
    return redirect(request.META.get("HTTP_REFERER", "/memory/list"))

@login_required
def favorites_memories_list(request):
    q = request.GET.get("q")

    memories = Memory.objects.filter(user=request.user,is_favorite=True)

    if q:
        memories = memories.filter(
            Q(title__icontains=q) |
            Q(text__icontains=q)
        )

    return render(request, "memories/memories_list_page.html",
                  {
              "memories": memories
          }
   )

@login_required
def toggle_archive(request,id):
    memory = get_object_or_404(Memory,id=id,user=request.user)
    memory.is_archived = not memory.is_archived
    memory.save()
    messages.success(request, 'Перемещено в архив')

    return redirect(request.META.get("HTTP_REFERER", "/memory/list"))

@login_required
def archives_memories_list(request):
    memories = Memory.objects.filter(user=request.user,is_archived =True)
    return render(request,'memories/memories_list_page.html',{'memories':memories})


@login_required
def fullscreen_memory(request,id):
    memory = get_object_or_404(Memory,id=id,user=request.user)
    return render(request,'memories/fullscreen_memory.html',{'memory':memory})
















