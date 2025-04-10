# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FirewallRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'description': 'str',
        'destination_ip_address': 'str',
        'destination_port': 'str',
        'enabled': 'bool',
        'id': 'str',
        'ip_version': 'int',
        'name': 'str',
        'operate_type': 'str',
        'protocol': 'str',
        'source_ip_address': 'str',
        'source_port': 'str'
    }

    attribute_map = {
        'action': 'action',
        'description': 'description',
        'destination_ip_address': 'destination_ip_address',
        'destination_port': 'destination_port',
        'enabled': 'enabled',
        'id': 'id',
        'ip_version': 'ip_version',
        'name': 'name',
        'operate_type': 'operate_type',
        'protocol': 'protocol',
        'source_ip_address': 'source_ip_address',
        'source_port': 'source_port'
    }

    def __init__(self, action=None, description=None, destination_ip_address=None, destination_port=None, enabled=None, id=None, ip_version=None, name=None, operate_type=None, protocol=None, source_ip_address=None, source_port=None):
        r"""FirewallRule

        The model defined in huaweicloud sdk

        :param action: 策略是否允许  取值范围：allow，deny，reject
        :type action: str
        :param description: 网络ACL规则描述。
        :type description: str
        :param destination_ip_address: 目的地IP地址，IPv4或IPv6的CIDR格式
        :type destination_ip_address: str
        :param destination_port: 目的地端口范围  取值范围：整数，比如80，或者以\&quot;-\&quot;隔开的范围，比如80-90
        :type destination_port: str
        :param enabled: 网络ACL规则使能开关。  取值范围：true，false
        :type enabled: bool
        :param id: 网络ACL规则ID。  进行更新规则时，如果operate_type为add，则该值为空。
        :type id: str
        :param ip_version: IP协议版本  取值范围：4、6
        :type ip_version: int
        :param name: 网络ACL规则名称。
        :type name: str
        :param operate_type: 网络ACL规则操作状态，作为请求时取值为\&quot;add\&quot;/\&quot;modify\&quot;/\&quot;delete\&quot;，作为返回值时为\&quot;normal\&quot;。 当请求更新规则时，本参数值为delete时，除id之外，本请求体其他参数均可为空。
        :type operate_type: str
        :param protocol: IP协议，为any时代表所有协议  取值范围：icmp，tcp，udp，[icmpv6，](tag:hide)any 
        :type protocol: str
        :param source_ip_address: 源IP地址，IPv4或IPv6的CIDR格式
        :type source_ip_address: str
        :param source_port: 源地端口范围  取值范围：整数，比如80，或者以\&quot;-\&quot;隔开的范围，比如80-90
        :type source_port: str
        """
        
        

        self._action = None
        self._description = None
        self._destination_ip_address = None
        self._destination_port = None
        self._enabled = None
        self._id = None
        self._ip_version = None
        self._name = None
        self._operate_type = None
        self._protocol = None
        self._source_ip_address = None
        self._source_port = None
        self.discriminator = None

        self.action = action
        if description is not None:
            self.description = description
        self.destination_ip_address = destination_ip_address
        self.destination_port = destination_port
        self.enabled = enabled
        self.id = id
        self.ip_version = ip_version
        self.name = name
        self.operate_type = operate_type
        self.protocol = protocol
        self.source_ip_address = source_ip_address
        self.source_port = source_port

    @property
    def action(self):
        r"""Gets the action of this FirewallRule.

        策略是否允许  取值范围：allow，deny，reject

        :return: The action of this FirewallRule.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this FirewallRule.

        策略是否允许  取值范围：allow，deny，reject

        :param action: The action of this FirewallRule.
        :type action: str
        """
        self._action = action

    @property
    def description(self):
        r"""Gets the description of this FirewallRule.

        网络ACL规则描述。

        :return: The description of this FirewallRule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this FirewallRule.

        网络ACL规则描述。

        :param description: The description of this FirewallRule.
        :type description: str
        """
        self._description = description

    @property
    def destination_ip_address(self):
        r"""Gets the destination_ip_address of this FirewallRule.

        目的地IP地址，IPv4或IPv6的CIDR格式

        :return: The destination_ip_address of this FirewallRule.
        :rtype: str
        """
        return self._destination_ip_address

    @destination_ip_address.setter
    def destination_ip_address(self, destination_ip_address):
        r"""Sets the destination_ip_address of this FirewallRule.

        目的地IP地址，IPv4或IPv6的CIDR格式

        :param destination_ip_address: The destination_ip_address of this FirewallRule.
        :type destination_ip_address: str
        """
        self._destination_ip_address = destination_ip_address

    @property
    def destination_port(self):
        r"""Gets the destination_port of this FirewallRule.

        目的地端口范围  取值范围：整数，比如80，或者以\"-\"隔开的范围，比如80-90

        :return: The destination_port of this FirewallRule.
        :rtype: str
        """
        return self._destination_port

    @destination_port.setter
    def destination_port(self, destination_port):
        r"""Sets the destination_port of this FirewallRule.

        目的地端口范围  取值范围：整数，比如80，或者以\"-\"隔开的范围，比如80-90

        :param destination_port: The destination_port of this FirewallRule.
        :type destination_port: str
        """
        self._destination_port = destination_port

    @property
    def enabled(self):
        r"""Gets the enabled of this FirewallRule.

        网络ACL规则使能开关。  取值范围：true，false

        :return: The enabled of this FirewallRule.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this FirewallRule.

        网络ACL规则使能开关。  取值范围：true，false

        :param enabled: The enabled of this FirewallRule.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def id(self):
        r"""Gets the id of this FirewallRule.

        网络ACL规则ID。  进行更新规则时，如果operate_type为add，则该值为空。

        :return: The id of this FirewallRule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this FirewallRule.

        网络ACL规则ID。  进行更新规则时，如果operate_type为add，则该值为空。

        :param id: The id of this FirewallRule.
        :type id: str
        """
        self._id = id

    @property
    def ip_version(self):
        r"""Gets the ip_version of this FirewallRule.

        IP协议版本  取值范围：4、6

        :return: The ip_version of this FirewallRule.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        r"""Sets the ip_version of this FirewallRule.

        IP协议版本  取值范围：4、6

        :param ip_version: The ip_version of this FirewallRule.
        :type ip_version: int
        """
        self._ip_version = ip_version

    @property
    def name(self):
        r"""Gets the name of this FirewallRule.

        网络ACL规则名称。

        :return: The name of this FirewallRule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this FirewallRule.

        网络ACL规则名称。

        :param name: The name of this FirewallRule.
        :type name: str
        """
        self._name = name

    @property
    def operate_type(self):
        r"""Gets the operate_type of this FirewallRule.

        网络ACL规则操作状态，作为请求时取值为\"add\"/\"modify\"/\"delete\"，作为返回值时为\"normal\"。 当请求更新规则时，本参数值为delete时，除id之外，本请求体其他参数均可为空。

        :return: The operate_type of this FirewallRule.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        r"""Sets the operate_type of this FirewallRule.

        网络ACL规则操作状态，作为请求时取值为\"add\"/\"modify\"/\"delete\"，作为返回值时为\"normal\"。 当请求更新规则时，本参数值为delete时，除id之外，本请求体其他参数均可为空。

        :param operate_type: The operate_type of this FirewallRule.
        :type operate_type: str
        """
        self._operate_type = operate_type

    @property
    def protocol(self):
        r"""Gets the protocol of this FirewallRule.

        IP协议，为any时代表所有协议  取值范围：icmp，tcp，udp，[icmpv6，](tag:hide)any 

        :return: The protocol of this FirewallRule.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this FirewallRule.

        IP协议，为any时代表所有协议  取值范围：icmp，tcp，udp，[icmpv6，](tag:hide)any 

        :param protocol: The protocol of this FirewallRule.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def source_ip_address(self):
        r"""Gets the source_ip_address of this FirewallRule.

        源IP地址，IPv4或IPv6的CIDR格式

        :return: The source_ip_address of this FirewallRule.
        :rtype: str
        """
        return self._source_ip_address

    @source_ip_address.setter
    def source_ip_address(self, source_ip_address):
        r"""Sets the source_ip_address of this FirewallRule.

        源IP地址，IPv4或IPv6的CIDR格式

        :param source_ip_address: The source_ip_address of this FirewallRule.
        :type source_ip_address: str
        """
        self._source_ip_address = source_ip_address

    @property
    def source_port(self):
        r"""Gets the source_port of this FirewallRule.

        源地端口范围  取值范围：整数，比如80，或者以\"-\"隔开的范围，比如80-90

        :return: The source_port of this FirewallRule.
        :rtype: str
        """
        return self._source_port

    @source_port.setter
    def source_port(self, source_port):
        r"""Sets the source_port of this FirewallRule.

        源地端口范围  取值范围：整数，比如80，或者以\"-\"隔开的范围，比如80-90

        :param source_port: The source_port of this FirewallRule.
        :type source_port: str
        """
        self._source_port = source_port

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
        if not isinstance(other, FirewallRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
