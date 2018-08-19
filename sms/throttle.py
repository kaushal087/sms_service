from rest_framework import throttling
from django.core.cache import cache
import datetime

class FromThrottle(throttling.BaseThrottle):

    def allow_request(self, request, view):
        data = request.data
        frm = data.get('from')
        if not frm:
            return True
        one_hour_ago = datetime.datetime.now() - datetime.timedelta(hours=1)
        timestamps = cache.get('request_' + frm, [])
        new_timestamps = [x for x in timestamps if x > one_hour_ago]

        if len(new_timestamps) >= 50:
            return False
        else:
            new_timestamps.append(datetime.datetime.now())

        cache.set('request_' + frm, new_timestamps)

        return True
