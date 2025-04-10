# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceTag:

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
        'value': 'str',
        'tag_type': 'str'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value',
        'tag_type': 'tag_type'
    }

    def __init__(self, key=None, value=None, tag_type=None):
        r"""ResourceTag

        The model defined in huaweicloud sdk

        :param key: 标签键
        :type key: str
        :param value: 标签值
        :type value: str
        :param tag_type: 标签类型
        :type tag_type: str
        """
        
        

        self._key = None
        self._value = None
        self._tag_type = None
        self.discriminator = None

        self.key = key
        self.value = value
        self.tag_type = tag_type

    @property
    def key(self):
        r"""Gets the key of this ResourceTag.

        标签键

        :return: The key of this ResourceTag.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this ResourceTag.

        标签键

        :param key: The key of this ResourceTag.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        r"""Gets the value of this ResourceTag.

        标签值

        :return: The value of this ResourceTag.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ResourceTag.

        标签值

        :param value: The value of this ResourceTag.
        :type value: str
        """
        self._value = value

    @property
    def tag_type(self):
        r"""Gets the tag_type of this ResourceTag.

        标签类型

        :return: The tag_type of this ResourceTag.
        :rtype: str
        """
        return self._tag_type

    @tag_type.setter
    def tag_type(self, tag_type):
        r"""Sets the tag_type of this ResourceTag.

        标签类型

        :param tag_type: The tag_type of this ResourceTag.
        :type tag_type: str
        """
        self._tag_type = tag_type

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
        if not isinstance(other, ResourceTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
