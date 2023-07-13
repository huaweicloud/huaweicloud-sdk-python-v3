# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RedisDeleteDbUserRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'names': 'list[str]'
    }

    attribute_map = {
        'names': 'names'
    }

    def __init__(self, names=None):
        """RedisDeleteDbUserRequest

        The model defined in huaweicloud sdk

        :param names: 需要删除的数据库账号名称列表。
        :type names: list[str]
        """
        
        

        self._names = None
        self.discriminator = None

        self.names = names

    @property
    def names(self):
        """Gets the names of this RedisDeleteDbUserRequest.

        需要删除的数据库账号名称列表。

        :return: The names of this RedisDeleteDbUserRequest.
        :rtype: list[str]
        """
        return self._names

    @names.setter
    def names(self, names):
        """Sets the names of this RedisDeleteDbUserRequest.

        需要删除的数据库账号名称列表。

        :param names: The names of this RedisDeleteDbUserRequest.
        :type names: list[str]
        """
        self._names = names

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
        if not isinstance(other, RedisDeleteDbUserRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
