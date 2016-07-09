from rest_framework import viewsets

from api.models import (
    SignUp
)

from api.serializers import (
    SignUpSerializer
)


class SignUpViewSet(viewsets.ModelViewSet):
    queryset = SignUp.objects.all()
    serializer_class = SignUpSerializer


sign_up_list = SignUpViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

sign_up_detail = SignUpViewSet.as_view({
     'get': 'retrieve',
     'put': 'update',
     'patch': 'partial_update',
     'delete': 'destroy'
})


