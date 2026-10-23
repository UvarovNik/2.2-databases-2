from django.db import migrations


def add_sample_tags_and_scopes(apps, schema_editor):
    Article = apps.get_model('articles', 'Article')
    Tag = apps.get_model('articles', 'Tag')
    Scope = apps.get_model('articles', 'Scope')

    # Создаём теги
    culture, _ = Tag.objects.get_or_create(name='Культура')
    science, _ = Tag.objects.get_or_create(name='Наука')
    society, _ = Tag.objects.get_or_create(name='Общество')
    space, _ = Tag.objects.get_or_create(name='Космос')
    health, _ = Tag.objects.get_or_create(name='Здоровье')

    # Связываем статьи с тегами
    articles = list(Article.objects.all().order_by('pk'))

    if len(articles) >= 1:
        # Статья 1: В "Детском мире" на Лубянке откроют музей
        Scope.objects.get_or_create(
            article=articles[0], tag=culture,
            defaults={'is_main': True}
        )
        Scope.objects.get_or_create(
            article=articles[0], tag=society,
            defaults={'is_main': False}
        )

    if len(articles) >= 2:
        # Статья 2: Ученые доказали вред периодического курения
        Scope.objects.get_or_create(
            article=articles[1], tag=health,
            defaults={'is_main': True}
        )
        Scope.objects.get_or_create(
            article=articles[1], tag=science,
            defaults={'is_main': False}
        )

    if len(articles) >= 3:
        # Статья 3: Директор ИКИ РАН ...
        Scope.objects.get_or_create(
            article=articles[2], tag=space,
            defaults={'is_main': True}
        )
        Scope.objects.get_or_create(
            article=articles[2], tag=science,
            defaults={'is_main': False}
        )
        Scope.objects.get_or_create(
            article=articles[2], tag=society,
            defaults={'is_main': False}
        )


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_alter_article_options_scope_article_tags'),
    ]

    operations = [
        migrations.RunPython(add_sample_tags_and_scopes, migrations.RunPython.noop),
    ]
