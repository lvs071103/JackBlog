from django.contrib import admin
from blog.models import Blog
from blog.models import BackendCkeditor
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

# Register your models here.
class PostAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = BackendCkeditor
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

admin.site.register(Blog, PostAdmin)
