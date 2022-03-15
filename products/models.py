from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'menus'


class Categories(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'


class Drinks(models.Model):
    kor_name = models.CharField(max_length=45)
    eng_name = models.CharField(max_length=45)
    desc = models.TextField()
    category = models.ForeignKey('categories', on_delete=models.CASCADE)

    class Meta:
        db_table = 'drinks'


class Images(models.Model):
    drink = models.ForeignKey('drinks', on_delete=models.CASCADE)
    img_url = models.CharField(max_length=1000)

    class Meta:
        db_table = 'images'


class Nutritions(models.Model):
    drink = models.ForeignKey('drinks', on_delete=models.CASCADE)
    size = models.ForeignKey('sizes', on_delete=models.CASCADE)
    img_url = models.CharField(max_length=1000)
    caffeine = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    protein = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    sugars = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    saturate = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    sodium = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    kca = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    class Meta:
        db_table = 'nutritions'


class Sizes(models.Model):
    name = models.CharField(max_length=45)
    size_ml = models.CharField(max_length=45, null=True)
    size_flu = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'sizes'


class Allergy_drink(models.Model):
    alergy = models.ForeignKey('allergy', on_delete=models.CASCADE)
    drink = models.ForeignKey('drinks', on_delete=models.CASCADE)

    class Meta:
        db_table = 'allergydrink'


class Allergy(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'alergies'
