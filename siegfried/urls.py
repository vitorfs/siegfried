from django.conf.urls import url, include

from siegfried.reviews import views

urlpatterns = [
    url(r'^$', views.ReviewListView.as_view(), name='review_list'),
    url(r'^new/$', views.ReviewCreateView.as_view(), name='review_create'),
    url(r'^(?P<pk>\d+)/', include([
        url(r'^$', views.ArticleListView.as_view(), name='article_list'),
        url(r'^clear/$', views.DeleteAllArticlesView.as_view(), name='delete_all_articles'),
        url(r'^import/$', views.ImportExcelView.as_view(), name='import_excel'),
        url(r'^criteria/$', views.CriteriaListView.as_view(), name='criteria_list'),
        url(r'^criteria/new/$', views.CriteriaCreateView.as_view(), name='criteria_create'),
    ])),
]
