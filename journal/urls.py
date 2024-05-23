from django.urls import path
from . import views

app_name = 'journal'




urlpatterns = [
    path('', views.main_page, name='main_page'),

    path('contact/', views.contact, name='contact'),
    path('save_contact/', views.save_contact, name='save_contact'),

    path('editorial/list/', views.editorial_list, name='editorial_list'),
    path('editorial/<int:id>/', views.editorial_detail, name='editorial_detail'),
    path('editorial/update/<int:id>/', views.editorial_update, name='editorial_update'),
    path('editorial/delete/<int:id>/', views.editorial_delete,
         name='editorial_delete'),
    path('editorial/create/', views.editorial_create.as_view(), name='editorial_create'),


    path('article/list/', views.article_list, name='article_list'),
    path('article/<slug:slug>/<int:id>/',
         views.article_detail, name='article_detail'),
    path('article/update/<slug:slug>/<int:id>/',
         views.article_update, name='article_update'),
    path('article/delete/<slug:slug>/<int:id>/', views.article_delete,
         name='article_delete'),
    path('article/create/', views.article_create, name='article_create'),

    path('post/list/',
         views.PostListView.as_view(), name='post_list'),
    path('post/<slug:slug>/<int:id>/',
         views.PostDetailView, name='post_detail'),
    path('post/update/<slug:slug>/<int:id>/',
         views.PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<slug:slug>/<int:id>/',
         views.PostDeleteView, name='post_delete'),
    path('post/create/', views.PostCreateView.as_view(),
         name='post_create'),

    path('journal/list/', views.journal_list, name='journal_list'),
    path('journal/create/', views.journal_create, name='journal_create'),
    path('journal/update/<int:id>/', views.journal_update, name='journal_update'),
    path('journal/delete/<int:id>/', views.journal_delete, name='journal_delete'),

    path('social/list/', views.social_media_list, name='social_media_list'),
    path('social/update/<int:id>/', views.social_media_update, name='social_media_update'),
    path('social/delete/<int:id>/', views.social_media_delete, name='social_media_delete'),
    path('social/create/', views.social_media_create, name='social_media_create'),

    path('message/list/', views.message_list, name='message_list'),
    path('message/delete/all/', views.message_delete_all, name='message_delete_all'),

    path('journal/about/', views.about, name='about_journal'),
    path('journal/about/<int:id>/', views.about_article_update, name='about_article_update'),
    path('booking/article/', views.booking_article, name='booking_article'),
    path('booking/article/<int:id>/', views.sending_article_update, name='sending_article_update'),

]
