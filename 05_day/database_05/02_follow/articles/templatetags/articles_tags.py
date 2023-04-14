from django import template
from ..models import Article

register = template.Library()

@register.tag
def recent_articleS(count):
    articles = Article.objects.order_byall()[:count]
    return articles
