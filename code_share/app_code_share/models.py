from __future__ import unicode_literals
from django.db import models


class CodeShare(models.Model):
    """
    Databse schema for handline the code snippet data


    :field code: text field for code content
    :field hash_value: unique hash ID for distinguishing code snipeets
    :field file_name: character field for file name
    :field language: type of programming language


    """

    code = models.TextField(max_length=100000,
                            null=True,
                            blank=True,
                            unique=False
                            )
    hash_value = models.SlugField(max_length=100,
                                  null=True,
                                  blank=True,
                                  unique=True)

    file_name = models.CharField(max_length=50,
                                 null=True,
                                 blank=True)

    language = models.CharField(max_length=20,
                                null=True,
                                blank=True,
                                default=None)

    def __unicode__(self):
        return str(self.hash_value)

    def __str__(self):
        return str(self.file_name)

    class Meta:
        verbose_name = 'CodeShare'
