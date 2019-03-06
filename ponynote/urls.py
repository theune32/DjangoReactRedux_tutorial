from django.conf.urls import url, include
from django.views.generic import TemplateView

from notes import endpoints

urlpatterns = [
    url(r'^api/', include(endpoints)),
    url(r'^', TemplateView.as_view(template_name="index.html")),
]
