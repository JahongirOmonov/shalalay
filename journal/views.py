from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.http import Http404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


from django.http import HttpRequest, HttpResponseForbidden, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import Journal, Post, Article, SocialMedia, About, Contact, SendingArticle, Editorial
from .forms import ContactForm, ArticleForm, PostForm, JournalForm, SocialForm, AboutForm, SendingArticleForm, \
    EditorialForm
# from journal.functions import get_or_save_statistic


def main_page(request: HttpRequest):
    # get_or_save_statistic(request)
    posts = Post.objects.all()[:2]
    articles = Article.objects.all()[:3]

    context = {
        'posts': posts,
        'articles': articles
    }

    return render(request,
                  'journal/home.html',
                  context=context)


def journal_list(request: HttpRequest):
#     get_or_save_statistic(request)
    journals = Journal.objects.all()
    return render(request,
                  template_name='journal/journal/list.html',
                  context={
                      'journals': journals
                  })


@login_required
def journal_create(request: HttpRequest):

    if not request.profile.is_admin:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = JournalForm(data=request.POST,
                           files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('journal:journal_list')
    else:
        form = JournalForm()

    return render(request, 'journal/journal/create.html',
                  {'form': form})


@login_required
def journal_update(request: HttpRequest, id):
    if not request.profile.is_admin:
        return HttpResponseForbidden()

    journal = get_object_or_404(Journal,
                                id=id)

    if request.method == 'POST':
        form = JournalForm(data=request.POST, instance=journal,
                           files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('journal:journal_list')
    else:
        form = JournalForm(instance=journal)

    return render(request, 'journal/journal/update.html',
                  {
                      'form': form,
                      'journal': journal
                  })


@login_required
def journal_delete(request: HttpRequest, id):
    if not request.profile.is_admin:
        return HttpResponseForbidden()

    journal = get_object_or_404(Journal,
                                id=id)

    if request.method == 'POST':
        journal.delete()
        return redirect('journal:journal_list')

    return render(request, 'journal/journal/delete.html',
                  {'journal': journal})


@login_required
def contact(request: HttpRequest):
#     get_or_save_statistic(request)
    form = ContactForm()

    context = {
        'form': form
    }

    return render(request, 'journal/contact.html',
                  context=context)


@login_required
@require_POST
def save_contact(request: HttpRequest):
    form = ContactForm(data=request.POST)
    if form.is_valid():

        contact = form.save(commit=False)
        contact.sender = request.user
        contact.save()
        messages.success(request, 'Sizning xabaringiz muvaffaqiyatli yuborildi!  ✅')

    else:
        messages.error(request, 'Iltimos to\'g\'ri ma\'lumot kiriting! ❌', extra_tags='danger')

    return redirect('journal:contact')


@login_required
def message_list(request: HttpRequest):

    messages = Contact.objects.all().order_by('-created_at').select_related('sender', 'sender__profile')
    messages.update(is_read=True)
    messages_count = messages.count()
    paginator = Paginator(messages, 5)
    page_number = request.GET.get('page', 1)

    try:
        messages = paginator.page(page_number)
    except PageNotAnInteger:
        messages = paginator.page(1)
    except EmptyPage:
        messages = paginator.page(paginator.num_pages)

    return render(request, 'journal/message/list.html',
                  {
                      'messages': messages,
                      'messages_count': messages_count
                  })


@require_POST
def message_delete_all(request: HttpRequest):
    if not request.user.profile.is_admin:
        return HttpResponseForbidden()
    messages = Contact.objects.filter(is_read=True)
    messages.delete()
    return redirect('users:profile')


def about(request: HttpRequest):
    datas = About.objects.all().first()

    return render(request, context={'datas': datas},
                  template_name='journal/about/about.html')


def booking_article(request: HttpRequest):
    data = SendingArticle.objects.all().first()
    context = {"data": data}
    return render(request, 'journal/guide_for_authors.html', context)


def editorial_list(request: HttpRequest):
    editorials = Editorial.objects.all()
    paginator = Paginator(editorials, 14)
    page_number = request.GET.get('page', 1)

    try:
        editorials = paginator.page(page_number)
    except PageNotAnInteger:
        editorials = paginator.page(1)
    except EmptyPage:
        editorials = paginator.page(paginator.num_pages)

    return render(request, context={
        'editorials': editorials,
        'pag_start':False,
        'pag_end':False,
    }, template_name='journal/editorial/list.html')


def article_list(request: HttpRequest):
    articles = Article.objects.all()
    paginator = Paginator(articles, 5)
    page_number = request.GET.get('page', 1)

    try:
        articles = paginator.page(page_number)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)


    return render(request,
                  'journal/article/list.html',
                  context={
                      'articles': articles,
                      'pag_start': False,
                      'pag_end': False,
                  })

def editorial_detail(request: HttpRequest, id):
    editorial = get_object_or_404(Editorial, id=id)
    return render(request, context={'editorial': editorial}, template_name='journal/editorial/detail.html')


def article_detail(request: HttpRequest, slug, id):
#     get_or_save_statistic(request)
    article = get_object_or_404(Article,
                                slug=slug,
                                id=id)
    article.views += 1
    article.save()

    return render(request, 'journal/article/detail.html',
                  {'article': article})


@login_required
def article_create(request: HttpRequest):
    if not request.user.is_superuser:
        return HttpResponseForbidden()

    if request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            if not article.slug:
                article.slug = slugify(article.title)
                article.save()

            return redirect('journal:article_detail',
                            slug=article.slug,
                            id=article.id)
    else:
        form = ArticleForm()

    context = {
        'form': form
    }

    return render(request,
                  'journal/article/create.html',
                  context=context)

# @login_required
# def editorial_create(request: HttpRequest):
#     if not request.user.is_superuser:
#         return HttpResponseForbidden()
#
#     if request.method == 'POST':
#         form = EditorialForm(data=request.POST)
#         if form.is_valid():
#             editorial = form.save()
#             return redirect('journal:editorial_detail', id=editorial.id)
#     else:
#         form = EditorialForm()
#
#     return render(request, 'journal/editorial/create.html',{'form': form})
class editorial_create(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = 'journal/editorial/create.html'
    model = Editorial
    form_class = EditorialForm

    def get_success_url(self):
        return reverse_lazy('journal:editorial_detail', kwargs={'id': self.object.pk})

    # def form_valid(self, form):
    #     instance = form.save(commit=False)
    #     instance.author = self.request.user
    #     instance.save()
    #     return super().form_valid(form)

    def test_func(self):
        return self.request.profile.is_admin



@login_required
def article_update(request: HttpRequest, slug, id):
    article = get_object_or_404(Article,
                                slug=slug, id=id)

    if not request.user.is_superuser:
        return HttpResponseForbidden()

    if request.method == 'POST':
        form = ArticleForm(data=request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('journal:article_detail',
                            slug=article.slug,
                            id=article.id)
    else:
        form = ArticleForm(instance=article)

    return render(request, 'journal/article/update.html',
                  {'form': form,
                   'article': article})


@login_required
def editorial_update(request: HttpRequest, id):
    editorial = get_object_or_404(Editorial, id=id)

    if not request.user.is_superuser:
        return HttpResponseForbidden()

    if request.method == 'POST':
        form = EditorialForm(data=request.POST, instance=editorial)
        if form.is_valid():
            editorial = form.save()
            return redirect('journal:editorial_detail', id = editorial.id)
    else:
        form = EditorialForm(instance=editorial)
        context = {'form': form, 'editorial': editorial}

    return render(request, 'journal/editorial/update.html', context=context)





def about_article_update(request: HttpRequest, id):
    if not request.user.is_superuser:
        return HttpResponseForbidden()
    about = get_object_or_404(About, id=id)

    if request.method == 'POST':
        forma = AboutForm(data=request.POST, instance=about)
        if forma.is_valid():
            forma.save()
            return redirect('journal:about_journal',)
    else:
        forma = AboutForm(instance=about)

    context = {'forma': forma, 'about': about}

    return render(request, template_name='journal/about/update.html',
                  context=context)


def sending_article_update(request: HttpRequest, id):
    if not request.user.is_superuser:
        return HttpResponseForbidden()
    article = get_object_or_404(SendingArticle, id=id)

    if request.method == 'POST':
        form = SendingArticleForm(data=request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('journal:booking_article',)
    else:
        form = SendingArticleForm(instance=article)
    context = {'form': form, 'article': article}
    return render(request, template_name='journal/guide_for_update.html', context=context)





@login_required
def article_delete(request: HttpRequest, slug, id):
    article = get_object_or_404(Article,
                                slug=slug,
                                id=id)
    if not request.user.is_superuser:
        return HttpResponseForbidden()

    if request.method == 'POST':
        article.delete()
        return redirect('journal:article_list')

    return render(request, 'journal/article/delete.html',
                  {'article': article})

@login_required
def editorial_delete(request: HttpRequest, id):
    editorial = get_object_or_404(Editorial, id=id)

    if not request.user.is_superuser:
        return HttpResponseForbidden()

    if request.method == 'POST':
        editorial.delete()
        return redirect('journal:editorial_list')

    return render(request, 'journal/editorial/delete.html', {'editorial': editorial})


@login_required
def social_media_list(request: HttpRequest):
    if not request.profile.is_admin:
        return HttpResponseForbidden()
    social_media = SocialMedia.objects.all()

    return render(request, 'journal/social/list.html',
                  {'social_media': social_media})


@login_required
def social_media_create(request: HttpRequest):
    if not request.profile.is_admin:
        return HttpResponseForbidden()

    if request.method == 'POST':
        form = SocialForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('journal:social_media_list')
    else:
        form = SocialForm()

    return render(request, ''
                           'journal/social/create.html',
                  {'form': form})


@login_required
def social_media_update(request: HttpRequest, id):
    if not request.profile.is_admin:
        return HttpResponseForbidden()
    social_media = get_object_or_404(SocialMedia, id=id)

    if request.method == 'POST':
        form = SocialForm(data=request.POST, instance=social_media)
        if form.is_valid():
            form.save()
            return redirect('journal:social_media_list')
    else:
        form = SocialForm(instance=social_media)

    return render(request, ''
                           'journal/social/update.html',
                  {
                      'form': form,
                      'social': social_media
                  })


@login_required
def social_media_delete(request: HttpRequest, id):
    if not request.profile.is_admin:
        return HttpResponseForbidden()

    social_media = get_object_or_404(SocialMedia, id=id)
    if request.method == 'POST':
        social_media.delete()
        return redirect('users:profile')

    return render(request, 'journal/social/delete.html',
                  {'social': social_media})


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'journal/post/list.html'
    paginate_by = 2

    # def get_context_data(self, **kwargs):
    #     get_or_save_statistic(self.request)
    #     return super().get_context_data(**kwargs)


# class PostDetailView(DetailView):
#
#     model = Post
#     context_object_name = 'post'
#     template_name = 'journal/post/detail.html'
#
#     def get(self, request, *args, **kwargs):
#         try:
#             article = self.get_object()
#             article.views += 1
#             article.save()
#             return super().get(request, *args, **kwargs)
#         except Http404:
#             # Handle case where no Post object is found
#             raise Http404("Post does not exist")

def PostDetailView(request: HttpRequest, slug, id):
#     get_or_save_statistic(request)
    post = get_object_or_404(Post,
                                slug=slug,
                                id=id)
    post.views += 1
    post.save()

    return render(request, 'journal/post/detail.html',
                  {'post': post})

from django.utils.text import slugify
class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = 'journal/post/create.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('journal:post_list')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save()
        self.object = form.save(commit=False)
        if not self.object.slug:
            self.object.slug = slugify(self.object.title)
        return super().form_valid(form)


    def test_func(self):
        return self.request.profile.is_admin


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'journal/post/update.html'

    def test_func(self):
        return self.request.profile.is_admin


# class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Post
#     template_name = 'journal/post/delete.html'
#     context_object_name = 'post'
#     success_url = reverse_lazy('journal:post_list')
#
#     def test_func(self):
#         return self.request.profile.is_admin


@login_required
def PostDeleteView(request: HttpRequest, slug, id):
    post = get_object_or_404(Post,
                                slug=slug,
                                id=id)
    if not request.user.is_superuser:
        return HttpResponseForbidden()

    if request.method == 'POST':
        post.delete()
        return redirect('journal:post_list')

    return render(request, 'journal/post/delete.html',
                  {'post': post})








