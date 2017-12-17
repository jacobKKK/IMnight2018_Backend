from django.conf.urls import url
from .views import (UserDetailsView)

urlpatterns = [
    # URLs that do not require a session or valid token
    url(r'^user/self$', UserDetailsView.as_view()),
]
