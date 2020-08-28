# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListCountiesResponse(SdkResponse):


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
        'counties': 'list[County]'
    }

    attribute_map = {
        'count': 'count',
        'counties': 'counties'
    }

    def __init__(self, count=None, counties=None):
        """ListCountiesResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._count = None
        self._counties = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if counties is not None:
            self.counties = counties

    @property
    def count(self):
        """Gets the count of this ListCountiesResponse.

        |参数名称：查询个数，成功的时候返回| |参数的约束及描述：查询个数，成功的时候返回|

        :return: The count of this ListCountiesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListCountiesResponse.

        |参数名称：查询个数，成功的时候返回| |参数的约束及描述：查询个数，成功的时候返回|

        :param count: The count of this ListCountiesResponse.
        :type: int
        """
        self._count = count

    @property
    def counties(self):
        """Gets the counties of this ListCountiesResponse.

        |参数名称：区县信息列表，成功的时候返回| |参数约束以及描述：区县信息列表，成功的时候返回|

        :return: The counties of this ListCountiesResponse.
        :rtype: list[County]
        """
        return self._counties

    @counties.setter
    def counties(self, counties):
        """Sets the counties of this ListCountiesResponse.

        |参数名称：区县信息列表，成功的时候返回| |参数约束以及描述：区县信息列表，成功的时候返回|

        :param counties: The counties of this ListCountiesResponse.
        :type: list[County]
        """
        self._counties = counties

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
        if not isinstance(other, ListCountiesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
