# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecordsetData:

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
        'type': 'str',
        'ttl': 'int',
        'records': 'list[str]',
        'status': 'str',
        'zone_id': 'str',
        'zone_name': 'str',
        'line': 'str',
        'alias_target': 'AliasTarget',
        'created_at': 'str',
        'updated_at': 'str',
        'health_check_id': 'str',
        'default': 'bool',
        'project_id': 'str',
        'links': 'Link',
        'weight': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'ttl': 'ttl',
        'records': 'records',
        'status': 'status',
        'zone_id': 'zone_id',
        'zone_name': 'zone_name',
        'line': 'line',
        'alias_target': 'alias_target',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'health_check_id': 'health_check_id',
        'default': 'default',
        'project_id': 'project_id',
        'links': 'links',
        'weight': 'weight'
    }

    def __init__(self, id=None, name=None, description=None, type=None, ttl=None, records=None, status=None, zone_id=None, zone_name=None, line=None, alias_target=None, created_at=None, updated_at=None, health_check_id=None, default=None, project_id=None, links=None, weight=None):
        r"""RecordsetData

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 记录集的ID。 **取值范围：** 不涉及。
        :type id: str
        :param name: **参数解释：** 记录集的名称。 **取值范围：** 不涉及。
        :type name: str
        :param description: **参数解释：** 记录集的描述信息。 **取值范围：** 长度不超过255个字符。
        :type description: str
        :param type: **参数解释：** 记录类型。 **取值范围：** - 公网域名的记录类型: A、AAAA、MX、CNAME、TXT、SRV、NS、SOA、CAA。 - 内网域名的记录类型: A、AAAA、MX、CNAME、TXT、PTR、SRV、NS、SOA。
        :type type: str
        :param ttl: **参数解释：** 解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。 **取值范围：** 1~2147483647。
        :type ttl: int
        :param records: **参数解释：** 域名解析后的值。 **取值范围：** 不涉及。
        :type records: list[str]
        :param status: **参数解释：** 记录集状态。 **取值范围：** - ACTIVE：正常 - PENDING_CREATE：创建中 - PENDING_UPDATE：更新中 - PENDING_DELETE：删除中 - PENDING_FREEZE：冻结中 - FREEZE：冻结 - ILLEGAL：违规冻结 - POLICE：公安冻结 - PENDING_DISABLE：暂停中 - DISABLE：暂停 - ERROR：失败
        :type status: str
        :param zone_id: **参数解释：** 托管该记录的域名ID。 **取值范围：** 不涉及。
        :type zone_id: str
        :param zone_name: **参数解释：** 托管该记录的域名。 **取值范围：** 不涉及。
        :type zone_name: str
        :param line: **参数解释：** 解析线路ID。 **取值范围：** 不涉及。
        :type line: str
        :param alias_target: 
        :type alias_target: :class:`huaweicloudsdkdns.v2.AliasTarget`
        :param created_at: **参数解释：** 创建时间。 格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS。 **取值范围：** 不涉及。
        :type created_at: str
        :param updated_at: **参数解释：** 更新时间。 格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS。 **取值范围：** 不涉及。
        :type updated_at: str
        :param health_check_id: **参数解释：** 健康检查ID。 **取值范围：** 不涉及。
        :type health_check_id: str
        :param default: **参数解释：** 标识是否由系统默认生成，系统默认生成的记录集不能删除。 **取值范围：** 不涉及。
        :type default: bool
        :param project_id: **参数解释：** 该记录集所属的项目ID。 **取值范围：** 不涉及。
        :type project_id: str
        :param links: 
        :type links: :class:`huaweicloudsdkdns.v2.Link`
        :param weight: **参数解释：** 解析记录的权重。 **取值范围：** 0~1000。
        :type weight: int
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._type = None
        self._ttl = None
        self._records = None
        self._status = None
        self._zone_id = None
        self._zone_name = None
        self._line = None
        self._alias_target = None
        self._created_at = None
        self._updated_at = None
        self._health_check_id = None
        self._default = None
        self._project_id = None
        self._links = None
        self._weight = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if ttl is not None:
            self.ttl = ttl
        if records is not None:
            self.records = records
        if status is not None:
            self.status = status
        if zone_id is not None:
            self.zone_id = zone_id
        if zone_name is not None:
            self.zone_name = zone_name
        if line is not None:
            self.line = line
        if alias_target is not None:
            self.alias_target = alias_target
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if health_check_id is not None:
            self.health_check_id = health_check_id
        if default is not None:
            self.default = default
        if project_id is not None:
            self.project_id = project_id
        if links is not None:
            self.links = links
        if weight is not None:
            self.weight = weight

    @property
    def id(self):
        r"""Gets the id of this RecordsetData.

        **参数解释：** 记录集的ID。 **取值范围：** 不涉及。

        :return: The id of this RecordsetData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RecordsetData.

        **参数解释：** 记录集的ID。 **取值范围：** 不涉及。

        :param id: The id of this RecordsetData.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this RecordsetData.

        **参数解释：** 记录集的名称。 **取值范围：** 不涉及。

        :return: The name of this RecordsetData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RecordsetData.

        **参数解释：** 记录集的名称。 **取值范围：** 不涉及。

        :param name: The name of this RecordsetData.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this RecordsetData.

        **参数解释：** 记录集的描述信息。 **取值范围：** 长度不超过255个字符。

        :return: The description of this RecordsetData.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RecordsetData.

        **参数解释：** 记录集的描述信息。 **取值范围：** 长度不超过255个字符。

        :param description: The description of this RecordsetData.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        r"""Gets the type of this RecordsetData.

        **参数解释：** 记录类型。 **取值范围：** - 公网域名的记录类型: A、AAAA、MX、CNAME、TXT、SRV、NS、SOA、CAA。 - 内网域名的记录类型: A、AAAA、MX、CNAME、TXT、PTR、SRV、NS、SOA。

        :return: The type of this RecordsetData.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RecordsetData.

        **参数解释：** 记录类型。 **取值范围：** - 公网域名的记录类型: A、AAAA、MX、CNAME、TXT、SRV、NS、SOA、CAA。 - 内网域名的记录类型: A、AAAA、MX、CNAME、TXT、PTR、SRV、NS、SOA。

        :param type: The type of this RecordsetData.
        :type type: str
        """
        self._type = type

    @property
    def ttl(self):
        r"""Gets the ttl of this RecordsetData.

        **参数解释：** 解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。 **取值范围：** 1~2147483647。

        :return: The ttl of this RecordsetData.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        r"""Sets the ttl of this RecordsetData.

        **参数解释：** 解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。 **取值范围：** 1~2147483647。

        :param ttl: The ttl of this RecordsetData.
        :type ttl: int
        """
        self._ttl = ttl

    @property
    def records(self):
        r"""Gets the records of this RecordsetData.

        **参数解释：** 域名解析后的值。 **取值范围：** 不涉及。

        :return: The records of this RecordsetData.
        :rtype: list[str]
        """
        return self._records

    @records.setter
    def records(self, records):
        r"""Sets the records of this RecordsetData.

        **参数解释：** 域名解析后的值。 **取值范围：** 不涉及。

        :param records: The records of this RecordsetData.
        :type records: list[str]
        """
        self._records = records

    @property
    def status(self):
        r"""Gets the status of this RecordsetData.

        **参数解释：** 记录集状态。 **取值范围：** - ACTIVE：正常 - PENDING_CREATE：创建中 - PENDING_UPDATE：更新中 - PENDING_DELETE：删除中 - PENDING_FREEZE：冻结中 - FREEZE：冻结 - ILLEGAL：违规冻结 - POLICE：公安冻结 - PENDING_DISABLE：暂停中 - DISABLE：暂停 - ERROR：失败

        :return: The status of this RecordsetData.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RecordsetData.

        **参数解释：** 记录集状态。 **取值范围：** - ACTIVE：正常 - PENDING_CREATE：创建中 - PENDING_UPDATE：更新中 - PENDING_DELETE：删除中 - PENDING_FREEZE：冻结中 - FREEZE：冻结 - ILLEGAL：违规冻结 - POLICE：公安冻结 - PENDING_DISABLE：暂停中 - DISABLE：暂停 - ERROR：失败

        :param status: The status of this RecordsetData.
        :type status: str
        """
        self._status = status

    @property
    def zone_id(self):
        r"""Gets the zone_id of this RecordsetData.

        **参数解释：** 托管该记录的域名ID。 **取值范围：** 不涉及。

        :return: The zone_id of this RecordsetData.
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        r"""Sets the zone_id of this RecordsetData.

        **参数解释：** 托管该记录的域名ID。 **取值范围：** 不涉及。

        :param zone_id: The zone_id of this RecordsetData.
        :type zone_id: str
        """
        self._zone_id = zone_id

    @property
    def zone_name(self):
        r"""Gets the zone_name of this RecordsetData.

        **参数解释：** 托管该记录的域名。 **取值范围：** 不涉及。

        :return: The zone_name of this RecordsetData.
        :rtype: str
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, zone_name):
        r"""Sets the zone_name of this RecordsetData.

        **参数解释：** 托管该记录的域名。 **取值范围：** 不涉及。

        :param zone_name: The zone_name of this RecordsetData.
        :type zone_name: str
        """
        self._zone_name = zone_name

    @property
    def line(self):
        r"""Gets the line of this RecordsetData.

        **参数解释：** 解析线路ID。 **取值范围：** 不涉及。

        :return: The line of this RecordsetData.
        :rtype: str
        """
        return self._line

    @line.setter
    def line(self, line):
        r"""Sets the line of this RecordsetData.

        **参数解释：** 解析线路ID。 **取值范围：** 不涉及。

        :param line: The line of this RecordsetData.
        :type line: str
        """
        self._line = line

    @property
    def alias_target(self):
        r"""Gets the alias_target of this RecordsetData.

        :return: The alias_target of this RecordsetData.
        :rtype: :class:`huaweicloudsdkdns.v2.AliasTarget`
        """
        return self._alias_target

    @alias_target.setter
    def alias_target(self, alias_target):
        r"""Sets the alias_target of this RecordsetData.

        :param alias_target: The alias_target of this RecordsetData.
        :type alias_target: :class:`huaweicloudsdkdns.v2.AliasTarget`
        """
        self._alias_target = alias_target

    @property
    def created_at(self):
        r"""Gets the created_at of this RecordsetData.

        **参数解释：** 创建时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。 **取值范围：** 不涉及。

        :return: The created_at of this RecordsetData.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this RecordsetData.

        **参数解释：** 创建时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。 **取值范围：** 不涉及。

        :param created_at: The created_at of this RecordsetData.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this RecordsetData.

        **参数解释：** 更新时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。 **取值范围：** 不涉及。

        :return: The updated_at of this RecordsetData.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this RecordsetData.

        **参数解释：** 更新时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。 **取值范围：** 不涉及。

        :param updated_at: The updated_at of this RecordsetData.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def health_check_id(self):
        r"""Gets the health_check_id of this RecordsetData.

        **参数解释：** 健康检查ID。 **取值范围：** 不涉及。

        :return: The health_check_id of this RecordsetData.
        :rtype: str
        """
        return self._health_check_id

    @health_check_id.setter
    def health_check_id(self, health_check_id):
        r"""Sets the health_check_id of this RecordsetData.

        **参数解释：** 健康检查ID。 **取值范围：** 不涉及。

        :param health_check_id: The health_check_id of this RecordsetData.
        :type health_check_id: str
        """
        self._health_check_id = health_check_id

    @property
    def default(self):
        r"""Gets the default of this RecordsetData.

        **参数解释：** 标识是否由系统默认生成，系统默认生成的记录集不能删除。 **取值范围：** 不涉及。

        :return: The default of this RecordsetData.
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        r"""Sets the default of this RecordsetData.

        **参数解释：** 标识是否由系统默认生成，系统默认生成的记录集不能删除。 **取值范围：** 不涉及。

        :param default: The default of this RecordsetData.
        :type default: bool
        """
        self._default = default

    @property
    def project_id(self):
        r"""Gets the project_id of this RecordsetData.

        **参数解释：** 该记录集所属的项目ID。 **取值范围：** 不涉及。

        :return: The project_id of this RecordsetData.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this RecordsetData.

        **参数解释：** 该记录集所属的项目ID。 **取值范围：** 不涉及。

        :param project_id: The project_id of this RecordsetData.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def links(self):
        r"""Gets the links of this RecordsetData.

        :return: The links of this RecordsetData.
        :rtype: :class:`huaweicloudsdkdns.v2.Link`
        """
        return self._links

    @links.setter
    def links(self, links):
        r"""Sets the links of this RecordsetData.

        :param links: The links of this RecordsetData.
        :type links: :class:`huaweicloudsdkdns.v2.Link`
        """
        self._links = links

    @property
    def weight(self):
        r"""Gets the weight of this RecordsetData.

        **参数解释：** 解析记录的权重。 **取值范围：** 0~1000。

        :return: The weight of this RecordsetData.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this RecordsetData.

        **参数解释：** 解析记录的权重。 **取值范围：** 0~1000。

        :param weight: The weight of this RecordsetData.
        :type weight: int
        """
        self._weight = weight

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
        if not isinstance(other, RecordsetData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
