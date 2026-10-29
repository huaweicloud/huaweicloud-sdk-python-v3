# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateLogStreamParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ttl_in_days': 'int',
        'tags': 'list[TagsBody]',
        'whether_log_storage': 'bool',
        'hot_cold_separation': 'bool',
        'hot_storage_days': 'int'
    }

    attribute_map = {
        'ttl_in_days': 'ttl_in_days',
        'tags': 'tags',
        'whether_log_storage': 'whether_log_storage',
        'hot_cold_separation': 'hot_cold_separation',
        'hot_storage_days': 'hot_storage_days'
    }

    def __init__(self, ttl_in_days=None, tags=None, whether_log_storage=None, hot_cold_separation=None, hot_storage_days=None):
        r"""UpdateLogStreamParams

        The model defined in huaweicloud sdk

        :param ttl_in_days: 日志存储时间（天）。
        :type ttl_in_days: int
        :param tags: 标签字段信息
        :type tags: list[:class:`huaweicloudsdklts.v2.TagsBody`]
        :param whether_log_storage: 日志是否存储
        :type whether_log_storage: bool
        :param hot_cold_separation: **参数解释：** 是否开启智能冷存储。 **约束限制：** 开启智能冷存储需要日志存储时间大于7天。开启智能冷存储后，需要设置标准存储层数据的保存时间。标准存储至少需保存7天才能转换为智能冷存储层数据。当日志保存时间大于标准存储层数据保存时间，且小于日志存储时间时，日志数据将自动转换为智能冷存储层数据存储。 **取值范围：** - true：开启智能冷存储。 - false：关闭智能冷存储。 **默认取值：** false
        :type hot_cold_separation: bool
        :param hot_storage_days: **参数解释：** 日志流标准存储时间（单位：天），即日志上报到LTS后日志标准存储的时间。 **约束限制：** 开启智能冷存储需要日志总存储时间大于7天。 **取值范围：** 最小值：7天 最大值：365天 **默认取值：** 不涉及。
        :type hot_storage_days: int
        """
        
        

        self._ttl_in_days = None
        self._tags = None
        self._whether_log_storage = None
        self._hot_cold_separation = None
        self._hot_storage_days = None
        self.discriminator = None

        self.ttl_in_days = ttl_in_days
        if tags is not None:
            self.tags = tags
        if whether_log_storage is not None:
            self.whether_log_storage = whether_log_storage
        if hot_cold_separation is not None:
            self.hot_cold_separation = hot_cold_separation
        if hot_storage_days is not None:
            self.hot_storage_days = hot_storage_days

    @property
    def ttl_in_days(self):
        r"""Gets the ttl_in_days of this UpdateLogStreamParams.

        日志存储时间（天）。

        :return: The ttl_in_days of this UpdateLogStreamParams.
        :rtype: int
        """
        return self._ttl_in_days

    @ttl_in_days.setter
    def ttl_in_days(self, ttl_in_days):
        r"""Sets the ttl_in_days of this UpdateLogStreamParams.

        日志存储时间（天）。

        :param ttl_in_days: The ttl_in_days of this UpdateLogStreamParams.
        :type ttl_in_days: int
        """
        self._ttl_in_days = ttl_in_days

    @property
    def tags(self):
        r"""Gets the tags of this UpdateLogStreamParams.

        标签字段信息

        :return: The tags of this UpdateLogStreamParams.
        :rtype: list[:class:`huaweicloudsdklts.v2.TagsBody`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this UpdateLogStreamParams.

        标签字段信息

        :param tags: The tags of this UpdateLogStreamParams.
        :type tags: list[:class:`huaweicloudsdklts.v2.TagsBody`]
        """
        self._tags = tags

    @property
    def whether_log_storage(self):
        r"""Gets the whether_log_storage of this UpdateLogStreamParams.

        日志是否存储

        :return: The whether_log_storage of this UpdateLogStreamParams.
        :rtype: bool
        """
        return self._whether_log_storage

    @whether_log_storage.setter
    def whether_log_storage(self, whether_log_storage):
        r"""Sets the whether_log_storage of this UpdateLogStreamParams.

        日志是否存储

        :param whether_log_storage: The whether_log_storage of this UpdateLogStreamParams.
        :type whether_log_storage: bool
        """
        self._whether_log_storage = whether_log_storage

    @property
    def hot_cold_separation(self):
        r"""Gets the hot_cold_separation of this UpdateLogStreamParams.

        **参数解释：** 是否开启智能冷存储。 **约束限制：** 开启智能冷存储需要日志存储时间大于7天。开启智能冷存储后，需要设置标准存储层数据的保存时间。标准存储至少需保存7天才能转换为智能冷存储层数据。当日志保存时间大于标准存储层数据保存时间，且小于日志存储时间时，日志数据将自动转换为智能冷存储层数据存储。 **取值范围：** - true：开启智能冷存储。 - false：关闭智能冷存储。 **默认取值：** false

        :return: The hot_cold_separation of this UpdateLogStreamParams.
        :rtype: bool
        """
        return self._hot_cold_separation

    @hot_cold_separation.setter
    def hot_cold_separation(self, hot_cold_separation):
        r"""Sets the hot_cold_separation of this UpdateLogStreamParams.

        **参数解释：** 是否开启智能冷存储。 **约束限制：** 开启智能冷存储需要日志存储时间大于7天。开启智能冷存储后，需要设置标准存储层数据的保存时间。标准存储至少需保存7天才能转换为智能冷存储层数据。当日志保存时间大于标准存储层数据保存时间，且小于日志存储时间时，日志数据将自动转换为智能冷存储层数据存储。 **取值范围：** - true：开启智能冷存储。 - false：关闭智能冷存储。 **默认取值：** false

        :param hot_cold_separation: The hot_cold_separation of this UpdateLogStreamParams.
        :type hot_cold_separation: bool
        """
        self._hot_cold_separation = hot_cold_separation

    @property
    def hot_storage_days(self):
        r"""Gets the hot_storage_days of this UpdateLogStreamParams.

        **参数解释：** 日志流标准存储时间（单位：天），即日志上报到LTS后日志标准存储的时间。 **约束限制：** 开启智能冷存储需要日志总存储时间大于7天。 **取值范围：** 最小值：7天 最大值：365天 **默认取值：** 不涉及。

        :return: The hot_storage_days of this UpdateLogStreamParams.
        :rtype: int
        """
        return self._hot_storage_days

    @hot_storage_days.setter
    def hot_storage_days(self, hot_storage_days):
        r"""Sets the hot_storage_days of this UpdateLogStreamParams.

        **参数解释：** 日志流标准存储时间（单位：天），即日志上报到LTS后日志标准存储的时间。 **约束限制：** 开启智能冷存储需要日志总存储时间大于7天。 **取值范围：** 最小值：7天 最大值：365天 **默认取值：** 不涉及。

        :param hot_storage_days: The hot_storage_days of this UpdateLogStreamParams.
        :type hot_storage_days: int
        """
        self._hot_storage_days = hot_storage_days

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
        if not isinstance(other, UpdateLogStreamParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
