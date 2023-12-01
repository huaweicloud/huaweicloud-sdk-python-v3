# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowElbIpGroupResponse(SdkResponse):

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
        'ip_groups': 'list[SwitchIpGroupRequestBodyIpGroups]',
        'enabled': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'ip_groups': 'ip_groups',
        'enabled': 'enabled'
    }

    def __init__(self, type=None, ip_groups=None, enabled=None):
        """ShowElbIpGroupResponse

        The model defined in huaweicloud sdk

        :param type: 类型选项，取值： - whiteList：白名单，只允许指定ip或网段访问。 - blackList：黑名单，不允许指定ip或网段访问。
        :type type: str
        :param ip_groups: IP地址组中包含的IP或网段列表。
        :type ip_groups: list[:class:`huaweicloudsdkgaussdbfornosql.v3.SwitchIpGroupRequestBodyIpGroups`]
        :param enabled: true：开启，false：关闭。
        :type enabled: bool
        """
        
        super(ShowElbIpGroupResponse, self).__init__()

        self._type = None
        self._ip_groups = None
        self._enabled = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if ip_groups is not None:
            self.ip_groups = ip_groups
        if enabled is not None:
            self.enabled = enabled

    @property
    def type(self):
        """Gets the type of this ShowElbIpGroupResponse.

        类型选项，取值： - whiteList：白名单，只允许指定ip或网段访问。 - blackList：黑名单，不允许指定ip或网段访问。

        :return: The type of this ShowElbIpGroupResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowElbIpGroupResponse.

        类型选项，取值： - whiteList：白名单，只允许指定ip或网段访问。 - blackList：黑名单，不允许指定ip或网段访问。

        :param type: The type of this ShowElbIpGroupResponse.
        :type type: str
        """
        self._type = type

    @property
    def ip_groups(self):
        """Gets the ip_groups of this ShowElbIpGroupResponse.

        IP地址组中包含的IP或网段列表。

        :return: The ip_groups of this ShowElbIpGroupResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.SwitchIpGroupRequestBodyIpGroups`]
        """
        return self._ip_groups

    @ip_groups.setter
    def ip_groups(self, ip_groups):
        """Sets the ip_groups of this ShowElbIpGroupResponse.

        IP地址组中包含的IP或网段列表。

        :param ip_groups: The ip_groups of this ShowElbIpGroupResponse.
        :type ip_groups: list[:class:`huaweicloudsdkgaussdbfornosql.v3.SwitchIpGroupRequestBodyIpGroups`]
        """
        self._ip_groups = ip_groups

    @property
    def enabled(self):
        """Gets the enabled of this ShowElbIpGroupResponse.

        true：开启，false：关闭。

        :return: The enabled of this ShowElbIpGroupResponse.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ShowElbIpGroupResponse.

        true：开启，false：关闭。

        :param enabled: The enabled of this ShowElbIpGroupResponse.
        :type enabled: bool
        """
        self._enabled = enabled

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
        if not isinstance(other, ShowElbIpGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
