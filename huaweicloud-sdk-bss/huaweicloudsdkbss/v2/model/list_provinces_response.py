# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListProvincesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'provinces': 'list[Province]'
    }

    attribute_map = {
        'count': 'count',
        'provinces': 'provinces'
    }

    def __init__(self, count=None, provinces=None):
        """ListProvincesResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._count = None
        self._provinces = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if provinces is not None:
            self.provinces = provinces

    @property
    def count(self):
        """Gets the count of this ListProvincesResponse.

        |参数名称：查询个数，成功的时候返回| |参数的约束及描述：查询个数，成功的时候返回|

        :return: The count of this ListProvincesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListProvincesResponse.

        |参数名称：查询个数，成功的时候返回| |参数的约束及描述：查询个数，成功的时候返回|

        :param count: The count of this ListProvincesResponse.
        :type: int
        """
        self._count = count

    @property
    def provinces(self):
        """Gets the provinces of this ListProvincesResponse.

        |参数名称：省份信息列表，成功的时候返回| |参数约束以及描述：省份信息列表，成功的时候返回|

        :return: The provinces of this ListProvincesResponse.
        :rtype: list[Province]
        """
        return self._provinces

    @provinces.setter
    def provinces(self, provinces):
        """Sets the provinces of this ListProvincesResponse.

        |参数名称：省份信息列表，成功的时候返回| |参数约束以及描述：省份信息列表，成功的时候返回|

        :param provinces: The provinces of this ListProvincesResponse.
        :type: list[Province]
        """
        self._provinces = provinces

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
        if not isinstance(other, ListProvincesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
