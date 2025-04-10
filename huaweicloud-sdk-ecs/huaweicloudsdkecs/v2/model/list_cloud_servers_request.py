# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCloudServersRequest:

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
        'status': 'str',
        'in_recycle_bin': 'bool',
        'spod_id': 'str',
        'flavor_name': 'str',
        'image_id': 'str',
        'metadata': 'str',
        'metadata_key': 'str',
        'tags': 'str',
        'not_tags': 'str',
        'availability_zone': 'str',
        'availability_zone_eq': 'str',
        'charging_mode': 'str',
        'key_name': 'str',
        'launched_since': 'str',
        'enterprise_project_id': 'str',
        'expect_fields': 'list[str]',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'in_recycle_bin': 'in_recycle_bin',
        'spod_id': 'spod_id',
        'flavor_name': 'flavor_name',
        'image_id': 'image_id',
        'metadata': 'metadata',
        'metadata_key': 'metadata-key',
        'tags': 'tags',
        'not_tags': 'not-tags',
        'availability_zone': 'availability_zone',
        'availability_zone_eq': 'availability_zone_eq',
        'charging_mode': 'charging_mode',
        'key_name': 'key_name',
        'launched_since': 'launched_since',
        'enterprise_project_id': 'enterprise_project_id',
        'expect_fields': 'expect-fields',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, id=None, name=None, status=None, in_recycle_bin=None, spod_id=None, flavor_name=None, image_id=None, metadata=None, metadata_key=None, tags=None, not_tags=None, availability_zone=None, availability_zone_eq=None, charging_mode=None, key_name=None, launched_since=None, enterprise_project_id=None, expect_fields=None, limit=None, marker=None):
        r"""ListCloudServersRequest

        The model defined in huaweicloud sdk

        :param id: 云服务器ID，格式为UUID，匹配规则为精确匹配。
        :type id: str
        :param name: 云服务器名称，匹配规则为模糊匹配。
        :type name: str
        :param status: 云服务器状态。  取值范围：  ACTIVE， BUILD，ERROR，HARD_REBOOT，MIGRATING，REBOOT，RESIZE，REVERT_RESIZE，SHELVED，SHELVED_OFFLOADED，SHUTOFF，UNKNOWN，VERIFY_RESIZE  弹性云服务器状态说明请参考[云服务器状态](https://support.huaweicloud.com/api-ecs/ecs_08_0002.html)
        :type status: str
        :param in_recycle_bin: 云服务器是否处于回收站中
        :type in_recycle_bin: bool
        :param spod_id: 共池裸机按整机柜发放的同一批次的批创id。
        :type spod_id: str
        :param flavor_name: 云服务器规格名称。
        :type flavor_name: str
        :param image_id: 镜像ID。
        :type image_id: str
        :param metadata: 元数据过滤，支持key&#x3D;value过滤。
        :type metadata: str
        :param metadata_key: 元数据key过滤。
        :type metadata_key: str
        :param tags: 查询tag字段中包含该值的云服务器。
        :type tags: str
        :param not_tags:  查询tag字段中不包含该值的云服务器
        :type not_tags: str
        :param availability_zone: 云服务器所在的AZ，匹配规则为模糊匹配。
        :type availability_zone: str
        :param availability_zone_eq: 云服务器所在的AZ，匹配规则为精确匹配。
        :type availability_zone_eq: str
        :param charging_mode: 云服务器的计费类型。
        :type charging_mode: str
        :param key_name: 云服务器使用的密钥对名称。
        :type key_name: str
        :param launched_since: 过滤在launched_since时间之后启动的云服务器。格式为ISO8601时间格式，例如：2013-06-09T06:42:18Z。
        :type launched_since: str
        :param enterprise_project_id: 过滤绑定某个企业项目的云服务器。 若需要查询当前用户所有企业项目绑定的云服务，请传参all_granted_eps。
        :type enterprise_project_id: str
        :param expect_fields: 控制查询输出的字段。在默认字段的基础上选择是否查询。   launched_at：云服务器启动时间。   key_name：云服务器使用的密钥对名称。   locked：云服务器是否为锁定状态。   root_device_name：云服务器系统盘的设备名称。   tenancy：在专属主机或共享池中创建云服务器。   dedicated_host_id：专属主机ID。   enterprise_project_id：查询绑定某个企业项目的云服务器。   tags：云服务器的标签列表。   metadata：云服务器元数据。   addresses：云服务器对应的网络地址信息。   security_groups：云服务器的安全组信息。   volumes_attached：云服务器挂载磁盘信息。   image：云服务器镜像信息。   power_state：云服务器电源状态。   cpu_options：自定义CPU选项。   market_info：云服务器计费信息，包含计费类型、到期时间等字段。
        :type expect_fields: list[str]
        :param limit: 查询返回VM数量限制。 limit 默认为10，最大为100。
        :type limit: int
        :param marker: 以单页最后一条server的ID作为分页标记。
        :type marker: str
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._in_recycle_bin = None
        self._spod_id = None
        self._flavor_name = None
        self._image_id = None
        self._metadata = None
        self._metadata_key = None
        self._tags = None
        self._not_tags = None
        self._availability_zone = None
        self._availability_zone_eq = None
        self._charging_mode = None
        self._key_name = None
        self._launched_since = None
        self._enterprise_project_id = None
        self._expect_fields = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if in_recycle_bin is not None:
            self.in_recycle_bin = in_recycle_bin
        if spod_id is not None:
            self.spod_id = spod_id
        if flavor_name is not None:
            self.flavor_name = flavor_name
        if image_id is not None:
            self.image_id = image_id
        if metadata is not None:
            self.metadata = metadata
        if metadata_key is not None:
            self.metadata_key = metadata_key
        if tags is not None:
            self.tags = tags
        if not_tags is not None:
            self.not_tags = not_tags
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if availability_zone_eq is not None:
            self.availability_zone_eq = availability_zone_eq
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if key_name is not None:
            self.key_name = key_name
        if launched_since is not None:
            self.launched_since = launched_since
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if expect_fields is not None:
            self.expect_fields = expect_fields
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def id(self):
        r"""Gets the id of this ListCloudServersRequest.

        云服务器ID，格式为UUID，匹配规则为精确匹配。

        :return: The id of this ListCloudServersRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListCloudServersRequest.

        云服务器ID，格式为UUID，匹配规则为精确匹配。

        :param id: The id of this ListCloudServersRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListCloudServersRequest.

        云服务器名称，匹配规则为模糊匹配。

        :return: The name of this ListCloudServersRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListCloudServersRequest.

        云服务器名称，匹配规则为模糊匹配。

        :param name: The name of this ListCloudServersRequest.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ListCloudServersRequest.

        云服务器状态。  取值范围：  ACTIVE， BUILD，ERROR，HARD_REBOOT，MIGRATING，REBOOT，RESIZE，REVERT_RESIZE，SHELVED，SHELVED_OFFLOADED，SHUTOFF，UNKNOWN，VERIFY_RESIZE  弹性云服务器状态说明请参考[云服务器状态](https://support.huaweicloud.com/api-ecs/ecs_08_0002.html)

        :return: The status of this ListCloudServersRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListCloudServersRequest.

        云服务器状态。  取值范围：  ACTIVE， BUILD，ERROR，HARD_REBOOT，MIGRATING，REBOOT，RESIZE，REVERT_RESIZE，SHELVED，SHELVED_OFFLOADED，SHUTOFF，UNKNOWN，VERIFY_RESIZE  弹性云服务器状态说明请参考[云服务器状态](https://support.huaweicloud.com/api-ecs/ecs_08_0002.html)

        :param status: The status of this ListCloudServersRequest.
        :type status: str
        """
        self._status = status

    @property
    def in_recycle_bin(self):
        r"""Gets the in_recycle_bin of this ListCloudServersRequest.

        云服务器是否处于回收站中

        :return: The in_recycle_bin of this ListCloudServersRequest.
        :rtype: bool
        """
        return self._in_recycle_bin

    @in_recycle_bin.setter
    def in_recycle_bin(self, in_recycle_bin):
        r"""Sets the in_recycle_bin of this ListCloudServersRequest.

        云服务器是否处于回收站中

        :param in_recycle_bin: The in_recycle_bin of this ListCloudServersRequest.
        :type in_recycle_bin: bool
        """
        self._in_recycle_bin = in_recycle_bin

    @property
    def spod_id(self):
        r"""Gets the spod_id of this ListCloudServersRequest.

        共池裸机按整机柜发放的同一批次的批创id。

        :return: The spod_id of this ListCloudServersRequest.
        :rtype: str
        """
        return self._spod_id

    @spod_id.setter
    def spod_id(self, spod_id):
        r"""Sets the spod_id of this ListCloudServersRequest.

        共池裸机按整机柜发放的同一批次的批创id。

        :param spod_id: The spod_id of this ListCloudServersRequest.
        :type spod_id: str
        """
        self._spod_id = spod_id

    @property
    def flavor_name(self):
        r"""Gets the flavor_name of this ListCloudServersRequest.

        云服务器规格名称。

        :return: The flavor_name of this ListCloudServersRequest.
        :rtype: str
        """
        return self._flavor_name

    @flavor_name.setter
    def flavor_name(self, flavor_name):
        r"""Sets the flavor_name of this ListCloudServersRequest.

        云服务器规格名称。

        :param flavor_name: The flavor_name of this ListCloudServersRequest.
        :type flavor_name: str
        """
        self._flavor_name = flavor_name

    @property
    def image_id(self):
        r"""Gets the image_id of this ListCloudServersRequest.

        镜像ID。

        :return: The image_id of this ListCloudServersRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ListCloudServersRequest.

        镜像ID。

        :param image_id: The image_id of this ListCloudServersRequest.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def metadata(self):
        r"""Gets the metadata of this ListCloudServersRequest.

        元数据过滤，支持key=value过滤。

        :return: The metadata of this ListCloudServersRequest.
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this ListCloudServersRequest.

        元数据过滤，支持key=value过滤。

        :param metadata: The metadata of this ListCloudServersRequest.
        :type metadata: str
        """
        self._metadata = metadata

    @property
    def metadata_key(self):
        r"""Gets the metadata_key of this ListCloudServersRequest.

        元数据key过滤。

        :return: The metadata_key of this ListCloudServersRequest.
        :rtype: str
        """
        return self._metadata_key

    @metadata_key.setter
    def metadata_key(self, metadata_key):
        r"""Sets the metadata_key of this ListCloudServersRequest.

        元数据key过滤。

        :param metadata_key: The metadata_key of this ListCloudServersRequest.
        :type metadata_key: str
        """
        self._metadata_key = metadata_key

    @property
    def tags(self):
        r"""Gets the tags of this ListCloudServersRequest.

        查询tag字段中包含该值的云服务器。

        :return: The tags of this ListCloudServersRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListCloudServersRequest.

        查询tag字段中包含该值的云服务器。

        :param tags: The tags of this ListCloudServersRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def not_tags(self):
        r"""Gets the not_tags of this ListCloudServersRequest.

         查询tag字段中不包含该值的云服务器

        :return: The not_tags of this ListCloudServersRequest.
        :rtype: str
        """
        return self._not_tags

    @not_tags.setter
    def not_tags(self, not_tags):
        r"""Sets the not_tags of this ListCloudServersRequest.

         查询tag字段中不包含该值的云服务器

        :param not_tags: The not_tags of this ListCloudServersRequest.
        :type not_tags: str
        """
        self._not_tags = not_tags

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this ListCloudServersRequest.

        云服务器所在的AZ，匹配规则为模糊匹配。

        :return: The availability_zone of this ListCloudServersRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this ListCloudServersRequest.

        云服务器所在的AZ，匹配规则为模糊匹配。

        :param availability_zone: The availability_zone of this ListCloudServersRequest.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def availability_zone_eq(self):
        r"""Gets the availability_zone_eq of this ListCloudServersRequest.

        云服务器所在的AZ，匹配规则为精确匹配。

        :return: The availability_zone_eq of this ListCloudServersRequest.
        :rtype: str
        """
        return self._availability_zone_eq

    @availability_zone_eq.setter
    def availability_zone_eq(self, availability_zone_eq):
        r"""Sets the availability_zone_eq of this ListCloudServersRequest.

        云服务器所在的AZ，匹配规则为精确匹配。

        :param availability_zone_eq: The availability_zone_eq of this ListCloudServersRequest.
        :type availability_zone_eq: str
        """
        self._availability_zone_eq = availability_zone_eq

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this ListCloudServersRequest.

        云服务器的计费类型。

        :return: The charging_mode of this ListCloudServersRequest.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this ListCloudServersRequest.

        云服务器的计费类型。

        :param charging_mode: The charging_mode of this ListCloudServersRequest.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def key_name(self):
        r"""Gets the key_name of this ListCloudServersRequest.

        云服务器使用的密钥对名称。

        :return: The key_name of this ListCloudServersRequest.
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        r"""Sets the key_name of this ListCloudServersRequest.

        云服务器使用的密钥对名称。

        :param key_name: The key_name of this ListCloudServersRequest.
        :type key_name: str
        """
        self._key_name = key_name

    @property
    def launched_since(self):
        r"""Gets the launched_since of this ListCloudServersRequest.

        过滤在launched_since时间之后启动的云服务器。格式为ISO8601时间格式，例如：2013-06-09T06:42:18Z。

        :return: The launched_since of this ListCloudServersRequest.
        :rtype: str
        """
        return self._launched_since

    @launched_since.setter
    def launched_since(self, launched_since):
        r"""Sets the launched_since of this ListCloudServersRequest.

        过滤在launched_since时间之后启动的云服务器。格式为ISO8601时间格式，例如：2013-06-09T06:42:18Z。

        :param launched_since: The launched_since of this ListCloudServersRequest.
        :type launched_since: str
        """
        self._launched_since = launched_since

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListCloudServersRequest.

        过滤绑定某个企业项目的云服务器。 若需要查询当前用户所有企业项目绑定的云服务，请传参all_granted_eps。

        :return: The enterprise_project_id of this ListCloudServersRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListCloudServersRequest.

        过滤绑定某个企业项目的云服务器。 若需要查询当前用户所有企业项目绑定的云服务，请传参all_granted_eps。

        :param enterprise_project_id: The enterprise_project_id of this ListCloudServersRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def expect_fields(self):
        r"""Gets the expect_fields of this ListCloudServersRequest.

        控制查询输出的字段。在默认字段的基础上选择是否查询。   launched_at：云服务器启动时间。   key_name：云服务器使用的密钥对名称。   locked：云服务器是否为锁定状态。   root_device_name：云服务器系统盘的设备名称。   tenancy：在专属主机或共享池中创建云服务器。   dedicated_host_id：专属主机ID。   enterprise_project_id：查询绑定某个企业项目的云服务器。   tags：云服务器的标签列表。   metadata：云服务器元数据。   addresses：云服务器对应的网络地址信息。   security_groups：云服务器的安全组信息。   volumes_attached：云服务器挂载磁盘信息。   image：云服务器镜像信息。   power_state：云服务器电源状态。   cpu_options：自定义CPU选项。   market_info：云服务器计费信息，包含计费类型、到期时间等字段。

        :return: The expect_fields of this ListCloudServersRequest.
        :rtype: list[str]
        """
        return self._expect_fields

    @expect_fields.setter
    def expect_fields(self, expect_fields):
        r"""Sets the expect_fields of this ListCloudServersRequest.

        控制查询输出的字段。在默认字段的基础上选择是否查询。   launched_at：云服务器启动时间。   key_name：云服务器使用的密钥对名称。   locked：云服务器是否为锁定状态。   root_device_name：云服务器系统盘的设备名称。   tenancy：在专属主机或共享池中创建云服务器。   dedicated_host_id：专属主机ID。   enterprise_project_id：查询绑定某个企业项目的云服务器。   tags：云服务器的标签列表。   metadata：云服务器元数据。   addresses：云服务器对应的网络地址信息。   security_groups：云服务器的安全组信息。   volumes_attached：云服务器挂载磁盘信息。   image：云服务器镜像信息。   power_state：云服务器电源状态。   cpu_options：自定义CPU选项。   market_info：云服务器计费信息，包含计费类型、到期时间等字段。

        :param expect_fields: The expect_fields of this ListCloudServersRequest.
        :type expect_fields: list[str]
        """
        self._expect_fields = expect_fields

    @property
    def limit(self):
        r"""Gets the limit of this ListCloudServersRequest.

        查询返回VM数量限制。 limit 默认为10，最大为100。

        :return: The limit of this ListCloudServersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCloudServersRequest.

        查询返回VM数量限制。 limit 默认为10，最大为100。

        :param limit: The limit of this ListCloudServersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListCloudServersRequest.

        以单页最后一条server的ID作为分页标记。

        :return: The marker of this ListCloudServersRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListCloudServersRequest.

        以单页最后一条server的ID作为分页标记。

        :param marker: The marker of this ListCloudServersRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListCloudServersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
