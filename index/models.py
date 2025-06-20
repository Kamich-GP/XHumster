from django.db import models


# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Категории'

    category_name = models.CharField(max_length=16)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.category_name)


class Product(models.Model):
    class Meta:
        verbose_name_plural = 'Продукты'

    product_name = models.CharField(max_length=128)
    product_des = models.TextField()
    product_count = models.IntegerField()
    product_price = models.FloatField()
    product_photo = models.ImageField(upload_to='media')
    product_category = models.ForeignKey(Category,
                                         on_delete=models.CASCADE)


    def __str__(self):
        return str(self.product_name)


class Cart(models.Model):
    class Meta:
        verbose_name_plural = 'Корзины'

    user_id = models.IntegerField()
    user_product = models.ForeignKey(Product,
                                     on_delete=models.CASCADE)
    user_pr_amount = models.IntegerField()


    def __str__(self):
        return str(self.user_id)
