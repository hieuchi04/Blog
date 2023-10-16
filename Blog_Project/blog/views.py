from django.shortcuts import render, redirect
from .models import PostModel
from .forms import PostModelForm, PostUpdateForm
# Create your views here.

def index(request):
    posts = PostModel.objects.all()
    #posts = PostModel.objects.all().order_by('-date_created')  post đc sắp xếp theo tgian gần nhất tới muộn nhất
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False) #lưu dữ liệu từ form nhưng chưa đẩy lên db
            instance.author = request.user  #user đã đăng nhập được gắn là author
            instance.save() #đẩy dữ liệu lên db
            return redirect('index')
            #sau khi post sẽ trở lại trang
    else:
        #Nếu yêu cầu không phải là một yêu cầu POST (thường là yêu cầu GET), chúng ta tạo một thể hiện mới của PostModelForm mà không có dữ liệu ban đầu
        form = PostModelForm()
    context = {
        'posts' : posts,
        'form' : form,
    }
    return render(request, 'blog/index.html', context)

def post_detail(request, pk):
    post = PostModel.objects.get(id=pk)
    context = {
        'post' : post,
    }
    return render(request, 'blog/post_detail.html', context)

def post_edit(request, pk):
    post = PostModel.objects.get(id=pk)
    if(request.method=='POST'):
        form = PostUpdateForm(request.POST,instance=post) #hiện post đã viết lên form
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.id)
    else:
        form = PostUpdateForm(instance=post)
    context = {
        'post':post,
        'form':form,
    }
    return render(request, 'blog/post_edit.html', context)

def post_delete(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    context={
        'post':post
    }
    return render(request, 'blog/post_delete.html', context)
