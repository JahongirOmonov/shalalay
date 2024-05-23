import os
from django import forms

from .models import Contact, Article, Post, Journal, SocialMedia, About, SendingArticle, Editorial


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('message',)

        widgets = {
            'message': forms.Textarea(attrs={
                'class': 'form-control my-4 border-1 w-100', 'placeholder': 'Message',
            }),
        }


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'title_uz', 'title_en', 'title_ru', 'authors', 'content', 'content_uz', 'content_en', 'content_ru')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'mb-4 mt-1 form-control',
                'placeholder': 'Sarlavha',
            }),
            'title_uz': forms.TextInput(attrs={
                'class': 'mb-4 mt-1 form-control',
                'placeholder': 'Sarlavha_uz',
            }),
            'title_en': forms.TextInput(attrs={
                'class': 'mb-4 mt-1 form-control',
                'placeholder': 'Sarlavha_en',
            }),
            'title_ru': forms.TextInput(attrs={
                'class': 'mb-4 mt-1 form-control',
                'placeholder': 'Sarlavha_ru',
            }),
            'content': forms.Textarea(attrs={
                'class': 'mb-4 mt-1 form-control',
                'placeholder': 'Kontent',
            }),
            'content_uz': forms.Textarea(attrs={
                'class': 'mb-4 mt-1 form-control',
                'placeholder': 'Content_uz',
            }),
            'content_en': forms.Textarea(attrs={
                'class': 'mb-4 mt-1 form-control',
                'placeholder': 'Content_en',
            }),
            'content_ru': forms.Textarea(attrs={
                'class': 'mb-4 mt-1 form-control',
                'placeholder': 'Content_ru',
            }),
            'authors': forms.TextInput(attrs={
                'class': 'mb-4 mt-1 form-control',
                'placeholder': 'Mualliflar',
            })
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_uz', 'title_en', 'title_ru', 'content', 'content_uz', 'content_en', 'content_ru', 'mediaImage')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Sarlavha'
            }),
            'title_uz': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Sarlavha_uz'
            }),
            'title_en': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Sarlavha_en'
            }),
            'title_ru': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Sarlavha_ru'
            }),
            'mediaImage': forms.FileInput(attrs={
                'class': 'form-control', 'placeholder': 'Rasm yoki Video yuklang'
            }),
            'content': forms.Textarea(attrs={
                'class': 'mb-4 mt-1 form-control',
                'placeholder': 'Content'
            }),
            'content_uz': forms.Textarea(attrs={
                'class': 'mb-4 mt-1 form-control',
                'placeholder': 'Content_uz'
            }),
            'content_en': forms.Textarea(attrs={
                'class': 'mb-4 mt-1 form-control',
                'placeholder': 'Content_en'
            }),
            'content_ru': forms.Textarea(attrs={
                'class': 'mb-4 mt-1 form-control',
                'placeholder': 'Content_ru'
            }),
        }


class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ('file', 'image', 'source_year', 'source_number')

        widgets = {
            'file': forms.FileInput(attrs={
                'class': 'form-control', 'placeholder': 'Pfd, Doc, Docx'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control', 'placeholder': 'Rasm'
            }),
            'source_year': forms.NumberInput(attrs={
                'class': 'form-control', 'placeholder': 'Yil'
            }),
            'source_number': forms.NumberInput(attrs={
                'class': 'form-control', 'placeholder': 'Son'
            })
        }


class SocialForm(forms.ModelForm):
    class Meta:
        model = SocialMedia
        fields = ('title', 'url', 'color')

        widgets = {
            'title': forms.Select(attrs={
                'class': 'form-control'
            }),
            "url": forms.URLInput(attrs={
                'class': 'form-control'
            }),
            'color': forms.Select(attrs={
                'class': 'form-control'
            })
        }


class SendingArticleForm(forms.ModelForm):
    class Meta:
        model = SendingArticle
        fields = ('content', 'content_uz', 'content_en', 'content_ru')

        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control my-4 border-1 w-100', 'placeholder': 'Content',
            }),
            'content_uz': forms.Textarea(attrs={
                'class': 'form-control my-4 border-1 w-100', 'placeholder': 'Content_uz',
            }),
            'content_en': forms.Textarea(attrs={
                'class': 'form-control my-4 border-1 w-100', 'placeholder': 'Content_en',
            }),
            'content_ru': forms.Textarea(attrs={
                'class': 'form-control my-4 border-1 w-100', 'placeholder': 'Content_ru',
            }),
        }


class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = ('image', 'content', 'content_uz', 'content_en', 'content_ru')

        widgets = {
            'image': forms.FileInput(attrs={
                'class': 'form-control', 'placeholder': 'Jpg, Png'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control my-4 border-1 w-100', 'placeholder': 'Content',
            }),
            'content_uz': forms.Textarea(attrs={
                'class': 'form-control my-4 border-1 w-100', 'placeholder': 'Content_uz',
            }),
            'content_en': forms.Textarea(attrs={
                'class': 'form-control my-4 border-1 w-100', 'placeholder': 'Content_en',
            }),
            'content_ru': forms.Textarea(attrs={
                'class': 'form-control my-4 border-1 w-100', 'placeholder': 'Content_ru',
            }),
        }


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ('journal_name', 'journal_name_uz', 'journal_name_en', 'journal_name_ru', 'content', 'content_uz', 'content_en', 'content_ru',
                   'journal_image',
                  'author_description', 'author_description_uz', 'author_description_en', 'author_description_ru', 'author_image')

        widgets = {
            'journal_name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Sarlavha',
            }),
            'journal_name_uz': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Sarlavha_uz',
            }),
            'journal_name_en': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Sarlavha_en',
            }),
            'journal_name_ru': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Sarlavha_ru',
            }),
            'content': forms.Textarea(attrs={
                'class': 'mb-4 mt-1 form-control', 'placeholder': 'Content',
            }),
            'content_uz': forms.Textarea(attrs={
                'class': 'mb-4 mt-1 form-control', 'placeholder': 'Content_uz',
            }),
            'content_en': forms.Textarea(attrs={
                'class': 'mb-4 mt-1 form-control', 'placeholder': 'Content_en',
            }),
            'content_ru': forms.Textarea(attrs={
                'class': 'mb-4 mt-1 form-control', 'placeholder': 'Content_ru',
            }),
            'journal_image': forms.FileInput(attrs={
                'class': 'form-control', 'placeholder': 'Rasm',
            }),
            'author_description': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Muallif haqida...',
            }),
            'author_description_uz': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Muallif haqida_uz...',
            }),
            'author_description_en': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Muallif haqida_en...',
            }),
            'author_description_ru': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Muallif haqida_ru...',
            }),
            'author_image': forms.FileInput(attrs={
                'class': 'form-control', 'placeholder': 'Rasm',
            })
        }




