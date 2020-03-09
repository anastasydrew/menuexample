from django.db import models

# Create your models here.


class TreeMenuCategory(models.Model):

    LABELS = {
        'name': 'Name',
        'verbose_name': 'Verbose name'
    }

    class Meta:
        verbose_name = 'Menu category'
        verbose_name_plural = 'Menu categories'

    name = models.CharField(LABELS['name'], max_length=255, blank=True, null=False)
    verbose_name = models.CharField(LABELS['verbose_name'], max_length=255, blank=True, null=False)

    def __str__(self):
        return self.verbose_name


class TreeMenu(models.Model):

    LABELS = {
        'name': 'Name',
        'category': 'Category',
        'path': 'Link',
        'parent': 'Parent element'
    }

    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'

    name = models.CharField(LABELS['name'], max_length=255, blank=True, null=False)

    category = models.ForeignKey(
        TreeMenuCategory,
        verbose_name=LABELS['category'],
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    path = models.CharField(LABELS['path'], max_length=1000, blank=True, null=False)

    parent = models.ForeignKey(
        'self',
        verbose_name=LABELS['parent'],
        on_delete=models.SET_DEFAULT,
        null=True,
        blank=True,
        default=0
    )

    def __str__(self):
        return self.name
