from django.conf.urls import url
from earth.views import DailyVocherView, StoreVocherView, UseVocherView

urlpatterns = [
    url(r'^vocher/$', StoreVocherView.as_view()),
    url(r'^vocher/(?P<storename>.+)/$', StoreVocherView.as_view()),
    url(r'^daily/$', DailyVocherView.as_view()),
    url(r'^vocher/user/(?P<label>.+)/$', UseVocherView.as_view()),
]
