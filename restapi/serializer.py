from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'image', 'score')


class ManyItemsSerializer(serializers.Serializer):
    """ All 'Item' Model serialize. """
    name = serializers.CharField()
    items = ItemSerializer(many=True, allow_null=True, default=Item.objects.all())

    def create(self, validated_data):
        """ Create and return a new 'Item' instance, given the validated data. """
        return Item.objects.create(**validated_data)