# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClouddcnSubnetOption:

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
        'cidr': 'str',
        'vpc_id': 'str',
        'gateway_ip': 'str',
        'dns_nameservers': 'list[str]',
        'availability_zone': 'str',
        'tags': 'list[TagEntity]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'cidr': 'cidr',
        'vpc_id': 'vpc_id',
        'gateway_ip': 'gateway_ip',
        'dns_nameservers': 'dns_nameservers',
        'availability_zone': 'availability_zone',
        'tags': 'tags'
    }

    def __init__(self, name=None, description=None, cidr=None, vpc_id=None, gateway_ip=None, dns_nameservers=None, availability_zone=None, tags=None):
        """CreateClouddcnSubnetOption

        The model defined in huaweicloud sdk

        :param name: 功能说明：clouddcn子网名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param description: 功能说明：clouddcn子网描述 取值范围：0-255个字符，不能包含“&lt;”和“&gt;”。
        :type description: str
        :param cidr: 功能说明：clouddcn子网的网段 取值范围：必须在vpc对应cidr范围内，不能和同vpc下其他普通子网的网段冲突 约束：必须是cidr格式。掩码长度不能大于28
        :type cidr: str
        :param vpc_id: clouddcn子网所在VPC标识
        :type vpc_id: str
        :param gateway_ip: 功能说明：clouddcn子网的网关 取值范围：clouddcn子网网段中的IP地址 约束：必须是ip格式
        :type gateway_ip: str
        :param dns_nameservers: 功能说明：clouddcn子网dns服务器地址的集合；如果想使用两个以上dns服务器，请使用该字段 约束：是子网dns服务器地址1跟子网dns服务器地址2的合集的父集，不支持IPv6地址。 默认值：不填时为空，无法使用云内网DNS功能 [内网DNS地址请参见](https://support.huaweicloud.com/dns_faq/dns_faq_002.html) [通过API获取请参见](https://support.huaweicloud.com/api-dns/dns_api_69001.html)
        :type dns_nameservers: list[str]
        :param availability_zone: 功能说明：可用区
        :type availability_zone: str
        :param tags: 功能说明：对接TMS
        :type tags: list[:class:`huaweicloudsdkvpc.v3.TagEntity`]
        """
        
        

        self._name = None
        self._description = None
        self._cidr = None
        self._vpc_id = None
        self._gateway_ip = None
        self._dns_nameservers = None
        self._availability_zone = None
        self._tags = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.cidr = cidr
        self.vpc_id = vpc_id
        self.gateway_ip = gateway_ip
        if dns_nameservers is not None:
            self.dns_nameservers = dns_nameservers
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        """Gets the name of this CreateClouddcnSubnetOption.

        功能说明：clouddcn子网名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this CreateClouddcnSubnetOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateClouddcnSubnetOption.

        功能说明：clouddcn子网名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this CreateClouddcnSubnetOption.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateClouddcnSubnetOption.

        功能说明：clouddcn子网描述 取值范围：0-255个字符，不能包含“<”和“>”。

        :return: The description of this CreateClouddcnSubnetOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateClouddcnSubnetOption.

        功能说明：clouddcn子网描述 取值范围：0-255个字符，不能包含“<”和“>”。

        :param description: The description of this CreateClouddcnSubnetOption.
        :type description: str
        """
        self._description = description

    @property
    def cidr(self):
        """Gets the cidr of this CreateClouddcnSubnetOption.

        功能说明：clouddcn子网的网段 取值范围：必须在vpc对应cidr范围内，不能和同vpc下其他普通子网的网段冲突 约束：必须是cidr格式。掩码长度不能大于28

        :return: The cidr of this CreateClouddcnSubnetOption.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this CreateClouddcnSubnetOption.

        功能说明：clouddcn子网的网段 取值范围：必须在vpc对应cidr范围内，不能和同vpc下其他普通子网的网段冲突 约束：必须是cidr格式。掩码长度不能大于28

        :param cidr: The cidr of this CreateClouddcnSubnetOption.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateClouddcnSubnetOption.

        clouddcn子网所在VPC标识

        :return: The vpc_id of this CreateClouddcnSubnetOption.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateClouddcnSubnetOption.

        clouddcn子网所在VPC标识

        :param vpc_id: The vpc_id of this CreateClouddcnSubnetOption.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def gateway_ip(self):
        """Gets the gateway_ip of this CreateClouddcnSubnetOption.

        功能说明：clouddcn子网的网关 取值范围：clouddcn子网网段中的IP地址 约束：必须是ip格式

        :return: The gateway_ip of this CreateClouddcnSubnetOption.
        :rtype: str
        """
        return self._gateway_ip

    @gateway_ip.setter
    def gateway_ip(self, gateway_ip):
        """Sets the gateway_ip of this CreateClouddcnSubnetOption.

        功能说明：clouddcn子网的网关 取值范围：clouddcn子网网段中的IP地址 约束：必须是ip格式

        :param gateway_ip: The gateway_ip of this CreateClouddcnSubnetOption.
        :type gateway_ip: str
        """
        self._gateway_ip = gateway_ip

    @property
    def dns_nameservers(self):
        """Gets the dns_nameservers of this CreateClouddcnSubnetOption.

        功能说明：clouddcn子网dns服务器地址的集合；如果想使用两个以上dns服务器，请使用该字段 约束：是子网dns服务器地址1跟子网dns服务器地址2的合集的父集，不支持IPv6地址。 默认值：不填时为空，无法使用云内网DNS功能 [内网DNS地址请参见](https://support.huaweicloud.com/dns_faq/dns_faq_002.html) [通过API获取请参见](https://support.huaweicloud.com/api-dns/dns_api_69001.html)

        :return: The dns_nameservers of this CreateClouddcnSubnetOption.
        :rtype: list[str]
        """
        return self._dns_nameservers

    @dns_nameservers.setter
    def dns_nameservers(self, dns_nameservers):
        """Sets the dns_nameservers of this CreateClouddcnSubnetOption.

        功能说明：clouddcn子网dns服务器地址的集合；如果想使用两个以上dns服务器，请使用该字段 约束：是子网dns服务器地址1跟子网dns服务器地址2的合集的父集，不支持IPv6地址。 默认值：不填时为空，无法使用云内网DNS功能 [内网DNS地址请参见](https://support.huaweicloud.com/dns_faq/dns_faq_002.html) [通过API获取请参见](https://support.huaweicloud.com/api-dns/dns_api_69001.html)

        :param dns_nameservers: The dns_nameservers of this CreateClouddcnSubnetOption.
        :type dns_nameservers: list[str]
        """
        self._dns_nameservers = dns_nameservers

    @property
    def availability_zone(self):
        """Gets the availability_zone of this CreateClouddcnSubnetOption.

        功能说明：可用区

        :return: The availability_zone of this CreateClouddcnSubnetOption.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this CreateClouddcnSubnetOption.

        功能说明：可用区

        :param availability_zone: The availability_zone of this CreateClouddcnSubnetOption.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def tags(self):
        """Gets the tags of this CreateClouddcnSubnetOption.

        功能说明：对接TMS

        :return: The tags of this CreateClouddcnSubnetOption.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.TagEntity`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateClouddcnSubnetOption.

        功能说明：对接TMS

        :param tags: The tags of this CreateClouddcnSubnetOption.
        :type tags: list[:class:`huaweicloudsdkvpc.v3.TagEntity`]
        """
        self._tags = tags

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
        if not isinstance(other, CreateClouddcnSubnetOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
