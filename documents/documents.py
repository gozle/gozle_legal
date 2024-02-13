from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from . import models

@registry.register_document
class DocDocument(Document):
    class Index:
        name = 'documents'
        settings = {
            'number_of_shards':1,
            'number_of_replicas':0
        }
    class Django:
        model = models.Document
        fields = [
            'header'
        ]