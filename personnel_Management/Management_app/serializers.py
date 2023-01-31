from rest_framework import serializers

from Management_app.models import Worker, Brigade


class WorkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Worker
        fields = ('roles', 'name_worker')


class BrigadeSerializer(serializers.ModelSerializer):
    foreman = serializers.StringRelatedField(many=False)
    workers = WorkerSerializer(many=True)

    class Meta:
        model = Brigade
        read_only = True
        fields = ('citi', 'foreman', 'workers')
        extra_kwargs = {
            'foreman': {'write_only': True},
            'workers': {'allow_blank': True}
        }

