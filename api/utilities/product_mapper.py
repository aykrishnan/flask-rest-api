from api.models import Product
from api.utilities import ObjectMapper


class ProductMapper(ObjectMapper):

    outgoing_fields = ('id', 'name', 'price')
    model_class = Product
