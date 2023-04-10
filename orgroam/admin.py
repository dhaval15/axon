from django.contrib import admin

from .models import Alias, Citation, File, Link, Node, Ref, Tag

# Register your models here.
admin.site.register(Alias)
admin.site.register(Citation)
admin.site.register(File)
admin.site.register(Link)
admin.site.register(Node)
admin.site.register(Ref)
admin.site.register(Tag)
