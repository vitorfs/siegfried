from django.db import models
from django.urls import reverse


class Review(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'review'
        verbose_name_plural = 'reviews'
        db_table = 'reviews'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_list', args=(self.pk, ))


class Article(models.Model):
    title = models.CharField(max_length=1000)
    abstract = models.TextField(blank=True)
    authors = models.CharField(max_length=4000, blank=True)
    review = models.ForeignKey(Review, related_name='articles')

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'
        db_table = 'articles'

    def __str__(self):
        return self.title
