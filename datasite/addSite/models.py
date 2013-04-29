from django.db import models

# Create your models here.
class webSite(models.Model):
	userId = models.ForeignKey(User)
	accountId = models.CharField(max_length=30)
	webPropertyId = models.CharField(max_length=4)

class dataSource(models.Model):
	webSiteId = models.ForeignKey(webSite)
	name = models.Model(max_length=90)
	description = models.Model(max_length=300)
	customDataSourceId = models.Model(max_length=35)