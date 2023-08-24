# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FirewallInsertRuleItemOption:

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
        'action': 'str',
        'protocol': 'str',
        'ip_version': 'int',
        'source_ip_address': 'str',
        'destination_ip_address': 'str',
        'source_port': 'str',
        'destination_port': 'str',
        'source_address_group_id': 'str',
        'destination_address_group_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'action': 'action',
        'protocol': 'protocol',
        'ip_version': 'ip_version',
        'source_ip_address': 'source_ip_address',
        'destination_ip_address': 'destination_ip_address',
        'source_port': 'source_port',
        'destination_port': 'destination_port',
        'source_address_group_id': 'source_address_group_id',
        'destination_address_group_id': 'destination_address_group_id'
    }

    def __init__(self, name=None, description=None, action=None, protocol=None, ip_version=None, source_ip_address=None, destination_ip_address=None, source_port=None, destination_port=None, source_address_group_id=None, destination_address_group_id=None):
        """FirewallInsertRuleItemOption

        The model defined in huaweicloud sdk

        :param name: 功能说明：ACL规则名称 取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param description: 功能说明：ACL规则描述信息 取值范围：0-255个字符 约束：不能包含“&lt;”和“&gt;”。
        :type description: str
        :param action: 功能说明：ACL规则对流量执行的操作放通或拒绝 取值范围：allow放通；deny拒绝
        :type action: str
        :param protocol: 功能说明：ACL规则协议 取值范围：支持tcp,udp,icmp,icmpv6或者协议号（0-255），any表示全部协议
        :type protocol: str
        :param ip_version: 功能说明：ACL规则的ip版本 取值范围：4, 表示ipv4；6, 表示ipv6
        :type ip_version: int
        :param source_ip_address: 功能说明：ACL规则源IP地址或者CIDR 约束：source_ip_address和source_address_group_id不能同时设置
        :type source_ip_address: str
        :param destination_ip_address: 功能说明：ACL规则目的IP地址或者CIDR 约束：destination_ip_address和destination_address_group_id不能同时设置
        :type destination_ip_address: str
        :param source_port: 功能说明：ACL规则的源端口 取值范围：支持端口号，一段端口范围，多个以逗号分隔 约束：支持的端口组的数量默认为20
        :type source_port: str
        :param destination_port: 功能说明：ACL规则的目的端口 取值范围：支持端口号，一段端口范围，多个以逗号分隔 约束：支持的端口组的数量默认为20
        :type destination_port: str
        :param source_address_group_id: 功能说明：ACL规则的源地址组ID 约束：source_ip_address和source_address_group_id不能同时设置
        :type source_address_group_id: str
        :param destination_address_group_id: 功能说明：ACL规则的目的地址组ID 约束：destination_ip_address和destination_address_group_id不能同时设置
        :type destination_address_group_id: str
        """
        
        

        self._name = None
        self._description = None
        self._action = None
        self._protocol = None
        self._ip_version = None
        self._source_ip_address = None
        self._destination_ip_address = None
        self._source_port = None
        self._destination_port = None
        self._source_address_group_id = None
        self._destination_address_group_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        self.action = action
        self.protocol = protocol
        self.ip_version = ip_version
        if source_ip_address is not None:
            self.source_ip_address = source_ip_address
        if destination_ip_address is not None:
            self.destination_ip_address = destination_ip_address
        if source_port is not None:
            self.source_port = source_port
        if destination_port is not None:
            self.destination_port = destination_port
        if source_address_group_id is not None:
            self.source_address_group_id = source_address_group_id
        if destination_address_group_id is not None:
            self.destination_address_group_id = destination_address_group_id

    @property
    def name(self):
        """Gets the name of this FirewallInsertRuleItemOption.

        功能说明：ACL规则名称 取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this FirewallInsertRuleItemOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FirewallInsertRuleItemOption.

        功能说明：ACL规则名称 取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this FirewallInsertRuleItemOption.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this FirewallInsertRuleItemOption.

        功能说明：ACL规则描述信息 取值范围：0-255个字符 约束：不能包含“<”和“>”。

        :return: The description of this FirewallInsertRuleItemOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FirewallInsertRuleItemOption.

        功能说明：ACL规则描述信息 取值范围：0-255个字符 约束：不能包含“<”和“>”。

        :param description: The description of this FirewallInsertRuleItemOption.
        :type description: str
        """
        self._description = description

    @property
    def action(self):
        """Gets the action of this FirewallInsertRuleItemOption.

        功能说明：ACL规则对流量执行的操作放通或拒绝 取值范围：allow放通；deny拒绝

        :return: The action of this FirewallInsertRuleItemOption.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this FirewallInsertRuleItemOption.

        功能说明：ACL规则对流量执行的操作放通或拒绝 取值范围：allow放通；deny拒绝

        :param action: The action of this FirewallInsertRuleItemOption.
        :type action: str
        """
        self._action = action

    @property
    def protocol(self):
        """Gets the protocol of this FirewallInsertRuleItemOption.

        功能说明：ACL规则协议 取值范围：支持tcp,udp,icmp,icmpv6或者协议号（0-255），any表示全部协议

        :return: The protocol of this FirewallInsertRuleItemOption.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this FirewallInsertRuleItemOption.

        功能说明：ACL规则协议 取值范围：支持tcp,udp,icmp,icmpv6或者协议号（0-255），any表示全部协议

        :param protocol: The protocol of this FirewallInsertRuleItemOption.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def ip_version(self):
        """Gets the ip_version of this FirewallInsertRuleItemOption.

        功能说明：ACL规则的ip版本 取值范围：4, 表示ipv4；6, 表示ipv6

        :return: The ip_version of this FirewallInsertRuleItemOption.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this FirewallInsertRuleItemOption.

        功能说明：ACL规则的ip版本 取值范围：4, 表示ipv4；6, 表示ipv6

        :param ip_version: The ip_version of this FirewallInsertRuleItemOption.
        :type ip_version: int
        """
        self._ip_version = ip_version

    @property
    def source_ip_address(self):
        """Gets the source_ip_address of this FirewallInsertRuleItemOption.

        功能说明：ACL规则源IP地址或者CIDR 约束：source_ip_address和source_address_group_id不能同时设置

        :return: The source_ip_address of this FirewallInsertRuleItemOption.
        :rtype: str
        """
        return self._source_ip_address

    @source_ip_address.setter
    def source_ip_address(self, source_ip_address):
        """Sets the source_ip_address of this FirewallInsertRuleItemOption.

        功能说明：ACL规则源IP地址或者CIDR 约束：source_ip_address和source_address_group_id不能同时设置

        :param source_ip_address: The source_ip_address of this FirewallInsertRuleItemOption.
        :type source_ip_address: str
        """
        self._source_ip_address = source_ip_address

    @property
    def destination_ip_address(self):
        """Gets the destination_ip_address of this FirewallInsertRuleItemOption.

        功能说明：ACL规则目的IP地址或者CIDR 约束：destination_ip_address和destination_address_group_id不能同时设置

        :return: The destination_ip_address of this FirewallInsertRuleItemOption.
        :rtype: str
        """
        return self._destination_ip_address

    @destination_ip_address.setter
    def destination_ip_address(self, destination_ip_address):
        """Sets the destination_ip_address of this FirewallInsertRuleItemOption.

        功能说明：ACL规则目的IP地址或者CIDR 约束：destination_ip_address和destination_address_group_id不能同时设置

        :param destination_ip_address: The destination_ip_address of this FirewallInsertRuleItemOption.
        :type destination_ip_address: str
        """
        self._destination_ip_address = destination_ip_address

    @property
    def source_port(self):
        """Gets the source_port of this FirewallInsertRuleItemOption.

        功能说明：ACL规则的源端口 取值范围：支持端口号，一段端口范围，多个以逗号分隔 约束：支持的端口组的数量默认为20

        :return: The source_port of this FirewallInsertRuleItemOption.
        :rtype: str
        """
        return self._source_port

    @source_port.setter
    def source_port(self, source_port):
        """Sets the source_port of this FirewallInsertRuleItemOption.

        功能说明：ACL规则的源端口 取值范围：支持端口号，一段端口范围，多个以逗号分隔 约束：支持的端口组的数量默认为20

        :param source_port: The source_port of this FirewallInsertRuleItemOption.
        :type source_port: str
        """
        self._source_port = source_port

    @property
    def destination_port(self):
        """Gets the destination_port of this FirewallInsertRuleItemOption.

        功能说明：ACL规则的目的端口 取值范围：支持端口号，一段端口范围，多个以逗号分隔 约束：支持的端口组的数量默认为20

        :return: The destination_port of this FirewallInsertRuleItemOption.
        :rtype: str
        """
        return self._destination_port

    @destination_port.setter
    def destination_port(self, destination_port):
        """Sets the destination_port of this FirewallInsertRuleItemOption.

        功能说明：ACL规则的目的端口 取值范围：支持端口号，一段端口范围，多个以逗号分隔 约束：支持的端口组的数量默认为20

        :param destination_port: The destination_port of this FirewallInsertRuleItemOption.
        :type destination_port: str
        """
        self._destination_port = destination_port

    @property
    def source_address_group_id(self):
        """Gets the source_address_group_id of this FirewallInsertRuleItemOption.

        功能说明：ACL规则的源地址组ID 约束：source_ip_address和source_address_group_id不能同时设置

        :return: The source_address_group_id of this FirewallInsertRuleItemOption.
        :rtype: str
        """
        return self._source_address_group_id

    @source_address_group_id.setter
    def source_address_group_id(self, source_address_group_id):
        """Sets the source_address_group_id of this FirewallInsertRuleItemOption.

        功能说明：ACL规则的源地址组ID 约束：source_ip_address和source_address_group_id不能同时设置

        :param source_address_group_id: The source_address_group_id of this FirewallInsertRuleItemOption.
        :type source_address_group_id: str
        """
        self._source_address_group_id = source_address_group_id

    @property
    def destination_address_group_id(self):
        """Gets the destination_address_group_id of this FirewallInsertRuleItemOption.

        功能说明：ACL规则的目的地址组ID 约束：destination_ip_address和destination_address_group_id不能同时设置

        :return: The destination_address_group_id of this FirewallInsertRuleItemOption.
        :rtype: str
        """
        return self._destination_address_group_id

    @destination_address_group_id.setter
    def destination_address_group_id(self, destination_address_group_id):
        """Sets the destination_address_group_id of this FirewallInsertRuleItemOption.

        功能说明：ACL规则的目的地址组ID 约束：destination_ip_address和destination_address_group_id不能同时设置

        :param destination_address_group_id: The destination_address_group_id of this FirewallInsertRuleItemOption.
        :type destination_address_group_id: str
        """
        self._destination_address_group_id = destination_address_group_id

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
        if not isinstance(other, FirewallInsertRuleItemOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
