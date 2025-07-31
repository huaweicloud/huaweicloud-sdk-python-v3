# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ZoneData:

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
        'ttl': 'int',
        'serial': 'int',
        'masters': 'list[str]',
        'status': 'str',
        'pool_id': 'str',
        'project_id': 'str',
        'zone_type': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'record_num': 'int',
        'links': 'Link'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'email': 'email',
        'ttl': 'ttl',
        'serial': 'serial',
        'masters': 'masters',
        'status': 'status',
        'pool_id': 'pool_id',
        'project_id': 'project_id',
        'zone_type': 'zone_type',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'record_num': 'record_num',
        'links': 'links'
    }

    def __init__(self, id=None, name=None, description=None, email=None, ttl=None, serial=None, masters=None, status=None, pool_id=None, project_id=None, zone_type=None, created_at=None, updated_at=None, record_num=None, links=None):
        r"""ZoneData

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 域名的ID，UUID形式的一个资源标识。 **取值范围：** 不涉及。
        :type id: str
        :param name: **参数解释：** 域名。 **取值范围：** 不涉及。
        :type name: str
        :param description: **参数解释：** 对域名的描述信息。 **取值范围：** 长度不超过255个字符。
        :type description: str
        :param email: **参数解释：** 管理该域名的管理员邮箱，用于生成该域名的SOA记录。 **取值范围：** 不涉及。
        :type email: str
        :param ttl: **参数解释：** 该域名下SOA记录中的有效缓存时间，以秒为单位。 **取值范围：** 1~2147483647。
        :type ttl: int
        :param serial: **参数解释：** 该域名下SOA记录中用于标识域名文件变更的序列值，用于主从节点同步。 该参数暂未使用。 **取值范围：** 不涉及。
        :type serial: int
        :param masters: **参数解释：** 主从模式中，从DNS服务器获取DNS信息。 目前暂未使用。 **取值范围：** 不涉及。
        :type masters: list[str]
        :param status: **参数解释：** 域名状态。 **取值范围：** - ACTIVE：正常 - PENDING_CREATE：创建中 - PENDING_UPDATE：更新中 - PENDING_DELETE：删除中 - PENDING_FREEZE：冻结中 - FREEZE：冻结 - ILLEGAL：违规冻结 - POLICE：公安冻结 - PENDING_DISABLE：暂停中 - DISABLE：暂停 - ERROR：失败
        :type status: str
        :param pool_id: **参数解释：** 托管该域名的pool，由系统分配。 **取值范围：** 不涉及。
        :type pool_id: str
        :param project_id: **参数解释：** 域名所属的项目ID。 **取值范围：** 不涉及。
        :type project_id: str
        :param zone_type: **参数解释：** 域名类型。 **取值范围：** - public：公网域名 - private：内网域名
        :type zone_type: str
        :param created_at: **参数解释：** 创建时间。 格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS。 **取值范围：** 不涉及。
        :type created_at: str
        :param updated_at: **参数解释：** 更新时间。 格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS。 **取值范围：** 不涉及。
        :type updated_at: str
        :param record_num: **参数解释：** 该域名下的记录集个数。 **取值范围：** 不涉及。
        :type record_num: int
        :param links: 
        :type links: :class:`huaweicloudsdkdns.v2.Link`
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._email = None
        self._ttl = None
        self._serial = None
        self._masters = None
        self._status = None
        self._pool_id = None
        self._project_id = None
        self._zone_type = None
        self._created_at = None
        self._updated_at = None
        self._record_num = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if email is not None:
            self.email = email
        if ttl is not None:
            self.ttl = ttl
        if serial is not None:
            self.serial = serial
        if masters is not None:
            self.masters = masters
        if status is not None:
            self.status = status
        if pool_id is not None:
            self.pool_id = pool_id
        if project_id is not None:
            self.project_id = project_id
        if zone_type is not None:
            self.zone_type = zone_type
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if record_num is not None:
            self.record_num = record_num
        if links is not None:
            self.links = links

    @property
    def id(self):
        r"""Gets the id of this ZoneData.

        **参数解释：** 域名的ID，UUID形式的一个资源标识。 **取值范围：** 不涉及。

        :return: The id of this ZoneData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ZoneData.

        **参数解释：** 域名的ID，UUID形式的一个资源标识。 **取值范围：** 不涉及。

        :param id: The id of this ZoneData.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ZoneData.

        **参数解释：** 域名。 **取值范围：** 不涉及。

        :return: The name of this ZoneData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ZoneData.

        **参数解释：** 域名。 **取值范围：** 不涉及。

        :param name: The name of this ZoneData.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ZoneData.

        **参数解释：** 对域名的描述信息。 **取值范围：** 长度不超过255个字符。

        :return: The description of this ZoneData.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ZoneData.

        **参数解释：** 对域名的描述信息。 **取值范围：** 长度不超过255个字符。

        :param description: The description of this ZoneData.
        :type description: str
        """
        self._description = description

    @property
    def email(self):
        r"""Gets the email of this ZoneData.

        **参数解释：** 管理该域名的管理员邮箱，用于生成该域名的SOA记录。 **取值范围：** 不涉及。

        :return: The email of this ZoneData.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this ZoneData.

        **参数解释：** 管理该域名的管理员邮箱，用于生成该域名的SOA记录。 **取值范围：** 不涉及。

        :param email: The email of this ZoneData.
        :type email: str
        """
        self._email = email

    @property
    def ttl(self):
        r"""Gets the ttl of this ZoneData.

        **参数解释：** 该域名下SOA记录中的有效缓存时间，以秒为单位。 **取值范围：** 1~2147483647。

        :return: The ttl of this ZoneData.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        r"""Sets the ttl of this ZoneData.

        **参数解释：** 该域名下SOA记录中的有效缓存时间，以秒为单位。 **取值范围：** 1~2147483647。

        :param ttl: The ttl of this ZoneData.
        :type ttl: int
        """
        self._ttl = ttl

    @property
    def serial(self):
        r"""Gets the serial of this ZoneData.

        **参数解释：** 该域名下SOA记录中用于标识域名文件变更的序列值，用于主从节点同步。 该参数暂未使用。 **取值范围：** 不涉及。

        :return: The serial of this ZoneData.
        :rtype: int
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        r"""Sets the serial of this ZoneData.

        **参数解释：** 该域名下SOA记录中用于标识域名文件变更的序列值，用于主从节点同步。 该参数暂未使用。 **取值范围：** 不涉及。

        :param serial: The serial of this ZoneData.
        :type serial: int
        """
        self._serial = serial

    @property
    def masters(self):
        r"""Gets the masters of this ZoneData.

        **参数解释：** 主从模式中，从DNS服务器获取DNS信息。 目前暂未使用。 **取值范围：** 不涉及。

        :return: The masters of this ZoneData.
        :rtype: list[str]
        """
        return self._masters

    @masters.setter
    def masters(self, masters):
        r"""Sets the masters of this ZoneData.

        **参数解释：** 主从模式中，从DNS服务器获取DNS信息。 目前暂未使用。 **取值范围：** 不涉及。

        :param masters: The masters of this ZoneData.
        :type masters: list[str]
        """
        self._masters = masters

    @property
    def status(self):
        r"""Gets the status of this ZoneData.

        **参数解释：** 域名状态。 **取值范围：** - ACTIVE：正常 - PENDING_CREATE：创建中 - PENDING_UPDATE：更新中 - PENDING_DELETE：删除中 - PENDING_FREEZE：冻结中 - FREEZE：冻结 - ILLEGAL：违规冻结 - POLICE：公安冻结 - PENDING_DISABLE：暂停中 - DISABLE：暂停 - ERROR：失败

        :return: The status of this ZoneData.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ZoneData.

        **参数解释：** 域名状态。 **取值范围：** - ACTIVE：正常 - PENDING_CREATE：创建中 - PENDING_UPDATE：更新中 - PENDING_DELETE：删除中 - PENDING_FREEZE：冻结中 - FREEZE：冻结 - ILLEGAL：违规冻结 - POLICE：公安冻结 - PENDING_DISABLE：暂停中 - DISABLE：暂停 - ERROR：失败

        :param status: The status of this ZoneData.
        :type status: str
        """
        self._status = status

    @property
    def pool_id(self):
        r"""Gets the pool_id of this ZoneData.

        **参数解释：** 托管该域名的pool，由系统分配。 **取值范围：** 不涉及。

        :return: The pool_id of this ZoneData.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this ZoneData.

        **参数解释：** 托管该域名的pool，由系统分配。 **取值范围：** 不涉及。

        :param pool_id: The pool_id of this ZoneData.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ZoneData.

        **参数解释：** 域名所属的项目ID。 **取值范围：** 不涉及。

        :return: The project_id of this ZoneData.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ZoneData.

        **参数解释：** 域名所属的项目ID。 **取值范围：** 不涉及。

        :param project_id: The project_id of this ZoneData.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def zone_type(self):
        r"""Gets the zone_type of this ZoneData.

        **参数解释：** 域名类型。 **取值范围：** - public：公网域名 - private：内网域名

        :return: The zone_type of this ZoneData.
        :rtype: str
        """
        return self._zone_type

    @zone_type.setter
    def zone_type(self, zone_type):
        r"""Sets the zone_type of this ZoneData.

        **参数解释：** 域名类型。 **取值范围：** - public：公网域名 - private：内网域名

        :param zone_type: The zone_type of this ZoneData.
        :type zone_type: str
        """
        self._zone_type = zone_type

    @property
    def created_at(self):
        r"""Gets the created_at of this ZoneData.

        **参数解释：** 创建时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。 **取值范围：** 不涉及。

        :return: The created_at of this ZoneData.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ZoneData.

        **参数解释：** 创建时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。 **取值范围：** 不涉及。

        :param created_at: The created_at of this ZoneData.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ZoneData.

        **参数解释：** 更新时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。 **取值范围：** 不涉及。

        :return: The updated_at of this ZoneData.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ZoneData.

        **参数解释：** 更新时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。 **取值范围：** 不涉及。

        :param updated_at: The updated_at of this ZoneData.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def record_num(self):
        r"""Gets the record_num of this ZoneData.

        **参数解释：** 该域名下的记录集个数。 **取值范围：** 不涉及。

        :return: The record_num of this ZoneData.
        :rtype: int
        """
        return self._record_num

    @record_num.setter
    def record_num(self, record_num):
        r"""Sets the record_num of this ZoneData.

        **参数解释：** 该域名下的记录集个数。 **取值范围：** 不涉及。

        :param record_num: The record_num of this ZoneData.
        :type record_num: int
        """
        self._record_num = record_num

    @property
    def links(self):
        r"""Gets the links of this ZoneData.

        :return: The links of this ZoneData.
        :rtype: :class:`huaweicloudsdkdns.v2.Link`
        """
        return self._links

    @links.setter
    def links(self, links):
        r"""Sets the links of this ZoneData.

        :param links: The links of this ZoneData.
        :type links: :class:`huaweicloudsdkdns.v2.Link`
        """
        self._links = links

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
        if not isinstance(other, ZoneData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
