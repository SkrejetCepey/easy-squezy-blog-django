from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    cats = Category.objects.all()
    # ordering = ['-id']
    # ordering = ['-post_date']
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu
        return context
        pass

    pass


def CategoryListView(request):
    category_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'category_menu_list': category_menu_list})
    pass


def CategoryView(request, choices):
    # category_posts = Post.objects.filter(category=choices.replace("-", " "))
    category_posts = Post.objects.filter(category=choices)
    return render(request, 'categories.html', {'choices': choices, 'category_posts': category_posts})
    pass


def ContactView(request):
    return render(request, 'contact.html')
    pass


# class ContactView(ListView):
#     model = None
#     template_name = 'contact.html'
#     pass


class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"
    pass


class AuthorDetailView(DetailView):
    model = Post
    template_name = "author_details.html"
    pass


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    # fields = '__all__'
    # fields = ('title', 'body')
    pass


class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = "add_category.html"
    fields = '__all__'
    # fields = ('title', 'body')
    pass


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "update_post.html"
    # fields = ['title', 'title_tag', 'body']
    pass


class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')
    pass
# def post(self):
#     context = {
#         'posts': Post.objects.filter(author=request.user)}
#     return render(request, 'author_details.html', context)
#     pass

# def home(request):
#     return render(request, 'index.html', {})
