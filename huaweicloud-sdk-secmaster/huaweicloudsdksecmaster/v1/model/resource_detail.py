# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceDetail:

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
        'provider': 'str',
        'type': 'str',
        'checksum': 'str',
        'created': 'date',
        'provisioning_state': 'str',
        'environment': 'ResourceEnvironment',
        'department': 'Department',
        'governance_user': 'GovernanceUser',
        'level': 'int',
        'properties': 'Properties'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'provider': 'provider',
        'type': 'type',
        'checksum': 'checksum',
        'created': 'created',
        'provisioning_state': 'provisioning_state',
        'environment': 'environment',
        'department': 'department',
        'governance_user': 'governance_user',
        'level': 'level',
        'properties': 'properties'
    }

    def __init__(self, id=None, name=None, provider=None, type=None, checksum=None, created=None, provisioning_state=None, environment=None, department=None, governance_user=None, level=None, properties=None):
        r"""ResourceDetail

        The model defined in huaweicloud sdk

        :param id: 资产id
        :type id: str
        :param name: 资产名称
        :type name: str
        :param provider: 资产来源，云服务名称(云上)，线下机房（IDC）
        :type provider: str
        :param type: 资产类型, 比如ECS/VPC/EVS/IP/URL等
        :type type: str
        :param checksum: 资产详情校验码。
        :type checksum: str
        :param created: 资产创建时间。
        :type created: date
        :param provisioning_state: 资产操作状态。
        :type provisioning_state: str
        :param environment: 
        :type environment: :class:`huaweicloudsdksecmaster.v1.ResourceEnvironment`
        :param department: 
        :type department: :class:`huaweicloudsdksecmaster.v1.Department`
        :param governance_user: 
        :type governance_user: :class:`huaweicloudsdksecmaster.v1.GovernanceUser`
        :param level: 0: 测试 1： 一般   2： 关键资产
        :type level: int
        :param properties: 
        :type properties: :class:`huaweicloudsdksecmaster.v1.Properties`
        """
        
        

        self._id = None
        self._name = None
        self._provider = None
        self._type = None
        self._checksum = None
        self._created = None
        self._provisioning_state = None
        self._environment = None
        self._department = None
        self._governance_user = None
        self._level = None
        self._properties = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.provider = provider
        self.type = type
        if checksum is not None:
            self.checksum = checksum
        if created is not None:
            self.created = created
        if provisioning_state is not None:
            self.provisioning_state = provisioning_state
        self.environment = environment
        if department is not None:
            self.department = department
        if governance_user is not None:
            self.governance_user = governance_user
        if level is not None:
            self.level = level
        self.properties = properties

    @property
    def id(self):
        r"""Gets the id of this ResourceDetail.

        资产id

        :return: The id of this ResourceDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ResourceDetail.

        资产id

        :param id: The id of this ResourceDetail.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ResourceDetail.

        资产名称

        :return: The name of this ResourceDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ResourceDetail.

        资产名称

        :param name: The name of this ResourceDetail.
        :type name: str
        """
        self._name = name

    @property
    def provider(self):
        r"""Gets the provider of this ResourceDetail.

        资产来源，云服务名称(云上)，线下机房（IDC）

        :return: The provider of this ResourceDetail.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this ResourceDetail.

        资产来源，云服务名称(云上)，线下机房（IDC）

        :param provider: The provider of this ResourceDetail.
        :type provider: str
        """
        self._provider = provider

    @property
    def type(self):
        r"""Gets the type of this ResourceDetail.

        资产类型, 比如ECS/VPC/EVS/IP/URL等

        :return: The type of this ResourceDetail.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ResourceDetail.

        资产类型, 比如ECS/VPC/EVS/IP/URL等

        :param type: The type of this ResourceDetail.
        :type type: str
        """
        self._type = type

    @property
    def checksum(self):
        r"""Gets the checksum of this ResourceDetail.

        资产详情校验码。

        :return: The checksum of this ResourceDetail.
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        r"""Sets the checksum of this ResourceDetail.

        资产详情校验码。

        :param checksum: The checksum of this ResourceDetail.
        :type checksum: str
        """
        self._checksum = checksum

    @property
    def created(self):
        r"""Gets the created of this ResourceDetail.

        资产创建时间。

        :return: The created of this ResourceDetail.
        :rtype: date
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this ResourceDetail.

        资产创建时间。

        :param created: The created of this ResourceDetail.
        :type created: date
        """
        self._created = created

    @property
    def provisioning_state(self):
        r"""Gets the provisioning_state of this ResourceDetail.

        资产操作状态。

        :return: The provisioning_state of this ResourceDetail.
        :rtype: str
        """
        return self._provisioning_state

    @provisioning_state.setter
    def provisioning_state(self, provisioning_state):
        r"""Sets the provisioning_state of this ResourceDetail.

        资产操作状态。

        :param provisioning_state: The provisioning_state of this ResourceDetail.
        :type provisioning_state: str
        """
        self._provisioning_state = provisioning_state

    @property
    def environment(self):
        r"""Gets the environment of this ResourceDetail.

        :return: The environment of this ResourceDetail.
        :rtype: :class:`huaweicloudsdksecmaster.v1.ResourceEnvironment`
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        r"""Sets the environment of this ResourceDetail.

        :param environment: The environment of this ResourceDetail.
        :type environment: :class:`huaweicloudsdksecmaster.v1.ResourceEnvironment`
        """
        self._environment = environment

    @property
    def department(self):
        r"""Gets the department of this ResourceDetail.

        :return: The department of this ResourceDetail.
        :rtype: :class:`huaweicloudsdksecmaster.v1.Department`
        """
        return self._department

    @department.setter
    def department(self, department):
        r"""Sets the department of this ResourceDetail.

        :param department: The department of this ResourceDetail.
        :type department: :class:`huaweicloudsdksecmaster.v1.Department`
        """
        self._department = department

    @property
    def governance_user(self):
        r"""Gets the governance_user of this ResourceDetail.

        :return: The governance_user of this ResourceDetail.
        :rtype: :class:`huaweicloudsdksecmaster.v1.GovernanceUser`
        """
        return self._governance_user

    @governance_user.setter
    def governance_user(self, governance_user):
        r"""Sets the governance_user of this ResourceDetail.

        :param governance_user: The governance_user of this ResourceDetail.
        :type governance_user: :class:`huaweicloudsdksecmaster.v1.GovernanceUser`
        """
        self._governance_user = governance_user

    @property
    def level(self):
        r"""Gets the level of this ResourceDetail.

        0: 测试 1： 一般   2： 关键资产

        :return: The level of this ResourceDetail.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this ResourceDetail.

        0: 测试 1： 一般   2： 关键资产

        :param level: The level of this ResourceDetail.
        :type level: int
        """
        self._level = level

    @property
    def properties(self):
        r"""Gets the properties of this ResourceDetail.

        :return: The properties of this ResourceDetail.
        :rtype: :class:`huaweicloudsdksecmaster.v1.Properties`
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this ResourceDetail.

        :param properties: The properties of this ResourceDetail.
        :type properties: :class:`huaweicloudsdksecmaster.v1.Properties`
        """
        self._properties = properties

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
        if not isinstance(other, ResourceDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
