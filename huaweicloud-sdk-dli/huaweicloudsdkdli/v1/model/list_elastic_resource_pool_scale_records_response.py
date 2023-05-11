# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListElasticResourcePoolScaleRecordsResponse(SdkResponse):

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
        'items': 'list[list[object]]',
        'x_auth_token': 'str'
    }

    attribute_map = {
        'count': 'count',
        'items': 'items',
        'x_auth_token': 'X-Auth-Token'
    }

    def __init__(self, count=None, items=None, x_auth_token=None):
        """ListElasticResourcePoolScaleRecordsResponse

        The model defined in huaweicloud sdk

        :param count: 返回数组长度
        :type count: int
        :param items: 数组中返回的数据
        :type items: list[list[object]]
        :param x_auth_token: 
        :type x_auth_token: str
        """
        
        super(ListElasticResourcePoolScaleRecordsResponse, self).__init__()

        self._count = None
        self._items = None
        self._x_auth_token = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if items is not None:
            self.items = items
        if x_auth_token is not None:
            self.x_auth_token = x_auth_token

    @property
    def count(self):
        """Gets the count of this ListElasticResourcePoolScaleRecordsResponse.

        返回数组长度

        :return: The count of this ListElasticResourcePoolScaleRecordsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListElasticResourcePoolScaleRecordsResponse.

        返回数组长度

        :param count: The count of this ListElasticResourcePoolScaleRecordsResponse.
        :type count: int
        """
        self._count = count

    @property
    def items(self):
        """Gets the items of this ListElasticResourcePoolScaleRecordsResponse.

        数组中返回的数据

        :return: The items of this ListElasticResourcePoolScaleRecordsResponse.
        :rtype: list[list[object]]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ListElasticResourcePoolScaleRecordsResponse.

        数组中返回的数据

        :param items: The items of this ListElasticResourcePoolScaleRecordsResponse.
        :type items: list[list[object]]
        """
        self._items = items

    @property
    def x_auth_token(self):
        """Gets the x_auth_token of this ListElasticResourcePoolScaleRecordsResponse.

        :return: The x_auth_token of this ListElasticResourcePoolScaleRecordsResponse.
        :rtype: str
        """
        return self._x_auth_token

    @x_auth_token.setter
    def x_auth_token(self, x_auth_token):
        """Sets the x_auth_token of this ListElasticResourcePoolScaleRecordsResponse.

        :param x_auth_token: The x_auth_token of this ListElasticResourcePoolScaleRecordsResponse.
        :type x_auth_token: str
        """
        self._x_auth_token = x_auth_token

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
        if not isinstance(other, ListElasticResourcePoolScaleRecordsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
