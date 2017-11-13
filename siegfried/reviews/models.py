from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
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


class Keyword(models.Model):
    text = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    class Meta:
        verbose_name = 'keyword'
        verbose_name_plural = 'keywords'
        db_table = 'keywords'

    def __str__(self):
        return self.text


class Article(models.Model):
    title = models.CharField(max_length=1000)
    abstract = models.TextField(blank=True)
    authors = models.CharField(max_length=4000, blank=True)
    review = models.ForeignKey(Review, related_name='articles')
    title_keywords = GenericRelation(Keyword)
    abstract_keywords = GenericRelation(Keyword)

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'
        db_table = 'articles'

    def __str__(self):
        return self.title


class Criteria(models.Model):
    INCLUSION = 1
    EXCLUSION = 2
    CRITERIA_TYPE_CHOICES = (
        (INCLUSION, 'inclusion criteria'),
        (EXCLUSION, 'exclusion criteria'),
    )

    review = models.ForeignKey(Review, related_name='criterion')
    text = models.CharField(max_length=1000)
    criteria_type = models.PositiveSmallIntegerField(choices=CRITERIA_TYPE_CHOICES, default=INCLUSION)

    class Meta:
        verbose_name = 'criteria'
        verbose_name_plural = 'criterion'
        db_table = 'criterion'
