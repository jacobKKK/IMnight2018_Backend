from django.conf.urls import url
from earth.views import DailyVocherView, StoreVocherView

urlpatterns = [
    url(r'^vocher/$', StoreVocherView.as_view()),
    url(r'^vocher/(?P<storename>.+)/$', StoreVocherView.as_view()),
    url(r'^daily/$', DailyVocherView.as_view()),
]
