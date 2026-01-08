# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Virsubnet:

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
        'dns_nameservers': 'list[str]',
        'zone_id': 'str',
        'vpc_id': 'str',
        'status': 'str',
        'project_id': 'str',
        'scope': 'str',
        'subnet_cidrs': 'list[SubnetCidr]',
        'tags': 'list[ResponseTag]',
        'extra_dhcp_opts': 'list[SubnetExtraDhcpOpt]',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'dns_nameservers': 'dns_nameservers',
        'zone_id': 'zone_id',
        'vpc_id': 'vpc_id',
        'status': 'status',
        'project_id': 'project_id',
        'scope': 'scope',
        'subnet_cidrs': 'subnet_cidrs',
        'tags': 'tags',
        'extra_dhcp_opts': 'extra_dhcp_opts',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, description=None, dns_nameservers=None, zone_id=None, vpc_id=None, status=None, project_id=None, scope=None, subnet_cidrs=None, tags=None, extra_dhcp_opts=None, created_at=None, updated_at=None):
        r"""Virsubnet

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 子网的资源ID。子网创建成功后，会生成一个子网 ID，是子网对应的唯一标识。 **取值范围**： 带“-”的标准UUID格式。
        :type id: str
        :param name: **参数解释**： 子网的名称。 **取值范围**： 1-64个字符，支持数字、字母、中文字符、_(下划线)、-（中划线）、.（点）。
        :type name: str
        :param description: **参数解释**： 子网的描述信息。 **取值范围**： 0-255个字符，不能包含“&lt;”和“&gt;”。
        :type description: str
        :param dns_nameservers: **参数解释**： 子网的DNS服务器地址列表。 **取值范围**： 不涉及。
        :type dns_nameservers: list[str]
        :param zone_id: **参数解释**： 子网的可用区ID。 **取值范围**： 不涉及。
        :type zone_id: str
        :param vpc_id: **参数解释**： 子网所属VPC的资源ID。 **取值范围**： 不涉及。
        :type vpc_id: str
        :param status: **参数解释**： 子网的状态。 **取值范围**： - ACTIVE：表示子网已挂载到VPC上。 - UNKNOWN：表示子网还未挂载到VPC上。 - ERROR：表示子网状态故障。
        :type status: str
        :param project_id: **参数解释**： 子网所属的项目ID。 **取值范围**： 不涉及。
        :type project_id: str
        :param scope: **参数解释**： 子网的作用域（边缘云场景）。 **取值范围**： - center：表示作用域为中心。 - {publicBorderGroup}：表示作用域为具体的公网边界组。公网边界组限制子网的可用区范围，可关联多个边缘可用区。
        :type scope: str
        :param subnet_cidrs: **参数解释**： OpenStack Neutron子网信息。 **取值范围**： 不涉及。
        :type subnet_cidrs: list[:class:`huaweicloudsdkvpc.v3.SubnetCidr`]
        :param tags: **参数解释**： 子网的标签信息，包括标签键和标签值，可用来分类和标识资源。详情请参见Tag对象。 **取值范围**： 不涉及。
        :type tags: list[:class:`huaweicloudsdkvpc.v3.ResponseTag`]
        :param extra_dhcp_opts: **参数解释**： 子网的DHCP属性，支持配置NTP地址、DNS域名或租约到期时间。 **取值范围**： 不涉及。
        :type extra_dhcp_opts: list[:class:`huaweicloudsdkvpc.v3.SubnetExtraDhcpOpt`]
        :param created_at: **参数解释**： 子网的创建时间。 **取值范围**： UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type created_at: datetime
        :param updated_at: **参数解释**： 子网的更新时间。 **取值范围**： UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._dns_nameservers = None
        self._zone_id = None
        self._vpc_id = None
        self._status = None
        self._project_id = None
        self._scope = None
        self._subnet_cidrs = None
        self._tags = None
        self._extra_dhcp_opts = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        self.dns_nameservers = dns_nameservers
        self.zone_id = zone_id
        self.vpc_id = vpc_id
        self.status = status
        self.project_id = project_id
        self.scope = scope
        self.subnet_cidrs = subnet_cidrs
        self.tags = tags
        self.extra_dhcp_opts = extra_dhcp_opts
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this Virsubnet.

        **参数解释**： 子网的资源ID。子网创建成功后，会生成一个子网 ID，是子网对应的唯一标识。 **取值范围**： 带“-”的标准UUID格式。

        :return: The id of this Virsubnet.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Virsubnet.

        **参数解释**： 子网的资源ID。子网创建成功后，会生成一个子网 ID，是子网对应的唯一标识。 **取值范围**： 带“-”的标准UUID格式。

        :param id: The id of this Virsubnet.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this Virsubnet.

        **参数解释**： 子网的名称。 **取值范围**： 1-64个字符，支持数字、字母、中文字符、_(下划线)、-（中划线）、.（点）。

        :return: The name of this Virsubnet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Virsubnet.

        **参数解释**： 子网的名称。 **取值范围**： 1-64个字符，支持数字、字母、中文字符、_(下划线)、-（中划线）、.（点）。

        :param name: The name of this Virsubnet.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this Virsubnet.

        **参数解释**： 子网的描述信息。 **取值范围**： 0-255个字符，不能包含“<”和“>”。

        :return: The description of this Virsubnet.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Virsubnet.

        **参数解释**： 子网的描述信息。 **取值范围**： 0-255个字符，不能包含“<”和“>”。

        :param description: The description of this Virsubnet.
        :type description: str
        """
        self._description = description

    @property
    def dns_nameservers(self):
        r"""Gets the dns_nameservers of this Virsubnet.

        **参数解释**： 子网的DNS服务器地址列表。 **取值范围**： 不涉及。

        :return: The dns_nameservers of this Virsubnet.
        :rtype: list[str]
        """
        return self._dns_nameservers

    @dns_nameservers.setter
    def dns_nameservers(self, dns_nameservers):
        r"""Sets the dns_nameservers of this Virsubnet.

        **参数解释**： 子网的DNS服务器地址列表。 **取值范围**： 不涉及。

        :param dns_nameservers: The dns_nameservers of this Virsubnet.
        :type dns_nameservers: list[str]
        """
        self._dns_nameservers = dns_nameservers

    @property
    def zone_id(self):
        r"""Gets the zone_id of this Virsubnet.

        **参数解释**： 子网的可用区ID。 **取值范围**： 不涉及。

        :return: The zone_id of this Virsubnet.
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        r"""Sets the zone_id of this Virsubnet.

        **参数解释**： 子网的可用区ID。 **取值范围**： 不涉及。

        :param zone_id: The zone_id of this Virsubnet.
        :type zone_id: str
        """
        self._zone_id = zone_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this Virsubnet.

        **参数解释**： 子网所属VPC的资源ID。 **取值范围**： 不涉及。

        :return: The vpc_id of this Virsubnet.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this Virsubnet.

        **参数解释**： 子网所属VPC的资源ID。 **取值范围**： 不涉及。

        :param vpc_id: The vpc_id of this Virsubnet.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def status(self):
        r"""Gets the status of this Virsubnet.

        **参数解释**： 子网的状态。 **取值范围**： - ACTIVE：表示子网已挂载到VPC上。 - UNKNOWN：表示子网还未挂载到VPC上。 - ERROR：表示子网状态故障。

        :return: The status of this Virsubnet.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Virsubnet.

        **参数解释**： 子网的状态。 **取值范围**： - ACTIVE：表示子网已挂载到VPC上。 - UNKNOWN：表示子网还未挂载到VPC上。 - ERROR：表示子网状态故障。

        :param status: The status of this Virsubnet.
        :type status: str
        """
        self._status = status

    @property
    def project_id(self):
        r"""Gets the project_id of this Virsubnet.

        **参数解释**： 子网所属的项目ID。 **取值范围**： 不涉及。

        :return: The project_id of this Virsubnet.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this Virsubnet.

        **参数解释**： 子网所属的项目ID。 **取值范围**： 不涉及。

        :param project_id: The project_id of this Virsubnet.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def scope(self):
        r"""Gets the scope of this Virsubnet.

        **参数解释**： 子网的作用域（边缘云场景）。 **取值范围**： - center：表示作用域为中心。 - {publicBorderGroup}：表示作用域为具体的公网边界组。公网边界组限制子网的可用区范围，可关联多个边缘可用区。

        :return: The scope of this Virsubnet.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this Virsubnet.

        **参数解释**： 子网的作用域（边缘云场景）。 **取值范围**： - center：表示作用域为中心。 - {publicBorderGroup}：表示作用域为具体的公网边界组。公网边界组限制子网的可用区范围，可关联多个边缘可用区。

        :param scope: The scope of this Virsubnet.
        :type scope: str
        """
        self._scope = scope

    @property
    def subnet_cidrs(self):
        r"""Gets the subnet_cidrs of this Virsubnet.

        **参数解释**： OpenStack Neutron子网信息。 **取值范围**： 不涉及。

        :return: The subnet_cidrs of this Virsubnet.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.SubnetCidr`]
        """
        return self._subnet_cidrs

    @subnet_cidrs.setter
    def subnet_cidrs(self, subnet_cidrs):
        r"""Sets the subnet_cidrs of this Virsubnet.

        **参数解释**： OpenStack Neutron子网信息。 **取值范围**： 不涉及。

        :param subnet_cidrs: The subnet_cidrs of this Virsubnet.
        :type subnet_cidrs: list[:class:`huaweicloudsdkvpc.v3.SubnetCidr`]
        """
        self._subnet_cidrs = subnet_cidrs

    @property
    def tags(self):
        r"""Gets the tags of this Virsubnet.

        **参数解释**： 子网的标签信息，包括标签键和标签值，可用来分类和标识资源。详情请参见Tag对象。 **取值范围**： 不涉及。

        :return: The tags of this Virsubnet.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.ResponseTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this Virsubnet.

        **参数解释**： 子网的标签信息，包括标签键和标签值，可用来分类和标识资源。详情请参见Tag对象。 **取值范围**： 不涉及。

        :param tags: The tags of this Virsubnet.
        :type tags: list[:class:`huaweicloudsdkvpc.v3.ResponseTag`]
        """
        self._tags = tags

    @property
    def extra_dhcp_opts(self):
        r"""Gets the extra_dhcp_opts of this Virsubnet.

        **参数解释**： 子网的DHCP属性，支持配置NTP地址、DNS域名或租约到期时间。 **取值范围**： 不涉及。

        :return: The extra_dhcp_opts of this Virsubnet.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.SubnetExtraDhcpOpt`]
        """
        return self._extra_dhcp_opts

    @extra_dhcp_opts.setter
    def extra_dhcp_opts(self, extra_dhcp_opts):
        r"""Sets the extra_dhcp_opts of this Virsubnet.

        **参数解释**： 子网的DHCP属性，支持配置NTP地址、DNS域名或租约到期时间。 **取值范围**： 不涉及。

        :param extra_dhcp_opts: The extra_dhcp_opts of this Virsubnet.
        :type extra_dhcp_opts: list[:class:`huaweicloudsdkvpc.v3.SubnetExtraDhcpOpt`]
        """
        self._extra_dhcp_opts = extra_dhcp_opts

    @property
    def created_at(self):
        r"""Gets the created_at of this Virsubnet.

        **参数解释**： 子网的创建时间。 **取值范围**： UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The created_at of this Virsubnet.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this Virsubnet.

        **参数解释**： 子网的创建时间。 **取值范围**： UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param created_at: The created_at of this Virsubnet.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this Virsubnet.

        **参数解释**： 子网的更新时间。 **取值范围**： UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The updated_at of this Virsubnet.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this Virsubnet.

        **参数解释**： 子网的更新时间。 **取值范围**： UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param updated_at: The updated_at of this Virsubnet.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Virsubnet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
