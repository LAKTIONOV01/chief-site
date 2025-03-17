from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin


# Register your models here.


class RecipeInline(admin.StackedInline):
    model = Recipe
    extra = 1


@admin.register(Categories)
class CategoriesAdmin(MPTTModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'serves', 'prep_time', 'cook_time']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'text', 'author']
    inlines = [RecipeInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'message']


admin.site.register(Tag)
