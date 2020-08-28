# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListPayPerUseCustomerResourcesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'data': 'list[OrderInstanceV2]',
        'total_count': 'int'
    }

    attribute_map = {
        'data': 'data',
        'total_count': 'total_count'
    }

    def __init__(self, data=None, total_count=None):
        """ListPayPerUseCustomerResourcesResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._data = None
        self._total_count = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if total_count is not None:
            self.total_count = total_count

    @property
    def data(self):
        """Gets the data of this ListPayPerUseCustomerResourcesResponse.

        |参数名称：资源列表。具体请参见表2 OrderInstanceV2。| |参数约束以及描述：资源列表。具体请参见表2 OrderInstanceV2。|

        :return: The data of this ListPayPerUseCustomerResourcesResponse.
        :rtype: list[OrderInstanceV2]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ListPayPerUseCustomerResourcesResponse.

        |参数名称：资源列表。具体请参见表2 OrderInstanceV2。| |参数约束以及描述：资源列表。具体请参见表2 OrderInstanceV2。|

        :param data: The data of this ListPayPerUseCustomerResourcesResponse.
        :type: list[OrderInstanceV2]
        """
        self._data = data

    @property
    def total_count(self):
        """Gets the total_count of this ListPayPerUseCustomerResourcesResponse.

        |参数名称：总记录数。| |参数的约束及描述：总记录数。|

        :return: The total_count of this ListPayPerUseCustomerResourcesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListPayPerUseCustomerResourcesResponse.

        |参数名称：总记录数。| |参数的约束及描述：总记录数。|

        :param total_count: The total_count of this ListPayPerUseCustomerResourcesResponse.
        :type: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListPayPerUseCustomerResourcesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
