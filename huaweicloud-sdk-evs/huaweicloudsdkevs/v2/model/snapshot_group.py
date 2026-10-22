# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SnapshotGroup:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_id': 'str',
        'volume_ids': 'list[str]',
        'instant_access': 'bool',
        'name': 'str',
        'description': 'str',
        'tags': 'dict(str, str)',
        'enterprise_project_id': 'str',
        'incremental': 'bool'
    }

    attribute_map = {
        'server_id': 'server_id',
        'volume_ids': 'volume_ids',
        'instant_access': 'instant_access',
        'name': 'name',
        'description': 'description',
        'tags': 'tags',
        'enterprise_project_id': 'enterprise_project_id',
        'incremental': 'incremental'
    }

    def __init__(self, server_id=None, volume_ids=None, instant_access=None, name=None, description=None, tags=None, enterprise_project_id=None, incremental=None):
        r"""SnapshotGroup

        The model defined in huaweicloud sdk

        :param server_id: **参数解释** 云服务器id。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type server_id: str
        :param volume_ids: **参数解释** 云硬盘id列表。 **约束限制** 格式为ids&#x3D;[\&quot;id1\&quot;,\&quot;id2\&quot;,...,\&quot;idx\&quot;]。 如果设置了server_id，则该参数只能设置指定实例内已挂载的云硬盘，不再支持设置多个跨实例的云硬盘ID。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type volume_ids: list[str]
        :param instant_access: **参数解释** 是否开启快照极速可用。 **约束限制** 不涉及。 **取值范围** - true：开启。 - false：关闭。 **默认取值** false
        :type instant_access: bool
        :param name: **参数解释** 快照一致性组名称。 **约束限制** 最大支持255个字节。 **取值范围** 最小长度：0 最大长度：255 **默认取值** 不涉及。
        :type name: str
        :param description: **参数解释** 快照一致性组描述。 **约束限制** 最大支持255个字节。 **取值范围** 最小长度：0 最大长度：255 **默认取值** 不涉及。
        :type description: str
        :param tags: **参数解释** 快照一致性组的标签。 标签的value：String类型，最大长度43个字符，可以为空字符串。 由英文字母、数字、下划线、点、中划线、UNICODE字符（\\u4E00-\\u9FFF）组成。  标签的value：String类型，最大长度43个字符，可以为空字符串。 由英文字母、数字、下划线、点、中划线、UNICODE字符（\\u4E00-\\u9FFF）组成。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type tags: dict(str, str)
        :param enterprise_project_id: **参数解释** 快照一致性组所属的企业项目ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type enterprise_project_id: str
        :param incremental: **参数解释** 是否创建增量快照。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type incremental: bool
        """
        
        

        self._server_id = None
        self._volume_ids = None
        self._instant_access = None
        self._name = None
        self._description = None
        self._tags = None
        self._enterprise_project_id = None
        self._incremental = None
        self.discriminator = None

        if server_id is not None:
            self.server_id = server_id
        if volume_ids is not None:
            self.volume_ids = volume_ids
        if instant_access is not None:
            self.instant_access = instant_access
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if incremental is not None:
            self.incremental = incremental

    @property
    def server_id(self):
        r"""Gets the server_id of this SnapshotGroup.

        **参数解释** 云服务器id。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The server_id of this SnapshotGroup.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this SnapshotGroup.

        **参数解释** 云服务器id。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param server_id: The server_id of this SnapshotGroup.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def volume_ids(self):
        r"""Gets the volume_ids of this SnapshotGroup.

        **参数解释** 云硬盘id列表。 **约束限制** 格式为ids=[\"id1\",\"id2\",...,\"idx\"]。 如果设置了server_id，则该参数只能设置指定实例内已挂载的云硬盘，不再支持设置多个跨实例的云硬盘ID。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The volume_ids of this SnapshotGroup.
        :rtype: list[str]
        """
        return self._volume_ids

    @volume_ids.setter
    def volume_ids(self, volume_ids):
        r"""Sets the volume_ids of this SnapshotGroup.

        **参数解释** 云硬盘id列表。 **约束限制** 格式为ids=[\"id1\",\"id2\",...,\"idx\"]。 如果设置了server_id，则该参数只能设置指定实例内已挂载的云硬盘，不再支持设置多个跨实例的云硬盘ID。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param volume_ids: The volume_ids of this SnapshotGroup.
        :type volume_ids: list[str]
        """
        self._volume_ids = volume_ids

    @property
    def instant_access(self):
        r"""Gets the instant_access of this SnapshotGroup.

        **参数解释** 是否开启快照极速可用。 **约束限制** 不涉及。 **取值范围** - true：开启。 - false：关闭。 **默认取值** false

        :return: The instant_access of this SnapshotGroup.
        :rtype: bool
        """
        return self._instant_access

    @instant_access.setter
    def instant_access(self, instant_access):
        r"""Sets the instant_access of this SnapshotGroup.

        **参数解释** 是否开启快照极速可用。 **约束限制** 不涉及。 **取值范围** - true：开启。 - false：关闭。 **默认取值** false

        :param instant_access: The instant_access of this SnapshotGroup.
        :type instant_access: bool
        """
        self._instant_access = instant_access

    @property
    def name(self):
        r"""Gets the name of this SnapshotGroup.

        **参数解释** 快照一致性组名称。 **约束限制** 最大支持255个字节。 **取值范围** 最小长度：0 最大长度：255 **默认取值** 不涉及。

        :return: The name of this SnapshotGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SnapshotGroup.

        **参数解释** 快照一致性组名称。 **约束限制** 最大支持255个字节。 **取值范围** 最小长度：0 最大长度：255 **默认取值** 不涉及。

        :param name: The name of this SnapshotGroup.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this SnapshotGroup.

        **参数解释** 快照一致性组描述。 **约束限制** 最大支持255个字节。 **取值范围** 最小长度：0 最大长度：255 **默认取值** 不涉及。

        :return: The description of this SnapshotGroup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this SnapshotGroup.

        **参数解释** 快照一致性组描述。 **约束限制** 最大支持255个字节。 **取值范围** 最小长度：0 最大长度：255 **默认取值** 不涉及。

        :param description: The description of this SnapshotGroup.
        :type description: str
        """
        self._description = description

    @property
    def tags(self):
        r"""Gets the tags of this SnapshotGroup.

        **参数解释** 快照一致性组的标签。 标签的value：String类型，最大长度43个字符，可以为空字符串。 由英文字母、数字、下划线、点、中划线、UNICODE字符（\\u4E00-\\u9FFF）组成。  标签的value：String类型，最大长度43个字符，可以为空字符串。 由英文字母、数字、下划线、点、中划线、UNICODE字符（\\u4E00-\\u9FFF）组成。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The tags of this SnapshotGroup.
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this SnapshotGroup.

        **参数解释** 快照一致性组的标签。 标签的value：String类型，最大长度43个字符，可以为空字符串。 由英文字母、数字、下划线、点、中划线、UNICODE字符（\\u4E00-\\u9FFF）组成。  标签的value：String类型，最大长度43个字符，可以为空字符串。 由英文字母、数字、下划线、点、中划线、UNICODE字符（\\u4E00-\\u9FFF）组成。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param tags: The tags of this SnapshotGroup.
        :type tags: dict(str, str)
        """
        self._tags = tags

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this SnapshotGroup.

        **参数解释** 快照一致性组所属的企业项目ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The enterprise_project_id of this SnapshotGroup.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this SnapshotGroup.

        **参数解释** 快照一致性组所属的企业项目ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param enterprise_project_id: The enterprise_project_id of this SnapshotGroup.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def incremental(self):
        r"""Gets the incremental of this SnapshotGroup.

        **参数解释** 是否创建增量快照。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The incremental of this SnapshotGroup.
        :rtype: bool
        """
        return self._incremental

    @incremental.setter
    def incremental(self, incremental):
        r"""Sets the incremental of this SnapshotGroup.

        **参数解释** 是否创建增量快照。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param incremental: The incremental of this SnapshotGroup.
        :type incremental: bool
        """
        self._incremental = incremental

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
        if not isinstance(other, SnapshotGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
