from rest_framework import serializers
from django.contrib.auth.models import User

from source.models import BlogUser


class BlogUserSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='bloguser-highlight', format='html')

    class Meta:
        model = BlogUser
        # fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner', )
        fields = ('url', 'id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    source = serializers.HyperlinkedIdentityField(many=True, view_name='bloguser-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'source')


if __name__ == '__main__':
    serializer = BlogUserSerializer()
    print(repr(serializer))
