from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def LikeView(request, pk):
    post = Post.objects.get(id=pk)

    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    # post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))
    #
    # post = get_object_or_404(Post, id=request.POST.get('post.id'))
    # post.likes.add(request.user)
    # return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))
    pass


class HomeView(ListView):
    model = Post
    # paginator = Paginator(Post.objects.all(), 5)
    template_name = 'index.html'
    paginate_by = 5
    queryset = Post.objects.all()

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


# def FavoriteView(request, pk):
#     # category_posts = Post.objects.filter(category=choices.replace("-", " "))
#
#     post = Post.objects.get(id=pk)
#
#     favorite_posts = Post.objects.filter(category=user)
#     return render(request, 'categories.html', {'choices': choices, 'category_posts': category_posts})
#     pass


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

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['category_menu'] = category_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context
        pass

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


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    
    template_name = "add_comment.html"
    # fields = '__all__'
    # fields = ('title', 'body')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')
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
