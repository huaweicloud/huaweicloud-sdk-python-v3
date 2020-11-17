# coding: utf-8

import pprint
import re

import six





class NeutronListFirewallPoliciesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'id': 'list[str]',
        'name': 'list[str]',
        'description': 'list[str]',
        'tenant_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'tenant_id': 'tenant_id'
    }

    def __init__(self, limit=2000, marker=None, id=None, name=None, description=None, tenant_id=None):
        """NeutronListFirewallPoliciesRequest - a model defined in huaweicloud sdk"""
        
        

        self._limit = None
        self._marker = None
        self._id = None
        self._name = None
        self._description = None
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
        if description is not None:
            self.description = description
        if tenant_id is not None:
            self.tenant_id = tenant_id

    @property
    def limit(self):
        """Gets the limit of this NeutronListFirewallPoliciesRequest.


        :return: The limit of this NeutronListFirewallPoliciesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this NeutronListFirewallPoliciesRequest.


        :param limit: The limit of this NeutronListFirewallPoliciesRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this NeutronListFirewallPoliciesRequest.


        :return: The marker of this NeutronListFirewallPoliciesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this NeutronListFirewallPoliciesRequest.


        :param marker: The marker of this NeutronListFirewallPoliciesRequest.
        :type: str
        """
        self._marker = marker

    @property
    def id(self):
        """Gets the id of this NeutronListFirewallPoliciesRequest.


        :return: The id of this NeutronListFirewallPoliciesRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NeutronListFirewallPoliciesRequest.


        :param id: The id of this NeutronListFirewallPoliciesRequest.
        :type: list[str]
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this NeutronListFirewallPoliciesRequest.


        :return: The name of this NeutronListFirewallPoliciesRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NeutronListFirewallPoliciesRequest.


        :param name: The name of this NeutronListFirewallPoliciesRequest.
        :type: list[str]
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this NeutronListFirewallPoliciesRequest.


        :return: The description of this NeutronListFirewallPoliciesRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NeutronListFirewallPoliciesRequest.


        :param description: The description of this NeutronListFirewallPoliciesRequest.
        :type: list[str]
        """
        self._description = description

    @property
    def tenant_id(self):
        """Gets the tenant_id of this NeutronListFirewallPoliciesRequest.


        :return: The tenant_id of this NeutronListFirewallPoliciesRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this NeutronListFirewallPoliciesRequest.


        :param tenant_id: The tenant_id of this NeutronListFirewallPoliciesRequest.
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
                if attr in self.sensitive_list:
                    result[attr] = "****"
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
        if not isinstance(other, NeutronListFirewallPoliciesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
