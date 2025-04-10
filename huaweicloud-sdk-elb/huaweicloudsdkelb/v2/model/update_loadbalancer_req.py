# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateLoadbalancerReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'admin_state_up': 'bool',
        'protection_status': 'str',
        'protection_reason': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'admin_state_up': 'admin_state_up',
        'protection_status': 'protection_status',
        'protection_reason': 'protection_reason'
    }

    def __init__(self, name=None, description=None, admin_state_up=None, protection_status=None, protection_reason=None):
        r"""UpdateLoadbalancerReq

        The model defined in huaweicloud sdk

        :param name: 负载均衡器名称。
        :type name: str
        :param description: 负载均衡器的描述信息
        :type description: str
        :param admin_state_up: 负载均衡器的管理状态。只支持设定为true，该字段的值无实际意义。
        :type admin_state_up: bool
        :param protection_status: 修改保护状态, 取值： - nonProtection: 不保护 - consoleProtection: 控制台修改保护
        :type protection_status: str
        :param protection_reason: 设置保护的原因 &gt;仅当protection_status为consoleProtection时有效。
        :type protection_reason: str
        """
        
        

        self._name = None
        self._description = None
        self._admin_state_up = None
        self._protection_status = None
        self._protection_reason = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if protection_status is not None:
            self.protection_status = protection_status
        if protection_reason is not None:
            self.protection_reason = protection_reason

    @property
    def name(self):
        r"""Gets the name of this UpdateLoadbalancerReq.

        负载均衡器名称。

        :return: The name of this UpdateLoadbalancerReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateLoadbalancerReq.

        负载均衡器名称。

        :param name: The name of this UpdateLoadbalancerReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateLoadbalancerReq.

        负载均衡器的描述信息

        :return: The description of this UpdateLoadbalancerReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateLoadbalancerReq.

        负载均衡器的描述信息

        :param description: The description of this UpdateLoadbalancerReq.
        :type description: str
        """
        self._description = description

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this UpdateLoadbalancerReq.

        负载均衡器的管理状态。只支持设定为true，该字段的值无实际意义。

        :return: The admin_state_up of this UpdateLoadbalancerReq.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this UpdateLoadbalancerReq.

        负载均衡器的管理状态。只支持设定为true，该字段的值无实际意义。

        :param admin_state_up: The admin_state_up of this UpdateLoadbalancerReq.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def protection_status(self):
        r"""Gets the protection_status of this UpdateLoadbalancerReq.

        修改保护状态, 取值： - nonProtection: 不保护 - consoleProtection: 控制台修改保护

        :return: The protection_status of this UpdateLoadbalancerReq.
        :rtype: str
        """
        return self._protection_status

    @protection_status.setter
    def protection_status(self, protection_status):
        r"""Sets the protection_status of this UpdateLoadbalancerReq.

        修改保护状态, 取值： - nonProtection: 不保护 - consoleProtection: 控制台修改保护

        :param protection_status: The protection_status of this UpdateLoadbalancerReq.
        :type protection_status: str
        """
        self._protection_status = protection_status

    @property
    def protection_reason(self):
        r"""Gets the protection_reason of this UpdateLoadbalancerReq.

        设置保护的原因 >仅当protection_status为consoleProtection时有效。

        :return: The protection_reason of this UpdateLoadbalancerReq.
        :rtype: str
        """
        return self._protection_reason

    @protection_reason.setter
    def protection_reason(self, protection_reason):
        r"""Sets the protection_reason of this UpdateLoadbalancerReq.

        设置保护的原因 >仅当protection_status为consoleProtection时有效。

        :param protection_reason: The protection_reason of this UpdateLoadbalancerReq.
        :type protection_reason: str
        """
        self._protection_reason = protection_reason

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
        if not isinstance(other, UpdateLoadbalancerReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
