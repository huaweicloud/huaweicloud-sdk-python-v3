# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SysTags:

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
        """SysTags

        The model defined in huaweicloud sdk

        :param key: 键。  系统标签的key，从白名单中取，不能随意定义。 目前仅支持 _sys_enterprise_project_id字段，对应 的value为企业项目ID。
        :type key: str
        :param values: 值列表。  目前仅会用到企业项目ID，其中默 认的企业项目ID为“0”。
        :type values: list[str]
        """
        
        

        self._key = None
        self._values = None
        self.discriminator = None

        self.key = key
        self.values = values

    @property
    def key(self):
        """Gets the key of this SysTags.

        键。  系统标签的key，从白名单中取，不能随意定义。 目前仅支持 _sys_enterprise_project_id字段，对应 的value为企业项目ID。

        :return: The key of this SysTags.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this SysTags.

        键。  系统标签的key，从白名单中取，不能随意定义。 目前仅支持 _sys_enterprise_project_id字段，对应 的value为企业项目ID。

        :param key: The key of this SysTags.
        :type key: str
        """
        self._key = key

    @property
    def values(self):
        """Gets the values of this SysTags.

        值列表。  目前仅会用到企业项目ID，其中默 认的企业项目ID为“0”。

        :return: The values of this SysTags.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this SysTags.

        值列表。  目前仅会用到企业项目ID，其中默 认的企业项目ID为“0”。

        :param values: The values of this SysTags.
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
        if not isinstance(other, SysTags):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
