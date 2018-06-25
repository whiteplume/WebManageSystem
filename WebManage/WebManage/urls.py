from django.conf.urls import patterns, include, url
from django.contrib import admin
from signatures.views import *
from cheats.views import *
from games.views import *


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WebManage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')), 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^exportsign/$', exportsign, name='exportsign'),
    url(r'^exportbrd/$', exportbrd, name='exportbrd'),
    url(r'^exportban/$', exportban, name='exportban'),
    url(r'^exportgame/$', exportgame, name='exportgame'),
    url(r'^exportrd/$', exportrd, name='exportrd'),
                       
    url(r'^line_index/$', line_index, name='line_index'),
    url(r'^column_index/$', column_index, name='column_index'),
    url(r'^pie_index/$', pie_index, name='pie_index'),


    url(r'^column/$', column, name='column'),
    url(r'^line/$', line, name='line'),
    url(r'^pie_game/$', pie_game, name='pie_game'),
)
