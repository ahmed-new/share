from django.forms import BaseModelForm
from django.shortcuts import render ,get_object_or_404
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from . models import Post , Category , Comment
from . forms import Addpostform ,Addcommentform
from django.urls import reverse_lazy , reverse
from django.http import HttpResponse, HttpResponseRedirect





def ctigoriesview (request,cats):
    category_posts=Post.objects.filter(category=cats)
    return render (request,'categories.html',{"cats":cats ,"category_posts":category_posts})


def likesview(request ,pk):
    post = get_object_or_404(Post , id=request.POST.get('post_id'))
    liked =False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('artical_detail', args=[str(pk)]))


class home (ListView):
    model= Post
    template_name='home/home.html'
    ordering=['-date']
    paginate_by=5

    def get_context_data(self,*args , **kwargs):
        cats_menu= Category.objects.all()
        context=super(home ,self).get_context_data(*args , **kwargs)
        context['cats_menu'] = cats_menu
        return context

class viewdetail(DetailView):
    model = Post
    template_name = 'artical_details.html'

    def get_context_data(self, *args, **kwargs):
        thing = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = thing.total_likes()  
        context = super(viewdetail, self).get_context_data(*args, **kwargs)
        liked=False
        if thing.likes.filter(id=self.request.user.id).exists():
            liked=True
        
        context['total_likes'] = total_likes
        context['liked']= liked
        return context


class Addpostview(CreateView):
    model = Post
    form_class= Addpostform
    template_name='home/add_post.html'
    #fields= '__all__'

class Addcategoryview(CreateView):
    model = Category
    template_name='add_category.html'
    fields= '__all__'



class Updatepostview(UpdateView):
    model = Post
    fields=['title','body']
    template_name='update_post.html'


class deletepostview(DeleteView):
    model = Post
    template_name='delete.html'
    success_url= reverse_lazy('home')


class Addcommenttview(CreateView):
    model = Comment
    form_class= Addcommentform
    template_name='home/add_comment.html'
    
    #fields= '__all__'

    def form_valid(self, form):
        post=Post.objects.get(pk=self.kwargs['pk'])
        form.instance.post= post 
        form.instance.name= self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('artical_detail' ,kwargs={'pk':self.kwargs['pk']})


       