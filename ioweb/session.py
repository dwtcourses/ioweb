from pprint import pprint

from .response import Response
from .request import Request
from .pycurl_transport import PycurlTransport
from .error import NetworkError


class Session(object):
    def __init__(self):
        self.req = Request()
        self.transport = PycurlTransport()

    def setup(self, **kwargs):
        self.req.setup(**kwargs)

    def request(self, url=None, **kwargs):
        self.setup(url=url, **kwargs)
        res = Response()
        self.transport.prepare_request(self.req, res)
        try:
            self.transport.request()
        except NetworkError as ex:
            err = ex
        else:
            err = None
        self.transport.prepare_response(self.req, res, err)
        return res
