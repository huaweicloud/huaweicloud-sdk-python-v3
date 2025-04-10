# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityGroupRulesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'id': 'list[str]',
        'security_group_id': 'list[str]',
        'protocol': 'list[str]',
        'description': 'list[str]',
        'remote_group_id': 'list[str]',
        'direction': 'str',
        'action': 'str',
        'remote_ip_prefix': 'str',
        'priority': 'list[int]',
        'ethertype': 'list[str]',
        'remote_address_group_id': 'list[str]',
        'enabled': 'bool'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'id': 'id',
        'security_group_id': 'security_group_id',
        'protocol': 'protocol',
        'description': 'description',
        'remote_group_id': 'remote_group_id',
        'direction': 'direction',
        'action': 'action',
        'remote_ip_prefix': 'remote_ip_prefix',
        'priority': 'priority',
        'ethertype': 'ethertype',
        'remote_address_group_id': 'remote_address_group_id',
        'enabled': 'enabled'
    }

    def __init__(self, limit=None, marker=None, id=None, security_group_id=None, protocol=None, description=None, remote_group_id=None, direction=None, action=None, remote_ip_prefix=None, priority=None, ethertype=None, remote_address_group_id=None, enabled=None):
        r"""ListSecurityGroupRulesRequest

        The model defined in huaweicloud sdk

        :param limit: 功能说明：每页返回个数 取值范围：0-2000
        :type limit: int
        :param marker: 分页查询起始的资源ID，为空时查询第一页
        :type marker: str
        :param id: 功能说明：安全组规则ID，支持多个ID过滤
        :type id: list[str]
        :param security_group_id: 功能说明：安全组规则所属安全组ID，支持多个ID过滤
        :type security_group_id: list[str]
        :param protocol: 功能说明：安全组规则协议，支持多条过滤
        :type protocol: list[str]
        :param description: 功能说明：安全组规则的描述，支持多个描述同时过滤
        :type description: list[str]
        :param remote_group_id: 功能说明：远端安全组ID，支持多ID过滤
        :type remote_group_id: list[str]
        :param direction: 功能说明：安全组规则方向
        :type direction: str
        :param action: 功能说明：安全组规则生效策略。 取值范围：allow表示允许，deny表示拒绝。
        :type action: str
        :param remote_ip_prefix: 功能说明：远端IP地址 取值范围：cidr格式
        :type remote_ip_prefix: str
        :param priority: 功能说明：优先级，支持多条过滤。
        :type priority: list[int]
        :param ethertype: 功能说明：IP协议类型，支持多条过滤。 取值范围：IPv4,IPv6,ipv4,ipv6
        :type ethertype: list[str]
        :param remote_address_group_id: 功能说明：远端IP地址组ID，支持多ID过滤。
        :type remote_address_group_id: list[str]
        :param enabled: 功能说明：是否启用安全组规则，不支持多值过滤。 取值范围：true, false。
        :type enabled: bool
        """
        
        

        self._limit = None
        self._marker = None
        self._id = None
        self._security_group_id = None
        self._protocol = None
        self._description = None
        self._remote_group_id = None
        self._direction = None
        self._action = None
        self._remote_ip_prefix = None
        self._priority = None
        self._ethertype = None
        self._remote_address_group_id = None
        self._enabled = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if id is not None:
            self.id = id
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if protocol is not None:
            self.protocol = protocol
        if description is not None:
            self.description = description
        if remote_group_id is not None:
            self.remote_group_id = remote_group_id
        if direction is not None:
            self.direction = direction
        if action is not None:
            self.action = action
        if remote_ip_prefix is not None:
            self.remote_ip_prefix = remote_ip_prefix
        if priority is not None:
            self.priority = priority
        if ethertype is not None:
            self.ethertype = ethertype
        if remote_address_group_id is not None:
            self.remote_address_group_id = remote_address_group_id
        if enabled is not None:
            self.enabled = enabled

    @property
    def limit(self):
        r"""Gets the limit of this ListSecurityGroupRulesRequest.

        功能说明：每页返回个数 取值范围：0-2000

        :return: The limit of this ListSecurityGroupRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSecurityGroupRulesRequest.

        功能说明：每页返回个数 取值范围：0-2000

        :param limit: The limit of this ListSecurityGroupRulesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListSecurityGroupRulesRequest.

        分页查询起始的资源ID，为空时查询第一页

        :return: The marker of this ListSecurityGroupRulesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListSecurityGroupRulesRequest.

        分页查询起始的资源ID，为空时查询第一页

        :param marker: The marker of this ListSecurityGroupRulesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def id(self):
        r"""Gets the id of this ListSecurityGroupRulesRequest.

        功能说明：安全组规则ID，支持多个ID过滤

        :return: The id of this ListSecurityGroupRulesRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListSecurityGroupRulesRequest.

        功能说明：安全组规则ID，支持多个ID过滤

        :param id: The id of this ListSecurityGroupRulesRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this ListSecurityGroupRulesRequest.

        功能说明：安全组规则所属安全组ID，支持多个ID过滤

        :return: The security_group_id of this ListSecurityGroupRulesRequest.
        :rtype: list[str]
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this ListSecurityGroupRulesRequest.

        功能说明：安全组规则所属安全组ID，支持多个ID过滤

        :param security_group_id: The security_group_id of this ListSecurityGroupRulesRequest.
        :type security_group_id: list[str]
        """
        self._security_group_id = security_group_id

    @property
    def protocol(self):
        r"""Gets the protocol of this ListSecurityGroupRulesRequest.

        功能说明：安全组规则协议，支持多条过滤

        :return: The protocol of this ListSecurityGroupRulesRequest.
        :rtype: list[str]
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this ListSecurityGroupRulesRequest.

        功能说明：安全组规则协议，支持多条过滤

        :param protocol: The protocol of this ListSecurityGroupRulesRequest.
        :type protocol: list[str]
        """
        self._protocol = protocol

    @property
    def description(self):
        r"""Gets the description of this ListSecurityGroupRulesRequest.

        功能说明：安全组规则的描述，支持多个描述同时过滤

        :return: The description of this ListSecurityGroupRulesRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListSecurityGroupRulesRequest.

        功能说明：安全组规则的描述，支持多个描述同时过滤

        :param description: The description of this ListSecurityGroupRulesRequest.
        :type description: list[str]
        """
        self._description = description

    @property
    def remote_group_id(self):
        r"""Gets the remote_group_id of this ListSecurityGroupRulesRequest.

        功能说明：远端安全组ID，支持多ID过滤

        :return: The remote_group_id of this ListSecurityGroupRulesRequest.
        :rtype: list[str]
        """
        return self._remote_group_id

    @remote_group_id.setter
    def remote_group_id(self, remote_group_id):
        r"""Sets the remote_group_id of this ListSecurityGroupRulesRequest.

        功能说明：远端安全组ID，支持多ID过滤

        :param remote_group_id: The remote_group_id of this ListSecurityGroupRulesRequest.
        :type remote_group_id: list[str]
        """
        self._remote_group_id = remote_group_id

    @property
    def direction(self):
        r"""Gets the direction of this ListSecurityGroupRulesRequest.

        功能说明：安全组规则方向

        :return: The direction of this ListSecurityGroupRulesRequest.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        r"""Sets the direction of this ListSecurityGroupRulesRequest.

        功能说明：安全组规则方向

        :param direction: The direction of this ListSecurityGroupRulesRequest.
        :type direction: str
        """
        self._direction = direction

    @property
    def action(self):
        r"""Gets the action of this ListSecurityGroupRulesRequest.

        功能说明：安全组规则生效策略。 取值范围：allow表示允许，deny表示拒绝。

        :return: The action of this ListSecurityGroupRulesRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ListSecurityGroupRulesRequest.

        功能说明：安全组规则生效策略。 取值范围：allow表示允许，deny表示拒绝。

        :param action: The action of this ListSecurityGroupRulesRequest.
        :type action: str
        """
        self._action = action

    @property
    def remote_ip_prefix(self):
        r"""Gets the remote_ip_prefix of this ListSecurityGroupRulesRequest.

        功能说明：远端IP地址 取值范围：cidr格式

        :return: The remote_ip_prefix of this ListSecurityGroupRulesRequest.
        :rtype: str
        """
        return self._remote_ip_prefix

    @remote_ip_prefix.setter
    def remote_ip_prefix(self, remote_ip_prefix):
        r"""Sets the remote_ip_prefix of this ListSecurityGroupRulesRequest.

        功能说明：远端IP地址 取值范围：cidr格式

        :param remote_ip_prefix: The remote_ip_prefix of this ListSecurityGroupRulesRequest.
        :type remote_ip_prefix: str
        """
        self._remote_ip_prefix = remote_ip_prefix

    @property
    def priority(self):
        r"""Gets the priority of this ListSecurityGroupRulesRequest.

        功能说明：优先级，支持多条过滤。

        :return: The priority of this ListSecurityGroupRulesRequest.
        :rtype: list[int]
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this ListSecurityGroupRulesRequest.

        功能说明：优先级，支持多条过滤。

        :param priority: The priority of this ListSecurityGroupRulesRequest.
        :type priority: list[int]
        """
        self._priority = priority

    @property
    def ethertype(self):
        r"""Gets the ethertype of this ListSecurityGroupRulesRequest.

        功能说明：IP协议类型，支持多条过滤。 取值范围：IPv4,IPv6,ipv4,ipv6

        :return: The ethertype of this ListSecurityGroupRulesRequest.
        :rtype: list[str]
        """
        return self._ethertype

    @ethertype.setter
    def ethertype(self, ethertype):
        r"""Sets the ethertype of this ListSecurityGroupRulesRequest.

        功能说明：IP协议类型，支持多条过滤。 取值范围：IPv4,IPv6,ipv4,ipv6

        :param ethertype: The ethertype of this ListSecurityGroupRulesRequest.
        :type ethertype: list[str]
        """
        self._ethertype = ethertype

    @property
    def remote_address_group_id(self):
        r"""Gets the remote_address_group_id of this ListSecurityGroupRulesRequest.

        功能说明：远端IP地址组ID，支持多ID过滤。

        :return: The remote_address_group_id of this ListSecurityGroupRulesRequest.
        :rtype: list[str]
        """
        return self._remote_address_group_id

    @remote_address_group_id.setter
    def remote_address_group_id(self, remote_address_group_id):
        r"""Sets the remote_address_group_id of this ListSecurityGroupRulesRequest.

        功能说明：远端IP地址组ID，支持多ID过滤。

        :param remote_address_group_id: The remote_address_group_id of this ListSecurityGroupRulesRequest.
        :type remote_address_group_id: list[str]
        """
        self._remote_address_group_id = remote_address_group_id

    @property
    def enabled(self):
        r"""Gets the enabled of this ListSecurityGroupRulesRequest.

        功能说明：是否启用安全组规则，不支持多值过滤。 取值范围：true, false。

        :return: The enabled of this ListSecurityGroupRulesRequest.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ListSecurityGroupRulesRequest.

        功能说明：是否启用安全组规则，不支持多值过滤。 取值范围：true, false。

        :param enabled: The enabled of this ListSecurityGroupRulesRequest.
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
        if not isinstance(other, ListSecurityGroupRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
