# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListSubCustomersResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'customer_infos': 'list[CustomerInformation]',
        'count': 'int'
    }

    attribute_map = {
        'customer_infos': 'customer_infos',
        'count': 'count'
    }

    def __init__(self, customer_infos=None, count=None):
        """ListSubCustomersResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._customer_infos = None
        self._count = None
        self.discriminator = None

        if customer_infos is not None:
            self.customer_infos = customer_infos
        if count is not None:
            self.count = count

    @property
    def customer_infos(self):
        """Gets the customer_infos of this ListSubCustomersResponse.

        |参数名称：客户信息列表。具体请参见表 CustomerInfo| |参数约束以及描述：客户信息列表。具体请参见表 CustomerInfo|

        :return: The customer_infos of this ListSubCustomersResponse.
        :rtype: list[CustomerInformation]
        """
        return self._customer_infos

    @customer_infos.setter
    def customer_infos(self, customer_infos):
        """Sets the customer_infos of this ListSubCustomersResponse.

        |参数名称：客户信息列表。具体请参见表 CustomerInfo| |参数约束以及描述：客户信息列表。具体请参见表 CustomerInfo|

        :param customer_infos: The customer_infos of this ListSubCustomersResponse.
        :type: list[CustomerInformation]
        """
        self._customer_infos = customer_infos

    @property
    def count(self):
        """Gets the count of this ListSubCustomersResponse.

        |参数名称：总记录数。| |参数的约束及描述：总记录数。|

        :return: The count of this ListSubCustomersResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListSubCustomersResponse.

        |参数名称：总记录数。| |参数的约束及描述：总记录数。|

        :param count: The count of this ListSubCustomersResponse.
        :type: int
        """
        self._count = count

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
        if not isinstance(other, ListSubCustomersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
