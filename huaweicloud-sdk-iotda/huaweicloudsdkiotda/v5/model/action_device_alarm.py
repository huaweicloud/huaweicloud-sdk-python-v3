# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActionDeviceAlarm:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'alarm_status': 'str',
        'severity': 'str',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'alarm_status': 'alarm_status',
        'severity': 'severity',
        'description': 'description'
    }

    def __init__(self, name=None, alarm_status=None, severity=None, description=None):
        """ActionDeviceAlarm

        The model defined in huaweicloud sdk

        :param name: **参数说明**：告警名称。
        :type name: str
        :param alarm_status: **参数说明**：告警状态。 **取值范围**： - fault：上报告警。 - recovery：恢复告警。
        :type alarm_status: str
        :param severity: **参数说明**：告警级别。 **取值范围**： - warning：警告。 - minor：一般。 - major：严重。 - critical：致命。
        :type severity: str
        :param description: **参数说明**：告警的描述信息。
        :type description: str
        """
        
        

        self._name = None
        self._alarm_status = None
        self._severity = None
        self._description = None
        self.discriminator = None

        self.name = name
        self.alarm_status = alarm_status
        self.severity = severity
        if description is not None:
            self.description = description

    @property
    def name(self):
        """Gets the name of this ActionDeviceAlarm.

        **参数说明**：告警名称。

        :return: The name of this ActionDeviceAlarm.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ActionDeviceAlarm.

        **参数说明**：告警名称。

        :param name: The name of this ActionDeviceAlarm.
        :type name: str
        """
        self._name = name

    @property
    def alarm_status(self):
        """Gets the alarm_status of this ActionDeviceAlarm.

        **参数说明**：告警状态。 **取值范围**： - fault：上报告警。 - recovery：恢复告警。

        :return: The alarm_status of this ActionDeviceAlarm.
        :rtype: str
        """
        return self._alarm_status

    @alarm_status.setter
    def alarm_status(self, alarm_status):
        """Sets the alarm_status of this ActionDeviceAlarm.

        **参数说明**：告警状态。 **取值范围**： - fault：上报告警。 - recovery：恢复告警。

        :param alarm_status: The alarm_status of this ActionDeviceAlarm.
        :type alarm_status: str
        """
        self._alarm_status = alarm_status

    @property
    def severity(self):
        """Gets the severity of this ActionDeviceAlarm.

        **参数说明**：告警级别。 **取值范围**： - warning：警告。 - minor：一般。 - major：严重。 - critical：致命。

        :return: The severity of this ActionDeviceAlarm.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this ActionDeviceAlarm.

        **参数说明**：告警级别。 **取值范围**： - warning：警告。 - minor：一般。 - major：严重。 - critical：致命。

        :param severity: The severity of this ActionDeviceAlarm.
        :type severity: str
        """
        self._severity = severity

    @property
    def description(self):
        """Gets the description of this ActionDeviceAlarm.

        **参数说明**：告警的描述信息。

        :return: The description of this ActionDeviceAlarm.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ActionDeviceAlarm.

        **参数说明**：告警的描述信息。

        :param description: The description of this ActionDeviceAlarm.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ActionDeviceAlarm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
