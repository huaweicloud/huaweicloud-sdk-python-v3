# coding: utf-8


class Route(object):
    openapi_types = {
        'destination': 'str',
        'nexthop': 'str'
    }

    attribute_map = {
        'destination': 'destination',
        'nexthop': 'nexthop'
    }

    def __init__(self, destination=None, nexthop=None):  # noqa: E501
        self.discriminator = None
        self.nexthop = None

        if destination is not None:
            self.destination = destination
        if nexthop is not None:
            self.nexthop = nexthop
