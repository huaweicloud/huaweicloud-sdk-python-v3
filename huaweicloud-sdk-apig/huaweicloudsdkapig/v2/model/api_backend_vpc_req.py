# coding: utf-8

import pprint
import re

import six





class ApiBackendVpcReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'vpc_channel_proxy_host': 'str',
        'vpc_channel_id': 'str'
    }

    attribute_map = {
        'vpc_channel_proxy_host': 'vpc_channel_proxy_host',
        'vpc_channel_id': 'vpc_channel_id'
    }

    def __init__(self, vpc_channel_proxy_host=None, vpc_channel_id=None):
        """ApiBackendVpcReq - a model defined in huaweicloud sdk"""
        
        

        self._vpc_channel_proxy_host = None
        self._vpc_channel_id = None
        self.discriminator = None

        if vpc_channel_proxy_host is not None:
            self.vpc_channel_proxy_host = vpc_channel_proxy_host
        self.vpc_channel_id = vpc_channel_id

    @property
    def vpc_channel_proxy_host(self):
        """Gets the vpc_channel_proxy_host of this ApiBackendVpcReq.

        代理主机

        :return: The vpc_channel_proxy_host of this ApiBackendVpcReq.
        :rtype: str
        """
        return self._vpc_channel_proxy_host

    @vpc_channel_proxy_host.setter
    def vpc_channel_proxy_host(self, vpc_channel_proxy_host):
        """Sets the vpc_channel_proxy_host of this ApiBackendVpcReq.

        代理主机

        :param vpc_channel_proxy_host: The vpc_channel_proxy_host of this ApiBackendVpcReq.
        :type: str
        """
        self._vpc_channel_proxy_host = vpc_channel_proxy_host

    @property
    def vpc_channel_id(self):
        """Gets the vpc_channel_id of this ApiBackendVpcReq.

        VPC通道编号

        :return: The vpc_channel_id of this ApiBackendVpcReq.
        :rtype: str
        """
        return self._vpc_channel_id

    @vpc_channel_id.setter
    def vpc_channel_id(self, vpc_channel_id):
        """Sets the vpc_channel_id of this ApiBackendVpcReq.

        VPC通道编号

        :param vpc_channel_id: The vpc_channel_id of this ApiBackendVpcReq.
        :type: str
        """
        self._vpc_channel_id = vpc_channel_id

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
        if not isinstance(other, ApiBackendVpcReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
