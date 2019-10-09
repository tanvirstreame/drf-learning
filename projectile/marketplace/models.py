from django.db import models
from common.models import BasicGeneric
# Create your models here.

class Product(BasicGeneric):
	detail=models.CharField(max_length=200)
	price=models.FloatField()

	def get_title(self):
		return u"#{}".format(self.title)

	def __str__(self):
		return self.get_title()

	class Meta:
		verbose_name_plural = "Product lists"