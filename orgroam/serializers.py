from rest_framework import serializers
from .models import Node, Tag, Link
from .utils import trim_quotes, extract_inline
import logging

class NodeSerializer(serializers.ModelSerializer):
    properties = serializers.DictField()

    def get_properties(self, obj):
        if isinstance(obj.properties, dict):
            return obj.properties.items
        return []

    class Meta:
        model = Node
        fields = [
            'id',
            'title',
            'file',
            'level',
            'pos',
            'todo',
            'priority',
            'scheduled',
            'deadline',
            'title',
            'properties',
            'olp',
        ]

class LinkSerializer(serializers.ModelSerializer):
    sourceTitle = serializers.SerializerMethodField()
    destTitle = serializers.SerializerMethodField()
    dest = serializers.SerializerMethodField()
    inline = serializers.SerializerMethodField()
    # properties = serializers.DictField()

    # def get_properties(self, obj):
    #     if isinstance(obj.properties, dict):
    #         return obj.properties.items
    #     return []

    def get_dest(self, obj):
        if isinstance(obj.dest, Node):
            return obj.dest.id
        return obj.dest

    def get_destTitle(self, obj):
        if isinstance(obj.dest, Node):
            return obj.dest.title

    def get_sourceTitle(self, obj):
        return obj.source.title

    def get_inline(self, obj):
        file = obj.source.file.file
        try:
            return extract_inline(file, obj.pos)
        except:
            logging.warning('Node: error occoured while fetching inline link')
            logging.warning(f'for {obj.source.title} at position {obj.pos}')

    class Meta:
        model = Link
        fields = [
            'pos',
            'source',
            'dest',
            'type',
            #'properties',
            'sourceTitle',
            'destTitle',
            'inline',
        ]

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['node', 'tag']
