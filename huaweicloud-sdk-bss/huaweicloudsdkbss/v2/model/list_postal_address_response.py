# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListPostalAddressResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'postal_address': 'list[CustomerPostalAddressV2]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'postal_address': 'postal_address'
    }

    def __init__(self, total_count=None, postal_address=None):
        """ListPostalAddressResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._total_count = None
        self._postal_address = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if postal_address is not None:
            self.postal_address = postal_address

    @property
    def total_count(self):
        """Gets the total_count of this ListPostalAddressResponse.

        |参数名称：查询个数，成功的时候返回| |参数的约束及描述：查询个数，成功的时候返回|

        :return: The total_count of this ListPostalAddressResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListPostalAddressResponse.

        |参数名称：查询个数，成功的时候返回| |参数的约束及描述：查询个数，成功的时候返回|

        :param total_count: The total_count of this ListPostalAddressResponse.
        :type: int
        """
        self._total_count = total_count

    @property
    def postal_address(self):
        """Gets the postal_address of this ListPostalAddressResponse.

        |参数名称：邮寄地址| |参数约束以及描述：邮寄地址|

        :return: The postal_address of this ListPostalAddressResponse.
        :rtype: list[CustomerPostalAddressV2]
        """
        return self._postal_address

    @postal_address.setter
    def postal_address(self, postal_address):
        """Sets the postal_address of this ListPostalAddressResponse.

        |参数名称：邮寄地址| |参数约束以及描述：邮寄地址|

        :param postal_address: The postal_address of this ListPostalAddressResponse.
        :type: list[CustomerPostalAddressV2]
        """
        self._postal_address = postal_address

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
        if not isinstance(other, ListPostalAddressResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
