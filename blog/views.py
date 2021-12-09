from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import unidecode

from .forms import CommentForm, PostForm
from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 3


# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'

@login_required
def post_detail(request, slug):
    template_name = "post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            new_comment.name = request.user
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )


class PostView(CreateView, LoginRequiredMixin):
    model = Post
    template_name = 'new_post.html'
    form_class = PostForm
    success_url = reverse_lazy('home')


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.slug = f"{unidecode.unidecode(form.cleaned_data['title']).replace(' ', '_')}_{self.request.user.id}"

        dup_check = Post.objects.filter(slug=self.object.slug)
        if dup_check:
            return HttpResponseRedirect(reverse_lazy('create_post'))

        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['title'] = 'Создать пост'
        return context


class PostUpdateView(UpdateView, LoginRequiredMixin):
    model = Post
    template_name = 'update_post.html'
    form_class = PostForm
    success_url = reverse_lazy('home')
    success_message = 'Пост успешно обновлен!'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Обновление поста'
        context['pk'] = self.kwargs.get('pk')
        return context


class PostDeleteView(DeleteView, LoginRequiredMixin):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Удаление поста'
        context['pk'] = self.kwargs.get('pk')
        return context

    def get(self, request, *args, **kwargs):
        Post.objects.get(id=self.kwargs.get('pk')).delete()
        return HttpResponseRedirect(reverse_lazy('home'))
