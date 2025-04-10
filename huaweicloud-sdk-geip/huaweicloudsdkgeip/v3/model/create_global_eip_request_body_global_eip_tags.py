# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateGlobalEipRequestBodyGlobalEipTags:

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
        'value': 'str'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value'
    }

    def __init__(self, key=None, value=None):
        r"""CreateGlobalEipRequestBodyGlobalEipTags

        The model defined in huaweicloud sdk

        :param key: - 功能说明：标签名称 - 约束：   - 创建的预定义标签如果与已有的预定义标签完全相同，则会覆盖已有的预定义标签；若只有“键”相同，“值”不同，则为新创建的预定义标签。   - 键的长度最大36字符，由英文字母、数字、下划线、中划线、中文字符组成。   - 单个资源最多可以添加20个标签。
        :type key: str
        :param value: - 功能说明：标签值 - 约束：   - 值的长度最大43字符，由英文字母、数字、下划线、点、中划线、中文字符组成。
        :type value: str
        """
        
        

        self._key = None
        self._value = None
        self.discriminator = None

        self.key = key
        self.value = value

    @property
    def key(self):
        r"""Gets the key of this CreateGlobalEipRequestBodyGlobalEipTags.

        - 功能说明：标签名称 - 约束：   - 创建的预定义标签如果与已有的预定义标签完全相同，则会覆盖已有的预定义标签；若只有“键”相同，“值”不同，则为新创建的预定义标签。   - 键的长度最大36字符，由英文字母、数字、下划线、中划线、中文字符组成。   - 单个资源最多可以添加20个标签。

        :return: The key of this CreateGlobalEipRequestBodyGlobalEipTags.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this CreateGlobalEipRequestBodyGlobalEipTags.

        - 功能说明：标签名称 - 约束：   - 创建的预定义标签如果与已有的预定义标签完全相同，则会覆盖已有的预定义标签；若只有“键”相同，“值”不同，则为新创建的预定义标签。   - 键的长度最大36字符，由英文字母、数字、下划线、中划线、中文字符组成。   - 单个资源最多可以添加20个标签。

        :param key: The key of this CreateGlobalEipRequestBodyGlobalEipTags.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        r"""Gets the value of this CreateGlobalEipRequestBodyGlobalEipTags.

        - 功能说明：标签值 - 约束：   - 值的长度最大43字符，由英文字母、数字、下划线、点、中划线、中文字符组成。

        :return: The value of this CreateGlobalEipRequestBodyGlobalEipTags.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this CreateGlobalEipRequestBodyGlobalEipTags.

        - 功能说明：标签值 - 约束：   - 值的长度最大43字符，由英文字母、数字、下划线、点、中划线、中文字符组成。

        :param value: The value of this CreateGlobalEipRequestBodyGlobalEipTags.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, CreateGlobalEipRequestBodyGlobalEipTags):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
