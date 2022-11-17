# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeletePrivateZoneResponse(SdkResponse):

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
        'routers': 'list[RouterWithStatus]'
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
        'routers': 'routers'
    }

    def __init__(self, id=None, name=None, description=None, email=None, zone_type=None, ttl=None, serial=None, status=None, record_num=None, pool_id=None, project_id=None, created_at=None, updated_at=None, links=None, masters=None, routers=None):
        """DeletePrivateZoneResponse

        The model defined in huaweicloud sdk

        :param id: zone的ID，uuid形式的一个资源标识。
        :type id: str
        :param name: zone名称。
        :type name: str
        :param description: 对zone的描述信息。
        :type description: str
        :param email: 管理该zone的管理员邮箱。
        :type email: str
        :param zone_type: zone类型，公网（public）或者内网（private）。
        :type zone_type: str
        :param ttl: 该zone下SOA记录中的ttl值。
        :type ttl: int
        :param serial: 该zone下SOA记录中用于标识zone文件变更的序列值，用于主从节点同步。
        :type serial: int
        :param status: 状态
        :type status: str
        :param record_num: 该zone下的recordset个数。
        :type record_num: int
        :param pool_id: 托管该zone的pool，由系统分配。
        :type pool_id: str
        :param project_id: zone所属的项目ID。
        :type project_id: str
        :param created_at: 创建时间。
        :type created_at: str
        :param updated_at: 更新时间。
        :type updated_at: str
        :param links: 
        :type links: :class:`huaweicloudsdkdns.v2.PageLink`
        :param masters: 主从模式中，从DNS服务器用以获取DNS信息。
        :type masters: list[str]
        :param routers: 与该zone关联的Router(VPC)列表。
        :type routers: list[:class:`huaweicloudsdkdns.v2.RouterWithStatus`]
        """
        
        super(DeletePrivateZoneResponse, self).__init__()

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

    @property
    def id(self):
        """Gets the id of this DeletePrivateZoneResponse.

        zone的ID，uuid形式的一个资源标识。

        :return: The id of this DeletePrivateZoneResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeletePrivateZoneResponse.

        zone的ID，uuid形式的一个资源标识。

        :param id: The id of this DeletePrivateZoneResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this DeletePrivateZoneResponse.

        zone名称。

        :return: The name of this DeletePrivateZoneResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeletePrivateZoneResponse.

        zone名称。

        :param name: The name of this DeletePrivateZoneResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this DeletePrivateZoneResponse.

        对zone的描述信息。

        :return: The description of this DeletePrivateZoneResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeletePrivateZoneResponse.

        对zone的描述信息。

        :param description: The description of this DeletePrivateZoneResponse.
        :type description: str
        """
        self._description = description

    @property
    def email(self):
        """Gets the email of this DeletePrivateZoneResponse.

        管理该zone的管理员邮箱。

        :return: The email of this DeletePrivateZoneResponse.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this DeletePrivateZoneResponse.

        管理该zone的管理员邮箱。

        :param email: The email of this DeletePrivateZoneResponse.
        :type email: str
        """
        self._email = email

    @property
    def zone_type(self):
        """Gets the zone_type of this DeletePrivateZoneResponse.

        zone类型，公网（public）或者内网（private）。

        :return: The zone_type of this DeletePrivateZoneResponse.
        :rtype: str
        """
        return self._zone_type

    @zone_type.setter
    def zone_type(self, zone_type):
        """Sets the zone_type of this DeletePrivateZoneResponse.

        zone类型，公网（public）或者内网（private）。

        :param zone_type: The zone_type of this DeletePrivateZoneResponse.
        :type zone_type: str
        """
        self._zone_type = zone_type

    @property
    def ttl(self):
        """Gets the ttl of this DeletePrivateZoneResponse.

        该zone下SOA记录中的ttl值。

        :return: The ttl of this DeletePrivateZoneResponse.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this DeletePrivateZoneResponse.

        该zone下SOA记录中的ttl值。

        :param ttl: The ttl of this DeletePrivateZoneResponse.
        :type ttl: int
        """
        self._ttl = ttl

    @property
    def serial(self):
        """Gets the serial of this DeletePrivateZoneResponse.

        该zone下SOA记录中用于标识zone文件变更的序列值，用于主从节点同步。

        :return: The serial of this DeletePrivateZoneResponse.
        :rtype: int
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this DeletePrivateZoneResponse.

        该zone下SOA记录中用于标识zone文件变更的序列值，用于主从节点同步。

        :param serial: The serial of this DeletePrivateZoneResponse.
        :type serial: int
        """
        self._serial = serial

    @property
    def status(self):
        """Gets the status of this DeletePrivateZoneResponse.

        状态

        :return: The status of this DeletePrivateZoneResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DeletePrivateZoneResponse.

        状态

        :param status: The status of this DeletePrivateZoneResponse.
        :type status: str
        """
        self._status = status

    @property
    def record_num(self):
        """Gets the record_num of this DeletePrivateZoneResponse.

        该zone下的recordset个数。

        :return: The record_num of this DeletePrivateZoneResponse.
        :rtype: int
        """
        return self._record_num

    @record_num.setter
    def record_num(self, record_num):
        """Sets the record_num of this DeletePrivateZoneResponse.

        该zone下的recordset个数。

        :param record_num: The record_num of this DeletePrivateZoneResponse.
        :type record_num: int
        """
        self._record_num = record_num

    @property
    def pool_id(self):
        """Gets the pool_id of this DeletePrivateZoneResponse.

        托管该zone的pool，由系统分配。

        :return: The pool_id of this DeletePrivateZoneResponse.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this DeletePrivateZoneResponse.

        托管该zone的pool，由系统分配。

        :param pool_id: The pool_id of this DeletePrivateZoneResponse.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def project_id(self):
        """Gets the project_id of this DeletePrivateZoneResponse.

        zone所属的项目ID。

        :return: The project_id of this DeletePrivateZoneResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this DeletePrivateZoneResponse.

        zone所属的项目ID。

        :param project_id: The project_id of this DeletePrivateZoneResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def created_at(self):
        """Gets the created_at of this DeletePrivateZoneResponse.

        创建时间。

        :return: The created_at of this DeletePrivateZoneResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DeletePrivateZoneResponse.

        创建时间。

        :param created_at: The created_at of this DeletePrivateZoneResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this DeletePrivateZoneResponse.

        更新时间。

        :return: The updated_at of this DeletePrivateZoneResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this DeletePrivateZoneResponse.

        更新时间。

        :param updated_at: The updated_at of this DeletePrivateZoneResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def links(self):
        """Gets the links of this DeletePrivateZoneResponse.

        :return: The links of this DeletePrivateZoneResponse.
        :rtype: :class:`huaweicloudsdkdns.v2.PageLink`
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this DeletePrivateZoneResponse.

        :param links: The links of this DeletePrivateZoneResponse.
        :type links: :class:`huaweicloudsdkdns.v2.PageLink`
        """
        self._links = links

    @property
    def masters(self):
        """Gets the masters of this DeletePrivateZoneResponse.

        主从模式中，从DNS服务器用以获取DNS信息。

        :return: The masters of this DeletePrivateZoneResponse.
        :rtype: list[str]
        """
        return self._masters

    @masters.setter
    def masters(self, masters):
        """Sets the masters of this DeletePrivateZoneResponse.

        主从模式中，从DNS服务器用以获取DNS信息。

        :param masters: The masters of this DeletePrivateZoneResponse.
        :type masters: list[str]
        """
        self._masters = masters

    @property
    def routers(self):
        """Gets the routers of this DeletePrivateZoneResponse.

        与该zone关联的Router(VPC)列表。

        :return: The routers of this DeletePrivateZoneResponse.
        :rtype: list[:class:`huaweicloudsdkdns.v2.RouterWithStatus`]
        """
        return self._routers

    @routers.setter
    def routers(self, routers):
        """Sets the routers of this DeletePrivateZoneResponse.

        与该zone关联的Router(VPC)列表。

        :param routers: The routers of this DeletePrivateZoneResponse.
        :type routers: list[:class:`huaweicloudsdkdns.v2.RouterWithStatus`]
        """
        self._routers = routers

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
        if not isinstance(other, DeletePrivateZoneResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
