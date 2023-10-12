from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from .forms import PostForm

# List all posts
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    return render(request, 'listing/post_list.html', {'posts': posts, 'category': categories})

# View a single post
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    # category = get_object_or_404(Category, pk=post_id)
    
    return render(request, 'listing/post_detail.html', {'post': post, })

# Create a new post
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listing:post_list')
    return render(request, 'listing/post_create.html', {'form': form})

# Edit an existing post
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('listing:post_detail', post_id=post.id)
    return render(request, 'listing/post_edit.html', {'form': form, 'post': post})

# Delete a post
def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('listing:post_list')
