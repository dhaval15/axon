from django.http import JsonResponse, HttpResponse
from django.db.models import Q
from .models import Node, Link, Tag
from .serializers import NodeSerializer, LinkSerializer, TagSerializer
from rest_framework.decorators import api_view
from .utils import trim_quotes, extract_content

@api_view(['GET'])
def orgroam(request):
    # Fetch all links
    values = Link.objects.all()
    serializer = LinkSerializer(values, many=True)
    links = serializer.data

    # Fetch all nodes
    values = Node.objects.all()
    serializer = NodeSerializer(values, many=True)
    nodes = serializer.data

    # Add ghost nodes
    linkIds = set(map(lambda link: link['dest'], links))
    nodeIds = set(map(lambda node: node['id'], nodes))
    ghostIds = list(linkIds - nodeIds)

    # Fetch all links
    values = Tag.objects.order_by('tag').values('tag').distinct()
    tags = list(map(lambda tag: tag['tag'], values))

    # Compose a orgroam dict
    orgroam = { 
        'nodes': nodes,
        'links': links,
        'tags': tags,
        'ghost': ghostIds,
    }
    return JsonResponse(orgroam, safe = False)

@api_view(['GET'])
def nodes(request):
    nodes = Node.objects.all()
    serializer = NodeSerializer(nodes, many=True)
    return JsonResponse(serializer.data, safe = False)

@api_view(['GET'])
def node(request, id):
    node = Node.objects.get(pk=id)
    serializer = NodeSerializer(node)
    return JsonResponse(serializer.data, safe = False)

@api_view(['GET'])
def read(request, id):
    node = Node.objects.get(pk=id)
    content = extract_content(node.file.file)
    return HttpResponse(content)

@api_view(['GET'])
def links(request):
    id = request.GET.get('id', '')
    source = request.GET.get('source', '')
    dest = request.GET.get('dest', '')
    if id != '':
        links = Link.objects.filter(Q(source=f'"{id}"') | Q(dest=f'"{id}"'))
    elif source !='':
        links = Link.objects.filter(source=f'"{source}"')
    elif dest !='':
        links = Link.objects.filter(dest=f'"{dest}"')
    else:
        links = Link.objects.all()
    serializer = LinkSerializer(links, many=True)
    return JsonResponse(serializer.data, safe = False)

@api_view(['GET'])
def tags(request):
    node = request.GET.get('node', '')
    if node == '':
        values = Tag.objects.order_by('tag').values('tag').distinct()
    else:
        values = Tag.objects \
            .filter(node=node) \
            .order_by('tag') \
            .values('tag') \
            .distinct()
    tags = list(map(lambda tag: tag['tag'], values))
    return JsonResponse(tags, safe = False)
