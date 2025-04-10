# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchIpGroupRequestBody:

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
        'enabled': 'bool',
        'ip_groups': 'list[SwitchIpGroupRequestBodyIpGroups]'
    }

    attribute_map = {
        'type': 'type',
        'enabled': 'enabled',
        'ip_groups': 'ip_groups'
    }

    def __init__(self, type=None, enabled=None, ip_groups=None):
        r"""SwitchIpGroupRequestBody

        The model defined in huaweicloud sdk

        :param type: 类型选项，取值： - whiteList：白名单，只允许指定ip或网段访问。 - blackList：黑名单，不允许指定ip或网段访问。
        :type type: str
        :param enabled: true 开启，false 关闭。
        :type enabled: bool
        :param ip_groups: IP地址组中包含的IP或网段列表。
        :type ip_groups: list[:class:`huaweicloudsdkgaussdbfornosql.v3.SwitchIpGroupRequestBodyIpGroups`]
        """
        
        

        self._type = None
        self._enabled = None
        self._ip_groups = None
        self.discriminator = None

        self.type = type
        self.enabled = enabled
        self.ip_groups = ip_groups

    @property
    def type(self):
        r"""Gets the type of this SwitchIpGroupRequestBody.

        类型选项，取值： - whiteList：白名单，只允许指定ip或网段访问。 - blackList：黑名单，不允许指定ip或网段访问。

        :return: The type of this SwitchIpGroupRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SwitchIpGroupRequestBody.

        类型选项，取值： - whiteList：白名单，只允许指定ip或网段访问。 - blackList：黑名单，不允许指定ip或网段访问。

        :param type: The type of this SwitchIpGroupRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def enabled(self):
        r"""Gets the enabled of this SwitchIpGroupRequestBody.

        true 开启，false 关闭。

        :return: The enabled of this SwitchIpGroupRequestBody.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this SwitchIpGroupRequestBody.

        true 开启，false 关闭。

        :param enabled: The enabled of this SwitchIpGroupRequestBody.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def ip_groups(self):
        r"""Gets the ip_groups of this SwitchIpGroupRequestBody.

        IP地址组中包含的IP或网段列表。

        :return: The ip_groups of this SwitchIpGroupRequestBody.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.SwitchIpGroupRequestBodyIpGroups`]
        """
        return self._ip_groups

    @ip_groups.setter
    def ip_groups(self, ip_groups):
        r"""Sets the ip_groups of this SwitchIpGroupRequestBody.

        IP地址组中包含的IP或网段列表。

        :param ip_groups: The ip_groups of this SwitchIpGroupRequestBody.
        :type ip_groups: list[:class:`huaweicloudsdkgaussdbfornosql.v3.SwitchIpGroupRequestBodyIpGroups`]
        """
        self._ip_groups = ip_groups

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
        if not isinstance(other, SwitchIpGroupRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
