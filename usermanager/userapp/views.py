import os
import json
import pandas as pd
from pathlib import Path
from .serializer import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response



class UsersView(APIView):

    def get(self, request):
        file_path = os.path.dirname(os.path.realpath(__file__)) + os.sep + "user-data.xlsx"
        df = pd.read_excel(file_path, parse_dates=['date'],engine='openpyxl')
        df["date"] = df["date"].dt.strftime("%Y-%m-%d")
        data = json.loads(df.to_json(orient='records'))
        serializer = UserSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class HealthCheck(APIView):

    def get(self, request):
        result = {"status": "Healthy"}
        return Response(result, status=status.HTTP_200_OK)







