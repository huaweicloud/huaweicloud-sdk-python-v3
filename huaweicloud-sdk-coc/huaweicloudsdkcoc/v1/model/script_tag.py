# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScriptTag:

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
        'values': 'list[str]'
    }

    attribute_map = {
        'key': 'key',
        'values': 'values'
    }

    def __init__(self, key=None, values=None):
        r"""ScriptTag

        The model defined in huaweicloud sdk

        :param key: 标签的key。
        :type key: str
        :param values: 标签的key对应的全部value。
        :type values: list[str]
        """
        
        

        self._key = None
        self._values = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if values is not None:
            self.values = values

    @property
    def key(self):
        r"""Gets the key of this ScriptTag.

        标签的key。

        :return: The key of this ScriptTag.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this ScriptTag.

        标签的key。

        :param key: The key of this ScriptTag.
        :type key: str
        """
        self._key = key

    @property
    def values(self):
        r"""Gets the values of this ScriptTag.

        标签的key对应的全部value。

        :return: The values of this ScriptTag.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this ScriptTag.

        标签的key对应的全部value。

        :param values: The values of this ScriptTag.
        :type values: list[str]
        """
        self._values = values

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
        if not isinstance(other, ScriptTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
