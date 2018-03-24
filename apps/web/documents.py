from django_elasticsearch_dsl import DocType, Index
from apps.products.models import Product


products = Index('products')

@products.doc_type
class ProductDocument(DocType):
    class Meta:
        model = Product

        fields = [
            'name',
            'price',
            'description',
            'image',
        ]
