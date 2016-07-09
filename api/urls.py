from django.conf.urls import url

from api.views import (
    sign_up_list,
    sign_up_detail
)


urlpatterns = [
    url(r'^sign_up/$', sign_up_list, name='sign_up_list'),
    url(r'^sign_up/(?P<pk>[0-9]+)/?$', sign_up_detail, name='sign_up_detail'),
]
