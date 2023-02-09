from rest_framework import serializers
from .models import Performer, Album


class AlbumSerializer(serializers.ModelSerializer):
    all_songs = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = ['year_of_release', 'all_songs']

    def get_all_songs(self, obj):
        p = obj.songs.all()
        list_of_song_info = []
        for i in range(p.count()):
            song_info = {}
            song_info['number'] = i+1
            song_info['title'] = p[i].title
            list_of_song_info.append(song_info)
        return list_of_song_info


class PerformerListSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True)

    class Meta:
        model = Performer
        fields = ['title', 'albums']
