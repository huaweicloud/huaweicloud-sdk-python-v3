# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        """ListCitiesResponse

        The model defined in huaweicloud sdk

        :param count: 查询个数，成功的时候返回。
        :type count: int
        :param cities: 城市信息列表，成功的时候返回，具体参见表2。
        :type cities: list[:class:`huaweicloudsdkbss.v2.City`]
        """
        
        super(ListCitiesResponse, self).__init__()

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

        查询个数，成功的时候返回。

        :return: The count of this ListCitiesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListCitiesResponse.

        查询个数，成功的时候返回。

        :param count: The count of this ListCitiesResponse.
        :type count: int
        """
        self._count = count

    @property
    def cities(self):
        """Gets the cities of this ListCitiesResponse.

        城市信息列表，成功的时候返回，具体参见表2。

        :return: The cities of this ListCitiesResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.City`]
        """
        return self._cities

    @cities.setter
    def cities(self, cities):
        """Sets the cities of this ListCitiesResponse.

        城市信息列表，成功的时候返回，具体参见表2。

        :param cities: The cities of this ListCitiesResponse.
        :type cities: list[:class:`huaweicloudsdkbss.v2.City`]
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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListCitiesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
