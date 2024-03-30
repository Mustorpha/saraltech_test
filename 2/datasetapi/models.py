from django.db import models

# Create your models here.

class Stock(models.Model):
    """
    The Business stock database model
    """

    CATEGORY = (
        ("electronics", "Electronics"),
        ("apparel", "Apparel"),
        ("home & kitchen", "Home & Kitchen"),
    )

    name = models.CharField(max_length=50, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    quantity = models.IntegerField(default=0)
    category = models.CharField(max_length=20, choices=CATEGORY, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} in {self.category}"
    