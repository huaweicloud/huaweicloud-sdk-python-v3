# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RefererConfig:

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
        'value': 'str',
        'include_empty': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'value': 'value',
        'include_empty': 'include_empty'
    }

    def __init__(self, type=None, value=None, include_empty=None):
        r"""RefererConfig

        The model defined in huaweicloud sdk

        :param type: Referer黑白名单类型，off：关闭Referer黑白名单，black：Referer黑名单，white：Referer白名单。
        :type type: str
        :param value: 域名或IP地址，以“,”进行分割，域名、IP地址可以混合输入，支持泛域名和带端口的域名。域名、IP地址总数不超过400个，端口取值范围1-65535。
        :type value: str
        :param include_empty: 是否包含空Referer，如果是黑名单并开启该选项，则表示无referer不允许访问，如果是白名单并开启该选项，则表示无referer允许访问，默认值false。
        :type include_empty: bool
        """
        
        

        self._type = None
        self._value = None
        self._include_empty = None
        self.discriminator = None

        self.type = type
        if value is not None:
            self.value = value
        if include_empty is not None:
            self.include_empty = include_empty

    @property
    def type(self):
        r"""Gets the type of this RefererConfig.

        Referer黑白名单类型，off：关闭Referer黑白名单，black：Referer黑名单，white：Referer白名单。

        :return: The type of this RefererConfig.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RefererConfig.

        Referer黑白名单类型，off：关闭Referer黑白名单，black：Referer黑名单，white：Referer白名单。

        :param type: The type of this RefererConfig.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        r"""Gets the value of this RefererConfig.

        域名或IP地址，以“,”进行分割，域名、IP地址可以混合输入，支持泛域名和带端口的域名。域名、IP地址总数不超过400个，端口取值范围1-65535。

        :return: The value of this RefererConfig.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this RefererConfig.

        域名或IP地址，以“,”进行分割，域名、IP地址可以混合输入，支持泛域名和带端口的域名。域名、IP地址总数不超过400个，端口取值范围1-65535。

        :param value: The value of this RefererConfig.
        :type value: str
        """
        self._value = value

    @property
    def include_empty(self):
        r"""Gets the include_empty of this RefererConfig.

        是否包含空Referer，如果是黑名单并开启该选项，则表示无referer不允许访问，如果是白名单并开启该选项，则表示无referer允许访问，默认值false。

        :return: The include_empty of this RefererConfig.
        :rtype: bool
        """
        return self._include_empty

    @include_empty.setter
    def include_empty(self, include_empty):
        r"""Sets the include_empty of this RefererConfig.

        是否包含空Referer，如果是黑名单并开启该选项，则表示无referer不允许访问，如果是白名单并开启该选项，则表示无referer允许访问，默认值false。

        :param include_empty: The include_empty of this RefererConfig.
        :type include_empty: bool
        """
        self._include_empty = include_empty

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
        if not isinstance(other, RefererConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
