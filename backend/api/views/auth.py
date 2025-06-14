from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from ..models import User, Group


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def save(self, **kwargs):
        user = User(username=self.validated_data['username'])
        password = self.validated_data['password']

        if len(password) < 6:
            raise serializers.ValidationError('Password length must be greater than 6.')

        user.set_password(password)
        user.save()

        group, _ = Group.objects.get_or_create(name='Regular')
        user.groups.add(group)
        user.save()

        return user

@api_view(['POST'])
@permission_classes(()) # allow everyone
def signup(request):
    serializer = SignupSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        return Response({
            'id': user.id,
        }, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

