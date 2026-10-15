# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutoscalingHistory:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tuning_id': 'str',
        'job_id': 'str',
        'action_type': 'str',
        'tuning_message': 'str',
        'old_resource_setting': 'AutoscalingHistoryOldResourceSetting',
        'new_resource_setting': 'AutoscalingHistoryNewResourceSetting',
        'trigger_time': 'datetime'
    }

    attribute_map = {
        'tuning_id': 'tuning_id',
        'job_id': 'job_id',
        'action_type': 'action_type',
        'tuning_message': 'tuning_message',
        'old_resource_setting': 'old_resource_setting',
        'new_resource_setting': 'new_resource_setting',
        'trigger_time': 'trigger_time'
    }

    def __init__(self, tuning_id=None, job_id=None, action_type=None, tuning_message=None, old_resource_setting=None, new_resource_setting=None, trigger_time=None):
        r"""AutoscalingHistory

        The model defined in huaweicloud sdk

        :param tuning_id: **参数解释**：调优记录唯一ID。 **取值范围**：UUID格式，长度为36个字符。
        :type tuning_id: str
        :param job_id: **参数解释**：Flink作业ID。 **取值范围**：UUIDv7格式，长度为36个字符。
        :type job_id: str
        :param action_type: **参数解释**：调优动作类型。 **取值范围**：   - SCALE_OUT：扩容（并行度增加）。   - SCALE_IN：缩容（并行度减少）。
        :type action_type: str
        :param tuning_message: **参数解释**：调优消息，国际化字符串，人类可读，不建议程序化解析。 **取值范围**：不涉及。
        :type tuning_message: str
        :param old_resource_setting: 
        :type old_resource_setting: :class:`huaweicloudsdkaidatalake.v2.AutoscalingHistoryOldResourceSetting`
        :param new_resource_setting: 
        :type new_resource_setting: :class:`huaweicloudsdkaidatalake.v2.AutoscalingHistoryNewResourceSetting`
        :param trigger_time: **参数解释**：调优触发时间，格式为ISO 8601标准的UTC日期时间字符串。 **取值范围**：不涉及。
        :type trigger_time: datetime
        """
        
        

        self._tuning_id = None
        self._job_id = None
        self._action_type = None
        self._tuning_message = None
        self._old_resource_setting = None
        self._new_resource_setting = None
        self._trigger_time = None
        self.discriminator = None

        self.tuning_id = tuning_id
        if job_id is not None:
            self.job_id = job_id
        self.action_type = action_type
        if tuning_message is not None:
            self.tuning_message = tuning_message
        if old_resource_setting is not None:
            self.old_resource_setting = old_resource_setting
        if new_resource_setting is not None:
            self.new_resource_setting = new_resource_setting
        self.trigger_time = trigger_time

    @property
    def tuning_id(self):
        r"""Gets the tuning_id of this AutoscalingHistory.

        **参数解释**：调优记录唯一ID。 **取值范围**：UUID格式，长度为36个字符。

        :return: The tuning_id of this AutoscalingHistory.
        :rtype: str
        """
        return self._tuning_id

    @tuning_id.setter
    def tuning_id(self, tuning_id):
        r"""Sets the tuning_id of this AutoscalingHistory.

        **参数解释**：调优记录唯一ID。 **取值范围**：UUID格式，长度为36个字符。

        :param tuning_id: The tuning_id of this AutoscalingHistory.
        :type tuning_id: str
        """
        self._tuning_id = tuning_id

    @property
    def job_id(self):
        r"""Gets the job_id of this AutoscalingHistory.

        **参数解释**：Flink作业ID。 **取值范围**：UUIDv7格式，长度为36个字符。

        :return: The job_id of this AutoscalingHistory.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this AutoscalingHistory.

        **参数解释**：Flink作业ID。 **取值范围**：UUIDv7格式，长度为36个字符。

        :param job_id: The job_id of this AutoscalingHistory.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def action_type(self):
        r"""Gets the action_type of this AutoscalingHistory.

        **参数解释**：调优动作类型。 **取值范围**：   - SCALE_OUT：扩容（并行度增加）。   - SCALE_IN：缩容（并行度减少）。

        :return: The action_type of this AutoscalingHistory.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        r"""Sets the action_type of this AutoscalingHistory.

        **参数解释**：调优动作类型。 **取值范围**：   - SCALE_OUT：扩容（并行度增加）。   - SCALE_IN：缩容（并行度减少）。

        :param action_type: The action_type of this AutoscalingHistory.
        :type action_type: str
        """
        self._action_type = action_type

    @property
    def tuning_message(self):
        r"""Gets the tuning_message of this AutoscalingHistory.

        **参数解释**：调优消息，国际化字符串，人类可读，不建议程序化解析。 **取值范围**：不涉及。

        :return: The tuning_message of this AutoscalingHistory.
        :rtype: str
        """
        return self._tuning_message

    @tuning_message.setter
    def tuning_message(self, tuning_message):
        r"""Sets the tuning_message of this AutoscalingHistory.

        **参数解释**：调优消息，国际化字符串，人类可读，不建议程序化解析。 **取值范围**：不涉及。

        :param tuning_message: The tuning_message of this AutoscalingHistory.
        :type tuning_message: str
        """
        self._tuning_message = tuning_message

    @property
    def old_resource_setting(self):
        r"""Gets the old_resource_setting of this AutoscalingHistory.

        :return: The old_resource_setting of this AutoscalingHistory.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.AutoscalingHistoryOldResourceSetting`
        """
        return self._old_resource_setting

    @old_resource_setting.setter
    def old_resource_setting(self, old_resource_setting):
        r"""Sets the old_resource_setting of this AutoscalingHistory.

        :param old_resource_setting: The old_resource_setting of this AutoscalingHistory.
        :type old_resource_setting: :class:`huaweicloudsdkaidatalake.v2.AutoscalingHistoryOldResourceSetting`
        """
        self._old_resource_setting = old_resource_setting

    @property
    def new_resource_setting(self):
        r"""Gets the new_resource_setting of this AutoscalingHistory.

        :return: The new_resource_setting of this AutoscalingHistory.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.AutoscalingHistoryNewResourceSetting`
        """
        return self._new_resource_setting

    @new_resource_setting.setter
    def new_resource_setting(self, new_resource_setting):
        r"""Sets the new_resource_setting of this AutoscalingHistory.

        :param new_resource_setting: The new_resource_setting of this AutoscalingHistory.
        :type new_resource_setting: :class:`huaweicloudsdkaidatalake.v2.AutoscalingHistoryNewResourceSetting`
        """
        self._new_resource_setting = new_resource_setting

    @property
    def trigger_time(self):
        r"""Gets the trigger_time of this AutoscalingHistory.

        **参数解释**：调优触发时间，格式为ISO 8601标准的UTC日期时间字符串。 **取值范围**：不涉及。

        :return: The trigger_time of this AutoscalingHistory.
        :rtype: datetime
        """
        return self._trigger_time

    @trigger_time.setter
    def trigger_time(self, trigger_time):
        r"""Sets the trigger_time of this AutoscalingHistory.

        **参数解释**：调优触发时间，格式为ISO 8601标准的UTC日期时间字符串。 **取值范围**：不涉及。

        :param trigger_time: The trigger_time of this AutoscalingHistory.
        :type trigger_time: datetime
        """
        self._trigger_time = trigger_time

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
        if not isinstance(other, AutoscalingHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
