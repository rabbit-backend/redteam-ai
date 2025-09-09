from mitmproxy.http import HTTPFlow

class LogRequests:
    def resquest(self, flow: HTTPFlow):
        with open("requests.log", "w+") as f:
            if flow.request.text:
                f.write(
                    flow.request.text
                )

    def response(self, flow: HTTPFlow):
        with open("response.log", "a+") as f:
            if flow.response and flow.response.text:
                f.write(
                    flow.response.text
                )

addons = [LogRequests()]
