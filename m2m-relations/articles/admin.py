from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        super().clean()

        main_count = sum(
            1 for form in self.forms
            if form.cleaned_data and form.cleaned_data.get('is_main')
        )

        if main_count != 1:
            raise ValidationError(
                'У статьи должен быть указан ровно один основной раздел.'
            )


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]




@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ('article', 'tag', 'is_main')
    list_filter = ('is_main', 'tag')
