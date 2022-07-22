from django.db import models

# Create your models here.

class PoolHash(models.Model):
    id = models.BigAutoField(primary_key=True)
    hash_raw = models.BinaryField(unique=True)
    view = models.CharField(max_length=10485760)

    class Meta:
        managed = False
        db_table = 'pool_hash'