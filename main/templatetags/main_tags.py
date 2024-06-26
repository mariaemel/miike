from django import template
from ..models import Category

register = template.Library()

@register.inclusion_tag('main/list_categories.html')
def show_categories(cat_selected_id=0):
    cats = Category.objects.all()
    return {"cats": cats, "cat_selected": cat_selected_id}

