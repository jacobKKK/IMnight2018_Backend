from django.conf.urls import url
from .views import (SelfDetailsView, UserDetailsView)

urlpatterns = [
    # URLs that do not require a session or valid token
    url(r'^user/self/', SelfDetailsView.as_view()),
    url(r'^user/$', UserDetailsView.as_view()),
    url(r'^user/(?P<username>.+)/', UserDetailsView.as_view()),
]
