# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CreatePostalResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'address_id': 'str'
    }

    attribute_map = {
        'address_id': 'address_id'
    }

    def __init__(self, address_id=None):
        """CreatePostalResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._address_id = None
        self.discriminator = None

        if address_id is not None:
            self.address_id = address_id

    @property
    def address_id(self):
        """Gets the address_id of this CreatePostalResponse.

        |参数名称：邮寄地址ID| |参数约束及描述：邮寄地址ID|

        :return: The address_id of this CreatePostalResponse.
        :rtype: str
        """
        return self._address_id

    @address_id.setter
    def address_id(self, address_id):
        """Sets the address_id of this CreatePostalResponse.

        |参数名称：邮寄地址ID| |参数约束及描述：邮寄地址ID|

        :param address_id: The address_id of this CreatePostalResponse.
        :type: str
        """
        self._address_id = address_id

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
        if not isinstance(other, CreatePostalResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
