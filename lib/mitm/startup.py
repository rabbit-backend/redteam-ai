import asyncio
from mitmproxy import options
from mitmproxy.tools import dump
from lib.mitm.addons.log_requests import LogRequests

async def _start_mitm_proxy():
    opts = options.Options(
        listen_host="127.0.0.1",
        listen_port=8080,
    )

    master = dump.DumpMaster(
        opts,
        with_dumper=False,
        with_termlog=False
    )

    master.addons.add(LogRequests())

    print("[x] starting mitm proxy on: 127.0.0.1:8080")
    await master.run()

def start_mitm_proxy():
    asyncio.run(_start_mitm_proxy())
