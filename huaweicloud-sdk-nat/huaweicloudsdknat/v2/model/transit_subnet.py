# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TransitSubnet:

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
        'virsubnet_project_id': 'str',
        'project_id': 'str',
        'vpc_id': 'str',
        'virsubnet_id': 'str',
        'cidr': 'str',
        'type': 'str',
        'status': 'str',
        'ip_count': 'int',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'virsubnet_project_id': 'virsubnet_project_id',
        'project_id': 'project_id',
        'vpc_id': 'vpc_id',
        'virsubnet_id': 'virsubnet_id',
        'cidr': 'cidr',
        'type': 'type',
        'status': 'status',
        'ip_count': 'ip_count',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'tags': 'tags'
    }

    def __init__(self, id=None, name=None, description=None, virsubnet_project_id=None, project_id=None, vpc_id=None, virsubnet_id=None, cidr=None, type=None, status=None, ip_count=None, created_at=None, updated_at=None, tags=None):
        r"""TransitSubnet

        The model defined in huaweicloud sdk

        :param id: 中转子网的ID
        :type id: str
        :param name: 中转子网的名称
        :type name: str
        :param description: 中转子网的描述
        :type description: str
        :param virsubnet_project_id: 中转子网的子网所属的项目ID
        :type virsubnet_project_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param vpc_id: 中转子网的子网所属VPC的ID
        :type vpc_id: str
        :param virsubnet_id: 中转子网的子网ID
        :type virsubnet_id: str
        :param cidr: 中转子网的子网网段
        :type cidr: str
        :param type: 中转子网类型。取值范围：VPC
        :type type: str
        :param status: 中转子网状态。 取值范围： ACTIVE： 当前资源状态正常。 INACTIVE： 不可用。
        :type status: str
        :param ip_count: 当前中转子网下已分配的中转子网IP数量。
        :type ip_count: int
        :param created_at: 中转子网创建时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ。
        :type created_at: datetime
        :param updated_at: 中转子网更新时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ。
        :type updated_at: datetime
        :param tags: 标签列表
        :type tags: list[:class:`huaweicloudsdknat.v2.Tag`]
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._virsubnet_project_id = None
        self._project_id = None
        self._vpc_id = None
        self._virsubnet_id = None
        self._cidr = None
        self._type = None
        self._status = None
        self._ip_count = None
        self._created_at = None
        self._updated_at = None
        self._tags = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        self.virsubnet_project_id = virsubnet_project_id
        self.project_id = project_id
        self.vpc_id = vpc_id
        self.virsubnet_id = virsubnet_id
        self.cidr = cidr
        self.type = type
        self.status = status
        self.ip_count = ip_count
        self.created_at = created_at
        self.updated_at = updated_at
        self.tags = tags

    @property
    def id(self):
        r"""Gets the id of this TransitSubnet.

        中转子网的ID

        :return: The id of this TransitSubnet.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TransitSubnet.

        中转子网的ID

        :param id: The id of this TransitSubnet.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this TransitSubnet.

        中转子网的名称

        :return: The name of this TransitSubnet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TransitSubnet.

        中转子网的名称

        :param name: The name of this TransitSubnet.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this TransitSubnet.

        中转子网的描述

        :return: The description of this TransitSubnet.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this TransitSubnet.

        中转子网的描述

        :param description: The description of this TransitSubnet.
        :type description: str
        """
        self._description = description

    @property
    def virsubnet_project_id(self):
        r"""Gets the virsubnet_project_id of this TransitSubnet.

        中转子网的子网所属的项目ID

        :return: The virsubnet_project_id of this TransitSubnet.
        :rtype: str
        """
        return self._virsubnet_project_id

    @virsubnet_project_id.setter
    def virsubnet_project_id(self, virsubnet_project_id):
        r"""Sets the virsubnet_project_id of this TransitSubnet.

        中转子网的子网所属的项目ID

        :param virsubnet_project_id: The virsubnet_project_id of this TransitSubnet.
        :type virsubnet_project_id: str
        """
        self._virsubnet_project_id = virsubnet_project_id

    @property
    def project_id(self):
        r"""Gets the project_id of this TransitSubnet.

        项目ID

        :return: The project_id of this TransitSubnet.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this TransitSubnet.

        项目ID

        :param project_id: The project_id of this TransitSubnet.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this TransitSubnet.

        中转子网的子网所属VPC的ID

        :return: The vpc_id of this TransitSubnet.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this TransitSubnet.

        中转子网的子网所属VPC的ID

        :param vpc_id: The vpc_id of this TransitSubnet.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def virsubnet_id(self):
        r"""Gets the virsubnet_id of this TransitSubnet.

        中转子网的子网ID

        :return: The virsubnet_id of this TransitSubnet.
        :rtype: str
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        r"""Sets the virsubnet_id of this TransitSubnet.

        中转子网的子网ID

        :param virsubnet_id: The virsubnet_id of this TransitSubnet.
        :type virsubnet_id: str
        """
        self._virsubnet_id = virsubnet_id

    @property
    def cidr(self):
        r"""Gets the cidr of this TransitSubnet.

        中转子网的子网网段

        :return: The cidr of this TransitSubnet.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        r"""Sets the cidr of this TransitSubnet.

        中转子网的子网网段

        :param cidr: The cidr of this TransitSubnet.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def type(self):
        r"""Gets the type of this TransitSubnet.

        中转子网类型。取值范围：VPC

        :return: The type of this TransitSubnet.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this TransitSubnet.

        中转子网类型。取值范围：VPC

        :param type: The type of this TransitSubnet.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this TransitSubnet.

        中转子网状态。 取值范围： ACTIVE： 当前资源状态正常。 INACTIVE： 不可用。

        :return: The status of this TransitSubnet.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this TransitSubnet.

        中转子网状态。 取值范围： ACTIVE： 当前资源状态正常。 INACTIVE： 不可用。

        :param status: The status of this TransitSubnet.
        :type status: str
        """
        self._status = status

    @property
    def ip_count(self):
        r"""Gets the ip_count of this TransitSubnet.

        当前中转子网下已分配的中转子网IP数量。

        :return: The ip_count of this TransitSubnet.
        :rtype: int
        """
        return self._ip_count

    @ip_count.setter
    def ip_count(self, ip_count):
        r"""Sets the ip_count of this TransitSubnet.

        当前中转子网下已分配的中转子网IP数量。

        :param ip_count: The ip_count of this TransitSubnet.
        :type ip_count: int
        """
        self._ip_count = ip_count

    @property
    def created_at(self):
        r"""Gets the created_at of this TransitSubnet.

        中转子网创建时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ。

        :return: The created_at of this TransitSubnet.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this TransitSubnet.

        中转子网创建时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ。

        :param created_at: The created_at of this TransitSubnet.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this TransitSubnet.

        中转子网更新时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ。

        :return: The updated_at of this TransitSubnet.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this TransitSubnet.

        中转子网更新时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ。

        :param updated_at: The updated_at of this TransitSubnet.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def tags(self):
        r"""Gets the tags of this TransitSubnet.

        标签列表

        :return: The tags of this TransitSubnet.
        :rtype: list[:class:`huaweicloudsdknat.v2.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this TransitSubnet.

        标签列表

        :param tags: The tags of this TransitSubnet.
        :type tags: list[:class:`huaweicloudsdknat.v2.Tag`]
        """
        self._tags = tags

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
        if not isinstance(other, TransitSubnet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
