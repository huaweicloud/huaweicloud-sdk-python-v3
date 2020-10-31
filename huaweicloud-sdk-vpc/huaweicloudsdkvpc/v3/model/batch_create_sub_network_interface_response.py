# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class BatchCreateSubNetworkInterfaceResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'sub_network_interfaces': 'list[SubNetworkInterface]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'sub_network_interfaces': 'sub_network_interfaces'
    }

    def __init__(self, request_id=None, sub_network_interfaces=None):
        """BatchCreateSubNetworkInterfaceResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._request_id = None
        self._sub_network_interfaces = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if sub_network_interfaces is not None:
            self.sub_network_interfaces = sub_network_interfaces

    @property
    def request_id(self):
        """Gets the request_id of this BatchCreateSubNetworkInterfaceResponse.

        请求ID

        :return: The request_id of this BatchCreateSubNetworkInterfaceResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this BatchCreateSubNetworkInterfaceResponse.

        请求ID

        :param request_id: The request_id of this BatchCreateSubNetworkInterfaceResponse.
        :type: str
        """
        self._request_id = request_id

    @property
    def sub_network_interfaces(self):
        """Gets the sub_network_interfaces of this BatchCreateSubNetworkInterfaceResponse.

        批量创建辅助弹性网卡的响应体

        :return: The sub_network_interfaces of this BatchCreateSubNetworkInterfaceResponse.
        :rtype: list[SubNetworkInterface]
        """
        return self._sub_network_interfaces

    @sub_network_interfaces.setter
    def sub_network_interfaces(self, sub_network_interfaces):
        """Sets the sub_network_interfaces of this BatchCreateSubNetworkInterfaceResponse.

        批量创建辅助弹性网卡的响应体

        :param sub_network_interfaces: The sub_network_interfaces of this BatchCreateSubNetworkInterfaceResponse.
        :type: list[SubNetworkInterface]
        """
        self._sub_network_interfaces = sub_network_interfaces

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
        if not isinstance(other, BatchCreateSubNetworkInterfaceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
