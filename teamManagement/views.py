from django.http import JsonResponse
from .models import TeamMember
from .serializers import TeamSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import os
from django.http import HttpResponse, Http404

FTP_UPLOAD_DIR = 'web/teamMember.html'

def teamMember_view(request):

    # check if requested page exists
    if os.path.exists(FTP_UPLOAD_DIR ):
        # if yes, then serve the page
        with open(FTP_UPLOAD_DIR ) as f:
            response = HttpResponse(f.read())
        return response

    else:
        raise Http404
    
@api_view(['GET','POST'])
def team_memberes(request):
    
    if request.method == 'GET':
        #get all the team members
        #serialize them
        #return json
        teams = TeamMember.objects.all()
        serializer = TeamSerializer(teams, many=True)
        data = serializer.data
        return JsonResponse({'count':len(data),'data':data})
    
    if request.method == 'POST':
        serializer = TeamSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
   
@api_view(['GET','PUT','DELETE'])     
def team_details(request,id):

    try:
        teams = TeamMember.objects.get(pk=id)
    except TeamMember.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TeamSerializer(teams)
        # data = serializer.data
        return Response(serializer.data)

    elif request.method == 'PUT':

        serializer = TeamSerializer(teams,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        teams.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
