# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HwcVpc:

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
        'protected_status': 'str',
        'cidr': 'str',
        'extend_cidrs': 'list[str]',
        'status': 'str',
        'project_id': 'str',
        'enterprise_project_id': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'cloud_resources': 'list[HwcVpcCloudResource]',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'protected_status': 'protected_status',
        'cidr': 'cidr',
        'extend_cidrs': 'extend_cidrs',
        'status': 'status',
        'project_id': 'project_id',
        'enterprise_project_id': 'enterprise_project_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'cloud_resources': 'cloud_resources',
        'tags': 'tags'
    }

    def __init__(self, id=None, name=None, description=None, protected_status=None, cidr=None, extend_cidrs=None, status=None, project_id=None, enterprise_project_id=None, created_at=None, updated_at=None, cloud_resources=None, tags=None):
        r"""HwcVpc

        The model defined in huaweicloud sdk

        :param id: VPC对应的唯一标识
        :type id: str
        :param name: VPC对应的名称
        :type name: str
        :param description: VPC的描述信息
        :type description: str
        :param protected_status: CFW开启或安全组规则配置状态：OPEN | CLOSE
        :type protected_status: str
        :param cidr: VPC下可用子网的范围 取值范围： 10.0.0.0/8~10.255.255.240/28 172.16.0.0/12 ~ 172.31.255.240/28 192.168.0.0/16 ~ 192.168.255.240/28 不指定cidr时，默认值为“” 约束：必须是ipv4 cidr格式，例如:192.168.0.0/16
        :type cidr: str
        :param extend_cidrs: VPC的扩展网段 约束：目前只支持ipv4
        :type extend_cidrs: list[str]
        :param status: VPC对应的状态 取值范围： PENDING：创建中 ACTIVE：创建成功
        :type status: str
        :param project_id: VPC所属的项目ID
        :type project_id: str
        :param enterprise_project_id: VPC所属的企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。
        :type enterprise_project_id: str
        :param created_at: VPC创建时间 取值范围：UTC时间格式，yyyy-MM-ddTHH:mm:ss
        :type created_at: str
        :param updated_at: VPC更新时间 取值范围：UTC时间格式，yyyy-MM-ddTHH:mm:ss
        :type updated_at: str
        :param cloud_resources: VPC关联资产类型和数量 取值范围：目前只返回VPC关联的routetable和virsubnet。virsubnet数量为ipv4和ipv6子网总数。
        :type cloud_resources: list[:class:`huaweicloudsdksecmaster.v1.HwcVpcCloudResource`]
        :param tags: VPC的标签信息，详情参见Tag对象 取值范围：0-10个标签键值对
        :type tags: list[:class:`huaweicloudsdksecmaster.v1.Tag`]
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._protected_status = None
        self._cidr = None
        self._extend_cidrs = None
        self._status = None
        self._project_id = None
        self._enterprise_project_id = None
        self._created_at = None
        self._updated_at = None
        self._cloud_resources = None
        self._tags = None
        self.discriminator = None

        self.id = id
        self.name = name
        if description is not None:
            self.description = description
        self.protected_status = protected_status
        if cidr is not None:
            self.cidr = cidr
        if extend_cidrs is not None:
            self.extend_cidrs = extend_cidrs
        self.status = status
        self.project_id = project_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.created_at = created_at
        self.updated_at = updated_at
        if cloud_resources is not None:
            self.cloud_resources = cloud_resources
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        r"""Gets the id of this HwcVpc.

        VPC对应的唯一标识

        :return: The id of this HwcVpc.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this HwcVpc.

        VPC对应的唯一标识

        :param id: The id of this HwcVpc.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this HwcVpc.

        VPC对应的名称

        :return: The name of this HwcVpc.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this HwcVpc.

        VPC对应的名称

        :param name: The name of this HwcVpc.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this HwcVpc.

        VPC的描述信息

        :return: The description of this HwcVpc.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this HwcVpc.

        VPC的描述信息

        :param description: The description of this HwcVpc.
        :type description: str
        """
        self._description = description

    @property
    def protected_status(self):
        r"""Gets the protected_status of this HwcVpc.

        CFW开启或安全组规则配置状态：OPEN | CLOSE

        :return: The protected_status of this HwcVpc.
        :rtype: str
        """
        return self._protected_status

    @protected_status.setter
    def protected_status(self, protected_status):
        r"""Sets the protected_status of this HwcVpc.

        CFW开启或安全组规则配置状态：OPEN | CLOSE

        :param protected_status: The protected_status of this HwcVpc.
        :type protected_status: str
        """
        self._protected_status = protected_status

    @property
    def cidr(self):
        r"""Gets the cidr of this HwcVpc.

        VPC下可用子网的范围 取值范围： 10.0.0.0/8~10.255.255.240/28 172.16.0.0/12 ~ 172.31.255.240/28 192.168.0.0/16 ~ 192.168.255.240/28 不指定cidr时，默认值为“” 约束：必须是ipv4 cidr格式，例如:192.168.0.0/16

        :return: The cidr of this HwcVpc.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        r"""Sets the cidr of this HwcVpc.

        VPC下可用子网的范围 取值范围： 10.0.0.0/8~10.255.255.240/28 172.16.0.0/12 ~ 172.31.255.240/28 192.168.0.0/16 ~ 192.168.255.240/28 不指定cidr时，默认值为“” 约束：必须是ipv4 cidr格式，例如:192.168.0.0/16

        :param cidr: The cidr of this HwcVpc.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def extend_cidrs(self):
        r"""Gets the extend_cidrs of this HwcVpc.

        VPC的扩展网段 约束：目前只支持ipv4

        :return: The extend_cidrs of this HwcVpc.
        :rtype: list[str]
        """
        return self._extend_cidrs

    @extend_cidrs.setter
    def extend_cidrs(self, extend_cidrs):
        r"""Sets the extend_cidrs of this HwcVpc.

        VPC的扩展网段 约束：目前只支持ipv4

        :param extend_cidrs: The extend_cidrs of this HwcVpc.
        :type extend_cidrs: list[str]
        """
        self._extend_cidrs = extend_cidrs

    @property
    def status(self):
        r"""Gets the status of this HwcVpc.

        VPC对应的状态 取值范围： PENDING：创建中 ACTIVE：创建成功

        :return: The status of this HwcVpc.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this HwcVpc.

        VPC对应的状态 取值范围： PENDING：创建中 ACTIVE：创建成功

        :param status: The status of this HwcVpc.
        :type status: str
        """
        self._status = status

    @property
    def project_id(self):
        r"""Gets the project_id of this HwcVpc.

        VPC所属的项目ID

        :return: The project_id of this HwcVpc.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this HwcVpc.

        VPC所属的项目ID

        :param project_id: The project_id of this HwcVpc.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this HwcVpc.

        VPC所属的企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。

        :return: The enterprise_project_id of this HwcVpc.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this HwcVpc.

        VPC所属的企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。

        :param enterprise_project_id: The enterprise_project_id of this HwcVpc.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def created_at(self):
        r"""Gets the created_at of this HwcVpc.

        VPC创建时间 取值范围：UTC时间格式，yyyy-MM-ddTHH:mm:ss

        :return: The created_at of this HwcVpc.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this HwcVpc.

        VPC创建时间 取值范围：UTC时间格式，yyyy-MM-ddTHH:mm:ss

        :param created_at: The created_at of this HwcVpc.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this HwcVpc.

        VPC更新时间 取值范围：UTC时间格式，yyyy-MM-ddTHH:mm:ss

        :return: The updated_at of this HwcVpc.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this HwcVpc.

        VPC更新时间 取值范围：UTC时间格式，yyyy-MM-ddTHH:mm:ss

        :param updated_at: The updated_at of this HwcVpc.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def cloud_resources(self):
        r"""Gets the cloud_resources of this HwcVpc.

        VPC关联资产类型和数量 取值范围：目前只返回VPC关联的routetable和virsubnet。virsubnet数量为ipv4和ipv6子网总数。

        :return: The cloud_resources of this HwcVpc.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.HwcVpcCloudResource`]
        """
        return self._cloud_resources

    @cloud_resources.setter
    def cloud_resources(self, cloud_resources):
        r"""Sets the cloud_resources of this HwcVpc.

        VPC关联资产类型和数量 取值范围：目前只返回VPC关联的routetable和virsubnet。virsubnet数量为ipv4和ipv6子网总数。

        :param cloud_resources: The cloud_resources of this HwcVpc.
        :type cloud_resources: list[:class:`huaweicloudsdksecmaster.v1.HwcVpcCloudResource`]
        """
        self._cloud_resources = cloud_resources

    @property
    def tags(self):
        r"""Gets the tags of this HwcVpc.

        VPC的标签信息，详情参见Tag对象 取值范围：0-10个标签键值对

        :return: The tags of this HwcVpc.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this HwcVpc.

        VPC的标签信息，详情参见Tag对象 取值范围：0-10个标签键值对

        :param tags: The tags of this HwcVpc.
        :type tags: list[:class:`huaweicloudsdksecmaster.v1.Tag`]
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
        if not isinstance(other, HwcVpc):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
