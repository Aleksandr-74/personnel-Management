from rest_framework import serializers

from Management_app.models import Worker, Brigade


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ('roles', 'name_worker')


class BrigadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brigade
        fields = '__all__'