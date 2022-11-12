import os

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


web.run_app(app, host="0.0.0.0", port=PORT)
