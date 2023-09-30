from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from shop.models import Product


@registry.register_document
class ShopDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'products'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    # Fields of the Elasticsearch document
    name_product = fields.TextField(attr='name')
    price_product = fields.FloatField(attr='price')

    class Django:
        model = Product # The model associated with this Document
        # The fields of the model you want to be indexed in Elasticsearch
        fields = ['name', 'price',]
