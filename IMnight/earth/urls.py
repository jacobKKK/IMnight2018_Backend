from django.conf.urls import url
from earth.views import DailyVocherView, StoreVocherView, hello_world

urlpatterns = [
    url(r'^vocher/$', StoreVocherView.as_view()),
    url(r'^vocher/(?P<storename>.+)/$', StoreVocherView.as_view()),
    url(r'^daily/$', DailyVocherView.as_view()),
    url(r'^use/vocher/$', hello_world),
]
