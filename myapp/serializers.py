from rest_framework import serializers
from .models import Singer,Song
class songSerializer(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields='__all__'
class SingerSerializer(serializers.ModelSerializer):
    #song=serializers.StringRelatedField(many=True,read_only=True)
    song=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='song-detail')
    class Meta:
        model=Singer
        fields='__all__'        