# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateOneClickAlarmsEnabledStateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_ids': 'list[str]',
        'alarm_enabled': 'bool',
        'retain_when_all_disabled': 'bool'
    }

    attribute_map = {
        'alarm_ids': 'alarm_ids',
        'alarm_enabled': 'alarm_enabled',
        'retain_when_all_disabled': 'retain_when_all_disabled'
    }

    def __init__(self, alarm_ids=None, alarm_enabled=None, retain_when_all_disabled=None):
        r"""BatchUpdateOneClickAlarmsEnabledStateRequestBody

        The model defined in huaweicloud sdk

        :param alarm_ids: 需要批量启停的告警规则的ID列表
        :type alarm_ids: list[str]
        :param alarm_enabled: **参数解释**： 是否开启告警规则。     **约束限制**： 不涉及。 **取值范围**： 布尔值。 - true:开启。 - false:关闭。 **默认取值**： true 
        :type alarm_enabled: bool
        :param retain_when_all_disabled: 一键告警中的规则全部被停用时是否保留规则信息。true:保留；false:删除。
        :type retain_when_all_disabled: bool
        """
        
        

        self._alarm_ids = None
        self._alarm_enabled = None
        self._retain_when_all_disabled = None
        self.discriminator = None

        self.alarm_ids = alarm_ids
        self.alarm_enabled = alarm_enabled
        if retain_when_all_disabled is not None:
            self.retain_when_all_disabled = retain_when_all_disabled

    @property
    def alarm_ids(self):
        r"""Gets the alarm_ids of this BatchUpdateOneClickAlarmsEnabledStateRequestBody.

        需要批量启停的告警规则的ID列表

        :return: The alarm_ids of this BatchUpdateOneClickAlarmsEnabledStateRequestBody.
        :rtype: list[str]
        """
        return self._alarm_ids

    @alarm_ids.setter
    def alarm_ids(self, alarm_ids):
        r"""Sets the alarm_ids of this BatchUpdateOneClickAlarmsEnabledStateRequestBody.

        需要批量启停的告警规则的ID列表

        :param alarm_ids: The alarm_ids of this BatchUpdateOneClickAlarmsEnabledStateRequestBody.
        :type alarm_ids: list[str]
        """
        self._alarm_ids = alarm_ids

    @property
    def alarm_enabled(self):
        r"""Gets the alarm_enabled of this BatchUpdateOneClickAlarmsEnabledStateRequestBody.

        **参数解释**： 是否开启告警规则。     **约束限制**： 不涉及。 **取值范围**： 布尔值。 - true:开启。 - false:关闭。 **默认取值**： true 

        :return: The alarm_enabled of this BatchUpdateOneClickAlarmsEnabledStateRequestBody.
        :rtype: bool
        """
        return self._alarm_enabled

    @alarm_enabled.setter
    def alarm_enabled(self, alarm_enabled):
        r"""Sets the alarm_enabled of this BatchUpdateOneClickAlarmsEnabledStateRequestBody.

        **参数解释**： 是否开启告警规则。     **约束限制**： 不涉及。 **取值范围**： 布尔值。 - true:开启。 - false:关闭。 **默认取值**： true 

        :param alarm_enabled: The alarm_enabled of this BatchUpdateOneClickAlarmsEnabledStateRequestBody.
        :type alarm_enabled: bool
        """
        self._alarm_enabled = alarm_enabled

    @property
    def retain_when_all_disabled(self):
        r"""Gets the retain_when_all_disabled of this BatchUpdateOneClickAlarmsEnabledStateRequestBody.

        一键告警中的规则全部被停用时是否保留规则信息。true:保留；false:删除。

        :return: The retain_when_all_disabled of this BatchUpdateOneClickAlarmsEnabledStateRequestBody.
        :rtype: bool
        """
        return self._retain_when_all_disabled

    @retain_when_all_disabled.setter
    def retain_when_all_disabled(self, retain_when_all_disabled):
        r"""Sets the retain_when_all_disabled of this BatchUpdateOneClickAlarmsEnabledStateRequestBody.

        一键告警中的规则全部被停用时是否保留规则信息。true:保留；false:删除。

        :param retain_when_all_disabled: The retain_when_all_disabled of this BatchUpdateOneClickAlarmsEnabledStateRequestBody.
        :type retain_when_all_disabled: bool
        """
        self._retain_when_all_disabled = retain_when_all_disabled

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
        if not isinstance(other, BatchUpdateOneClickAlarmsEnabledStateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
