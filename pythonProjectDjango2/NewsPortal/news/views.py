from django.views.generic import DetailView, ListView
from .models import *
from datetime import datetime



#
# class AuthorsList(ListView):
#     model = Author
#     template_name = 'authors.html'
#     context_object_name = 'Authors'
#     queryset = Author.objects.all()
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
#         context['value1'] = None  # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
#         return context

#
# class AuthorsDetail(DetailView):
#     model = Author
#     template_name = 'author.html'
#     context_object_name = 'author'
#     queryset = Author.objects.all().order_by('id')  # queryset =model, но с помощью него можно делать ORM запросы.
                                                  # (например вызвать авторов по алфавту или по рейтингу)


class PostsList(ListView):
    model = Post
    template_name = 'news1.html'
    context_object_name = 'Posts'
    queryset = Post.objects.order_by('-dateCreation')
    # queryset = Post.objects.all().order_by('postCategory')

    # def get_queryset(self):
        # return Post.objects.filter(author=self.request.user).order_by('rating').reverse()
        # return Post.objects.filter(author=self.request.postCategory).order_by('rating')

        # return Post.objects.all().order_by('postCategory')[0]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['value1'] = None
        return context


class PostsDetail(DetailView):
    model = Post
    template_name = 'news2.html'
    context_object_name = 'Post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['value1'] = None
        return context


    # def get_queryset(self):
    #     self.postCategory = Post.objects.get(pk=id(1))
    #     return Post.obgects.filter(postCategory=self.postCategory)




#
# class CategorysDetail(DetailView):
#     model = Category
#     template_name = 'news1.html'
#     context_object_name = 'categories'
#
#
# class CommentsList(DetailView):
#     model = Comment
#     template_name = 'news1.html'
#     context_object_name = 'comments'
#
# #
# class PostCategorysList(ListView):
#     model = PostCategory
#     template_name = 'news1.html'
#     context_object_name = 'comments'
#
# class PostCategorysDetail(DetailView):
#     model = PostCategory
#     template_name = 'news2.html'
#     context_object_name = 'comment'
#
# class NewsDetail(DetailView):
#     model = Post
#     context_object_name = 'Post'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['comment_list'] = Comment.objects.filter(comment_post=self.kwargs['pk'])
#         return context
#

