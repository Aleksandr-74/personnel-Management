from rest_framework import serializers

from Management_app.models import Worker, Brigade


class WorkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Worker
        fields = ('roles', 'name_worker')


class BrigadeSerializer(serializers.ModelSerializer):
    workers = WorkerSerializer(many=True)

    class Meta:
        model = Brigade
        read_only = True
        fields = ('citi', 'workers')
        extra_kwargs = {
           'workers': {'allow_blank': False}
        }

