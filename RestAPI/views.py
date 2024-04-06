from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from django.db.models import Q

class HelloView(APIView):
    permission_classes = IsAuthenticated,

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


# class PostAPIView(APIView):
#     # permission_classes = IsAuthenticated,
#     def get(self, request):
#         posts = Post.objects.all()
#         content = PostSerializer(posts, many=True)
#         return Response(content.data)


class PostBackendView(APIView):
    # permission_classes = IsAuthenticated,
    def get(self, request):
        s = request.GET.get('s')
        sort = request.GET.get('sort')
        sortorder = request.GET.get('sortorder')
        page = int(request.GET.get('page', 1))
        perpage = int(request.GET.get('per_page', 20))

        posts = Post.objects.all()

        if not s:
            posts = Post.objects.all()
        else:
            search_terms = Q()
            for field in ('tlink', 'wlink', 'user', 'source', 'text', 'hashtags', 'location'):
                search_terms |= Q(**{f'{field}__icontains': s})
            posts = Post.objects.filter(search_terms)
        if sort:
            if sortorder == 'desc':
                sort = f'-{sort}'
            elif sortorder == 'asc':
                sort = f'{sort}'
            posts = posts.order_by(sort)

        total = posts.count()
        start = (page - 1) * perpage
        end = page * perpage

        content = PostSerializer(posts[start:end], many=True)
        return Response(
            {
                'data': content.data,
                'page': page,
            }
        )
