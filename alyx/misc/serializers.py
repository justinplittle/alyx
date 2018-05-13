from rest_framework import serializers
from subjects.models import Subject
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    subjects_responsible = serializers.SlugRelatedField(
        many=True, queryset=Subject.objects.all(), slug_field='nickname')

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.prefetch_related('subjects_responsible')
        return queryset

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'subjects_responsible')
