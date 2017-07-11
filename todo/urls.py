from django.conf.urls import url
import todo.views as views

urlpatterns = [
    url(r'^$', views.todo_list, name="todo"),
    url(r'^id=(?P<pk>[0-9]+)$', views.detail_by_pk, name="detail_pk"),
    url(r'^(?P<priority>\d+)$', views.detail_by_priority, name="detail_priority"),
    url(r'^suggest', views.suggest, name="suggest"),
]
