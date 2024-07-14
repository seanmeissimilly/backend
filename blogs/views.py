from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes, schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogSerializer, CommentSerializer
from .models import Blog, Comment
from users.models import User
from users.permissions import IsAdmin, IsEditor, IsReader
from rest_framework.schemas import ManualSchema


@api_view(["GET"])
#!: Reviso si está autentificado.
@permission_classes([IsAuthenticated])
def getBlogs(request):
    blog = Blog.objects.filter().order_by("-date")
    serializer = BlogSerializer(blog, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
#!: Reviso si está autentificado.
@permission_classes([IsAuthenticated])
def getSoloBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    serializer = BlogSerializer(blog, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
#!: Reviso si está autentificado y si tiene rol de Editor o Administrador.
@permission_classes([IsAuthenticated & IsAdmin | IsAuthenticated & IsEditor])
def postBlog(request):
    data = request.data
    image_file = request.FILES.get("image")

    # todo: Creo un diccionario con los datos que siempre se pasan.
    blog_data = {
        "user": request.user,
        "body": data["body"],
    }

    # todo: Si me pasaron alguna imagen, la añado al diccionario.
    if image_file is not None:
        blog_data["image"] = image_file

    # todo: Creo el objeto Blog con los datos del diccionario.
    blog = Blog.objects.create(**blog_data)

    serializer = BlogSerializer(blog, many=False)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["POST"])
#!: Reviso si está autentificado.
@permission_classes([IsAuthenticated & IsAdmin | IsAuthenticated & IsEditor])
def uploadImage(request, pk):
    data = request.data
    user = data["user"]
    blog = blog.objects.get(id=pk)
    #!: Reviso que el usuario que hizo el blog sea el mismo que la esté actualizando la foto o que tenga el rol de admin.
    if blog.user == user or user.role == "admin":
        blog.image = request.FILES.get("image")
        blog.save()
        return Response("Imagen subida")
    else:
        return Response({"Error": "No autorizado"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(["PUT"])
# !: Reviso si está autentificado.
@permission_classes([IsAuthenticated & IsAdmin | IsAuthenticated & IsEditor])
def putBlog(request, pk):
    data = request.data
    try:
        blog = Blog.objects.get(id=pk)
    except Blog.DoesNotExist:
        return Response(
            {"Error": "Blog no encontrado"}, status=status.HTTP_404_NOT_FOUND
        )
    serializer = BlogSerializer(instance=blog, data=data)
    #!: Reviso que el usuario que hizo el blog sea el mismo que la esté actualizando o que tenga el rol de admin.
    if blog.user == request.user or request.user.role == "admin":
        if serializer.is_valid():
            serializer.save()
    else:
        return Response({"Error": "No autorizado"}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.data)


@api_view(["DELETE"])
#!: Reviso si está autentificado.
@permission_classes([IsAuthenticated & IsAdmin | IsAuthenticated & IsEditor])
def deleteBlog(request, pk):
    # Busco el blog segun el id.
    try:
        blog = Blog.objects.get(id=pk)
    except Blog.DoesNotExist:
        return Response(
            {"Error": "Blog no encontrado"}, status=status.HTTP_404_NOT_FOUND
        )

    #!: Reviso que el usuario que hizo el blog sea el mismo que la esté borrando o que tenga el rol de admin.
    if blog.user == request.user or request.user.role == "admin":
        blog.delete()
        return Response({"Mensaje": "Publicación Eliminada", "id": pk})
    else:
        return Response({"Error": "No autorizado"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(["POST"])
#!: Reviso si está autentificado.
@permission_classes([IsAuthenticated])
def comment(request, pk):
    try:
        blog = Blog.objects.get(id=pk)
    except Blog.DoesNotExist:
        return Response(
            {"error": "Blog no encontrado"}, status=status.HTTP_404_NOT_FOUND
        )
    user = request.user
    data = request.data
    comment = Comment.objects.create(user=user, blog=blog, text=data["text"])
    serializer = CommentSerializer(instance=comment)
    blog.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)
