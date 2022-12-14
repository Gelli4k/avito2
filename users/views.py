import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet

from avito import settings
from users.models import User, Location
from users.serializers import *


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


# class UserListView(ListView):
#     model = User
#     queryset = User.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         super().get(self, *args, **kwargs)
#         self.object_list = self.object_list.order_by("username")
#         paginator = Paginator(object_list=self.object_list, per_page=settings.TOTAL_ON_PAGE)
#         page = request.GET.get('page')
#         page_obj = paginator.get_page(page)
#         result = []
#         for user in page_obj:
#             result.append({
#                 "id": user.id,
#                 "username": user.username,
#                 "first_name": user.first_name,
#                 "last_name": user.last_name,
#                 "role": user.role,
#                 "ads_count": user.ads.count()
#
#
#             })
#         return JsonResponse({'users': result, 'page': page_obj.number, 'total': page_obj.paginator.count},
#                             safe=False, json_dumps_params={'ensure_ascii': False})


# @method_decorator(csrf_exempt, name='dispatch')
# class UserCreateView(CreateView):
#     model = User
#     fields = ['username', 'password', 'first_name', 'last_name', 'role', 'locations']
#
#     def post(self, request, *args, **kwargs):
#         data = json.load(request.body)
#         user = User.objects.create(
#             username=data['username'],
#             first_name=data['first_name'],
#             last_name=data['last_name'],
#             role=data['role'],
#             password=data['password'],
#         )
#         for loc in data['location']:
#             location, _ = Location.objects.get_or_create(name=loc)
#             user.location.add(location)
#
#         return JsonResponse({
#             'id': user.id,
#             'first_name': user.first_name,
#             'last_name': user.last_name,
#             'role': user.role,
#             'location': [str(u) for u in user.location.all()],
#               }
#         )
# @method_decorator(csrf_exempt, name='dispatch')
# class UserUpdateView(UpdateView):
#     model = User
#     fields = ['username', 'password', 'first_name', 'last_name', 'role', 'locations']
#
#         def patch(self, request, *args, **kwargs):
#         super().post(request, *args, **kwargs)
#         data = json.loads(request.body)
#         self.object.name = data['username', 'password', 'first_name', 'last_name', 'role', 'locations']
#         self.object.save()
#         return JsonResponse({
#             'id': self.object.id,
#             'first_name': self.object.first_name,
#             'last_name': self.object.last_name,
#             'role': self.object.role,
#             'location': [str(u) for u in self.object.location.all()],
#               }
#         )

# @method_decorator(csrf_exempt, name='dispatch')
# class UserDeleteView(DeleteView):
#     model = User
#     success_url = '/'
#
#     def delete(self, request, *args, **kwargs):
#         super().delete(request, *args, **kwargs)
#         return JsonResponse({}, status=204)

class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDeleteSerializer
