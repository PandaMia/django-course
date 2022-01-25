from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Relationship, Tag


class RelationshipInLineFormset(BaseInlineFormSet):
    def clean(self):
        num_main_scopes = 0
        for form in self.forms:
            form_dict = form.cleaned_data
            if form_dict.get('is_main') is None:
                continue
            elif form_dict['is_main']:
                num_main_scopes += 1
        if num_main_scopes == 0:
            raise ValidationError('Укажите основной раздел')
        elif num_main_scopes > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Relationship
    formset = RelationshipInLineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]
    save_on_top = True


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

