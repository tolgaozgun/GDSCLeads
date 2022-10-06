from django.core.serializers.json import DjangoJSONEncoder

from map.models import User, Community, Event


class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return str(obj)
        elif isinstance(obj, Community):
            return str(obj)
        elif isinstance(obj, Event):
            return str(obj)
        return super().default(obj)

