from django.shortcuts import render
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ResourceSerializers , TagSerializer
from .user_serializers import RegisterSerializers
from .models import Resources , Tag
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema

# Create your views here.
@extend_schema(
    request=RegisterSerializers,
    responses=RegisterSerializers
)
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated]) # adds authentication layer for validating user
def first_api(request):
    search = request.query_params.get('search')
    resource_type = request.query_params.get('resource_type')
    order = request.query_params.get('order')
    tags = request.query_params.get('tags')
    data = Resources.objects.filter(owner=request.user)
    # data = Resources.objects.all()
    if request.method == 'POST' :
        serializer = ResourceSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save(owner = request.user) # it triggers the create() function
            return Response(serializer.data , status = 201)
        return Response(serializer.errors, status = 400)
    # 400 : for client side error
    # 500 : for internal server error
    # filtering 
    if search :
        data = data.filter(name=search)
    if resource_type:
        data = data.filter(resource_type=resource_type)
    # _icontains is ORM lookup used to use the case insesnsitive , _contains is used for case sensitive to filter
    # ordering
    if order=='newest' :
        data = data.order_by('-created_at')
    if order=='oldest' :
        data = data.order_by('created_at')
    if tags :
        data = data.filter(tag__id=tags)
    
    paginator = PageNumberPagination()
    paginator.page_size = 1

    paginated_queryset = paginator.paginate_queryset(data, request)

    serializer = ResourceSerializers(paginated_queryset, many=True)

    return paginator.get_paginated_response(serializer.data)

        

# register api view
@extend_schema(
    request=ResourceSerializers,
    responses=ResourceSerializers
)
@api_view(['POST'])
def register_api(request):
    if request.method=='POST':
        serializer = RegisterSerializers(data=request.data )
        if serializer.is_valid():
            serializer.save() # it triggers the create() function
            return Response({"msg":"user registered successfully"},status=201)
        return Response(serializer.errors, status=400)
        
# login view , now JWT takes this work of authentication 
# @api_view(['POST'])
# def login_api(request):
    
#     username = request.data.get('username')
#     password = request.data.get('password')
#     # checking whether user with specific username and password exists or not
#     user = authenticate(username=username ,password= password)
#     # return user objects or None
    
#     if not user :
#         return Response({'error':'invalid credentials'}, status=401)
    
#     token,created = Token.objects.get_or_create(user=user)
#     # if token exists use it else create one
#     # .get_or_create returns a tuple : (token_object, created_boolean)
#     return Response({'token': token.key})

@extend_schema(
    request=TagSerializer,
    responses=TagSerializer
)
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def tag_api(request):
    if request.method =="POST" :
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    tags = Tag.objects.all()
    serializer = TagSerializer(tags, many=True)

    return Response(serializer.data)

@extend_schema(
    request=ResourceSerializers,
    responses=ResourceSerializers
)
@api_view(['PUT','DELETE'])
@permission_classes([IsAuthenticated])
def resource_operation_api(request,id):
        
    resource = get_object_or_404(Resources, id=id)

    # ownership check
    if resource.owner != request.user:
        return Response({"error": "Not allowed"}, status=403)

    # GET single resource
    if request.method == 'GET':
        serializer = ResourceSerializers(resource)
        return Response(serializer.data)

    # UPDATE
    if request.method == 'PUT':
        serializer = ResourceSerializers(resource, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    # DELETE
    if request.method == 'DELETE':
        resource.delete()
        return Response({"message": "Deleted"}, status=204)
