"""alyx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.authtoken import views as av
from rest_framework.documentation import include_docs_urls

from subjects import views as subjects_views
from actions import views as actions_views
from data import views as data_views
from misc import views as misc_views


datarepositorytype_list = data_views.DataRepositoryTypeViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
datarepositorytype_detail = data_views.DataRepositoryTypeViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


datarepository_list = data_views.DataRepositoryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
datarepository_detail = data_views.DataRepositoryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


datasettype_list = data_views.DatasetTypeViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
datasettype_detail = data_views.DatasetTypeViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


data_format_list = data_views.DataFormatViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
data_format_detail = data_views.DataFormatViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


dataset_list = data_views.DatasetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
dataset_detail = data_views.DatasetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


project_list = subjects_views.ProjectViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
project_detail = subjects_views.ProjectViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


filerecord_list = data_views.FileRecordViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
filerecord_detail = data_views.FileRecordViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
register_file = data_views.RegisterFileViewSet.as_view({
    'post': 'create'
})


timescale_list = data_views.TimescaleViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
timescale_detail = data_views.TimescaleViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


user_list = misc_views.UserViewSet.as_view({
    'get': 'list'
})
user_detail = misc_views.UserViewSet.as_view({
    'get': 'retrieve'
})

admin.site.site_header = 'Alyx'

urlpatterns = [
    url(r'^$', misc_views.api_root),
    url(r'^docs/', include_docs_urls(title='Alyx REST API documentation')),

    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth-token', av.obtain_auth_token),

    url(r'^weighings$', actions_views.WeighingAPIListCreate.as_view(), name="weighing-create"),
    url(r'^weighings/(?P<pk>[-_\w].+)$', actions_views.WeighingAPIDetail.as_view(),
        name="weighing-detail"),

    url(r'^water-administrations$', actions_views.WaterAdministrationAPIListCreate.as_view(),
        name="water-administration-create"),

    url(r'^water-administrations/(?P<pk>[-_\w].+)$',
        actions_views.WaterAdministrationAPIDetail.as_view(), name="water-administration-detail"),

    url(r'^subjects$', subjects_views.SubjectList.as_view(), name="subject-list"),
    url(r'^subjects/(?P<nickname>[-._~\w]+)$', subjects_views.SubjectDetail.as_view(),
        name="subject-detail"),

    url(r'^sessions$', actions_views.SessionAPIList.as_view(), name="session-list"),
    url(r'^sessions/(?P<pk>[-_\w].+)$', actions_views.SessionAPIDetail.as_view(),
        name="session-detail"),

    url(r'^exp-metadata$', data_views.ExpMetadataList.as_view(), name="exp-metadata-list"),
    url(r'^exp-metadata/(?P<pk>[-_\w].+)$', data_views.ExpMetadataDetail.as_view(),
        name="exp-metadata-detail"),


    url(r'^data-repository-type$', datarepositorytype_list, name="datarepositorytype-list"),
    url(r'^data-repository-type/(?P<name>[-_\w].+)$', datarepositorytype_detail,
        name="datarepositorytype-detail"),

    url(r'^data-repository$', datarepository_list, name="datarepository-list"),
    url(r'^data-repository/(?P<name>[-_\w].+)$', datarepository_detail,
        name="datarepository-detail"),

    url(r'^data-formats$', data_format_list, name="dataformat-list"),
    url(r'^data-formats/(?P<name>[-_\w].+)$', data_format_detail, name="dataformat-detail"),

    url(r'^dataset-types$', datasettype_list, name="datasettype-list"),
    url(r'^dataset-types/(?P<name>[-_\w].+)$', datasettype_detail, name="datasettype-detail"),

    url(r'^datasets$', dataset_list, name="dataset-list"),
    url(r'^datasets/(?P<pk>[-_\w].+)$', dataset_detail, name="dataset-detail"),

    url(r'^projects$', project_list, name="project-list"),
    url(r'^projects/(?P<name>[-_\w].+)$', project_detail, name="project-detail"),

    url(r'^files$', filerecord_list, name="filerecord-list"),
    url(r'^files/(?P<pk>[-_\w].+)$', filerecord_detail, name="filerecord-detail"),

    url(r'^register-file$', register_file, name="register-file"),

    url(r'^timescales$', timescale_list, name="timescale-list"),
    url(r'^timescales/(?P<pk>[-_\w].+)$', timescale_detail, name="timescale-detail"),


    url(r'^users$', user_list, name='user-list'),
    url(r'^users/(?P<username>[-_\w].+)$', user_detail, name='user-detail'),

    url(r'^water-restricted-subjects$', subjects_views.WaterRestrictedSubjectList.as_view(),
        name="water-restricted-subject-list"),

    url(r'^water-requirement/(?P<nickname>[-._~\w]+)$', actions_views.WaterRequirement.as_view(),
        name='water-requirement'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^admin-subjects/', include('subjects.urls')),
    url(r'^admin-actions/', include('actions.urls')),

]
