from django.urls import include, path

urlpatterns = [
    path('', include('dndtoolshelper.api.urls')),
]

handler400 = 'rest_framework.exceptions.bad_request'
handler500 = 'rest_framework.exceptions.server_error'
