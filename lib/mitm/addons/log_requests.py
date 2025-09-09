from mitmproxy.http import HTTPFlow
from lib.jsondb.db import JsonDB


class LogRequests:
    def __init__(self):
        self._db = JsonDB("__requests.json")

    def get_request(self, flow: HTTPFlow):
        return {
            "url": flow.request.url,
            "body": flow.request.text,
            "method": flow.request.method,
            "headers": {}
        }

    def get_response(self, flow: HTTPFlow):
        if flow.response:
            return {
                "body": flow.response.text,
                "headers": {}
            }

        return None


    def response(self, flow: HTTPFlow):
        self._db.add_key(
            flow.request.url,
            {
                "__original": {
                    "request": self.get_request(flow),
                    "response": self.get_response(flow)
                },
                "request": self.get_request(flow),
                "response": self.get_response(flow),
                "is_overridden": False
            }
        )

addons = [LogRequests()]
