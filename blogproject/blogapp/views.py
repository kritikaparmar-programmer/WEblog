from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import BlogPost
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


def cover(request):
    return render(request, 'blogapp/cover.html')


posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'E-learning is growing at a lightning speed, as the Internet has made learning and knowledge accessible to everyone. There will always be people looking to gain new knowledge and skills online, from the comfort of their home.If you have particular knowledge or skills that you’re passionate about writing, why not help other people become experts as well? You can give guitar lessons, coding lessons, dog training lessons, tutorials about using any kind of software, language lessons, and pretty much anything else you want.',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Gamers are interested in the tech market, so combining the two will help you earn a significant amount of money. This is one of the most profitable niches you can choose from and, again, it comes with plenty of sub-niches and affiliate opportunities.You can write an app and video game reviews, tech gadget reviews, tips about mobile and PC repairs, video game tutorials, or any other related topic you’re interested in and have a lot to say about.',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
    context = {
        'posts': BlogPost.objects.all()
    }
    return render(request, 'blogapp/home.html', context)


def about(request):
    return render(request, 'blogapp/about.html', {'title': 'About'})


class PostListView(ListView):
    model = BlogPost
    template_name = 'blogapp/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4  # 4 posts per page


class UserPostListView(ListView):
    model = BlogPost
    template_name = 'blogapp/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    # ordering = ['-date_posted']
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return BlogPost.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = BlogPost


class PostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPost
    success_url = 'home/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False