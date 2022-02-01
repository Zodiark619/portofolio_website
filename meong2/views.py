from django.shortcuts import render

from rest_framework.response import Response
from meong2.models import waifu,expansion,faction,type
from meong2.serializer import WaifuSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer,TemplateHTMLRenderer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
def django_rest(request):
    return render(request,'drf.html',{})







@api_view(['GET', 'POST'])
def django_rest1_api(request):
    permission_classes = [IsAuthenticated]
    

    if request.method == 'GET':
        momo = waifu.objects.all()
        serializer = WaifuSerializer(momo, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = WaifuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    # if request.method == 'PUT':
    #     bucin = waifu.objects.get(pk=pk)
    #     serializer = WaifuSerializer(bucin, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # if request.method == 'DELETE':
    #     bucin = waifu.objects.get(pk=pk)
    #     bucin.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)




def django_rest1(request):
    waifus = waifu.objects.all()
    expansions=expansion.objects.all()
    factions=faction.objects.all()
    types=type.objects.all()

    data = {
        'waifus': list(waifus.values()),
        'expansions': list(expansions.values()),
        'factions': list(factions.values()),
        'types': list(types.values())


        }

    if request.POST.get('request-type')=='detail-api':
        data['command']=True
    elif request.POST.get('request-type')=='filter-api':
        data['command']=False

    if request.POST.get('detail-query')=='detail-query':
        detail_id=request.POST.get('detail')
        details=waifu.objects.get(pk=detail_id)
        data['exist']=True
        data['result']=details
        detail_type=details.type.values_list()
        detail_result=''
        for meong in detail_type:
            detail_result+=meong[:][1]
            detail_result+=' ,'
        detail_result=detail_result[:-1]
        data['message']=f"This object ID is {detail_id}. Her name is {details.name} from {details.faction} faction and appeared in {details.expansion} expansion. She is {detail_result} type(s)"

    if request.POST.get('filter-query')=='filter-query':
        factions=request.POST.get('factions')
        types=request.POST.get('types')
        expansions=request.POST.get('expansions')
        result=waifu.objects.filter(expansion__name__icontains=expansions,type__name__icontains=types,faction__name__icontains=factions)
        message=f"Your query is to filter waifus with {types} type in {factions} faction and released on {expansions} expansion"
        data['message']=message


        if result.exists():
            data['result']=list(result.values())
        else:   
            data['exist']=True
            data['result']='No result found. Try different combination.'
        
            
        
        print(data['result'])
    # return JsonResponse(data)
    return render(request,'drf1.html',data)


 



    # if request.method == 'GET':
    #     susu = waifu.objects.all()
    #     serializer = WaifuSerializer(susu, many=True)
    #     # return render(request,'drf1.html',{'serializer':serializer.data})
    #     return Response(serializer.data)
    # if request.method == 'POST':
    #     serializer =WaifuSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return render(request,'drf1.html',{'serializer':serializer.data})
    #     else:
    #         return Response(serializer.errors)


    