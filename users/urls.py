# Copyright 2015 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

from . import views

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'users\login.html'}, name='login'),
    url(r'^password_reset/$', auth_views.password_reset, {'template_name': 'users\password_reset.html'}, name='password_reset'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register/sent/$', views.sent, name='sent'),
]
