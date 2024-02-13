from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Category, Document

@receiver([post_save, post_delete], sender=Category)
def invalidate_category_cache(sender, instance, **kwargs):
    cache.delete('cached_categories')

@receiver([post_save, post_delete], sender=Category)
def invalidate_single_category_cache(sender, instance, **kwargs):
    cache.delete('cached_category')

@receiver([post_save, post_delete], sender=Document)
def invalidate_document_cache(sender, instance, **kwargs):
    cache.delete(f'cached_document{instance.id}')

@receiver([post_save, post_delete], sender=Document)
def invalidate_documents_cache(sender, instance, **kwargs):
    cache.delete('cached_documents')
