# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FirewallRuleDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'action': 'str',
        'project_id': 'str',
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
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'action': 'action',
        'project_id': 'project_id',
        'protocol': 'protocol',
        'ip_version': 'ip_version',
        'source_ip_address': 'source_ip_address',
        'destination_ip_address': 'destination_ip_address',
        'source_port': 'source_port',
        'destination_port': 'destination_port',
        'source_address_group_id': 'source_address_group_id',
        'destination_address_group_id': 'destination_address_group_id'
    }

    def __init__(self, id=None, name=None, description=None, action=None, project_id=None, protocol=None, ip_version=None, source_ip_address=None, destination_ip_address=None, source_port=None, destination_port=None, source_address_group_id=None, destination_address_group_id=None):
        """FirewallRuleDetail

        The model defined in huaweicloud sdk

        :param id: 功能说明：ACL规则唯一标识 取值范围：合法UUID的字符串
        :type id: str
        :param name: 功能说明：ACL规则名称 取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param description: 功能说明：ACL规则描述信息 取值范围：0-255个字符 约束：不能包含“&lt;”和“&gt;”。
        :type description: str
        :param action: 功能说明：ACL规则对流量执行的操作放通或拒绝 取值范围：allow放通；deny拒绝
        :type action: str
        :param project_id: 功能说明：资源所属项目ID
        :type project_id: str
        :param protocol: 功能说明：ACL规则协议 取值范围：支持TCP,UDP,ICMP, ICMPV6或者IP协议号（0-255）
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
        
        

        self._id = None
        self._name = None
        self._description = None
        self._action = None
        self._project_id = None
        self._protocol = None
        self._ip_version = None
        self._source_ip_address = None
        self._destination_ip_address = None
        self._source_port = None
        self._destination_port = None
        self._source_address_group_id = None
        self._destination_address_group_id = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        self.action = action
        self.project_id = project_id
        self.protocol = protocol
        self.ip_version = ip_version
        self.source_ip_address = source_ip_address
        self.destination_ip_address = destination_ip_address
        self.source_port = source_port
        self.destination_port = destination_port
        self.source_address_group_id = source_address_group_id
        self.destination_address_group_id = destination_address_group_id

    @property
    def id(self):
        """Gets the id of this FirewallRuleDetail.

        功能说明：ACL规则唯一标识 取值范围：合法UUID的字符串

        :return: The id of this FirewallRuleDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FirewallRuleDetail.

        功能说明：ACL规则唯一标识 取值范围：合法UUID的字符串

        :param id: The id of this FirewallRuleDetail.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this FirewallRuleDetail.

        功能说明：ACL规则名称 取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this FirewallRuleDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FirewallRuleDetail.

        功能说明：ACL规则名称 取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this FirewallRuleDetail.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this FirewallRuleDetail.

        功能说明：ACL规则描述信息 取值范围：0-255个字符 约束：不能包含“<”和“>”。

        :return: The description of this FirewallRuleDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FirewallRuleDetail.

        功能说明：ACL规则描述信息 取值范围：0-255个字符 约束：不能包含“<”和“>”。

        :param description: The description of this FirewallRuleDetail.
        :type description: str
        """
        self._description = description

    @property
    def action(self):
        """Gets the action of this FirewallRuleDetail.

        功能说明：ACL规则对流量执行的操作放通或拒绝 取值范围：allow放通；deny拒绝

        :return: The action of this FirewallRuleDetail.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this FirewallRuleDetail.

        功能说明：ACL规则对流量执行的操作放通或拒绝 取值范围：allow放通；deny拒绝

        :param action: The action of this FirewallRuleDetail.
        :type action: str
        """
        self._action = action

    @property
    def project_id(self):
        """Gets the project_id of this FirewallRuleDetail.

        功能说明：资源所属项目ID

        :return: The project_id of this FirewallRuleDetail.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this FirewallRuleDetail.

        功能说明：资源所属项目ID

        :param project_id: The project_id of this FirewallRuleDetail.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def protocol(self):
        """Gets the protocol of this FirewallRuleDetail.

        功能说明：ACL规则协议 取值范围：支持TCP,UDP,ICMP, ICMPV6或者IP协议号（0-255）

        :return: The protocol of this FirewallRuleDetail.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this FirewallRuleDetail.

        功能说明：ACL规则协议 取值范围：支持TCP,UDP,ICMP, ICMPV6或者IP协议号（0-255）

        :param protocol: The protocol of this FirewallRuleDetail.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def ip_version(self):
        """Gets the ip_version of this FirewallRuleDetail.

        功能说明：ACL规则的ip版本 取值范围：4, 表示ipv4；6, 表示ipv6

        :return: The ip_version of this FirewallRuleDetail.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this FirewallRuleDetail.

        功能说明：ACL规则的ip版本 取值范围：4, 表示ipv4；6, 表示ipv6

        :param ip_version: The ip_version of this FirewallRuleDetail.
        :type ip_version: int
        """
        self._ip_version = ip_version

    @property
    def source_ip_address(self):
        """Gets the source_ip_address of this FirewallRuleDetail.

        功能说明：ACL规则源IP地址或者CIDR 约束：source_ip_address和source_address_group_id不能同时设置

        :return: The source_ip_address of this FirewallRuleDetail.
        :rtype: str
        """
        return self._source_ip_address

    @source_ip_address.setter
    def source_ip_address(self, source_ip_address):
        """Sets the source_ip_address of this FirewallRuleDetail.

        功能说明：ACL规则源IP地址或者CIDR 约束：source_ip_address和source_address_group_id不能同时设置

        :param source_ip_address: The source_ip_address of this FirewallRuleDetail.
        :type source_ip_address: str
        """
        self._source_ip_address = source_ip_address

    @property
    def destination_ip_address(self):
        """Gets the destination_ip_address of this FirewallRuleDetail.

        功能说明：ACL规则目的IP地址或者CIDR 约束：destination_ip_address和destination_address_group_id不能同时设置

        :return: The destination_ip_address of this FirewallRuleDetail.
        :rtype: str
        """
        return self._destination_ip_address

    @destination_ip_address.setter
    def destination_ip_address(self, destination_ip_address):
        """Sets the destination_ip_address of this FirewallRuleDetail.

        功能说明：ACL规则目的IP地址或者CIDR 约束：destination_ip_address和destination_address_group_id不能同时设置

        :param destination_ip_address: The destination_ip_address of this FirewallRuleDetail.
        :type destination_ip_address: str
        """
        self._destination_ip_address = destination_ip_address

    @property
    def source_port(self):
        """Gets the source_port of this FirewallRuleDetail.

        功能说明：ACL规则的源端口 取值范围：支持端口号，一段端口范围，多个以逗号分隔 约束：支持的端口组的数量默认为20

        :return: The source_port of this FirewallRuleDetail.
        :rtype: str
        """
        return self._source_port

    @source_port.setter
    def source_port(self, source_port):
        """Sets the source_port of this FirewallRuleDetail.

        功能说明：ACL规则的源端口 取值范围：支持端口号，一段端口范围，多个以逗号分隔 约束：支持的端口组的数量默认为20

        :param source_port: The source_port of this FirewallRuleDetail.
        :type source_port: str
        """
        self._source_port = source_port

    @property
    def destination_port(self):
        """Gets the destination_port of this FirewallRuleDetail.

        功能说明：ACL规则的目的端口 取值范围：支持端口号，一段端口范围，多个以逗号分隔 约束：支持的端口组的数量默认为20

        :return: The destination_port of this FirewallRuleDetail.
        :rtype: str
        """
        return self._destination_port

    @destination_port.setter
    def destination_port(self, destination_port):
        """Sets the destination_port of this FirewallRuleDetail.

        功能说明：ACL规则的目的端口 取值范围：支持端口号，一段端口范围，多个以逗号分隔 约束：支持的端口组的数量默认为20

        :param destination_port: The destination_port of this FirewallRuleDetail.
        :type destination_port: str
        """
        self._destination_port = destination_port

    @property
    def source_address_group_id(self):
        """Gets the source_address_group_id of this FirewallRuleDetail.

        功能说明：ACL规则的源地址组ID 约束：source_ip_address和source_address_group_id不能同时设置

        :return: The source_address_group_id of this FirewallRuleDetail.
        :rtype: str
        """
        return self._source_address_group_id

    @source_address_group_id.setter
    def source_address_group_id(self, source_address_group_id):
        """Sets the source_address_group_id of this FirewallRuleDetail.

        功能说明：ACL规则的源地址组ID 约束：source_ip_address和source_address_group_id不能同时设置

        :param source_address_group_id: The source_address_group_id of this FirewallRuleDetail.
        :type source_address_group_id: str
        """
        self._source_address_group_id = source_address_group_id

    @property
    def destination_address_group_id(self):
        """Gets the destination_address_group_id of this FirewallRuleDetail.

        功能说明：ACL规则的目的地址组ID 约束：destination_ip_address和destination_address_group_id不能同时设置

        :return: The destination_address_group_id of this FirewallRuleDetail.
        :rtype: str
        """
        return self._destination_address_group_id

    @destination_address_group_id.setter
    def destination_address_group_id(self, destination_address_group_id):
        """Sets the destination_address_group_id of this FirewallRuleDetail.

        功能说明：ACL规则的目的地址组ID 约束：destination_ip_address和destination_address_group_id不能同时设置

        :param destination_address_group_id: The destination_address_group_id of this FirewallRuleDetail.
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
        if not isinstance(other, FirewallRuleDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
