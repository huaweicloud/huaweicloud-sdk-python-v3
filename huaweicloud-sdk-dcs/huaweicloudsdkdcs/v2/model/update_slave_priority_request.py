# coding: utf-8

import pprint
import re

import six





class UpdateSlavePriorityRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'group_id': 'str',
        'node_id': 'str',
        'body': 'PriorityBody'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'group_id': 'group_id',
        'node_id': 'node_id',
        'body': 'body'
    }

    def __init__(self, instance_id=None, group_id=None, node_id=None, body=None):
        """UpdateSlavePriorityRequest - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._group_id = None
        self._node_id = None
        self._body = None
        self.discriminator = None

        self.instance_id = instance_id
        self.group_id = group_id
        self.node_id = node_id
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        """Gets the instance_id of this UpdateSlavePriorityRequest.


        :return: The instance_id of this UpdateSlavePriorityRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this UpdateSlavePriorityRequest.


        :param instance_id: The instance_id of this UpdateSlavePriorityRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def group_id(self):
        """Gets the group_id of this UpdateSlavePriorityRequest.


        :return: The group_id of this UpdateSlavePriorityRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this UpdateSlavePriorityRequest.


        :param group_id: The group_id of this UpdateSlavePriorityRequest.
        :type: str
        """
        self._group_id = group_id

    @property
    def node_id(self):
        """Gets the node_id of this UpdateSlavePriorityRequest.


        :return: The node_id of this UpdateSlavePriorityRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this UpdateSlavePriorityRequest.


        :param node_id: The node_id of this UpdateSlavePriorityRequest.
        :type: str
        """
        self._node_id = node_id

    @property
    def body(self):
        """Gets the body of this UpdateSlavePriorityRequest.


        :return: The body of this UpdateSlavePriorityRequest.
        :rtype: PriorityBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateSlavePriorityRequest.


        :param body: The body of this UpdateSlavePriorityRequest.
        :type: PriorityBody
        """
        self._body = body

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
        if not isinstance(other, UpdateSlavePriorityRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
