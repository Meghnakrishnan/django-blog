from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Category
from .forms import PostForm,UpdateForm
from django.urls import reverse_lazy
# Create your views here.
# def home(request):
#     return render(request,'home.html')
class HomeView(ListView):
    model=Post
    template_name='home.html'
    # ordering=['-id'] #for list the newly added post at top
    ordering=['-post_date']

class DetailView(DetailView):
    model=Post 
    template_name='article_detail.html'   

class AddPostView(CreateView):
    model=Post
    form_class=PostForm
    template_name='add_post.html'
    #fields=('title','body')
    # fields='__all__'

class AddCategoryView(CreateView):
    model=Category
    # form_class=PostForm
    template_name='add_category.html'
    #fields=('title','body')
    fields='__all__'

class UpdatePostView(UpdateView):
    model=Post
    template_name='update_post.html'
    form_class=UpdateForm

class DeletePostView(DeleteView):
    model=Post
    template_name='delete_post.html'
    success_url= reverse_lazy('home')