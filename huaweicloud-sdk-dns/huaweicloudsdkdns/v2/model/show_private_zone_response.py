# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPrivateZoneResponse(SdkResponse):

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
        'email': 'str',
        'zone_type': 'str',
        'ttl': 'int',
        'serial': 'int',
        'status': 'str',
        'record_num': 'int',
        'pool_id': 'str',
        'project_id': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'links': 'PageLink',
        'masters': 'list[str]',
        'routers': 'list[Router]',
        'proxy_pattern': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'email': 'email',
        'zone_type': 'zone_type',
        'ttl': 'ttl',
        'serial': 'serial',
        'status': 'status',
        'record_num': 'record_num',
        'pool_id': 'pool_id',
        'project_id': 'project_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'links': 'links',
        'masters': 'masters',
        'routers': 'routers',
        'proxy_pattern': 'proxy_pattern',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, id=None, name=None, description=None, email=None, zone_type=None, ttl=None, serial=None, status=None, record_num=None, pool_id=None, project_id=None, created_at=None, updated_at=None, links=None, masters=None, routers=None, proxy_pattern=None, enterprise_project_id=None):
        r"""ShowPrivateZoneResponse

        The model defined in huaweicloud sdk

        :param id: 域名的ID，UUID形式的一个资源标识。
        :type id: str
        :param name: 域名。
        :type name: str
        :param description: 对域名的描述信息。
        :type description: str
        :param email: 管理该域名的管理员邮箱，用于生成该域名的SOA记录。
        :type email: str
        :param zone_type: 域名类型，内网（private）。
        :type zone_type: str
        :param ttl: 该域名下SOA记录中的ttl值。
        :type ttl: int
        :param serial: 该域名下SOA记录中用于标识域名文件变更的序列值，用于主从节点同步。
        :type serial: int
        :param status: 资源状态。
        :type status: str
        :param record_num: 该域名下的记录集个数。
        :type record_num: int
        :param pool_id: 托管该域名的pool，由系统分配。
        :type pool_id: str
        :param project_id: 域名所属的项目ID。
        :type project_id: str
        :param created_at: 创建时间。 格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS。
        :type created_at: str
        :param updated_at: 更新时间。 格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS。
        :type updated_at: str
        :param links: 
        :type links: :class:`huaweicloudsdkdns.v2.PageLink`
        :param masters: 主从模式中，从DNS服务器获取DNS信息。
        :type masters: list[str]
        :param routers: 与该域名关联的Router(VPC)列表。
        :type routers: list[:class:`huaweicloudsdkdns.v2.Router`]
        :param proxy_pattern: 内网域名的子域名递归解析代理模式。  取值范围：  AUTHORITY：当前域名未开启递归解析代理 RECURSIVE：当前域名已开启递归解析代理
        :type proxy_pattern: str
        :param enterprise_project_id: 域名关联的企业项目ID，长度不超过36个字符。
        :type enterprise_project_id: str
        """
        
        super(ShowPrivateZoneResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._email = None
        self._zone_type = None
        self._ttl = None
        self._serial = None
        self._status = None
        self._record_num = None
        self._pool_id = None
        self._project_id = None
        self._created_at = None
        self._updated_at = None
        self._links = None
        self._masters = None
        self._routers = None
        self._proxy_pattern = None
        self._enterprise_project_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if email is not None:
            self.email = email
        if zone_type is not None:
            self.zone_type = zone_type
        if ttl is not None:
            self.ttl = ttl
        if serial is not None:
            self.serial = serial
        if status is not None:
            self.status = status
        if record_num is not None:
            self.record_num = record_num
        if pool_id is not None:
            self.pool_id = pool_id
        if project_id is not None:
            self.project_id = project_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if links is not None:
            self.links = links
        if masters is not None:
            self.masters = masters
        if routers is not None:
            self.routers = routers
        if proxy_pattern is not None:
            self.proxy_pattern = proxy_pattern
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        r"""Gets the id of this ShowPrivateZoneResponse.

        域名的ID，UUID形式的一个资源标识。

        :return: The id of this ShowPrivateZoneResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowPrivateZoneResponse.

        域名的ID，UUID形式的一个资源标识。

        :param id: The id of this ShowPrivateZoneResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowPrivateZoneResponse.

        域名。

        :return: The name of this ShowPrivateZoneResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowPrivateZoneResponse.

        域名。

        :param name: The name of this ShowPrivateZoneResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ShowPrivateZoneResponse.

        对域名的描述信息。

        :return: The description of this ShowPrivateZoneResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowPrivateZoneResponse.

        对域名的描述信息。

        :param description: The description of this ShowPrivateZoneResponse.
        :type description: str
        """
        self._description = description

    @property
    def email(self):
        r"""Gets the email of this ShowPrivateZoneResponse.

        管理该域名的管理员邮箱，用于生成该域名的SOA记录。

        :return: The email of this ShowPrivateZoneResponse.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this ShowPrivateZoneResponse.

        管理该域名的管理员邮箱，用于生成该域名的SOA记录。

        :param email: The email of this ShowPrivateZoneResponse.
        :type email: str
        """
        self._email = email

    @property
    def zone_type(self):
        r"""Gets the zone_type of this ShowPrivateZoneResponse.

        域名类型，内网（private）。

        :return: The zone_type of this ShowPrivateZoneResponse.
        :rtype: str
        """
        return self._zone_type

    @zone_type.setter
    def zone_type(self, zone_type):
        r"""Sets the zone_type of this ShowPrivateZoneResponse.

        域名类型，内网（private）。

        :param zone_type: The zone_type of this ShowPrivateZoneResponse.
        :type zone_type: str
        """
        self._zone_type = zone_type

    @property
    def ttl(self):
        r"""Gets the ttl of this ShowPrivateZoneResponse.

        该域名下SOA记录中的ttl值。

        :return: The ttl of this ShowPrivateZoneResponse.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        r"""Sets the ttl of this ShowPrivateZoneResponse.

        该域名下SOA记录中的ttl值。

        :param ttl: The ttl of this ShowPrivateZoneResponse.
        :type ttl: int
        """
        self._ttl = ttl

    @property
    def serial(self):
        r"""Gets the serial of this ShowPrivateZoneResponse.

        该域名下SOA记录中用于标识域名文件变更的序列值，用于主从节点同步。

        :return: The serial of this ShowPrivateZoneResponse.
        :rtype: int
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        r"""Sets the serial of this ShowPrivateZoneResponse.

        该域名下SOA记录中用于标识域名文件变更的序列值，用于主从节点同步。

        :param serial: The serial of this ShowPrivateZoneResponse.
        :type serial: int
        """
        self._serial = serial

    @property
    def status(self):
        r"""Gets the status of this ShowPrivateZoneResponse.

        资源状态。

        :return: The status of this ShowPrivateZoneResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowPrivateZoneResponse.

        资源状态。

        :param status: The status of this ShowPrivateZoneResponse.
        :type status: str
        """
        self._status = status

    @property
    def record_num(self):
        r"""Gets the record_num of this ShowPrivateZoneResponse.

        该域名下的记录集个数。

        :return: The record_num of this ShowPrivateZoneResponse.
        :rtype: int
        """
        return self._record_num

    @record_num.setter
    def record_num(self, record_num):
        r"""Sets the record_num of this ShowPrivateZoneResponse.

        该域名下的记录集个数。

        :param record_num: The record_num of this ShowPrivateZoneResponse.
        :type record_num: int
        """
        self._record_num = record_num

    @property
    def pool_id(self):
        r"""Gets the pool_id of this ShowPrivateZoneResponse.

        托管该域名的pool，由系统分配。

        :return: The pool_id of this ShowPrivateZoneResponse.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this ShowPrivateZoneResponse.

        托管该域名的pool，由系统分配。

        :param pool_id: The pool_id of this ShowPrivateZoneResponse.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowPrivateZoneResponse.

        域名所属的项目ID。

        :return: The project_id of this ShowPrivateZoneResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowPrivateZoneResponse.

        域名所属的项目ID。

        :param project_id: The project_id of this ShowPrivateZoneResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowPrivateZoneResponse.

        创建时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :return: The created_at of this ShowPrivateZoneResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowPrivateZoneResponse.

        创建时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :param created_at: The created_at of this ShowPrivateZoneResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ShowPrivateZoneResponse.

        更新时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :return: The updated_at of this ShowPrivateZoneResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ShowPrivateZoneResponse.

        更新时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :param updated_at: The updated_at of this ShowPrivateZoneResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def links(self):
        r"""Gets the links of this ShowPrivateZoneResponse.

        :return: The links of this ShowPrivateZoneResponse.
        :rtype: :class:`huaweicloudsdkdns.v2.PageLink`
        """
        return self._links

    @links.setter
    def links(self, links):
        r"""Sets the links of this ShowPrivateZoneResponse.

        :param links: The links of this ShowPrivateZoneResponse.
        :type links: :class:`huaweicloudsdkdns.v2.PageLink`
        """
        self._links = links

    @property
    def masters(self):
        r"""Gets the masters of this ShowPrivateZoneResponse.

        主从模式中，从DNS服务器获取DNS信息。

        :return: The masters of this ShowPrivateZoneResponse.
        :rtype: list[str]
        """
        return self._masters

    @masters.setter
    def masters(self, masters):
        r"""Sets the masters of this ShowPrivateZoneResponse.

        主从模式中，从DNS服务器获取DNS信息。

        :param masters: The masters of this ShowPrivateZoneResponse.
        :type masters: list[str]
        """
        self._masters = masters

    @property
    def routers(self):
        r"""Gets the routers of this ShowPrivateZoneResponse.

        与该域名关联的Router(VPC)列表。

        :return: The routers of this ShowPrivateZoneResponse.
        :rtype: list[:class:`huaweicloudsdkdns.v2.Router`]
        """
        return self._routers

    @routers.setter
    def routers(self, routers):
        r"""Sets the routers of this ShowPrivateZoneResponse.

        与该域名关联的Router(VPC)列表。

        :param routers: The routers of this ShowPrivateZoneResponse.
        :type routers: list[:class:`huaweicloudsdkdns.v2.Router`]
        """
        self._routers = routers

    @property
    def proxy_pattern(self):
        r"""Gets the proxy_pattern of this ShowPrivateZoneResponse.

        内网域名的子域名递归解析代理模式。  取值范围：  AUTHORITY：当前域名未开启递归解析代理 RECURSIVE：当前域名已开启递归解析代理

        :return: The proxy_pattern of this ShowPrivateZoneResponse.
        :rtype: str
        """
        return self._proxy_pattern

    @proxy_pattern.setter
    def proxy_pattern(self, proxy_pattern):
        r"""Sets the proxy_pattern of this ShowPrivateZoneResponse.

        内网域名的子域名递归解析代理模式。  取值范围：  AUTHORITY：当前域名未开启递归解析代理 RECURSIVE：当前域名已开启递归解析代理

        :param proxy_pattern: The proxy_pattern of this ShowPrivateZoneResponse.
        :type proxy_pattern: str
        """
        self._proxy_pattern = proxy_pattern

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowPrivateZoneResponse.

        域名关联的企业项目ID，长度不超过36个字符。

        :return: The enterprise_project_id of this ShowPrivateZoneResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowPrivateZoneResponse.

        域名关联的企业项目ID，长度不超过36个字符。

        :param enterprise_project_id: The enterprise_project_id of this ShowPrivateZoneResponse.
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
        if not isinstance(other, ShowPrivateZoneResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
