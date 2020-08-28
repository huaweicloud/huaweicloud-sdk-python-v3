# coding: utf-8

import pprint
import re

import six





class ListSecurityGroupRulesRequest:


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
        'security_group_id': 'list[str]',
        'protocol': 'list[str]',
        'description': 'list[str]',
        'remote_group_id': 'list[str]',
        'direction': 'str',
        'action': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'id': 'id',
        'security_group_id': 'security_group_id',
        'protocol': 'protocol',
        'description': 'description',
        'remote_group_id': 'remote_group_id',
        'direction': 'direction',
        'action': 'action'
    }

    def __init__(self, limit=None, marker=None, id=None, security_group_id=None, protocol=None, description=None, remote_group_id=None, direction=None, action=None):
        """ListSecurityGroupRulesRequest - a model defined in huaweicloud sdk"""
        
        

        self._limit = None
        self._marker = None
        self._id = None
        self._security_group_id = None
        self._protocol = None
        self._description = None
        self._remote_group_id = None
        self._direction = None
        self._action = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if id is not None:
            self.id = id
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if protocol is not None:
            self.protocol = protocol
        if description is not None:
            self.description = description
        if remote_group_id is not None:
            self.remote_group_id = remote_group_id
        if direction is not None:
            self.direction = direction
        if action is not None:
            self.action = action

    @property
    def limit(self):
        """Gets the limit of this ListSecurityGroupRulesRequest.


        :return: The limit of this ListSecurityGroupRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSecurityGroupRulesRequest.


        :param limit: The limit of this ListSecurityGroupRulesRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListSecurityGroupRulesRequest.


        :return: The marker of this ListSecurityGroupRulesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListSecurityGroupRulesRequest.


        :param marker: The marker of this ListSecurityGroupRulesRequest.
        :type: str
        """
        self._marker = marker

    @property
    def id(self):
        """Gets the id of this ListSecurityGroupRulesRequest.


        :return: The id of this ListSecurityGroupRulesRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListSecurityGroupRulesRequest.


        :param id: The id of this ListSecurityGroupRulesRequest.
        :type: list[str]
        """
        self._id = id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this ListSecurityGroupRulesRequest.


        :return: The security_group_id of this ListSecurityGroupRulesRequest.
        :rtype: list[str]
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this ListSecurityGroupRulesRequest.


        :param security_group_id: The security_group_id of this ListSecurityGroupRulesRequest.
        :type: list[str]
        """
        self._security_group_id = security_group_id

    @property
    def protocol(self):
        """Gets the protocol of this ListSecurityGroupRulesRequest.


        :return: The protocol of this ListSecurityGroupRulesRequest.
        :rtype: list[str]
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ListSecurityGroupRulesRequest.


        :param protocol: The protocol of this ListSecurityGroupRulesRequest.
        :type: list[str]
        """
        self._protocol = protocol

    @property
    def description(self):
        """Gets the description of this ListSecurityGroupRulesRequest.


        :return: The description of this ListSecurityGroupRulesRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListSecurityGroupRulesRequest.


        :param description: The description of this ListSecurityGroupRulesRequest.
        :type: list[str]
        """
        self._description = description

    @property
    def remote_group_id(self):
        """Gets the remote_group_id of this ListSecurityGroupRulesRequest.


        :return: The remote_group_id of this ListSecurityGroupRulesRequest.
        :rtype: list[str]
        """
        return self._remote_group_id

    @remote_group_id.setter
    def remote_group_id(self, remote_group_id):
        """Sets the remote_group_id of this ListSecurityGroupRulesRequest.


        :param remote_group_id: The remote_group_id of this ListSecurityGroupRulesRequest.
        :type: list[str]
        """
        self._remote_group_id = remote_group_id

    @property
    def direction(self):
        """Gets the direction of this ListSecurityGroupRulesRequest.


        :return: The direction of this ListSecurityGroupRulesRequest.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this ListSecurityGroupRulesRequest.


        :param direction: The direction of this ListSecurityGroupRulesRequest.
        :type: str
        """
        self._direction = direction

    @property
    def action(self):
        """Gets the action of this ListSecurityGroupRulesRequest.


        :return: The action of this ListSecurityGroupRulesRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ListSecurityGroupRulesRequest.


        :param action: The action of this ListSecurityGroupRulesRequest.
        :type: str
        """
        self._action = action

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
        if not isinstance(other, ListSecurityGroupRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
