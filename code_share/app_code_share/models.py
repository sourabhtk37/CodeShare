from __future__ import unicode_literals
from django.db import models


class CodeShare(models.Model):
    """
    Databse schema for handline the code snippet data

    :field code: text field for code content
    :field hash_value: unique hash ID for distinguishing code snipeets
    :field file_name: character field for file name

    """

    code = models.TextField(max_length=100000,
                            null=True,
                            blank=True,
                            unique=False)

    hash_value = models.SlugField(max_length=100,
                                  null=True,
                                  blank=True,
                                  unique=True)

    file_name = models.CharField(max_length=50,
                                 null=True,
                                 blank=True)

    def __unicode__(self):
        return str(self.hash_value)

    class Meta:
      verbose_name='CodeShare'
