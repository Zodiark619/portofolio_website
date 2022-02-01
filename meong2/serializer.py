from rest_framework import serializers
from meong2 import models

class WaifuSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.waifu
        fields = '__all__'