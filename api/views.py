from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ServiceSerializerWeb,BusinesSerializerWeb,UserSerializerWeb,FaqSerializerWeb,ClientSerializerWeb,CommentSerializerWeb
from .models import Services,Busines,Users,FAQs,Clients,Comments
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import TokenAuthentication



class ServiceViewsetWeb(viewsets.ModelViewSet):
    serializer_class = ServiceSerializerWeb
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return Services.objects.filter(status='pb')

    def get(self, request):
        query = self.get_queryset()
        search_data = request.query_params.get('search')
        if search_data is not None:
            query = query.filter(title__icontains=search_data)
        serializer = ServiceSerializerWeb(query, many=True)
        return Response(data=serializer.data)

    @action(detail=True, methods=['GET',])
    def see(self,request,*args,**kwargs):
        service = self.get_object()
        service.see += 1
        service.save()
        return Response(data={'seen':service.see})

    @action(detail=False, methods=['GET',])
    def null_see(self,request,*args,**kwargs):
        services = self.get_queryset().filter(see=0)
        serializer = ServiceSerializerWeb(services, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET',])
    def all_see(self,request,*args,**kwargs):
        services = self.get_queryset()
        for service in services:
            service.see += 1
            service.save()
        return Response(data={"message":"all service seen"})





class BusinesViewsetWeb(viewsets.ModelViewSet):
    serializer_class = BusinesSerializerWeb
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return Busines.objects.filter(status='pb')

    def get(self, request):
        query = self.get_queryset()
        search_data = request.query_params.get('search')
        if search_data is not None:
            query = query.filter(title__icontains=search_data)
        serializer = BusinesSerializerWeb(query, many=True)
        return Response(data=serializer.data)

    @action(detail=True, methods=['GET',])
    def see(self,request,*args,**kwargs):
        busines = self.get_object()
        busines.see += 1
        busines.save()
        return Response(data={'seen':busines.see})

    @action(detail=False, methods=['GET',])
    def null_see(self,request,*args,**kwargs):
        businesses = self.get_queryset().filter(see=0)
        serializer = BusinesSerializerWeb(businesses, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET',])
    def all_see(self,request,*args,**kwargs):
        businesses = self.get_queryset()
        for busines in businesses:
            busines.see += 1
            busines.save()
        return Response(data={"message":"all busines seen"})




class UserViewsetWeb(viewsets.ModelViewSet):
    serializer_class = UserSerializerWeb
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return Users.objects.filter(status='pb')

    def get(self, request):
        query = self.get_queryset()
        search_data = request.query_params.get('search')
        if search_data is not None:
            query = query.filter(first_name__icontains=search_data)
        serializer = UserSerializerWeb(query, many=True)
        return Response(data=serializer.data)

    @action(detail=True, methods=['GET',])
    def see(self,request,*args,**kwargs):
        user = self.get_object()
        user.see += 1
        user.save()
        return Response(data={'seen':user.see})

    @action(detail=False, methods=['GET',])
    def null_see(self,request,*args,**kwargs):
        users = self.get_queryset().filter(see=0)
        serializer = UserSerializerWeb(users, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET',])
    def all_see(self,request,*args,**kwargs):
        users = self.get_queryset()
        for user in users:
            user.see += 1
            user.save()
        return Response(data={"message":"all user seen"})




class ClientViewsetWeb(viewsets.ModelViewSet):
    serializer_class = ClientSerializerWeb
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return Clients.objects.filter(status='pb')

    def get(self, request):
        query = self.get_queryset()
        search_data = request.query_params.get('search')
        if search_data is not None:
            query = query.filter(first_name__icontains=search_data)
        serializer = ClientSerializerWeb(query, many=True)
        return Response(data=serializer.data)

    @action(detail=True, methods=['GET',])
    def see(self,request,*args,**kwargs):
        client = self.get_object()
        client.see += 1
        client.save()
        return Response(data={'seen':client.see})

    @action(detail=False, methods=['GET',])
    def null_see(self,request,*args,**kwargs):
        clients = self.get_queryset().filter(see=0)
        serializer = ClientSerializerWeb(clients, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET',])
    def all_see(self,request,*args,**kwargs):
        clients = self.get_queryset()
        for client in clients:
            client.see += 1
            client.save()
        return Response(data={"message":"all client seen"})




class FaqViewsetWeb(viewsets.ModelViewSet):
    serializer_class = FaqSerializerWeb
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return FAQs.objects.filter(status='pb')

    def get(self, request):
        query = self.get_queryset()
        search_data = request.query_params.get('search')
        if search_data is not None:
            query = query.filter(question__icontains=search_data)
        serializer = FaqSerializerWeb(query, many=True)
        return Response(data=serializer.data)

    @action(detail=True, methods=['GET',])
    def see(self,request,*args,**kwargs):
        faq = self.get_object()
        faq.see += 1
        faq.save()
        return Response(data={'seen':faq.see})

    @action(detail=False, methods=['GET',])
    def null_see(self,request,*args,**kwargs):
        faqs = self.get_queryset().filter(see=0)
        serializer = FaqSerializerWeb(faqs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET',])
    def all_see(self,request,*args,**kwargs):
        faqs = self.get_queryset()
        for faq in faqs:
            faq.see += 1
            faq.save()
        return Response(data={"message":"all faq seen"})




class CommentViewsetWeb(viewsets.ModelViewSet):
    serializer_class = CommentSerializerWeb
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return Comments.objects.filter(status='pb')

    def get(self, request):
        query = self.get_queryset()
        search_data = request.query_params.get('search')
        if search_data is not None:
            query = query.filter(comment__icontains=search_data)
        serializer = CommentSerializerWeb(query, many=True)
        return Response(data=serializer.data)

    @action(detail=True, methods=['GET',])
    def see(self,request,*args,**kwargs):
        comment = self.get_object()
        comment.see += 1
        comment.save()
        return Response(data={'seen':comment.see})

    @action(detail=False, methods=['GET',])
    def null_see(self,request,*args,**kwargs):
        comments = self.get_queryset().filter(see=0)
        serializer = CommentSerializerWeb(comments, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET',])
    def all_see(self,request,*args,**kwargs):
        comments = self.get_queryset()
        for comment in comments:
            comment.see += 1
            comment.save()
        return Response(data={"message":"all comment seen"})