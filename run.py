#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import argparse

from api import app


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('port', type=int, nargs='?', default=50031)
    parser.add_argument('-d', dest='debug', const=True, nargs='?')
    return parser.parse_args()


def apply_args(app, args):
    if not args.debug is None:
        app.debug = args.debug


# standalone mode
if __name__ == '__main__':
    args = parse_args()
    apply_args(app, args)
    app.run(host='0.0.0.0', port=args.port)

