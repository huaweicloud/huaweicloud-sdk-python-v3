# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CacheUrlParameterFilter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'value': 'str'
    }

    attribute_map = {
        'type': 'type',
        'value': 'value'
    }

    def __init__(self, type=None, value=None):
        r"""CacheUrlParameterFilter

        The model defined in huaweicloud sdk

        :param type: 缓存URL参数操作类型： - full_url：缓存所有参数； - ignore_url_params：忽略所有参数； - del_params：忽略指定URL参数； - reserve_params：保留指定URL参数。   &gt; 本接口参数有调整，参数替换如下：   &gt; - del_params替代del_args。   &gt; - reserve_params替代reserve_args。
        :type type: str
        :param value: 参数值，多个参数使用分号分隔。
        :type value: str
        """
        
        

        self._type = None
        self._value = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if value is not None:
            self.value = value

    @property
    def type(self):
        r"""Gets the type of this CacheUrlParameterFilter.

        缓存URL参数操作类型： - full_url：缓存所有参数； - ignore_url_params：忽略所有参数； - del_params：忽略指定URL参数； - reserve_params：保留指定URL参数。   > 本接口参数有调整，参数替换如下：   > - del_params替代del_args。   > - reserve_params替代reserve_args。

        :return: The type of this CacheUrlParameterFilter.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CacheUrlParameterFilter.

        缓存URL参数操作类型： - full_url：缓存所有参数； - ignore_url_params：忽略所有参数； - del_params：忽略指定URL参数； - reserve_params：保留指定URL参数。   > 本接口参数有调整，参数替换如下：   > - del_params替代del_args。   > - reserve_params替代reserve_args。

        :param type: The type of this CacheUrlParameterFilter.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        r"""Gets the value of this CacheUrlParameterFilter.

        参数值，多个参数使用分号分隔。

        :return: The value of this CacheUrlParameterFilter.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this CacheUrlParameterFilter.

        参数值，多个参数使用分号分隔。

        :param value: The value of this CacheUrlParameterFilter.
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
        if not isinstance(other, CacheUrlParameterFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
