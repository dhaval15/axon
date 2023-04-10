from django.db import models
from .fields import QuotedTextField, QuotedForeignKey, PropertiesField

class Alias(models.Model):
    node = models.ForeignKey('Node', models.DO_NOTHING)
    alias = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'aliases'


class Citation(models.Model):
    node = models.ForeignKey('Node', models.DO_NOTHING)
    cite_key = models.TextField()  # This field type is a guess.
    pos = models.TextField()  # This field type is a guess.
    properties = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'citations'


class File(models.Model):
    file = QuotedTextField(primary_key=True, blank=True)  # This field type is a guess.
    title = models.TextField(blank=True, null=True)  # This field type is a guess.
    hash = models.TextField()  # This field type is a guess.
    atime = models.TextField()  # This field type is a guess.
    mtime = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'files'
    def __str__(self):
        return self.title


class Node(models.Model):
    id = QuotedTextField(primary_key=True)  # This field type is a guess.
    file = QuotedForeignKey(File, models.DO_NOTHING, db_column='file')
    level = models.TextField()  # This field type is a guess.
    pos = models.TextField()  # This field type is a guess.
    todo = models.TextField(blank=True, null=True)  # This field type is a guess.
    priority = models.TextField(blank=True, null=True)  # This field type is a guess.
    scheduled = models.TextField(blank=True, null=True)
    deadline = models.TextField(blank=True, null=True)
    title = QuotedTextField(blank=True, null=True)  # This field type is a guess.
    properties = PropertiesField(blank=True, null=True)  # This field type is a guess.
    olp = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'nodes'

    def __str__(self):
        return self.title

class Link(models.Model):
    pos = models.TextField()  # This field type is a guess.
    source = QuotedForeignKey(Node, models.DO_NOTHING, db_column='source', unique=False, primary_key=True)
    # dest = QuotedTextField()  # This field type is a guess.
    dest = QuotedForeignKey(Node, models.DO_NOTHING, db_column='dest', unique=False, related_name='dest', blank=True, null=True)
    type = QuotedTextField()  # This field type is a guess.
    properties = PropertiesField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'links'
        unique_together = ('source', 'dest', 'pos')

    def __str__(self):
        return f'{self.source.title} => {self.type}:{self.dest}'


class Ref(models.Model):
    node = models.ForeignKey(Node, models.DO_NOTHING)
    ref = models.TextField()  # This field type is a guess.
    type = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'refs'


class Tag(models.Model):
    # node = models.TextField(Node, models.DO_NOTHING, primary_key=True, unique=False)
    node = QuotedTextField(primary_key=True, unique=False, db_column='node_id')
    tag = QuotedTextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tags'
        unique_together = ('node', 'tag')

# Hack for Link 'dest' column throwing exception when no node found.

from django.db.models.fields.related_descriptors import ForwardManyToOneDescriptor

def get_object(self, instance):
    try:
        qs = self.get_queryset(instance=instance)
        return qs.get(self.field.get_reverse_related_filter(instance))
    except:
        return getattr(instance, 'dest_id')

ForwardManyToOneDescriptor.get_object = get_object
