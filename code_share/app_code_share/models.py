from __future__ import unicode_literals

from django.db import models



class CodeShare(models.Model):
    
	code = models.TextField(max_length=100000, 
                            null=True, 
                            blank=True,
                            )
	hash_value = models.SlugField(max_length=100,
                              null=True,
                              blank=True,
                              unique=True)
	file_name = models.CharField(max_length=50,
                                null=True,
                                blank=True)	

	def __unicode__(self):
		return str(self.file_name)

	 	
