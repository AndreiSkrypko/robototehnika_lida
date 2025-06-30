from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import ForumPost
from .forms import ForumPostForm

@login_required
def forum_list(request):
    posts = ForumPost.objects.all().order_by('-created_at')
    context = {
        'posts': posts,
        'now': timezone.now().strftime('%H:%M:%S')
    }
    return render(request, 'forum_app/forum_list.html', context)

@login_required
def create_post(request):
    if request.method == 'POST':
        form = ForumPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Пост успешно создан!')
            return redirect('forum_list')
    else:
        form = ForumPostForm()
    
    return render(request, 'forum_app/create_post.html', {'form': form})