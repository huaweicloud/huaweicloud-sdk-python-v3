# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePrivateZoneResponse(SdkResponse):

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
        'proxy_pattern': 'str',
        'pool_id': 'str',
        'project_id': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'links': 'PageLink',
        'masters': 'list[str]',
        'router': 'RouterWithStatus'
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
        'proxy_pattern': 'proxy_pattern',
        'pool_id': 'pool_id',
        'project_id': 'project_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'links': 'links',
        'masters': 'masters',
        'router': 'router'
    }

    def __init__(self, id=None, name=None, description=None, email=None, zone_type=None, ttl=None, serial=None, status=None, record_num=None, proxy_pattern=None, pool_id=None, project_id=None, created_at=None, updated_at=None, links=None, masters=None, router=None):
        r"""CreatePrivateZoneResponse

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
        :param serial: 该域名下SOA记录中用于标识域名文件变更的序列值，用于主从节点同步。  该参数暂未使用。
        :type serial: int
        :param status: 资源状态。
        :type status: str
        :param record_num: 该域名下的记录集个数。
        :type record_num: int
        :param proxy_pattern: 内网域名的子域名递归解析代理模式。  取值范围：  AUTHORITY：当前域名未开启递归解析代理 RECURSIVE：当前域名已开启递归解析代理
        :type proxy_pattern: str
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
        :param router: 
        :type router: :class:`huaweicloudsdkdns.v2.RouterWithStatus`
        """
        
        super(CreatePrivateZoneResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._email = None
        self._zone_type = None
        self._ttl = None
        self._serial = None
        self._status = None
        self._record_num = None
        self._proxy_pattern = None
        self._pool_id = None
        self._project_id = None
        self._created_at = None
        self._updated_at = None
        self._links = None
        self._masters = None
        self._router = None
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
        if proxy_pattern is not None:
            self.proxy_pattern = proxy_pattern
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
        if router is not None:
            self.router = router

    @property
    def id(self):
        r"""Gets the id of this CreatePrivateZoneResponse.

        域名的ID，UUID形式的一个资源标识。

        :return: The id of this CreatePrivateZoneResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreatePrivateZoneResponse.

        域名的ID，UUID形式的一个资源标识。

        :param id: The id of this CreatePrivateZoneResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CreatePrivateZoneResponse.

        域名。

        :return: The name of this CreatePrivateZoneResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreatePrivateZoneResponse.

        域名。

        :param name: The name of this CreatePrivateZoneResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreatePrivateZoneResponse.

        对域名的描述信息。

        :return: The description of this CreatePrivateZoneResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreatePrivateZoneResponse.

        对域名的描述信息。

        :param description: The description of this CreatePrivateZoneResponse.
        :type description: str
        """
        self._description = description

    @property
    def email(self):
        r"""Gets the email of this CreatePrivateZoneResponse.

        管理该域名的管理员邮箱，用于生成该域名的SOA记录。

        :return: The email of this CreatePrivateZoneResponse.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this CreatePrivateZoneResponse.

        管理该域名的管理员邮箱，用于生成该域名的SOA记录。

        :param email: The email of this CreatePrivateZoneResponse.
        :type email: str
        """
        self._email = email

    @property
    def zone_type(self):
        r"""Gets the zone_type of this CreatePrivateZoneResponse.

        域名类型，内网（private）。

        :return: The zone_type of this CreatePrivateZoneResponse.
        :rtype: str
        """
        return self._zone_type

    @zone_type.setter
    def zone_type(self, zone_type):
        r"""Sets the zone_type of this CreatePrivateZoneResponse.

        域名类型，内网（private）。

        :param zone_type: The zone_type of this CreatePrivateZoneResponse.
        :type zone_type: str
        """
        self._zone_type = zone_type

    @property
    def ttl(self):
        r"""Gets the ttl of this CreatePrivateZoneResponse.

        该域名下SOA记录中的ttl值。

        :return: The ttl of this CreatePrivateZoneResponse.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        r"""Sets the ttl of this CreatePrivateZoneResponse.

        该域名下SOA记录中的ttl值。

        :param ttl: The ttl of this CreatePrivateZoneResponse.
        :type ttl: int
        """
        self._ttl = ttl

    @property
    def serial(self):
        r"""Gets the serial of this CreatePrivateZoneResponse.

        该域名下SOA记录中用于标识域名文件变更的序列值，用于主从节点同步。  该参数暂未使用。

        :return: The serial of this CreatePrivateZoneResponse.
        :rtype: int
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        r"""Sets the serial of this CreatePrivateZoneResponse.

        该域名下SOA记录中用于标识域名文件变更的序列值，用于主从节点同步。  该参数暂未使用。

        :param serial: The serial of this CreatePrivateZoneResponse.
        :type serial: int
        """
        self._serial = serial

    @property
    def status(self):
        r"""Gets the status of this CreatePrivateZoneResponse.

        资源状态。

        :return: The status of this CreatePrivateZoneResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreatePrivateZoneResponse.

        资源状态。

        :param status: The status of this CreatePrivateZoneResponse.
        :type status: str
        """
        self._status = status

    @property
    def record_num(self):
        r"""Gets the record_num of this CreatePrivateZoneResponse.

        该域名下的记录集个数。

        :return: The record_num of this CreatePrivateZoneResponse.
        :rtype: int
        """
        return self._record_num

    @record_num.setter
    def record_num(self, record_num):
        r"""Sets the record_num of this CreatePrivateZoneResponse.

        该域名下的记录集个数。

        :param record_num: The record_num of this CreatePrivateZoneResponse.
        :type record_num: int
        """
        self._record_num = record_num

    @property
    def proxy_pattern(self):
        r"""Gets the proxy_pattern of this CreatePrivateZoneResponse.

        内网域名的子域名递归解析代理模式。  取值范围：  AUTHORITY：当前域名未开启递归解析代理 RECURSIVE：当前域名已开启递归解析代理

        :return: The proxy_pattern of this CreatePrivateZoneResponse.
        :rtype: str
        """
        return self._proxy_pattern

    @proxy_pattern.setter
    def proxy_pattern(self, proxy_pattern):
        r"""Sets the proxy_pattern of this CreatePrivateZoneResponse.

        内网域名的子域名递归解析代理模式。  取值范围：  AUTHORITY：当前域名未开启递归解析代理 RECURSIVE：当前域名已开启递归解析代理

        :param proxy_pattern: The proxy_pattern of this CreatePrivateZoneResponse.
        :type proxy_pattern: str
        """
        self._proxy_pattern = proxy_pattern

    @property
    def pool_id(self):
        r"""Gets the pool_id of this CreatePrivateZoneResponse.

        托管该域名的pool，由系统分配。

        :return: The pool_id of this CreatePrivateZoneResponse.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this CreatePrivateZoneResponse.

        托管该域名的pool，由系统分配。

        :param pool_id: The pool_id of this CreatePrivateZoneResponse.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def project_id(self):
        r"""Gets the project_id of this CreatePrivateZoneResponse.

        域名所属的项目ID。

        :return: The project_id of this CreatePrivateZoneResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CreatePrivateZoneResponse.

        域名所属的项目ID。

        :param project_id: The project_id of this CreatePrivateZoneResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def created_at(self):
        r"""Gets the created_at of this CreatePrivateZoneResponse.

        创建时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :return: The created_at of this CreatePrivateZoneResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CreatePrivateZoneResponse.

        创建时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :param created_at: The created_at of this CreatePrivateZoneResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this CreatePrivateZoneResponse.

        更新时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :return: The updated_at of this CreatePrivateZoneResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this CreatePrivateZoneResponse.

        更新时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :param updated_at: The updated_at of this CreatePrivateZoneResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def links(self):
        r"""Gets the links of this CreatePrivateZoneResponse.

        :return: The links of this CreatePrivateZoneResponse.
        :rtype: :class:`huaweicloudsdkdns.v2.PageLink`
        """
        return self._links

    @links.setter
    def links(self, links):
        r"""Sets the links of this CreatePrivateZoneResponse.

        :param links: The links of this CreatePrivateZoneResponse.
        :type links: :class:`huaweicloudsdkdns.v2.PageLink`
        """
        self._links = links

    @property
    def masters(self):
        r"""Gets the masters of this CreatePrivateZoneResponse.

        主从模式中，从DNS服务器获取DNS信息。

        :return: The masters of this CreatePrivateZoneResponse.
        :rtype: list[str]
        """
        return self._masters

    @masters.setter
    def masters(self, masters):
        r"""Sets the masters of this CreatePrivateZoneResponse.

        主从模式中，从DNS服务器获取DNS信息。

        :param masters: The masters of this CreatePrivateZoneResponse.
        :type masters: list[str]
        """
        self._masters = masters

    @property
    def router(self):
        r"""Gets the router of this CreatePrivateZoneResponse.

        :return: The router of this CreatePrivateZoneResponse.
        :rtype: :class:`huaweicloudsdkdns.v2.RouterWithStatus`
        """
        return self._router

    @router.setter
    def router(self, router):
        r"""Sets the router of this CreatePrivateZoneResponse.

        :param router: The router of this CreatePrivateZoneResponse.
        :type router: :class:`huaweicloudsdkdns.v2.RouterWithStatus`
        """
        self._router = router

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
        if not isinstance(other, CreatePrivateZoneResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
