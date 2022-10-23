from django.db import models


class ObjectsP(models.Model):
    """ Construction objects model """

    fid = models.AutoField(db_column='FID', primary_key=True)
    geom = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True,
                            help_text="str: name of object")
    org = models.CharField(max_length=254, blank=True, null=True,
                           help_text="str: organization performer")
    year = models.IntegerField(blank=True, null=True,
                               help_text="int: year of work")
    region = models.IntegerField(blank=True, null=True,
                                 help_text="int: region number")
    sign = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'objects_p'
