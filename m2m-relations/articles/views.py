from django.views.generic import ListView

from articles.models import Article


class ArticlesListView(ListView):
    model = Article
    queryset = Article.objects.all().order_by('-published_at')
    template_name = 'articles/news.html'


articles_list = ArticlesListView.as_view()
