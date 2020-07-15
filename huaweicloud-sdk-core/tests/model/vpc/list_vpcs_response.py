# coding= utf-8
"""
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache LICENSE, Version 2.0 (the
 "LICENSE"); you may not use this file except in compliance
 with the LICENSE.  You may obtain a copy of the LICENSE at

     http=//www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the LICENSE is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the LICENSE for the
 specific language governing permissions and limitations
 under the LICENSE.
"""


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


class Route(object):
    openapi_types = {
        'destination': 'str',
        'nexthop': 'str'
    }

    attribute_map = {
        'destination': 'destination',
        'nexthop': 'nexthop'
    }

    def __init__(self, destination=None, nexthop=None):
        self.discriminator = None
        self.nexthop = None

        if destination is not None:
            self.destination = destination
        if nexthop is not None:
            self.nexthop = nexthop
