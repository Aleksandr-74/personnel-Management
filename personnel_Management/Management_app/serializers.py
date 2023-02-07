from rest_framework import serializers

from Management_app.models import Worker, Brigade, Objectes


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


class ObjectSeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Objectes
        fields = ('name', 'place_work', 'description', 'type_works',
                  'status_work', 'start_time', 'finishing_time', 'brigades')

