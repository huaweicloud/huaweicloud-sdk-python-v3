# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RouteTableListResp:

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
        'default': 'bool',
        'subnets': 'list[SubnetList]',
        'tenant_id': 'str',
        'vpc_id': 'str',
        'description': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'default': 'default',
        'subnets': 'subnets',
        'tenant_id': 'tenant_id',
        'vpc_id': 'vpc_id',
        'description': 'description',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, default=None, subnets=None, tenant_id=None, vpc_id=None, description=None, created_at=None, updated_at=None):
        """RouteTableListResp

        The model defined in huaweicloud sdk

        :param id: 功能说明：路由表ID  取值范围：标准UUID
        :type id: str
        :param name: 功能说明：路由表名称  取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param default: 功能说明：是否为默认路由表  取值范围：true表示默认路由表；false表示自定义路由表
        :type default: bool
        :param subnets: 功能说明：路由表所关联的子网  约束：只能关联路由表所属VPC下的子网
        :type subnets: list[:class:`huaweicloudsdkvpc.v2.SubnetList`]
        :param tenant_id: 项目ID
        :type tenant_id: str
        :param vpc_id: 路由表所在的虚拟私有云ID
        :type vpc_id: str
        :param description: 功能说明：路由表描述信息  取值范围：0-255个字符，不能包含“&lt;”和“&gt;”
        :type description: str
        :param created_at: 功能说明：资源创建UTC时间 格式：yyyy-MM-ddTHH:mm:ss
        :type created_at: datetime
        :param updated_at: 功能说明：资源更新UTC时间 格式：yyyy-MM-ddTHH:mm:ss
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._name = None
        self._default = None
        self._subnets = None
        self._tenant_id = None
        self._vpc_id = None
        self._description = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.default = default
        self.subnets = subnets
        self.tenant_id = tenant_id
        self.vpc_id = vpc_id
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this RouteTableListResp.

        功能说明：路由表ID  取值范围：标准UUID

        :return: The id of this RouteTableListResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RouteTableListResp.

        功能说明：路由表ID  取值范围：标准UUID

        :param id: The id of this RouteTableListResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this RouteTableListResp.

        功能说明：路由表名称  取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this RouteTableListResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RouteTableListResp.

        功能说明：路由表名称  取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this RouteTableListResp.
        :type name: str
        """
        self._name = name

    @property
    def default(self):
        """Gets the default of this RouteTableListResp.

        功能说明：是否为默认路由表  取值范围：true表示默认路由表；false表示自定义路由表

        :return: The default of this RouteTableListResp.
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this RouteTableListResp.

        功能说明：是否为默认路由表  取值范围：true表示默认路由表；false表示自定义路由表

        :param default: The default of this RouteTableListResp.
        :type default: bool
        """
        self._default = default

    @property
    def subnets(self):
        """Gets the subnets of this RouteTableListResp.

        功能说明：路由表所关联的子网  约束：只能关联路由表所属VPC下的子网

        :return: The subnets of this RouteTableListResp.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.SubnetList`]
        """
        return self._subnets

    @subnets.setter
    def subnets(self, subnets):
        """Sets the subnets of this RouteTableListResp.

        功能说明：路由表所关联的子网  约束：只能关联路由表所属VPC下的子网

        :param subnets: The subnets of this RouteTableListResp.
        :type subnets: list[:class:`huaweicloudsdkvpc.v2.SubnetList`]
        """
        self._subnets = subnets

    @property
    def tenant_id(self):
        """Gets the tenant_id of this RouteTableListResp.

        项目ID

        :return: The tenant_id of this RouteTableListResp.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this RouteTableListResp.

        项目ID

        :param tenant_id: The tenant_id of this RouteTableListResp.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this RouteTableListResp.

        路由表所在的虚拟私有云ID

        :return: The vpc_id of this RouteTableListResp.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this RouteTableListResp.

        路由表所在的虚拟私有云ID

        :param vpc_id: The vpc_id of this RouteTableListResp.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def description(self):
        """Gets the description of this RouteTableListResp.

        功能说明：路由表描述信息  取值范围：0-255个字符，不能包含“<”和“>”

        :return: The description of this RouteTableListResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RouteTableListResp.

        功能说明：路由表描述信息  取值范围：0-255个字符，不能包含“<”和“>”

        :param description: The description of this RouteTableListResp.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this RouteTableListResp.

        功能说明：资源创建UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :return: The created_at of this RouteTableListResp.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this RouteTableListResp.

        功能说明：资源创建UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :param created_at: The created_at of this RouteTableListResp.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this RouteTableListResp.

        功能说明：资源更新UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :return: The updated_at of this RouteTableListResp.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this RouteTableListResp.

        功能说明：资源更新UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :param updated_at: The updated_at of this RouteTableListResp.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, RouteTableListResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
