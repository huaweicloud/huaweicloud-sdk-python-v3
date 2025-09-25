# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmHistoryRecordResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_id': 'str',
        'name': 'str',
        'status': 'str',
        'alarm_type': 'str',
        'level': 'int',
        'instance_id': 'str',
        'instance_name': 'str',
        'begin_time': 'int',
        'update_time': 'int'
    }

    attribute_map = {
        'alarm_id': 'alarm_id',
        'name': 'name',
        'status': 'status',
        'alarm_type': 'alarm_type',
        'level': 'level',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'begin_time': 'begin_time',
        'update_time': 'update_time'
    }

    def __init__(self, alarm_id=None, name=None, status=None, alarm_type=None, level=None, instance_id=None, instance_name=None, begin_time=None, update_time=None):
        r"""AlarmHistoryRecordResult

        The model defined in huaweicloud sdk

        :param alarm_id: **参数解释**： 告警规则ID。 **取值范围**： 不涉及。
        :type alarm_id: str
        :param name: **参数解释**： 告警规则名称。 **取值范围**： 不涉及。
        :type name: str
        :param status: **参数解释**： 告警记录的状态。 **取值范围**： - ok：正常。 - alarm：告警。 - invalid：已失效。
        :type status: str
        :param alarm_type: **参数解释**： 告警规则类型。 **取值范围**： - EVENT.SYS：系统事件告警。 - EVENT.CUSTOM：自定义事件告警。 - DNSHealthCheck：DNS健康检查告警。 - RESOURCE_GROUP：资源分组告警。 - MULTI_INSTANCE：指定资源告警。
        :type alarm_type: str
        :param level: **参数解释**： 告警历史的告警级别。 **取值范围**： - 1：紧急。 - 2：重要。 - 3：次要。 - 4：提示。
        :type level: int
        :param instance_id: **参数解释**： 实例ID。 **取值范围**： 只能由英文字母、数字组成，且长度为36个字符。
        :type instance_id: str
        :param instance_name: **参数解释**： 实例名称。 **取值范围**： 不涉及。
        :type instance_name: str
        :param begin_time: **参数解释**： 告警开始时间。 **取值范围**： UNIX时间戳，单位毫秒，例如：1603131199000。
        :type begin_time: int
        :param update_time: **参数解释**： 告警规则的最后更新时间。 **取值范围**： UNIX时间戳，单位毫秒，例如：1603131199000。
        :type update_time: int
        """
        
        

        self._alarm_id = None
        self._name = None
        self._status = None
        self._alarm_type = None
        self._level = None
        self._instance_id = None
        self._instance_name = None
        self._begin_time = None
        self._update_time = None
        self.discriminator = None

        self.alarm_id = alarm_id
        self.name = name
        self.status = status
        self.alarm_type = alarm_type
        self.level = level
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.begin_time = begin_time
        self.update_time = update_time

    @property
    def alarm_id(self):
        r"""Gets the alarm_id of this AlarmHistoryRecordResult.

        **参数解释**： 告警规则ID。 **取值范围**： 不涉及。

        :return: The alarm_id of this AlarmHistoryRecordResult.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        r"""Sets the alarm_id of this AlarmHistoryRecordResult.

        **参数解释**： 告警规则ID。 **取值范围**： 不涉及。

        :param alarm_id: The alarm_id of this AlarmHistoryRecordResult.
        :type alarm_id: str
        """
        self._alarm_id = alarm_id

    @property
    def name(self):
        r"""Gets the name of this AlarmHistoryRecordResult.

        **参数解释**： 告警规则名称。 **取值范围**： 不涉及。

        :return: The name of this AlarmHistoryRecordResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AlarmHistoryRecordResult.

        **参数解释**： 告警规则名称。 **取值范围**： 不涉及。

        :param name: The name of this AlarmHistoryRecordResult.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this AlarmHistoryRecordResult.

        **参数解释**： 告警记录的状态。 **取值范围**： - ok：正常。 - alarm：告警。 - invalid：已失效。

        :return: The status of this AlarmHistoryRecordResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AlarmHistoryRecordResult.

        **参数解释**： 告警记录的状态。 **取值范围**： - ok：正常。 - alarm：告警。 - invalid：已失效。

        :param status: The status of this AlarmHistoryRecordResult.
        :type status: str
        """
        self._status = status

    @property
    def alarm_type(self):
        r"""Gets the alarm_type of this AlarmHistoryRecordResult.

        **参数解释**： 告警规则类型。 **取值范围**： - EVENT.SYS：系统事件告警。 - EVENT.CUSTOM：自定义事件告警。 - DNSHealthCheck：DNS健康检查告警。 - RESOURCE_GROUP：资源分组告警。 - MULTI_INSTANCE：指定资源告警。

        :return: The alarm_type of this AlarmHistoryRecordResult.
        :rtype: str
        """
        return self._alarm_type

    @alarm_type.setter
    def alarm_type(self, alarm_type):
        r"""Sets the alarm_type of this AlarmHistoryRecordResult.

        **参数解释**： 告警规则类型。 **取值范围**： - EVENT.SYS：系统事件告警。 - EVENT.CUSTOM：自定义事件告警。 - DNSHealthCheck：DNS健康检查告警。 - RESOURCE_GROUP：资源分组告警。 - MULTI_INSTANCE：指定资源告警。

        :param alarm_type: The alarm_type of this AlarmHistoryRecordResult.
        :type alarm_type: str
        """
        self._alarm_type = alarm_type

    @property
    def level(self):
        r"""Gets the level of this AlarmHistoryRecordResult.

        **参数解释**： 告警历史的告警级别。 **取值范围**： - 1：紧急。 - 2：重要。 - 3：次要。 - 4：提示。

        :return: The level of this AlarmHistoryRecordResult.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this AlarmHistoryRecordResult.

        **参数解释**： 告警历史的告警级别。 **取值范围**： - 1：紧急。 - 2：重要。 - 3：次要。 - 4：提示。

        :param level: The level of this AlarmHistoryRecordResult.
        :type level: int
        """
        self._level = level

    @property
    def instance_id(self):
        r"""Gets the instance_id of this AlarmHistoryRecordResult.

        **参数解释**： 实例ID。 **取值范围**： 只能由英文字母、数字组成，且长度为36个字符。

        :return: The instance_id of this AlarmHistoryRecordResult.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this AlarmHistoryRecordResult.

        **参数解释**： 实例ID。 **取值范围**： 只能由英文字母、数字组成，且长度为36个字符。

        :param instance_id: The instance_id of this AlarmHistoryRecordResult.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this AlarmHistoryRecordResult.

        **参数解释**： 实例名称。 **取值范围**： 不涉及。

        :return: The instance_name of this AlarmHistoryRecordResult.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this AlarmHistoryRecordResult.

        **参数解释**： 实例名称。 **取值范围**： 不涉及。

        :param instance_name: The instance_name of this AlarmHistoryRecordResult.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def begin_time(self):
        r"""Gets the begin_time of this AlarmHistoryRecordResult.

        **参数解释**： 告警开始时间。 **取值范围**： UNIX时间戳，单位毫秒，例如：1603131199000。

        :return: The begin_time of this AlarmHistoryRecordResult.
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this AlarmHistoryRecordResult.

        **参数解释**： 告警开始时间。 **取值范围**： UNIX时间戳，单位毫秒，例如：1603131199000。

        :param begin_time: The begin_time of this AlarmHistoryRecordResult.
        :type begin_time: int
        """
        self._begin_time = begin_time

    @property
    def update_time(self):
        r"""Gets the update_time of this AlarmHistoryRecordResult.

        **参数解释**： 告警规则的最后更新时间。 **取值范围**： UNIX时间戳，单位毫秒，例如：1603131199000。

        :return: The update_time of this AlarmHistoryRecordResult.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AlarmHistoryRecordResult.

        **参数解释**： 告警规则的最后更新时间。 **取值范围**： UNIX时间戳，单位毫秒，例如：1603131199000。

        :param update_time: The update_time of this AlarmHistoryRecordResult.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, AlarmHistoryRecordResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
