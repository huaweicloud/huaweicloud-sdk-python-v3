# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClouddcnSubnet:

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
        'project_id': 'str',
        'name': 'str',
        'description': 'str',
        'cidr': 'str',
        'gateway_ip': 'str',
        'dns_nameservers': 'list[str]',
        'vpc_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'availability_zone': 'str',
        'tags': 'list[TagEntity]',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'name': 'name',
        'description': 'description',
        'cidr': 'cidr',
        'gateway_ip': 'gateway_ip',
        'dns_nameservers': 'dns_nameservers',
        'vpc_id': 'vpc_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'availability_zone': 'availability_zone',
        'tags': 'tags',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, id=None, project_id=None, name=None, description=None, cidr=None, gateway_ip=None, dns_nameservers=None, vpc_id=None, created_at=None, updated_at=None, availability_zone=None, tags=None, enterprise_project_id=None):
        """ClouddcnSubnet

        The model defined in huaweicloud sdk

        :param id: clouddcn子网ID
        :type id: str
        :param project_id: 功能说明：VPC所属的项目ID
        :type project_id: str
        :param name: 功能说明：子网名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param description: 功能说明：子网描述 取值范围：0-255个字符，不能包含“&lt;”和“&gt;”。
        :type description: str
        :param cidr: 功能说明：子网的网段 取值范围：必须在vpc对应cidr范围内 约束：必须是cidr格式。掩码长度不能大于28
        :type cidr: str
        :param gateway_ip: 功能说明：子网的网关 取值范围：子网网段中的IP地址 约束：必须是ip格式
        :type gateway_ip: str
        :param dns_nameservers: clouddcn子网dns服务器地址列表
        :type dns_nameservers: list[str]
        :param vpc_id: clouddcn子网所在VPC标识
        :type vpc_id: str
        :param created_at: 功能说明：资源创建UTC时间 格式：yyyy-MM-ddTHH:mm:ss
        :type created_at: datetime
        :param updated_at: 功能说明：资源更新UTC时间 格式：yyyy-MM-ddTHH:mm:ss
        :type updated_at: datetime
        :param availability_zone: 功能说明：可用区
        :type availability_zone: str
        :param tags: 功能说明：对接TMS
        :type tags: list[:class:`huaweicloudsdkvpc.v3.TagEntity`]
        :param enterprise_project_id: 功能说明：对接TPS
        :type enterprise_project_id: str
        """
        
        

        self._id = None
        self._project_id = None
        self._name = None
        self._description = None
        self._cidr = None
        self._gateway_ip = None
        self._dns_nameservers = None
        self._vpc_id = None
        self._created_at = None
        self._updated_at = None
        self._availability_zone = None
        self._tags = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.id = id
        self.project_id = project_id
        self.name = name
        self.description = description
        self.cidr = cidr
        self.gateway_ip = gateway_ip
        self.dns_nameservers = dns_nameservers
        self.vpc_id = vpc_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.availability_zone = availability_zone
        self.tags = tags
        self.enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        """Gets the id of this ClouddcnSubnet.

        clouddcn子网ID

        :return: The id of this ClouddcnSubnet.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClouddcnSubnet.

        clouddcn子网ID

        :param id: The id of this ClouddcnSubnet.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this ClouddcnSubnet.

        功能说明：VPC所属的项目ID

        :return: The project_id of this ClouddcnSubnet.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ClouddcnSubnet.

        功能说明：VPC所属的项目ID

        :param project_id: The project_id of this ClouddcnSubnet.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def name(self):
        """Gets the name of this ClouddcnSubnet.

        功能说明：子网名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this ClouddcnSubnet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClouddcnSubnet.

        功能说明：子网名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this ClouddcnSubnet.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ClouddcnSubnet.

        功能说明：子网描述 取值范围：0-255个字符，不能包含“<”和“>”。

        :return: The description of this ClouddcnSubnet.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ClouddcnSubnet.

        功能说明：子网描述 取值范围：0-255个字符，不能包含“<”和“>”。

        :param description: The description of this ClouddcnSubnet.
        :type description: str
        """
        self._description = description

    @property
    def cidr(self):
        """Gets the cidr of this ClouddcnSubnet.

        功能说明：子网的网段 取值范围：必须在vpc对应cidr范围内 约束：必须是cidr格式。掩码长度不能大于28

        :return: The cidr of this ClouddcnSubnet.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this ClouddcnSubnet.

        功能说明：子网的网段 取值范围：必须在vpc对应cidr范围内 约束：必须是cidr格式。掩码长度不能大于28

        :param cidr: The cidr of this ClouddcnSubnet.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def gateway_ip(self):
        """Gets the gateway_ip of this ClouddcnSubnet.

        功能说明：子网的网关 取值范围：子网网段中的IP地址 约束：必须是ip格式

        :return: The gateway_ip of this ClouddcnSubnet.
        :rtype: str
        """
        return self._gateway_ip

    @gateway_ip.setter
    def gateway_ip(self, gateway_ip):
        """Sets the gateway_ip of this ClouddcnSubnet.

        功能说明：子网的网关 取值范围：子网网段中的IP地址 约束：必须是ip格式

        :param gateway_ip: The gateway_ip of this ClouddcnSubnet.
        :type gateway_ip: str
        """
        self._gateway_ip = gateway_ip

    @property
    def dns_nameservers(self):
        """Gets the dns_nameservers of this ClouddcnSubnet.

        clouddcn子网dns服务器地址列表

        :return: The dns_nameservers of this ClouddcnSubnet.
        :rtype: list[str]
        """
        return self._dns_nameservers

    @dns_nameservers.setter
    def dns_nameservers(self, dns_nameservers):
        """Sets the dns_nameservers of this ClouddcnSubnet.

        clouddcn子网dns服务器地址列表

        :param dns_nameservers: The dns_nameservers of this ClouddcnSubnet.
        :type dns_nameservers: list[str]
        """
        self._dns_nameservers = dns_nameservers

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ClouddcnSubnet.

        clouddcn子网所在VPC标识

        :return: The vpc_id of this ClouddcnSubnet.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ClouddcnSubnet.

        clouddcn子网所在VPC标识

        :param vpc_id: The vpc_id of this ClouddcnSubnet.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def created_at(self):
        """Gets the created_at of this ClouddcnSubnet.

        功能说明：资源创建UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :return: The created_at of this ClouddcnSubnet.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ClouddcnSubnet.

        功能说明：资源创建UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :param created_at: The created_at of this ClouddcnSubnet.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ClouddcnSubnet.

        功能说明：资源更新UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :return: The updated_at of this ClouddcnSubnet.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ClouddcnSubnet.

        功能说明：资源更新UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :param updated_at: The updated_at of this ClouddcnSubnet.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def availability_zone(self):
        """Gets the availability_zone of this ClouddcnSubnet.

        功能说明：可用区

        :return: The availability_zone of this ClouddcnSubnet.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this ClouddcnSubnet.

        功能说明：可用区

        :param availability_zone: The availability_zone of this ClouddcnSubnet.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def tags(self):
        """Gets the tags of this ClouddcnSubnet.

        功能说明：对接TMS

        :return: The tags of this ClouddcnSubnet.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.TagEntity`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ClouddcnSubnet.

        功能说明：对接TMS

        :param tags: The tags of this ClouddcnSubnet.
        :type tags: list[:class:`huaweicloudsdkvpc.v3.TagEntity`]
        """
        self._tags = tags

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ClouddcnSubnet.

        功能说明：对接TPS

        :return: The enterprise_project_id of this ClouddcnSubnet.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ClouddcnSubnet.

        功能说明：对接TPS

        :param enterprise_project_id: The enterprise_project_id of this ClouddcnSubnet.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ClouddcnSubnet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
