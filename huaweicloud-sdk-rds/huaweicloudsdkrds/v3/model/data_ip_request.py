# coding: utf-8

import pprint
import re

import six





class DataIpRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'new_ip': 'str'
    }

    attribute_map = {
        'new_ip': 'new_ip'
    }

    def __init__(self, new_ip=None):
        """DataIpRequest - a model defined in huaweicloud sdk"""
        
        

        self._new_ip = None
        self.discriminator = None

        self.new_ip = new_ip

    @property
    def new_ip(self):
        """Gets the new_ip of this DataIpRequest.

        内网ip

        :return: The new_ip of this DataIpRequest.
        :rtype: str
        """
        return self._new_ip

    @new_ip.setter
    def new_ip(self, new_ip):
        """Sets the new_ip of this DataIpRequest.

        内网ip

        :param new_ip: The new_ip of this DataIpRequest.
        :type: str
        """
        self._new_ip = new_ip

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
        if not isinstance(other, DataIpRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
