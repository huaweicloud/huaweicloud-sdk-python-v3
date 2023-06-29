# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddressGroup:

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
        'max_capacity': 'int',
        'ip_set': 'list[str]',
        'ip_version': 'int',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'tenant_id': 'str',
        'enterprise_project_id': 'str',
        'tags': 'list[ResourceTag]',
        'status': 'str',
        'status_message': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'max_capacity': 'max_capacity',
        'ip_set': 'ip_set',
        'ip_version': 'ip_version',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'tenant_id': 'tenant_id',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'status': 'status',
        'status_message': 'status_message'
    }

    def __init__(self, id=None, name=None, description=None, max_capacity=None, ip_set=None, ip_version=None, created_at=None, updated_at=None, tenant_id=None, enterprise_project_id=None, tags=None, status=None, status_message=None):
        """AddressGroup

        The model defined in huaweicloud sdk

        :param id: 功能说明：地址组唯一标识 取值范围：合法UUID的字符串 
        :type id: str
        :param name: 功能说明：地址组名称 取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param description: 功能说明：地址组描述信息 取值范围：0-255个字符 约束：不能包含“&lt;”和“&gt;”。
        :type description: str
        :param max_capacity: 功能说明：地址组最大条目数，限制地址组可以包含的地址数量 取值范围：0-20 默认值：20
        :type max_capacity: int
        :param ip_set: 功能说明：地址组可包含地址集 取值范围：可以是单个ip地址，ip地址范围，ip地址cidr 约束：当前一个地址组ip_set数量限制默认值为20，即配置的ip地址、ip地址范围或ip地址cidr的总数默认限制20 
        :type ip_set: list[str]
        :param ip_version: 功能说明：IP地址组ip版本 取值范围：4, 表示ipv4地址组；6, 表示ipv6地址组
        :type ip_version: int
        :param created_at: 功能说明：地址组创建时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss；系统自动生成 
        :type created_at: datetime
        :param updated_at: 功能描述：地址组最近一次更新资源的时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss；系统自动生成
        :type updated_at: datetime
        :param tenant_id: 功能说明：资源所属项目ID
        :type tenant_id: str
        :param enterprise_project_id: 功能说明：企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。
        :type enterprise_project_id: str
        :param tags: IP地址组资源标签
        :type tags: list[:class:`huaweicloudsdkvpc.v3.ResourceTag`]
        :param status: 功能说明：地址组状态 取值范围：       NORMAL：正常       UPDATING：更新中       UPDATE_FAILED：更新失败 默认值：NORMAL 约束：当地址组处于UPDATING（更新中）状态时，不允许再次更新
        :type status: str
        :param status_message: 功能说明：地址组状态详情信息
        :type status_message: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._max_capacity = None
        self._ip_set = None
        self._ip_version = None
        self._created_at = None
        self._updated_at = None
        self._tenant_id = None
        self._enterprise_project_id = None
        self._tags = None
        self._status = None
        self._status_message = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        self.max_capacity = max_capacity
        self.ip_set = ip_set
        self.ip_version = ip_version
        self.created_at = created_at
        self.updated_at = updated_at
        self.tenant_id = tenant_id
        self.enterprise_project_id = enterprise_project_id
        self.tags = tags
        self.status = status
        self.status_message = status_message

    @property
    def id(self):
        """Gets the id of this AddressGroup.

        功能说明：地址组唯一标识 取值范围：合法UUID的字符串 

        :return: The id of this AddressGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AddressGroup.

        功能说明：地址组唯一标识 取值范围：合法UUID的字符串 

        :param id: The id of this AddressGroup.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this AddressGroup.

        功能说明：地址组名称 取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this AddressGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddressGroup.

        功能说明：地址组名称 取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this AddressGroup.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this AddressGroup.

        功能说明：地址组描述信息 取值范围：0-255个字符 约束：不能包含“<”和“>”。

        :return: The description of this AddressGroup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AddressGroup.

        功能说明：地址组描述信息 取值范围：0-255个字符 约束：不能包含“<”和“>”。

        :param description: The description of this AddressGroup.
        :type description: str
        """
        self._description = description

    @property
    def max_capacity(self):
        """Gets the max_capacity of this AddressGroup.

        功能说明：地址组最大条目数，限制地址组可以包含的地址数量 取值范围：0-20 默认值：20

        :return: The max_capacity of this AddressGroup.
        :rtype: int
        """
        return self._max_capacity

    @max_capacity.setter
    def max_capacity(self, max_capacity):
        """Sets the max_capacity of this AddressGroup.

        功能说明：地址组最大条目数，限制地址组可以包含的地址数量 取值范围：0-20 默认值：20

        :param max_capacity: The max_capacity of this AddressGroup.
        :type max_capacity: int
        """
        self._max_capacity = max_capacity

    @property
    def ip_set(self):
        """Gets the ip_set of this AddressGroup.

        功能说明：地址组可包含地址集 取值范围：可以是单个ip地址，ip地址范围，ip地址cidr 约束：当前一个地址组ip_set数量限制默认值为20，即配置的ip地址、ip地址范围或ip地址cidr的总数默认限制20 

        :return: The ip_set of this AddressGroup.
        :rtype: list[str]
        """
        return self._ip_set

    @ip_set.setter
    def ip_set(self, ip_set):
        """Sets the ip_set of this AddressGroup.

        功能说明：地址组可包含地址集 取值范围：可以是单个ip地址，ip地址范围，ip地址cidr 约束：当前一个地址组ip_set数量限制默认值为20，即配置的ip地址、ip地址范围或ip地址cidr的总数默认限制20 

        :param ip_set: The ip_set of this AddressGroup.
        :type ip_set: list[str]
        """
        self._ip_set = ip_set

    @property
    def ip_version(self):
        """Gets the ip_version of this AddressGroup.

        功能说明：IP地址组ip版本 取值范围：4, 表示ipv4地址组；6, 表示ipv6地址组

        :return: The ip_version of this AddressGroup.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this AddressGroup.

        功能说明：IP地址组ip版本 取值范围：4, 表示ipv4地址组；6, 表示ipv6地址组

        :param ip_version: The ip_version of this AddressGroup.
        :type ip_version: int
        """
        self._ip_version = ip_version

    @property
    def created_at(self):
        """Gets the created_at of this AddressGroup.

        功能说明：地址组创建时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss；系统自动生成 

        :return: The created_at of this AddressGroup.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AddressGroup.

        功能说明：地址组创建时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss；系统自动生成 

        :param created_at: The created_at of this AddressGroup.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this AddressGroup.

        功能描述：地址组最近一次更新资源的时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss；系统自动生成

        :return: The updated_at of this AddressGroup.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AddressGroup.

        功能描述：地址组最近一次更新资源的时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss；系统自动生成

        :param updated_at: The updated_at of this AddressGroup.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def tenant_id(self):
        """Gets the tenant_id of this AddressGroup.

        功能说明：资源所属项目ID

        :return: The tenant_id of this AddressGroup.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this AddressGroup.

        功能说明：资源所属项目ID

        :param tenant_id: The tenant_id of this AddressGroup.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this AddressGroup.

        功能说明：企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。

        :return: The enterprise_project_id of this AddressGroup.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this AddressGroup.

        功能说明：企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。

        :param enterprise_project_id: The enterprise_project_id of this AddressGroup.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        """Gets the tags of this AddressGroup.

        IP地址组资源标签

        :return: The tags of this AddressGroup.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AddressGroup.

        IP地址组资源标签

        :param tags: The tags of this AddressGroup.
        :type tags: list[:class:`huaweicloudsdkvpc.v3.ResourceTag`]
        """
        self._tags = tags

    @property
    def status(self):
        """Gets the status of this AddressGroup.

        功能说明：地址组状态 取值范围：       NORMAL：正常       UPDATING：更新中       UPDATE_FAILED：更新失败 默认值：NORMAL 约束：当地址组处于UPDATING（更新中）状态时，不允许再次更新

        :return: The status of this AddressGroup.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AddressGroup.

        功能说明：地址组状态 取值范围：       NORMAL：正常       UPDATING：更新中       UPDATE_FAILED：更新失败 默认值：NORMAL 约束：当地址组处于UPDATING（更新中）状态时，不允许再次更新

        :param status: The status of this AddressGroup.
        :type status: str
        """
        self._status = status

    @property
    def status_message(self):
        """Gets the status_message of this AddressGroup.

        功能说明：地址组状态详情信息

        :return: The status_message of this AddressGroup.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this AddressGroup.

        功能说明：地址组状态详情信息

        :param status_message: The status_message of this AddressGroup.
        :type status_message: str
        """
        self._status_message = status_message

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
        if not isinstance(other, AddressGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
