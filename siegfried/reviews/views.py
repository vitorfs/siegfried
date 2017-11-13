from django.views.generic import CreateView, DetailView, FormView, ListView, View
from django.shortcuts import redirect

import xlrd

from .forms import UploadArticlesForm
from .mixins import ReviewMixin
from .models import Article, Review


class ReviewListView(ListView):
    model = Review
    context_object_name = 'reviews'


class ReviewCreateView(CreateView):
    model = Review
    fields = ('title', )


class ArticleListView(ReviewMixin, ListView):
    model = Article
    context_object_name = 'articles'
    paginate_by = 100

    def get_queryset(self):
        return self.review.articles.order_by('title')


class ImportExcelView(ReviewMixin, FormView):
    form_class = UploadArticlesForm
    template_name = 'reviews/import_excel.html'

    def form_valid(self, form):
        spreadsheet = form.cleaned_data.get('spreadsheet')
        wb = xlrd.open_workbook(filename=None, file_contents=spreadsheet.read())
        ws = wb.sheets()[0]
        articles = list()
        for row in range(1, ws.nrows):
            authors = ws.cell(row, 2).value
            title = ws.cell(row, 3).value
            abstract = ws.cell(row, 5).value
            articles.append(Article(authors=authors, title=title, abstract=abstract, review=self.review))
        Article.objects.bulk_create(articles)
        return redirect(self.review.get_absolute_url())


class DeleteAllArticlesView(ReviewMixin, View):
    def post(self, request, pk):
        self.review.articles.all().delete()
        return redirect('article_list', self.review.pk)
