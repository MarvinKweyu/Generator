from datetime import datetime
from rest_framework import generics
from rest_framework.response import Response
from generationapp.models import IdStamp
from generationapp.serializers import IdStampSerializer

class IdStampList(generics.ListAPIView):
    queryset = IdStamp.objects.all()
    serializer_class = IdStampSerializer

    def list(self, request, *args, **kwargs):
        #  create new item everytime I make a get request
        new_idstamp = IdStamp(
              timestamp=datetime.now()
        )
        new_idstamp.save()
        # item saved

        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        #  reverse this result to return the latest item first
        data = {obj['timestamp']: obj['id'] for obj in list(reversed(serializer.data))}
        return Response(data)


class IdStampDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IdStamp.objects.all()
    serializer_class = IdStampSerializer

