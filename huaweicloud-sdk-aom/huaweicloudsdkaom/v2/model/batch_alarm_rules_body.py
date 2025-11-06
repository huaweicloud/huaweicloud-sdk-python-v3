# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchAlarmRulesBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_rule_enable': 'bool',
        'alarm_rule_id': 'int',
        'alarm_rule_name': 'str',
        'alarm_rule_type': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'alarm_rule_enable': 'alarm_rule_enable',
        'alarm_rule_id': 'alarm_rule_id',
        'alarm_rule_name': 'alarm_rule_name',
        'alarm_rule_type': 'alarm_rule_type',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, alarm_rule_enable=None, alarm_rule_id=None, alarm_rule_name=None, alarm_rule_type=None, enterprise_project_id=None):
        r"""BatchAlarmRulesBody

        The model defined in huaweicloud sdk

        :param alarm_rule_enable: 当前状态是否启用。
        :type alarm_rule_enable: bool
        :param alarm_rule_id: 告警规则id。
        :type alarm_rule_id: int
        :param alarm_rule_name: 告警规则名称。
        :type alarm_rule_name: str
        :param alarm_rule_type: 告警规则类型。 - metric：Prometheus指标 - event： 事件
        :type alarm_rule_type: str
        :param enterprise_project_id: 企业项目id。获取方式请参见：[获取企业项目ID](aom_04_0024.xml) 。  批量启停或批量修改单个企业项目下实例，填写企业项目id。
        :type enterprise_project_id: str
        """
        
        

        self._alarm_rule_enable = None
        self._alarm_rule_id = None
        self._alarm_rule_name = None
        self._alarm_rule_type = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.alarm_rule_enable = alarm_rule_enable
        self.alarm_rule_id = alarm_rule_id
        self.alarm_rule_name = alarm_rule_name
        self.alarm_rule_type = alarm_rule_type
        self.enterprise_project_id = enterprise_project_id

    @property
    def alarm_rule_enable(self):
        r"""Gets the alarm_rule_enable of this BatchAlarmRulesBody.

        当前状态是否启用。

        :return: The alarm_rule_enable of this BatchAlarmRulesBody.
        :rtype: bool
        """
        return self._alarm_rule_enable

    @alarm_rule_enable.setter
    def alarm_rule_enable(self, alarm_rule_enable):
        r"""Sets the alarm_rule_enable of this BatchAlarmRulesBody.

        当前状态是否启用。

        :param alarm_rule_enable: The alarm_rule_enable of this BatchAlarmRulesBody.
        :type alarm_rule_enable: bool
        """
        self._alarm_rule_enable = alarm_rule_enable

    @property
    def alarm_rule_id(self):
        r"""Gets the alarm_rule_id of this BatchAlarmRulesBody.

        告警规则id。

        :return: The alarm_rule_id of this BatchAlarmRulesBody.
        :rtype: int
        """
        return self._alarm_rule_id

    @alarm_rule_id.setter
    def alarm_rule_id(self, alarm_rule_id):
        r"""Sets the alarm_rule_id of this BatchAlarmRulesBody.

        告警规则id。

        :param alarm_rule_id: The alarm_rule_id of this BatchAlarmRulesBody.
        :type alarm_rule_id: int
        """
        self._alarm_rule_id = alarm_rule_id

    @property
    def alarm_rule_name(self):
        r"""Gets the alarm_rule_name of this BatchAlarmRulesBody.

        告警规则名称。

        :return: The alarm_rule_name of this BatchAlarmRulesBody.
        :rtype: str
        """
        return self._alarm_rule_name

    @alarm_rule_name.setter
    def alarm_rule_name(self, alarm_rule_name):
        r"""Sets the alarm_rule_name of this BatchAlarmRulesBody.

        告警规则名称。

        :param alarm_rule_name: The alarm_rule_name of this BatchAlarmRulesBody.
        :type alarm_rule_name: str
        """
        self._alarm_rule_name = alarm_rule_name

    @property
    def alarm_rule_type(self):
        r"""Gets the alarm_rule_type of this BatchAlarmRulesBody.

        告警规则类型。 - metric：Prometheus指标 - event： 事件

        :return: The alarm_rule_type of this BatchAlarmRulesBody.
        :rtype: str
        """
        return self._alarm_rule_type

    @alarm_rule_type.setter
    def alarm_rule_type(self, alarm_rule_type):
        r"""Sets the alarm_rule_type of this BatchAlarmRulesBody.

        告警规则类型。 - metric：Prometheus指标 - event： 事件

        :param alarm_rule_type: The alarm_rule_type of this BatchAlarmRulesBody.
        :type alarm_rule_type: str
        """
        self._alarm_rule_type = alarm_rule_type

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this BatchAlarmRulesBody.

        企业项目id。获取方式请参见：[获取企业项目ID](aom_04_0024.xml) 。  批量启停或批量修改单个企业项目下实例，填写企业项目id。

        :return: The enterprise_project_id of this BatchAlarmRulesBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this BatchAlarmRulesBody.

        企业项目id。获取方式请参见：[获取企业项目ID](aom_04_0024.xml) 。  批量启停或批量修改单个企业项目下实例，填写企业项目id。

        :param enterprise_project_id: The enterprise_project_id of this BatchAlarmRulesBody.
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
        if not isinstance(other, BatchAlarmRulesBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
