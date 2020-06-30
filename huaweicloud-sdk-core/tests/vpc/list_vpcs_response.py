# coding: utf-8


class ListVpcsResponse(object):
    openapi_types = {
        'vpcs': 'list[Vpc]'
    }

    attribute_map = {
        'vpcs': 'vpcs'
    }

    def __init__(self, vpcs=None):
        self.vpcs = None

        if vpcs is not None:
            self.vpcs = vpcs
