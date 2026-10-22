# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateStandardSnapshot:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'volume_id': 'str',
        'name': 'str',
        'description': 'str',
        'tags': 'dict(str, str)',
        'enterprise_project_id': 'str',
        'instant_access': 'bool',
        'incremental': 'bool',
        'retention_days': 'int'
    }

    attribute_map = {
        'volume_id': 'volume_id',
        'name': 'name',
        'description': 'description',
        'tags': 'tags',
        'enterprise_project_id': 'enterprise_project_id',
        'instant_access': 'instant_access',
        'incremental': 'incremental',
        'retention_days': 'retention_days'
    }

    def __init__(self, volume_id=None, name=None, description=None, tags=None, enterprise_project_id=None, instant_access=None, incremental=None, retention_days=None):
        r"""CreateStandardSnapshot

        The model defined in huaweicloud sdk

        :param volume_id: **参数解释** 云硬盘id。 可通过[查询所有云硬盘详情](evs_04_2006.xml)获取云硬盘ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type volume_id: str
        :param name: **参数解释** 云硬盘快照名称。 可通过[查询云硬盘快照详情列表](evs_04_2021.xml)接口获取云硬盘快照名称。 **约束限制** 不涉及。 **取值范围** 最大支持64个字符。 **默认取值** 不涉及。
        :type name: str
        :param description: **参数解释** 云硬盘快照描述。 **约束限制** 不涉及。 **取值范围** 最大支持85个字符。 **默认取值** 不涉及。
        :type description: str
        :param tags: **参数解释** 云硬盘快照的标签。 标签的key：String类型，最大长度36个字符。 由英文字母、数字、下划线、中划线、UNICODE字符（\\u4E00-\\u9FFF）组成。  标签的value：String类型，最大长度43个字符，可以为空字符串。 由英文字母、数字、下划线、点、中划线、UNICODE字符（\\u4E00-\\u9FFF）组成。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type tags: dict(str, str)
        :param enterprise_project_id: **参数解释** 云硬盘快照的企业项目id。  关于企业项目ID的获取及企业项目特性的详细信息，请参考：\&quot;[[企业管理用户指南](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0123692049.html)\&quot;](tag:hws)[[企业管理用户指南](https://support.huaweicloud.com/intl/zh-cn/usermanual-em/zh-cn_topic_0123692049.html)](tag:hws_hk)。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 0，表示default企业项目。
        :type enterprise_project_id: str
        :param instant_access: **参数解释** 是否开启极速可用功能。 **约束限制** 不涉及。 **取值范围** - true：表示开启。 - false：表示不开启。 **默认取值** 默认为false，表示不开启。
        :type instant_access: bool
        :param incremental: **参数解释** 是否创建增量快照。 **约束限制** 不涉及。 **取值范围** - true：创建增量快照。 - false：创建全量快照。 **默认取值** true
        :type incremental: bool
        :param retention_days: **参数解释** 设置快照的保留时间，单位为天。保留时间到期后快照会被自动释放。 **约束限制** 不涉及。 **取值范围** 1~65536。 **默认取值** 空，表示快照不会被自动释放。
        :type retention_days: int
        """
        
        

        self._volume_id = None
        self._name = None
        self._description = None
        self._tags = None
        self._enterprise_project_id = None
        self._instant_access = None
        self._incremental = None
        self._retention_days = None
        self.discriminator = None

        if volume_id is not None:
            self.volume_id = volume_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if instant_access is not None:
            self.instant_access = instant_access
        if incremental is not None:
            self.incremental = incremental
        if retention_days is not None:
            self.retention_days = retention_days

    @property
    def volume_id(self):
        r"""Gets the volume_id of this CreateStandardSnapshot.

        **参数解释** 云硬盘id。 可通过[查询所有云硬盘详情](evs_04_2006.xml)获取云硬盘ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The volume_id of this CreateStandardSnapshot.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        r"""Sets the volume_id of this CreateStandardSnapshot.

        **参数解释** 云硬盘id。 可通过[查询所有云硬盘详情](evs_04_2006.xml)获取云硬盘ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param volume_id: The volume_id of this CreateStandardSnapshot.
        :type volume_id: str
        """
        self._volume_id = volume_id

    @property
    def name(self):
        r"""Gets the name of this CreateStandardSnapshot.

        **参数解释** 云硬盘快照名称。 可通过[查询云硬盘快照详情列表](evs_04_2021.xml)接口获取云硬盘快照名称。 **约束限制** 不涉及。 **取值范围** 最大支持64个字符。 **默认取值** 不涉及。

        :return: The name of this CreateStandardSnapshot.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateStandardSnapshot.

        **参数解释** 云硬盘快照名称。 可通过[查询云硬盘快照详情列表](evs_04_2021.xml)接口获取云硬盘快照名称。 **约束限制** 不涉及。 **取值范围** 最大支持64个字符。 **默认取值** 不涉及。

        :param name: The name of this CreateStandardSnapshot.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateStandardSnapshot.

        **参数解释** 云硬盘快照描述。 **约束限制** 不涉及。 **取值范围** 最大支持85个字符。 **默认取值** 不涉及。

        :return: The description of this CreateStandardSnapshot.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateStandardSnapshot.

        **参数解释** 云硬盘快照描述。 **约束限制** 不涉及。 **取值范围** 最大支持85个字符。 **默认取值** 不涉及。

        :param description: The description of this CreateStandardSnapshot.
        :type description: str
        """
        self._description = description

    @property
    def tags(self):
        r"""Gets the tags of this CreateStandardSnapshot.

        **参数解释** 云硬盘快照的标签。 标签的key：String类型，最大长度36个字符。 由英文字母、数字、下划线、中划线、UNICODE字符（\\u4E00-\\u9FFF）组成。  标签的value：String类型，最大长度43个字符，可以为空字符串。 由英文字母、数字、下划线、点、中划线、UNICODE字符（\\u4E00-\\u9FFF）组成。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The tags of this CreateStandardSnapshot.
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateStandardSnapshot.

        **参数解释** 云硬盘快照的标签。 标签的key：String类型，最大长度36个字符。 由英文字母、数字、下划线、中划线、UNICODE字符（\\u4E00-\\u9FFF）组成。  标签的value：String类型，最大长度43个字符，可以为空字符串。 由英文字母、数字、下划线、点、中划线、UNICODE字符（\\u4E00-\\u9FFF）组成。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param tags: The tags of this CreateStandardSnapshot.
        :type tags: dict(str, str)
        """
        self._tags = tags

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateStandardSnapshot.

        **参数解释** 云硬盘快照的企业项目id。  关于企业项目ID的获取及企业项目特性的详细信息，请参考：\"[[企业管理用户指南](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0123692049.html)\"](tag:hws)[[企业管理用户指南](https://support.huaweicloud.com/intl/zh-cn/usermanual-em/zh-cn_topic_0123692049.html)](tag:hws_hk)。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 0，表示default企业项目。

        :return: The enterprise_project_id of this CreateStandardSnapshot.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateStandardSnapshot.

        **参数解释** 云硬盘快照的企业项目id。  关于企业项目ID的获取及企业项目特性的详细信息，请参考：\"[[企业管理用户指南](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0123692049.html)\"](tag:hws)[[企业管理用户指南](https://support.huaweicloud.com/intl/zh-cn/usermanual-em/zh-cn_topic_0123692049.html)](tag:hws_hk)。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 0，表示default企业项目。

        :param enterprise_project_id: The enterprise_project_id of this CreateStandardSnapshot.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def instant_access(self):
        r"""Gets the instant_access of this CreateStandardSnapshot.

        **参数解释** 是否开启极速可用功能。 **约束限制** 不涉及。 **取值范围** - true：表示开启。 - false：表示不开启。 **默认取值** 默认为false，表示不开启。

        :return: The instant_access of this CreateStandardSnapshot.
        :rtype: bool
        """
        return self._instant_access

    @instant_access.setter
    def instant_access(self, instant_access):
        r"""Sets the instant_access of this CreateStandardSnapshot.

        **参数解释** 是否开启极速可用功能。 **约束限制** 不涉及。 **取值范围** - true：表示开启。 - false：表示不开启。 **默认取值** 默认为false，表示不开启。

        :param instant_access: The instant_access of this CreateStandardSnapshot.
        :type instant_access: bool
        """
        self._instant_access = instant_access

    @property
    def incremental(self):
        r"""Gets the incremental of this CreateStandardSnapshot.

        **参数解释** 是否创建增量快照。 **约束限制** 不涉及。 **取值范围** - true：创建增量快照。 - false：创建全量快照。 **默认取值** true

        :return: The incremental of this CreateStandardSnapshot.
        :rtype: bool
        """
        return self._incremental

    @incremental.setter
    def incremental(self, incremental):
        r"""Sets the incremental of this CreateStandardSnapshot.

        **参数解释** 是否创建增量快照。 **约束限制** 不涉及。 **取值范围** - true：创建增量快照。 - false：创建全量快照。 **默认取值** true

        :param incremental: The incremental of this CreateStandardSnapshot.
        :type incremental: bool
        """
        self._incremental = incremental

    @property
    def retention_days(self):
        r"""Gets the retention_days of this CreateStandardSnapshot.

        **参数解释** 设置快照的保留时间，单位为天。保留时间到期后快照会被自动释放。 **约束限制** 不涉及。 **取值范围** 1~65536。 **默认取值** 空，表示快照不会被自动释放。

        :return: The retention_days of this CreateStandardSnapshot.
        :rtype: int
        """
        return self._retention_days

    @retention_days.setter
    def retention_days(self, retention_days):
        r"""Sets the retention_days of this CreateStandardSnapshot.

        **参数解释** 设置快照的保留时间，单位为天。保留时间到期后快照会被自动释放。 **约束限制** 不涉及。 **取值范围** 1~65536。 **默认取值** 空，表示快照不会被自动释放。

        :param retention_days: The retention_days of this CreateStandardSnapshot.
        :type retention_days: int
        """
        self._retention_days = retention_days

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
        if not isinstance(other, CreateStandardSnapshot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
