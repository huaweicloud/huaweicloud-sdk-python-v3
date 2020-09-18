# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListCitiesResponse(SdkResponse):


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
        'cities': 'list[City]'
    }

    attribute_map = {
        'count': 'count',
        'cities': 'cities'
    }

    def __init__(self, count=None, cities=None):
        """ListCitiesResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._count = None
        self._cities = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if cities is not None:
            self.cities = cities

    @property
    def count(self):
        """Gets the count of this ListCitiesResponse.

        |参数名称：查询个数，成功的时候返回| |参数的约束及描述：查询个数，成功的时候返回|

        :return: The count of this ListCitiesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListCitiesResponse.

        |参数名称：查询个数，成功的时候返回| |参数的约束及描述：查询个数，成功的时候返回|

        :param count: The count of this ListCitiesResponse.
        :type: int
        """
        self._count = count

    @property
    def cities(self):
        """Gets the cities of this ListCitiesResponse.

        |参数名称：城市信息列表，成功的时候返回| |参数约束以及描述：城市信息列表，成功的时候返回|

        :return: The cities of this ListCitiesResponse.
        :rtype: list[City]
        """
        return self._cities

    @cities.setter
    def cities(self, cities):
        """Sets the cities of this ListCitiesResponse.

        |参数名称：城市信息列表，成功的时候返回| |参数约束以及描述：城市信息列表，成功的时候返回|

        :param cities: The cities of this ListCitiesResponse.
        :type: list[City]
        """
        self._cities = cities

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
        if not isinstance(other, ListCitiesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
