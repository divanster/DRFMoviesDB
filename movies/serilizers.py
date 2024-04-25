from rest_framework import serializers
from .models import Moviedata


class MovieSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(max_length=None, allow_empty_file=False, required=False, use_url=True)
    # This can be added if fields are not ALL, if you specified separate fiels. Its variable, must be put into fields...

    class Meta:
        model = Moviedata
        fields = '__all__'
