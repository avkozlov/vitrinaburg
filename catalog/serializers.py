
from rest_framework import serializers
from .models import Coll, Picture


class CollSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coll
        fields = ('id', 'title', 'description','slug', 'owner')



