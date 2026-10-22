# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetSnapshotPolicy:

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
        'repeat_weekdays': 'list[str]',
        'repeat_interval_days': 'int',
        'time_points': 'list[str]',
        'retention_days': 'int',
        'created_at': 'str',
        'updated_at': 'str',
        'tags': 'dict(str, str)',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'repeat_weekdays': 'repeat_weekdays',
        'repeat_interval_days': 'repeat_interval_days',
        'time_points': 'time_points',
        'retention_days': 'retention_days',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'tags': 'tags',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, id=None, name=None, repeat_weekdays=None, repeat_interval_days=None, time_points=None, retention_days=None, created_at=None, updated_at=None, tags=None, enterprise_project_id=None):
        r"""GetSnapshotPolicy

        The model defined in huaweicloud sdk

        :param id: 自动快照策略ID。
        :type id: str
        :param name: 自动快照策略名称。最大支持255个字节。  最小长度：0  最大长度：255
        :type name: str
        :param repeat_weekdays: 自动快照的重复日期，单位为天，周期为星期。取值范围为 1~7，如 1 表示周一。  当一星期内需要创建多次自动快照时，可以传入多个时间点：  最多传入 7 个时间点。 多个时间点用一个格式类似\&quot;1\&quot;, \&quot;2\&quot;, … \&quot;7\&quot;的 JSON 数组表示，时间点之间用半角逗号（,）隔开。
        :type repeat_weekdays: list[str]
        :param repeat_interval_days: 自动快照的间隔日期，单位为天，取值范围为 1~30,如1表示每天。
        :type repeat_interval_days: int
        :param time_points: 自动快照的创建时间点。使用 UTC +8 时间，单位为小时。取值范围为 0~23，代表 00:00 至 23:00 共 24 个时间点，如 1 表示 01:00。  当一天内需要创建多次自动快照时，可以传入多个时间点：  最多传入 24 个时间点。 多个时间点用一个格式类似\&quot;0\&quot;, \&quot;1\&quot;, … \&quot;23\&quot;的 JSON 数组表示，时间点之间用半角逗号（,）隔开。
        :type time_points: list[str]
        :param retention_days: 设置快照的保留时间，单位为天。保留时间到期后快照会被自动释放，取值范围：1~65536。 缺省值：-1，表示快照持续保留。
        :type retention_days: int
        :param created_at: 自动快照策略的创建时间。
        :type created_at: str
        :param updated_at: 自动快照策略的更新时间。
        :type updated_at: str
        :param tags: 设置自动快照策略的标签。
        :type tags: dict(str, str)
        :param enterprise_project_id: 企业项目id。
        :type enterprise_project_id: str
        """
        
        

        self._id = None
        self._name = None
        self._repeat_weekdays = None
        self._repeat_interval_days = None
        self._time_points = None
        self._retention_days = None
        self._created_at = None
        self._updated_at = None
        self._tags = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.repeat_weekdays = repeat_weekdays
        self.repeat_interval_days = repeat_interval_days
        self.time_points = time_points
        self.retention_days = retention_days
        self.created_at = created_at
        self.updated_at = updated_at
        self.tags = tags
        self.enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        r"""Gets the id of this GetSnapshotPolicy.

        自动快照策略ID。

        :return: The id of this GetSnapshotPolicy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GetSnapshotPolicy.

        自动快照策略ID。

        :param id: The id of this GetSnapshotPolicy.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this GetSnapshotPolicy.

        自动快照策略名称。最大支持255个字节。  最小长度：0  最大长度：255

        :return: The name of this GetSnapshotPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GetSnapshotPolicy.

        自动快照策略名称。最大支持255个字节。  最小长度：0  最大长度：255

        :param name: The name of this GetSnapshotPolicy.
        :type name: str
        """
        self._name = name

    @property
    def repeat_weekdays(self):
        r"""Gets the repeat_weekdays of this GetSnapshotPolicy.

        自动快照的重复日期，单位为天，周期为星期。取值范围为 1~7，如 1 表示周一。  当一星期内需要创建多次自动快照时，可以传入多个时间点：  最多传入 7 个时间点。 多个时间点用一个格式类似\"1\", \"2\", … \"7\"的 JSON 数组表示，时间点之间用半角逗号（,）隔开。

        :return: The repeat_weekdays of this GetSnapshotPolicy.
        :rtype: list[str]
        """
        return self._repeat_weekdays

    @repeat_weekdays.setter
    def repeat_weekdays(self, repeat_weekdays):
        r"""Sets the repeat_weekdays of this GetSnapshotPolicy.

        自动快照的重复日期，单位为天，周期为星期。取值范围为 1~7，如 1 表示周一。  当一星期内需要创建多次自动快照时，可以传入多个时间点：  最多传入 7 个时间点。 多个时间点用一个格式类似\"1\", \"2\", … \"7\"的 JSON 数组表示，时间点之间用半角逗号（,）隔开。

        :param repeat_weekdays: The repeat_weekdays of this GetSnapshotPolicy.
        :type repeat_weekdays: list[str]
        """
        self._repeat_weekdays = repeat_weekdays

    @property
    def repeat_interval_days(self):
        r"""Gets the repeat_interval_days of this GetSnapshotPolicy.

        自动快照的间隔日期，单位为天，取值范围为 1~30,如1表示每天。

        :return: The repeat_interval_days of this GetSnapshotPolicy.
        :rtype: int
        """
        return self._repeat_interval_days

    @repeat_interval_days.setter
    def repeat_interval_days(self, repeat_interval_days):
        r"""Sets the repeat_interval_days of this GetSnapshotPolicy.

        自动快照的间隔日期，单位为天，取值范围为 1~30,如1表示每天。

        :param repeat_interval_days: The repeat_interval_days of this GetSnapshotPolicy.
        :type repeat_interval_days: int
        """
        self._repeat_interval_days = repeat_interval_days

    @property
    def time_points(self):
        r"""Gets the time_points of this GetSnapshotPolicy.

        自动快照的创建时间点。使用 UTC +8 时间，单位为小时。取值范围为 0~23，代表 00:00 至 23:00 共 24 个时间点，如 1 表示 01:00。  当一天内需要创建多次自动快照时，可以传入多个时间点：  最多传入 24 个时间点。 多个时间点用一个格式类似\"0\", \"1\", … \"23\"的 JSON 数组表示，时间点之间用半角逗号（,）隔开。

        :return: The time_points of this GetSnapshotPolicy.
        :rtype: list[str]
        """
        return self._time_points

    @time_points.setter
    def time_points(self, time_points):
        r"""Sets the time_points of this GetSnapshotPolicy.

        自动快照的创建时间点。使用 UTC +8 时间，单位为小时。取值范围为 0~23，代表 00:00 至 23:00 共 24 个时间点，如 1 表示 01:00。  当一天内需要创建多次自动快照时，可以传入多个时间点：  最多传入 24 个时间点。 多个时间点用一个格式类似\"0\", \"1\", … \"23\"的 JSON 数组表示，时间点之间用半角逗号（,）隔开。

        :param time_points: The time_points of this GetSnapshotPolicy.
        :type time_points: list[str]
        """
        self._time_points = time_points

    @property
    def retention_days(self):
        r"""Gets the retention_days of this GetSnapshotPolicy.

        设置快照的保留时间，单位为天。保留时间到期后快照会被自动释放，取值范围：1~65536。 缺省值：-1，表示快照持续保留。

        :return: The retention_days of this GetSnapshotPolicy.
        :rtype: int
        """
        return self._retention_days

    @retention_days.setter
    def retention_days(self, retention_days):
        r"""Sets the retention_days of this GetSnapshotPolicy.

        设置快照的保留时间，单位为天。保留时间到期后快照会被自动释放，取值范围：1~65536。 缺省值：-1，表示快照持续保留。

        :param retention_days: The retention_days of this GetSnapshotPolicy.
        :type retention_days: int
        """
        self._retention_days = retention_days

    @property
    def created_at(self):
        r"""Gets the created_at of this GetSnapshotPolicy.

        自动快照策略的创建时间。

        :return: The created_at of this GetSnapshotPolicy.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this GetSnapshotPolicy.

        自动快照策略的创建时间。

        :param created_at: The created_at of this GetSnapshotPolicy.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this GetSnapshotPolicy.

        自动快照策略的更新时间。

        :return: The updated_at of this GetSnapshotPolicy.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this GetSnapshotPolicy.

        自动快照策略的更新时间。

        :param updated_at: The updated_at of this GetSnapshotPolicy.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def tags(self):
        r"""Gets the tags of this GetSnapshotPolicy.

        设置自动快照策略的标签。

        :return: The tags of this GetSnapshotPolicy.
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this GetSnapshotPolicy.

        设置自动快照策略的标签。

        :param tags: The tags of this GetSnapshotPolicy.
        :type tags: dict(str, str)
        """
        self._tags = tags

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this GetSnapshotPolicy.

        企业项目id。

        :return: The enterprise_project_id of this GetSnapshotPolicy.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this GetSnapshotPolicy.

        企业项目id。

        :param enterprise_project_id: The enterprise_project_id of this GetSnapshotPolicy.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, GetSnapshotPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
