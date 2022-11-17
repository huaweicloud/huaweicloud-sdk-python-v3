# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeAlarmRuleStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_rule_id': 'str',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'alarm_rule_id': 'alarm_rule_id',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, alarm_rule_id=None, status=None, type=None):
        """ChangeAlarmRuleStatus

        The model defined in huaweicloud sdk

        :param alarm_rule_id: 告警规则ID
        :type alarm_rule_id: str
        :param status: 状态（RUNNING/STOPPING）
        :type status: str
        :param type: 类型
        :type type: str
        """
        
        

        self._alarm_rule_id = None
        self._status = None
        self._type = None
        self.discriminator = None

        self.alarm_rule_id = alarm_rule_id
        self.status = status
        self.type = type

    @property
    def alarm_rule_id(self):
        """Gets the alarm_rule_id of this ChangeAlarmRuleStatus.

        告警规则ID

        :return: The alarm_rule_id of this ChangeAlarmRuleStatus.
        :rtype: str
        """
        return self._alarm_rule_id

    @alarm_rule_id.setter
    def alarm_rule_id(self, alarm_rule_id):
        """Sets the alarm_rule_id of this ChangeAlarmRuleStatus.

        告警规则ID

        :param alarm_rule_id: The alarm_rule_id of this ChangeAlarmRuleStatus.
        :type alarm_rule_id: str
        """
        self._alarm_rule_id = alarm_rule_id

    @property
    def status(self):
        """Gets the status of this ChangeAlarmRuleStatus.

        状态（RUNNING/STOPPING）

        :return: The status of this ChangeAlarmRuleStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ChangeAlarmRuleStatus.

        状态（RUNNING/STOPPING）

        :param status: The status of this ChangeAlarmRuleStatus.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this ChangeAlarmRuleStatus.

        类型

        :return: The type of this ChangeAlarmRuleStatus.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ChangeAlarmRuleStatus.

        类型

        :param type: The type of this ChangeAlarmRuleStatus.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ChangeAlarmRuleStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
