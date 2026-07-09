# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CsbResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[CsbResourceTag]',
        'affected_resources': 'list[AffectedResource]',
        'create_time': 'datetime',
        'description': 'str',
        'environment': 'ResourceEnvironment',
        'name': 'str',
        'provider': 'str',
        'resource_id': 'str',
        'security_group_id': 'str',
        'subnet_id': 'str',
        'type': 'str',
        'update_time': 'datetime',
        'urn': 'str',
        'urnext': 'str',
        'vpc_id': 'str'
    }

    attribute_map = {
        'tags': 'tags',
        'affected_resources': 'affected_resources',
        'create_time': 'create_time',
        'description': 'description',
        'environment': 'environment',
        'name': 'name',
        'provider': 'provider',
        'resource_id': 'resource_id',
        'security_group_id': 'security_group_id',
        'subnet_id': 'subnet_id',
        'type': 'type',
        'update_time': 'update_time',
        'urn': 'urn',
        'urnext': 'urnext',
        'vpc_id': 'vpc_id'
    }

    def __init__(self, tags=None, affected_resources=None, create_time=None, description=None, environment=None, name=None, provider=None, resource_id=None, security_group_id=None, subnet_id=None, type=None, update_time=None, urn=None, urnext=None, vpc_id=None):
        r"""CsbResource

        The model defined in huaweicloud sdk

        :param tags: 资源标签
        :type tags: list[:class:`huaweicloudsdkdbss.v1.CsbResourceTag`]
        :param affected_resources: 防护资源对象列表
        :type affected_resources: list[:class:`huaweicloudsdkdbss.v1.AffectedResource`]
        :param create_time: 创建时间
        :type create_time: datetime
        :param description: 资源描述
        :type description: str
        :param environment: 
        :type environment: :class:`huaweicloudsdkdbss.v1.ResourceEnvironment`
        :param name: 资源名称
        :type name: str
        :param provider: 所属云服务，dbss
        :type provider: str
        :param resource_id: 资源ID
        :type resource_id: str
        :param security_group_id: 安全组ID
        :type security_group_id: str
        :param subnet_id: 子网ID
        :type subnet_id: str
        :param type: 资源类型   - cloudservers: 审计   - dbEncrypt: 加密   - dbOm: 运维
        :type type: str
        :param update_time: 更新时间
        :type update_time: datetime
        :param urn: 资源URN
        :type urn: str
        :param urnext: 资源URN扩展
        :type urnext: str
        :param vpc_id: VPC ID
        :type vpc_id: str
        """
        
        

        self._tags = None
        self._affected_resources = None
        self._create_time = None
        self._description = None
        self._environment = None
        self._name = None
        self._provider = None
        self._resource_id = None
        self._security_group_id = None
        self._subnet_id = None
        self._type = None
        self._update_time = None
        self._urn = None
        self._urnext = None
        self._vpc_id = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if affected_resources is not None:
            self.affected_resources = affected_resources
        if create_time is not None:
            self.create_time = create_time
        if description is not None:
            self.description = description
        if environment is not None:
            self.environment = environment
        if name is not None:
            self.name = name
        if provider is not None:
            self.provider = provider
        if resource_id is not None:
            self.resource_id = resource_id
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if type is not None:
            self.type = type
        if update_time is not None:
            self.update_time = update_time
        if urn is not None:
            self.urn = urn
        if urnext is not None:
            self.urnext = urnext
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def tags(self):
        r"""Gets the tags of this CsbResource.

        资源标签

        :return: The tags of this CsbResource.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.CsbResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CsbResource.

        资源标签

        :param tags: The tags of this CsbResource.
        :type tags: list[:class:`huaweicloudsdkdbss.v1.CsbResourceTag`]
        """
        self._tags = tags

    @property
    def affected_resources(self):
        r"""Gets the affected_resources of this CsbResource.

        防护资源对象列表

        :return: The affected_resources of this CsbResource.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.AffectedResource`]
        """
        return self._affected_resources

    @affected_resources.setter
    def affected_resources(self, affected_resources):
        r"""Sets the affected_resources of this CsbResource.

        防护资源对象列表

        :param affected_resources: The affected_resources of this CsbResource.
        :type affected_resources: list[:class:`huaweicloudsdkdbss.v1.AffectedResource`]
        """
        self._affected_resources = affected_resources

    @property
    def create_time(self):
        r"""Gets the create_time of this CsbResource.

        创建时间

        :return: The create_time of this CsbResource.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CsbResource.

        创建时间

        :param create_time: The create_time of this CsbResource.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def description(self):
        r"""Gets the description of this CsbResource.

        资源描述

        :return: The description of this CsbResource.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CsbResource.

        资源描述

        :param description: The description of this CsbResource.
        :type description: str
        """
        self._description = description

    @property
    def environment(self):
        r"""Gets the environment of this CsbResource.

        :return: The environment of this CsbResource.
        :rtype: :class:`huaweicloudsdkdbss.v1.ResourceEnvironment`
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        r"""Sets the environment of this CsbResource.

        :param environment: The environment of this CsbResource.
        :type environment: :class:`huaweicloudsdkdbss.v1.ResourceEnvironment`
        """
        self._environment = environment

    @property
    def name(self):
        r"""Gets the name of this CsbResource.

        资源名称

        :return: The name of this CsbResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CsbResource.

        资源名称

        :param name: The name of this CsbResource.
        :type name: str
        """
        self._name = name

    @property
    def provider(self):
        r"""Gets the provider of this CsbResource.

        所属云服务，dbss

        :return: The provider of this CsbResource.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this CsbResource.

        所属云服务，dbss

        :param provider: The provider of this CsbResource.
        :type provider: str
        """
        self._provider = provider

    @property
    def resource_id(self):
        r"""Gets the resource_id of this CsbResource.

        资源ID

        :return: The resource_id of this CsbResource.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this CsbResource.

        资源ID

        :param resource_id: The resource_id of this CsbResource.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this CsbResource.

        安全组ID

        :return: The security_group_id of this CsbResource.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this CsbResource.

        安全组ID

        :param security_group_id: The security_group_id of this CsbResource.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this CsbResource.

        子网ID

        :return: The subnet_id of this CsbResource.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this CsbResource.

        子网ID

        :param subnet_id: The subnet_id of this CsbResource.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def type(self):
        r"""Gets the type of this CsbResource.

        资源类型   - cloudservers: 审计   - dbEncrypt: 加密   - dbOm: 运维

        :return: The type of this CsbResource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CsbResource.

        资源类型   - cloudservers: 审计   - dbEncrypt: 加密   - dbOm: 运维

        :param type: The type of this CsbResource.
        :type type: str
        """
        self._type = type

    @property
    def update_time(self):
        r"""Gets the update_time of this CsbResource.

        更新时间

        :return: The update_time of this CsbResource.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CsbResource.

        更新时间

        :param update_time: The update_time of this CsbResource.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def urn(self):
        r"""Gets the urn of this CsbResource.

        资源URN

        :return: The urn of this CsbResource.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        r"""Sets the urn of this CsbResource.

        资源URN

        :param urn: The urn of this CsbResource.
        :type urn: str
        """
        self._urn = urn

    @property
    def urnext(self):
        r"""Gets the urnext of this CsbResource.

        资源URN扩展

        :return: The urnext of this CsbResource.
        :rtype: str
        """
        return self._urnext

    @urnext.setter
    def urnext(self, urnext):
        r"""Sets the urnext of this CsbResource.

        资源URN扩展

        :param urnext: The urnext of this CsbResource.
        :type urnext: str
        """
        self._urnext = urnext

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CsbResource.

        VPC ID

        :return: The vpc_id of this CsbResource.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CsbResource.

        VPC ID

        :param vpc_id: The vpc_id of this CsbResource.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

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
        if not isinstance(other, CsbResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
