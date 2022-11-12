import os

import aiohttp_cors
from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response

from counter import SimpleFileCounter

app = web.Application()

PORT = os.environ.get("COUNTER_PORT", default=9000)

routes = web.RouteTableDef()


counter = SimpleFileCounter()


@routes.get(path="/")
async def hello(_: Request) -> Response:
    current = counter.current_value
    await counter.increment()
    return web.json_response(data={"current_value": current})

app.add_routes(routes)


async def setup_cors(app: web.Application):
    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
            allow_methods="*"
        )
    })

    for route in list(app.router.routes()):
        cors.add(route)

app.on_startup.append(setup_cors)
web.run_app(app, host="0.0.0.0", port=PORT)
