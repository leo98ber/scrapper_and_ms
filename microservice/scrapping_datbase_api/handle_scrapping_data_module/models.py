from django.db import models


class ScrappingData(models.Model):
    """Model to save scrapping data."""

    name = models.CharField(max_length=150, unique=True, blank=False, null=False)

    class Meta:
        db_table = "testtable"

    def __str__(self):
        return self.name
