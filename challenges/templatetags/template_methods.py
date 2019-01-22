from django import template
from challenges.models import Challenge

register = template.Library()

@register.simple_tag
def user_is_in_challenge(challengeid, userid):
    if Challenge.objects.get(pk=challengeid).developers.filter(pk__in = userid):
        return True
    else:return False