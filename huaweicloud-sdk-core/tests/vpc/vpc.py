# coding: utf-8


class Vpc(object):
    openapi_types = {
        'id': 'str',
        'name': 'str',
        'cidr': 'str',
        'description': 'str',
        'routes': 'list[Route]',
        'status': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'cidr': 'cidr',
        'description': 'description',
        'routes': 'routes',
        'status': 'status',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, id=None, name=None, cidr=None, description=None, routes=None, status=None,
                 enterprise_project_id=None):
        self.id = id
        self.name = name
        self.cidr = cidr
        self.description = description
        self.routes = routes
        self.status = status
        self.enterprise_project_id = enterprise_project_id
