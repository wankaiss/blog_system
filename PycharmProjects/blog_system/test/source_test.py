# coding: utf-8

from source.models import BlogUser
from source.serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

user1 = BlogUser(code='name = "Gerald"\n')
user1.save()

user2 = BlogUser(code='print "Hello, world"\n')
user2.save()

serializer = UserSerializer(user2)
serializer.data

content = JSONRenderer().render(serializer.data)
content

from django.utils.six import BytesIO

stream = BytesIO(content)
data = JSONParser().parse(stream)

serializer = UserSerializer(data=data)
serializer.is_valid()
# True
serializer.validated_data
# OrderedDict([('title', ''), ('code', 'print "hello, world"\n'), ('linenos', False), ('language', 'python'),
# ('style', 'friendly')])
serializer.save()

serializer = UserSerializer(BlogUser.objects.all(), many=True)
serializer.data

from source.serializers import UserSerializer
serializer = UserSerializer()
print(repr(serializer))
