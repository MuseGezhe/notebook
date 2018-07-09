from rest_framework import serializers
from axf.models import Product,SliderShow,MainDescription

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("name","long_name","product_id","store_nums","specifics","sort","market_price",
                  "price","category_id","child_cid","img","keywords","brand_id","brand_name","safe_day","safe_unit","safe_unit_desc","isDelete")


class SliderShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderShow
        fields = ("name","img","sort","trackid")


class MainDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainDescription
        fields = ("category_id","category_name","img","product1","product2","product3")