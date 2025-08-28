# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RemoveHeaderConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str'
    }

    attribute_map = {
        'key': 'key'
    }

    def __init__(self, key=None):
        r"""RemoveHeaderConfig

        The model defined in huaweicloud sdk

        :param key: **参数解释**：被移除的请求头的参数名。  **取值范围**：1-40个字符，字母a-z（不区分大小写）、数字，短划线-和下划线_。
        :type key: str
        """
        
        

        self._key = None
        self.discriminator = None

        self.key = key

    @property
    def key(self):
        r"""Gets the key of this RemoveHeaderConfig.

        **参数解释**：被移除的请求头的参数名。  **取值范围**：1-40个字符，字母a-z（不区分大小写）、数字，短划线-和下划线_。

        :return: The key of this RemoveHeaderConfig.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this RemoveHeaderConfig.

        **参数解释**：被移除的请求头的参数名。  **取值范围**：1-40个字符，字母a-z（不区分大小写）、数字，短划线-和下划线_。

        :param key: The key of this RemoveHeaderConfig.
        :type key: str
        """
        self._key = key

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
        if not isinstance(other, RemoveHeaderConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
