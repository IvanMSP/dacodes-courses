# Third Party Libraries
from rest_framework.response import Response


class EnvelopeResponse(Response):
    def __init__(self, data=None, *args, **kwargs):
        if 'status' in kwargs:
            status_code = kwargs['status']
        else:
            status_code = self.status_code
        result = {
            'status': status_code,
            'data': data,
        }
        super(EnvelopeResponse, self).__init__(data=result, *args, **kwargs)


class EnvelopeErrorResponse(Response):
    def __init__(self, data=None, *args, **kwargs):
        if 'status' in kwargs:
            status_code = kwargs['status']
        else:
            status_code = self.status_code
        result = {
         "error": {
           "status": status_code,
           "description": data
         }
        }
        super(EnvelopeErrorResponse, self).__init__(data=result, *args, **kwargs)
