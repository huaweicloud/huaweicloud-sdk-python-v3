# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Sorted:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'reverse': 'bool'
    }

    attribute_map = {
        'key': 'key',
        'reverse': 'reverse'
    }

    def __init__(self, key=None, reverse=None):
        """Sorted

        The model defined in huaweicloud sdk

        :param key: 按key值对请求内容进行排序
        :type key: str
        :param reverse: 是否采用倒序
        :type reverse: bool
        """
        
        

        self._key = None
        self._reverse = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if reverse is not None:
            self.reverse = reverse

    @property
    def key(self):
        """Gets the key of this Sorted.

        按key值对请求内容进行排序

        :return: The key of this Sorted.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Sorted.

        按key值对请求内容进行排序

        :param key: The key of this Sorted.
        :type key: str
        """
        self._key = key

    @property
    def reverse(self):
        """Gets the reverse of this Sorted.

        是否采用倒序

        :return: The reverse of this Sorted.
        :rtype: bool
        """
        return self._reverse

    @reverse.setter
    def reverse(self, reverse):
        """Sets the reverse of this Sorted.

        是否采用倒序

        :param reverse: The reverse of this Sorted.
        :type reverse: bool
        """
        self._reverse = reverse

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
        if not isinstance(other, Sorted):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
