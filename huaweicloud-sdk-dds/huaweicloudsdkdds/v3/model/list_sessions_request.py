# coding: utf-8

import pprint
import re

import six





class ListSessionsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'plan_summary': 'str',
        'type': 'str',
        'namespace': 'str',
        'cost_time': 'int'
    }

    attribute_map = {
        'node_id': 'node_id',
        'offset': 'offset',
        'limit': 'limit',
        'plan_summary': 'plan_summary',
        'type': 'type',
        'namespace': 'namespace',
        'cost_time': 'cost_time'
    }

    def __init__(self, node_id=None, offset=None, limit=None, plan_summary=None, type=None, namespace=None, cost_time=None):
        """ListSessionsRequest - a model defined in huaweicloud sdk"""
        
        

        self._node_id = None
        self._offset = None
        self._limit = None
        self._plan_summary = None
        self._type = None
        self._namespace = None
        self._cost_time = None
        self.discriminator = None

        self.node_id = node_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if plan_summary is not None:
            self.plan_summary = plan_summary
        if type is not None:
            self.type = type
        if namespace is not None:
            self.namespace = namespace
        if cost_time is not None:
            self.cost_time = cost_time

    @property
    def node_id(self):
        """Gets the node_id of this ListSessionsRequest.


        :return: The node_id of this ListSessionsRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this ListSessionsRequest.


        :param node_id: The node_id of this ListSessionsRequest.
        :type: str
        """
        self._node_id = node_id

    @property
    def offset(self):
        """Gets the offset of this ListSessionsRequest.


        :return: The offset of this ListSessionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSessionsRequest.


        :param offset: The offset of this ListSessionsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListSessionsRequest.


        :return: The limit of this ListSessionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSessionsRequest.


        :param limit: The limit of this ListSessionsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def plan_summary(self):
        """Gets the plan_summary of this ListSessionsRequest.


        :return: The plan_summary of this ListSessionsRequest.
        :rtype: str
        """
        return self._plan_summary

    @plan_summary.setter
    def plan_summary(self, plan_summary):
        """Sets the plan_summary of this ListSessionsRequest.


        :param plan_summary: The plan_summary of this ListSessionsRequest.
        :type: str
        """
        self._plan_summary = plan_summary

    @property
    def type(self):
        """Gets the type of this ListSessionsRequest.


        :return: The type of this ListSessionsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListSessionsRequest.


        :param type: The type of this ListSessionsRequest.
        :type: str
        """
        self._type = type

    @property
    def namespace(self):
        """Gets the namespace of this ListSessionsRequest.


        :return: The namespace of this ListSessionsRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ListSessionsRequest.


        :param namespace: The namespace of this ListSessionsRequest.
        :type: str
        """
        self._namespace = namespace

    @property
    def cost_time(self):
        """Gets the cost_time of this ListSessionsRequest.


        :return: The cost_time of this ListSessionsRequest.
        :rtype: int
        """
        return self._cost_time

    @cost_time.setter
    def cost_time(self, cost_time):
        """Sets the cost_time of this ListSessionsRequest.


        :param cost_time: The cost_time of this ListSessionsRequest.
        :type: int
        """
        self._cost_time = cost_time

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
        if not isinstance(other, ListSessionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
