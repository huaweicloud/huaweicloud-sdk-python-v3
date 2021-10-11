# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VpcCreate:


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
        'type': 'int',
        'port': 'int',
        'balance_strategy': 'int',
        'member_type': 'str',
        'members': 'list[MemberInfo]',
        'vpc_health_config': 'VpcHealthConfig'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'port': 'port',
        'balance_strategy': 'balance_strategy',
        'member_type': 'member_type',
        'members': 'members',
        'vpc_health_config': 'vpc_health_config'
    }

    def __init__(self, name=None, type=None, port=None, balance_strategy=None, member_type=None, members=None, vpc_health_config=None):
        """VpcCreate - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._type = None
        self._port = None
        self._balance_strategy = None
        self._member_type = None
        self._members = None
        self._vpc_health_config = None
        self.discriminator = None

        self.name = name
        self.type = type
        if port is not None:
            self.port = port
        if balance_strategy is not None:
            self.balance_strategy = balance_strategy
        if member_type is not None:
            self.member_type = member_type
        if members is not None:
            self.members = members
        if vpc_health_config is not None:
            self.vpc_health_config = vpc_health_config

    @property
    def name(self):
        """Gets the name of this VpcCreate.

        VPC通道的名称。  长度为3 ~ 64位的字符串，字符串由中文、英文字母、数字、中划线、下划线组成，且只能以英文或中文开头。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The name of this VpcCreate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VpcCreate.

        VPC通道的名称。  长度为3 ~ 64位的字符串，字符串由中文、英文字母、数字、中划线、下划线组成，且只能以英文或中文开头。 > 中文字符必须为UTF-8或者unicode编码。

        :param name: The name of this VpcCreate.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this VpcCreate.

        VPC通道的类型。 - 1：私网ELB通道（待废弃） - 2：API网关内置支持负载均衡功能的快速通道类型

        :return: The type of this VpcCreate.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VpcCreate.

        VPC通道的类型。 - 1：私网ELB通道（待废弃） - 2：API网关内置支持负载均衡功能的快速通道类型

        :param type: The type of this VpcCreate.
        :type: int
        """
        self._type = type

    @property
    def port(self):
        """Gets the port of this VpcCreate.

        VPC通道中主机的端口号。  取值范围1 ~ 65535，仅VPC通道类型为2时有效。  VPC通道类型为2时必选。

        :return: The port of this VpcCreate.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this VpcCreate.

        VPC通道中主机的端口号。  取值范围1 ~ 65535，仅VPC通道类型为2时有效。  VPC通道类型为2时必选。

        :param port: The port of this VpcCreate.
        :type: int
        """
        self._port = port

    @property
    def balance_strategy(self):
        """Gets the balance_strategy of this VpcCreate.

        分发算法。 - 1：加权轮询（wrr） - 2：加权最少连接（wleastconn） - 3：源地址哈希（source） - 4：URI哈希（uri）  VPC通道类型为2时必选。

        :return: The balance_strategy of this VpcCreate.
        :rtype: int
        """
        return self._balance_strategy

    @balance_strategy.setter
    def balance_strategy(self, balance_strategy):
        """Sets the balance_strategy of this VpcCreate.

        分发算法。 - 1：加权轮询（wrr） - 2：加权最少连接（wleastconn） - 3：源地址哈希（source） - 4：URI哈希（uri）  VPC通道类型为2时必选。

        :param balance_strategy: The balance_strategy of this VpcCreate.
        :type: int
        """
        self._balance_strategy = balance_strategy

    @property
    def member_type(self):
        """Gets the member_type of this VpcCreate.

        VPC通道的成员类型。 - ip - ecs  VPC通道类型为2时必选。

        :return: The member_type of this VpcCreate.
        :rtype: str
        """
        return self._member_type

    @member_type.setter
    def member_type(self, member_type):
        """Sets the member_type of this VpcCreate.

        VPC通道的成员类型。 - ip - ecs  VPC通道类型为2时必选。

        :param member_type: The member_type of this VpcCreate.
        :type: str
        """
        self._member_type = member_type

    @property
    def members(self):
        """Gets the members of this VpcCreate.

        VPC后端实例列表，VPC通道类型为1时，有且仅有1个后端实例。

        :return: The members of this VpcCreate.
        :rtype: list[MemberInfo]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this VpcCreate.

        VPC后端实例列表，VPC通道类型为1时，有且仅有1个后端实例。

        :param members: The members of this VpcCreate.
        :type: list[MemberInfo]
        """
        self._members = members

    @property
    def vpc_health_config(self):
        """Gets the vpc_health_config of this VpcCreate.


        :return: The vpc_health_config of this VpcCreate.
        :rtype: VpcHealthConfig
        """
        return self._vpc_health_config

    @vpc_health_config.setter
    def vpc_health_config(self, vpc_health_config):
        """Sets the vpc_health_config of this VpcCreate.


        :param vpc_health_config: The vpc_health_config of this VpcCreate.
        :type: VpcHealthConfig
        """
        self._vpc_health_config = vpc_health_config

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
        if not isinstance(other, VpcCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
