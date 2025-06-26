# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Restore:

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
        'subnet_id': 'str',
        'security_group_id': 'str',
        'vpc_id': 'str',
        'availability_zone': 'str',
        'port': 'int',
        'public_ip': 'PublicIp',
        'enterprise_project_id': 'str',
        'ipv6_enable': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'vpc_id': 'vpc_id',
        'availability_zone': 'availability_zone',
        'port': 'port',
        'public_ip': 'public_ip',
        'enterprise_project_id': 'enterprise_project_id',
        'ipv6_enable': 'ipv6_enable'
    }

    def __init__(self, name=None, subnet_id=None, security_group_id=None, vpc_id=None, availability_zone=None, port=None, public_ip=None, enterprise_project_id=None, ipv6_enable=None):
        r"""Restore

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 集群名称。 **取值范围**： 要求唯一性，必须以字母开头并只包含字母、数字、中划线，下划线，长度为4~64个字符。
        :type name: str
        :param subnet_id: **参数解释**： 指定子网ID，用于集群网络配置。 **取值范围**： 默认值与原集群相同。
        :type subnet_id: str
        :param security_group_id: **参数解释**： 指定安全组ID，用于集群网络配置。默认值与原集群相同。 **取值范围**： 不涉及。
        :type security_group_id: str
        :param vpc_id: **参数解释**： 指定虚拟私有云ID，用于集群网络配置。默认值与原集群相同。 **取值范围**： 不涉及。
        :type vpc_id: str
        :param availability_zone: **参数解释**： 指定集群可用区。默认值与原集群相同。 **取值范围**： 不涉及。
        :type availability_zone: str
        :param port: **参数解释**： 指定集群服务端口。 **取值范围**： 不涉及。
        :type port: int
        :param public_ip: 
        :type public_ip: :class:`huaweicloudsdkdws.v2.PublicIp`
        :param enterprise_project_id: **参数解释**： 企业项目ID，对集群指定企业项目。如果未指定，则使用默认企业项目“default”的ID，即0。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 0
        :type enterprise_project_id: str
        :param ipv6_enable: **参数解释**： 指定网络协议类型，表明是否支持IPv6，默认不使用IPv6。 **取值范围**： 不涉及。
        :type ipv6_enable: bool
        """
        
        

        self._name = None
        self._subnet_id = None
        self._security_group_id = None
        self._vpc_id = None
        self._availability_zone = None
        self._port = None
        self._public_ip = None
        self._enterprise_project_id = None
        self._ipv6_enable = None
        self.discriminator = None

        self.name = name
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if port is not None:
            self.port = port
        if public_ip is not None:
            self.public_ip = public_ip
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable

    @property
    def name(self):
        r"""Gets the name of this Restore.

        **参数解释**： 集群名称。 **取值范围**： 要求唯一性，必须以字母开头并只包含字母、数字、中划线，下划线，长度为4~64个字符。

        :return: The name of this Restore.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Restore.

        **参数解释**： 集群名称。 **取值范围**： 要求唯一性，必须以字母开头并只包含字母、数字、中划线，下划线，长度为4~64个字符。

        :param name: The name of this Restore.
        :type name: str
        """
        self._name = name

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this Restore.

        **参数解释**： 指定子网ID，用于集群网络配置。 **取值范围**： 默认值与原集群相同。

        :return: The subnet_id of this Restore.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this Restore.

        **参数解释**： 指定子网ID，用于集群网络配置。 **取值范围**： 默认值与原集群相同。

        :param subnet_id: The subnet_id of this Restore.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this Restore.

        **参数解释**： 指定安全组ID，用于集群网络配置。默认值与原集群相同。 **取值范围**： 不涉及。

        :return: The security_group_id of this Restore.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this Restore.

        **参数解释**： 指定安全组ID，用于集群网络配置。默认值与原集群相同。 **取值范围**： 不涉及。

        :param security_group_id: The security_group_id of this Restore.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this Restore.

        **参数解释**： 指定虚拟私有云ID，用于集群网络配置。默认值与原集群相同。 **取值范围**： 不涉及。

        :return: The vpc_id of this Restore.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this Restore.

        **参数解释**： 指定虚拟私有云ID，用于集群网络配置。默认值与原集群相同。 **取值范围**： 不涉及。

        :param vpc_id: The vpc_id of this Restore.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this Restore.

        **参数解释**： 指定集群可用区。默认值与原集群相同。 **取值范围**： 不涉及。

        :return: The availability_zone of this Restore.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this Restore.

        **参数解释**： 指定集群可用区。默认值与原集群相同。 **取值范围**： 不涉及。

        :param availability_zone: The availability_zone of this Restore.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def port(self):
        r"""Gets the port of this Restore.

        **参数解释**： 指定集群服务端口。 **取值范围**： 不涉及。

        :return: The port of this Restore.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this Restore.

        **参数解释**： 指定集群服务端口。 **取值范围**： 不涉及。

        :param port: The port of this Restore.
        :type port: int
        """
        self._port = port

    @property
    def public_ip(self):
        r"""Gets the public_ip of this Restore.

        :return: The public_ip of this Restore.
        :rtype: :class:`huaweicloudsdkdws.v2.PublicIp`
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this Restore.

        :param public_ip: The public_ip of this Restore.
        :type public_ip: :class:`huaweicloudsdkdws.v2.PublicIp`
        """
        self._public_ip = public_ip

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this Restore.

        **参数解释**： 企业项目ID，对集群指定企业项目。如果未指定，则使用默认企业项目“default”的ID，即0。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 0

        :return: The enterprise_project_id of this Restore.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this Restore.

        **参数解释**： 企业项目ID，对集群指定企业项目。如果未指定，则使用默认企业项目“default”的ID，即0。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 0

        :param enterprise_project_id: The enterprise_project_id of this Restore.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def ipv6_enable(self):
        r"""Gets the ipv6_enable of this Restore.

        **参数解释**： 指定网络协议类型，表明是否支持IPv6，默认不使用IPv6。 **取值范围**： 不涉及。

        :return: The ipv6_enable of this Restore.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        r"""Sets the ipv6_enable of this Restore.

        **参数解释**： 指定网络协议类型，表明是否支持IPv6，默认不使用IPv6。 **取值范围**： 不涉及。

        :param ipv6_enable: The ipv6_enable of this Restore.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

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
        if not isinstance(other, Restore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
