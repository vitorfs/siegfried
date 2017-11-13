from django.http import Http404

from .models import Review


class ReviewMixin:
    _cached_review = None

    @property
    def review(self):
        if self._cached_review:
            return self._cached_review
        pk = self.kwargs.get('pk')
        try:
            self._cached_review = Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            raise Http404
        return self._cached_review

    def get_context_data(self, **kwargs):
        '''
        Insert the review into the context dict.
        '''
        if 'review' not in kwargs:
            kwargs['review'] = self.review
        return super().get_context_data(**kwargs)