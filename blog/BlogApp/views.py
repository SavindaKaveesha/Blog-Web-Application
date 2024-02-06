from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView, DeleteView
from .models import post
from .forms import postForm,editForm
from django.urls import reverse_lazy

#def home(request):
#    return render(request,'home.html',{})

class HomeView(ListView):
    model= post
    template_name = "home.html"
    ordering = ['-post_datetime']

class articalDetailView(DetailView):
    model=post
    template_name = "Artical_details.html"

class createPostView(CreateView):
    model = post
    form_class = postForm
    template_name = 'create post.html'
    #fields = '__all__'

class editPostView(UpdateView):
    model = post
    form_class = editForm
    template_name = "edit Post.html"
    #fields = [ 'title', 'title_tag', 'body']

class deletePostView(DeleteView):
    model = post
    template_name = 'delete post.html'
    success_url = reverse_lazy('home')