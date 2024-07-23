from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import date
from .models import RawData, NewData
from .serializers import NewDataSerializer

class TransformDataView(APIView):
    def post(self, request):
        raw_data = RawData.objects.all()
        new_data_entries = []

        for data in raw_data:
            nombre_completo = f"{data.nombre} {data.apellido}"
            edad_nominal = (date.today() - data.edad).days // 365
            new_data_entry = NewData(nombre_completo=nombre_completo, edad_nominal=edad_nominal)
            new_data_entries.append(new_data_entry)
        
        NewData.objects.bulk_create(new_data_entries)
        return Response({'status': 'Se ha tranformado su informacion correctamente'}, status=status.HTTP_201_CREATED)

class NewDataListView(generics.ListAPIView):
    queryset = NewData.objects.all()
    serializer_class = NewDataSerializer
