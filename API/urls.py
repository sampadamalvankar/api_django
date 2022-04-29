from django.conf.urls import url
from API import views

urlpatterns=[
    url(r'^user$',views.userapi),
    url(r'^user/([0-9]+)$',views.userapi),

    url(r'^user$',views.clientapi),
    url(r'^user/([0-9]+)$',views.clientapi),

    url(r'^user$',views.projectapi),
    url(r'^user/([0-9]+)$',views.projectapi)

]