from rest_framework import serializers

from Management_app.models import Worker, Brigade


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ('roles', 'name_worker')


class BrigadeSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
    foreman = serializers.StringRelatedField(many=False)
    workers = WorkerSerializer(many=True)

    class Meta:
        model = Brigade
        fields = ('citi', 'foreman', 'workers')

=======
    class Meta:
        model = Brigade
        fields = '__all__'
>>>>>>> origin/authorization
