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
    keywords = GenericRelation(Keyword, related_query_name='articles')

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

    GREATER_THAN = 1
    LESS_THAN = 2
    IN = 3
    EQUAL = 5
    OPERATOR_CHOICES = (
        (GREATER_THAN, 'greater than'),
        (LESS_THAN, 'less than'),
        (IN, 'in'),
        (EQUAL, 'equal to'),
    )

    ILLNESS_LENGTH = 1
    FOLLOW_UP_PERIOD = 2
    SPECTRUM_OF_DISEASE = 3
    TYPE_OF_STUDY = 4
    DIAGNOSIS_SYSTEM = 5
    CATEGORY_CHOICES = (
        (ILLNESS_LENGTH, 'illness length'),
        (FOLLOW_UP_PERIOD, 'follow-up period'),
        (SPECTRUM_OF_DISEASE, 'spectrum of disease'),
        (TYPE_OF_STUDY, 'type of study'),
        (DIAGNOSIS_SYSTEM, 'diagnosis system'),
    )
    CATEGORY_META = {
        ILLNESS_LENGTH: {
            'cast': int,
            'accept': (GREATER_THAN, LESS_THAN, EQUAL, )
        },
        ILLNESS_LENGTH: {
            'cast': int,
            'accept': (GREATER_THAN, LESS_THAN, EQUAL, )
        },
        SPECTRUM_OF_DISEASE: {
            'cast': list,
            'accept': (IN, )
        }

    }

    review = models.ForeignKey(Review, related_name='criteria')
    text = models.TextField(max_length=1000)
    criteria_type = models.PositiveSmallIntegerField(choices=CRITERIA_TYPE_CHOICES, default=INCLUSION)
    category = models.PositiveSmallIntegerField(choices=CATEGORY_CHOICES)
    operator = models.PositiveSmallIntegerField(choices=OPERATOR_CHOICES)

    class Meta:
        verbose_name = 'criteria'
        verbose_name_plural = 'criteria'
        db_table = 'criteria'
