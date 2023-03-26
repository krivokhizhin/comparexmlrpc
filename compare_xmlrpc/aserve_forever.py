import asyncio

# from server import AsyncPoolXMLRPCServer
from ..aioserver.xmlrpc.server import AsyncXMLRPCServer
from examples.load import load


def parse_args():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='localhost', type=str,
                        help='Specify server address [default: localhost]')
    parser.add_argument('--port', default=6677, type=int,
                        help='Specify alternate port [default: 6677]')
    parser.add_argument('--max_workers', type=int, default=0,
                       help='Number of worker processes in pool to process the request [default: 0]')
    return parser.parse_args()


async def main():
    args = parse_args()

    # server = AsyncPoolXMLRPCServer((args.host, args.port), args.max_workers)
    server = AsyncXMLRPCServer((args.host, args.port))
    server.register_introspection_functions()
    server.register_function(load)

    await server.serve_forever()


asyncio.run(main())