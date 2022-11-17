# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Vpc:

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
        'cidr': 'str',
        'extend_cidrs': 'list[str]',
        'status': 'str',
        'project_id': 'str',
        'enterprise_project_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'cloud_resources': 'list[CloudResource]',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
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

    def __init__(self, id=None, name=None, description=None, cidr=None, extend_cidrs=None, status=None, project_id=None, enterprise_project_id=None, created_at=None, updated_at=None, cloud_resources=None, tags=None):
        """Vpc

        The model defined in huaweicloud sdk

        :param id: 功能描述：VPC对应的唯一标识 取值范围：带“-”的UUID格式
        :type id: str
        :param name: 功能说明：VPC对应的名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param description: 功能说明：VPC的描述信息 取值范围：0-255个字符，不能包含“&lt;”和“&gt;”
        :type description: str
        :param cidr: 功能说明：VPC下可用子网的范围 取值范围： - 10.0.0.0/8~10.255.255.240/28 - 172.16.0.0/12 ~ 172.31.255.240/28 - 192.168.0.0/16 ~ 192.168.255.240/28 不指定cidr时，默认值为“” 约束：必须是ipv4 cidr格式，例如:192.168.0.0/16
        :type cidr: str
        :param extend_cidrs: 功能描述：VPC的扩展网段 取值范围： 约束：目前只支持ipv4
        :type extend_cidrs: list[str]
        :param status: 功能说明：VPC对应的状态 取值范围：PENDING：创建中；ACTIVE：创建成功 
        :type status: str
        :param project_id: 功能说明：VPC所属的项目ID
        :type project_id: str
        :param enterprise_project_id: 功能说明：VPC所属的企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。
        :type enterprise_project_id: str
        :param created_at: 功能说明：VPC创建时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss
        :type created_at: datetime
        :param updated_at: 功能说明：VPC更新时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss
        :type updated_at: datetime
        :param cloud_resources: 功能说明：VPC关联资源类型和数量 取值范围：目前只返回VPC关联的routetable和virsubnet
        :type cloud_resources: list[:class:`huaweicloudsdkvpc.v3.CloudResource`]
        :param tags: 功能说明：VPC的标签信息，详情参见Tag对象 取值范围：0-10个标签键值对
        :type tags: list[:class:`huaweicloudsdkvpc.v3.Tag`]
        """
        
        

        self._id = None
        self._name = None
        self._description = None
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
        self.description = description
        self.cidr = cidr
        self.extend_cidrs = extend_cidrs
        self.status = status
        self.project_id = project_id
        self.enterprise_project_id = enterprise_project_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.cloud_resources = cloud_resources
        self.tags = tags

    @property
    def id(self):
        """Gets the id of this Vpc.

        功能描述：VPC对应的唯一标识 取值范围：带“-”的UUID格式

        :return: The id of this Vpc.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Vpc.

        功能描述：VPC对应的唯一标识 取值范围：带“-”的UUID格式

        :param id: The id of this Vpc.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Vpc.

        功能说明：VPC对应的名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this Vpc.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Vpc.

        功能说明：VPC对应的名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this Vpc.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this Vpc.

        功能说明：VPC的描述信息 取值范围：0-255个字符，不能包含“<”和“>”

        :return: The description of this Vpc.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Vpc.

        功能说明：VPC的描述信息 取值范围：0-255个字符，不能包含“<”和“>”

        :param description: The description of this Vpc.
        :type description: str
        """
        self._description = description

    @property
    def cidr(self):
        """Gets the cidr of this Vpc.

        功能说明：VPC下可用子网的范围 取值范围： - 10.0.0.0/8~10.255.255.240/28 - 172.16.0.0/12 ~ 172.31.255.240/28 - 192.168.0.0/16 ~ 192.168.255.240/28 不指定cidr时，默认值为“” 约束：必须是ipv4 cidr格式，例如:192.168.0.0/16

        :return: The cidr of this Vpc.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this Vpc.

        功能说明：VPC下可用子网的范围 取值范围： - 10.0.0.0/8~10.255.255.240/28 - 172.16.0.0/12 ~ 172.31.255.240/28 - 192.168.0.0/16 ~ 192.168.255.240/28 不指定cidr时，默认值为“” 约束：必须是ipv4 cidr格式，例如:192.168.0.0/16

        :param cidr: The cidr of this Vpc.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def extend_cidrs(self):
        """Gets the extend_cidrs of this Vpc.

        功能描述：VPC的扩展网段 取值范围： 约束：目前只支持ipv4

        :return: The extend_cidrs of this Vpc.
        :rtype: list[str]
        """
        return self._extend_cidrs

    @extend_cidrs.setter
    def extend_cidrs(self, extend_cidrs):
        """Sets the extend_cidrs of this Vpc.

        功能描述：VPC的扩展网段 取值范围： 约束：目前只支持ipv4

        :param extend_cidrs: The extend_cidrs of this Vpc.
        :type extend_cidrs: list[str]
        """
        self._extend_cidrs = extend_cidrs

    @property
    def status(self):
        """Gets the status of this Vpc.

        功能说明：VPC对应的状态 取值范围：PENDING：创建中；ACTIVE：创建成功 

        :return: The status of this Vpc.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Vpc.

        功能说明：VPC对应的状态 取值范围：PENDING：创建中；ACTIVE：创建成功 

        :param status: The status of this Vpc.
        :type status: str
        """
        self._status = status

    @property
    def project_id(self):
        """Gets the project_id of this Vpc.

        功能说明：VPC所属的项目ID

        :return: The project_id of this Vpc.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Vpc.

        功能说明：VPC所属的项目ID

        :param project_id: The project_id of this Vpc.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this Vpc.

        功能说明：VPC所属的企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。

        :return: The enterprise_project_id of this Vpc.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this Vpc.

        功能说明：VPC所属的企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。

        :param enterprise_project_id: The enterprise_project_id of this Vpc.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def created_at(self):
        """Gets the created_at of this Vpc.

        功能说明：VPC创建时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss

        :return: The created_at of this Vpc.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Vpc.

        功能说明：VPC创建时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss

        :param created_at: The created_at of this Vpc.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Vpc.

        功能说明：VPC更新时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss

        :return: The updated_at of this Vpc.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Vpc.

        功能说明：VPC更新时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss

        :param updated_at: The updated_at of this Vpc.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def cloud_resources(self):
        """Gets the cloud_resources of this Vpc.

        功能说明：VPC关联资源类型和数量 取值范围：目前只返回VPC关联的routetable和virsubnet

        :return: The cloud_resources of this Vpc.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.CloudResource`]
        """
        return self._cloud_resources

    @cloud_resources.setter
    def cloud_resources(self, cloud_resources):
        """Sets the cloud_resources of this Vpc.

        功能说明：VPC关联资源类型和数量 取值范围：目前只返回VPC关联的routetable和virsubnet

        :param cloud_resources: The cloud_resources of this Vpc.
        :type cloud_resources: list[:class:`huaweicloudsdkvpc.v3.CloudResource`]
        """
        self._cloud_resources = cloud_resources

    @property
    def tags(self):
        """Gets the tags of this Vpc.

        功能说明：VPC的标签信息，详情参见Tag对象 取值范围：0-10个标签键值对

        :return: The tags of this Vpc.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Vpc.

        功能说明：VPC的标签信息，详情参见Tag对象 取值范围：0-10个标签键值对

        :param tags: The tags of this Vpc.
        :type tags: list[:class:`huaweicloudsdkvpc.v3.Tag`]
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
        if not isinstance(other, Vpc):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
