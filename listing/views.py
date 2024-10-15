from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.db.models import Count



@login_required
# List all posts
def post_list(request):
    # Make sure the topic belongs to the current user.
    if not request.user.is_authenticated:
        raise Http404
    
    posts = Post.objects.filter(owner=request.user)
   
    
    categories = Category.objects.annotate(post_count=Count('post')).all()

    # categories = Category.objects.all()

    # count_category = categories.count()
    
    return render(request, 'listing/post_list.html', {'posts': posts, 'categories': categories})

def posts_by_category(request, category_id):
    if not request.user.is_authenticated:
        raise Http404
    category = get_object_or_404(Category, pk=category_id)
    posts = Post.objects.filter(category=category).order_by('-created_at')
    categories = Category.objects.annotate(post_count=Count('post')).all()
    return render(request, 'listing/posts_by_category.html', {'posts': posts, 'category': category, 'categories': categories})

# View a single post
def post_detail(request, post_id):
    if not request.user.is_authenticated:
        raise Http404
    # category = get_object_or_404(Category, pk=post_id)
    # posts = Post.objects.filter().order_by('-created_at')
    post = get_object_or_404(Post, pk=post_id)
    categories = Category.objects.annotate(post_count=Count('post')).all()
    
    
    return render(request, 'listing/post_detail.html', {'post': post, 'categories': categories})





@login_required
# Create a new post
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.owner = request.user
        new_post.save()
 
        # form.save()
        return redirect('listing:post_list')
    return render(request, 'listing/post_create.html', {'form': form})

@login_required
# Edit an existing post
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('listing:post_detail', post_id=post.id)
    return render(request, 'listing/post_edit.html', {'form': form, 'post': post})

@login_required
# Delete a post
def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('listing:post_list')






