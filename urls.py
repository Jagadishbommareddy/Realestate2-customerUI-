
from django.conf.urls import  include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns =[
    url(r'^admin/', include(admin.site.urls)),
    url(r'^formtestt/$', "Tagent2.views.hello"),
    url(r'^formtestt/([1-9][0-9]*)$', "Tagent2.views.helloparams"),
    url(r'^people$', "Tagent2.views.people"),
    url(r'^$', "Tagent2.views.index"),


]