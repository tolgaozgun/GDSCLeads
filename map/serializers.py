from django.core.serializers.json import DjangoJSONEncoder

from map.models import Lead, Community


class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Lead):
            return str(obj)
        elif isinstance(obj, Community):
            return str(obj)
        return super().default(obj)

