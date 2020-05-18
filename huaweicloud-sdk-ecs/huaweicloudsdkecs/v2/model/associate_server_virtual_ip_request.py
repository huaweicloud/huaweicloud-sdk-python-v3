# coding: utf-8

import pprint
import re

import six


class AssociateServerVirtualIpRequest(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'nic_id': 'str',
        'body': 'AssociateServerVirtualIpRequestBody'
    }

    attribute_map = {
        'nic_id': 'nic_id',
        'body': 'body'
    }

    def __init__(self, nic_id=None, body=None):  # noqa: E501
        """AssociateServerVirtualIpRequest - a model defined in huaweicloud sdk"""

        self._nic_id = None
        self._body = None
        self.discriminator = None

        self.nic_id = nic_id
        if body is not None:
            self.body = body

    @property
    def nic_id(self):
        """Gets the nic_id of this AssociateServerVirtualIpRequest.


        :return: The nic_id of this AssociateServerVirtualIpRequest.
        :rtype: str
        """
        return self._nic_id

    @nic_id.setter
    def nic_id(self, nic_id):
        """Sets the nic_id of this AssociateServerVirtualIpRequest.


        :param nic_id: The nic_id of this AssociateServerVirtualIpRequest.
        :type: str
        """
        self._nic_id = nic_id

    @property
    def body(self):
        """Gets the body of this AssociateServerVirtualIpRequest.


        :return: The body of this AssociateServerVirtualIpRequest.
        :rtype: AssociateServerVirtualIpRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this AssociateServerVirtualIpRequest.


        :param body: The body of this AssociateServerVirtualIpRequest.
        :type: AssociateServerVirtualIpRequestBody
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
        if not isinstance(other, AssociateServerVirtualIpRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
