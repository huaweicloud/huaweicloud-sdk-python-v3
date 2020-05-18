# coding: utf-8

import pprint
import re

import six


class NeutronListNetworksRequest(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'id': 'str',
        'name': 'str',
        'status': 'str',
        'shared': 'bool',
        'routerexternal': 'bool',
        'admin_state_up': 'bool',
        'providernetwork_type': 'str',
        'tenant_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'shared': 'shared',
        'routerexternal': 'router:external',
        'admin_state_up': 'admin_state_up',
        'providernetwork_type': 'provider:network_type',
        'tenant_id': 'tenant_id'
    }

    def __init__(self, limit=2000, marker=None, id=None, name=None, status=None, shared=None, routerexternal=None, admin_state_up=None, providernetwork_type='N/A', tenant_id=None):  # noqa: E501
        """NeutronListNetworksRequest - a model defined in huaweicloud sdk"""

        self._limit = None
        self._marker = None
        self._id = None
        self._name = None
        self._status = None
        self._shared = None
        self._routerexternal = None
        self._admin_state_up = None
        self._providernetwork_type = None
        self._tenant_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if shared is not None:
            self.shared = shared
        if routerexternal is not None:
            self.routerexternal = routerexternal
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if providernetwork_type is not None:
            self.providernetwork_type = providernetwork_type
        if tenant_id is not None:
            self.tenant_id = tenant_id

    @property
    def limit(self):
        """Gets the limit of this NeutronListNetworksRequest.


        :return: The limit of this NeutronListNetworksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this NeutronListNetworksRequest.


        :param limit: The limit of this NeutronListNetworksRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this NeutronListNetworksRequest.


        :return: The marker of this NeutronListNetworksRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this NeutronListNetworksRequest.


        :param marker: The marker of this NeutronListNetworksRequest.
        :type: str
        """
        self._marker = marker

    @property
    def id(self):
        """Gets the id of this NeutronListNetworksRequest.


        :return: The id of this NeutronListNetworksRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NeutronListNetworksRequest.


        :param id: The id of this NeutronListNetworksRequest.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this NeutronListNetworksRequest.


        :return: The name of this NeutronListNetworksRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NeutronListNetworksRequest.


        :param name: The name of this NeutronListNetworksRequest.
        :type: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this NeutronListNetworksRequest.


        :return: The status of this NeutronListNetworksRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NeutronListNetworksRequest.


        :param status: The status of this NeutronListNetworksRequest.
        :type: str
        """
        self._status = status

    @property
    def shared(self):
        """Gets the shared of this NeutronListNetworksRequest.


        :return: The shared of this NeutronListNetworksRequest.
        :rtype: bool
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """Sets the shared of this NeutronListNetworksRequest.


        :param shared: The shared of this NeutronListNetworksRequest.
        :type: bool
        """
        self._shared = shared

    @property
    def routerexternal(self):
        """Gets the routerexternal of this NeutronListNetworksRequest.


        :return: The routerexternal of this NeutronListNetworksRequest.
        :rtype: bool
        """
        return self._routerexternal

    @routerexternal.setter
    def routerexternal(self, routerexternal):
        """Sets the routerexternal of this NeutronListNetworksRequest.


        :param routerexternal: The routerexternal of this NeutronListNetworksRequest.
        :type: bool
        """
        self._routerexternal = routerexternal

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this NeutronListNetworksRequest.


        :return: The admin_state_up of this NeutronListNetworksRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this NeutronListNetworksRequest.


        :param admin_state_up: The admin_state_up of this NeutronListNetworksRequest.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def providernetwork_type(self):
        """Gets the providernetwork_type of this NeutronListNetworksRequest.


        :return: The providernetwork_type of this NeutronListNetworksRequest.
        :rtype: str
        """
        return self._providernetwork_type

    @providernetwork_type.setter
    def providernetwork_type(self, providernetwork_type):
        """Sets the providernetwork_type of this NeutronListNetworksRequest.


        :param providernetwork_type: The providernetwork_type of this NeutronListNetworksRequest.
        :type: str
        """
        self._providernetwork_type = providernetwork_type

    @property
    def tenant_id(self):
        """Gets the tenant_id of this NeutronListNetworksRequest.


        :return: The tenant_id of this NeutronListNetworksRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this NeutronListNetworksRequest.


        :param tenant_id: The tenant_id of this NeutronListNetworksRequest.
        :type: str
        """
        self._tenant_id = tenant_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NeutronListNetworksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
