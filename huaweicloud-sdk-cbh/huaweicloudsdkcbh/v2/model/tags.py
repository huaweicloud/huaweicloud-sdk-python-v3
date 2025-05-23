# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Tags:

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
        r"""Tags

        The model defined in huaweicloud sdk

        :param key: 键。  &gt; 说明： - key不能为空，长度1~128个字符（中文也可以输入128个字符） - 可用 UTF-8 格式表示的字母(包含中文)、数字和空格，以及以下字符： _ . : &#x3D; + - @ - _sys_开头属于系统标签，租户不能输入 - 建议正则：^((?!_sys_)[\\\\p{L}\\\\p{Z}\\\\p{N}_.:&#x3D;+\\\\-@]*)$
        :type key: str
        :param values: 值列表。  &gt; 说明： - 长度0~255个字符（中文也可以输入255个字符） - 可用 UTF-8 格式表示的字母(包含中文)、数字和空格，以及以下字符： _ . : / &#x3D; + - @ 建议正则：^([\\p{L}\\p{Z}\\p{N}_.:/&#x3D;+\\-@]*)$ - 资源标签值可以为空（empty or null） - 预定义标签值不可以为空
        :type values: list[str]
        """
        
        

        self._key = None
        self._values = None
        self.discriminator = None

        self.key = key
        self.values = values

    @property
    def key(self):
        r"""Gets the key of this Tags.

        键。  > 说明： - key不能为空，长度1~128个字符（中文也可以输入128个字符） - 可用 UTF-8 格式表示的字母(包含中文)、数字和空格，以及以下字符： _ . : = + - @ - _sys_开头属于系统标签，租户不能输入 - 建议正则：^((?!_sys_)[\\\\p{L}\\\\p{Z}\\\\p{N}_.:=+\\\\-@]*)$

        :return: The key of this Tags.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this Tags.

        键。  > 说明： - key不能为空，长度1~128个字符（中文也可以输入128个字符） - 可用 UTF-8 格式表示的字母(包含中文)、数字和空格，以及以下字符： _ . : = + - @ - _sys_开头属于系统标签，租户不能输入 - 建议正则：^((?!_sys_)[\\\\p{L}\\\\p{Z}\\\\p{N}_.:=+\\\\-@]*)$

        :param key: The key of this Tags.
        :type key: str
        """
        self._key = key

    @property
    def values(self):
        r"""Gets the values of this Tags.

        值列表。  > 说明： - 长度0~255个字符（中文也可以输入255个字符） - 可用 UTF-8 格式表示的字母(包含中文)、数字和空格，以及以下字符： _ . : / = + - @ 建议正则：^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$ - 资源标签值可以为空（empty or null） - 预定义标签值不可以为空

        :return: The values of this Tags.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this Tags.

        值列表。  > 说明： - 长度0~255个字符（中文也可以输入255个字符） - 可用 UTF-8 格式表示的字母(包含中文)、数字和空格，以及以下字符： _ . : / = + - @ 建议正则：^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$ - 资源标签值可以为空（empty or null） - 预定义标签值不可以为空

        :param values: The values of this Tags.
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
        if not isinstance(other, Tags):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
