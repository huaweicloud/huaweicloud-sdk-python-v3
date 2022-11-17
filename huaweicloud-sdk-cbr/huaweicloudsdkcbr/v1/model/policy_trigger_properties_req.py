# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyTriggerPropertiesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pattern': 'list[str]'
    }

    attribute_map = {
        'pattern': 'pattern'
    }

    def __init__(self, pattern=None):
        """PolicyTriggerPropertiesReq

        The model defined in huaweicloud sdk

        :param pattern: 调度规则。限制24条规则。调度器的调度规则，可参照iCalendar RFC 2445规范中的事件规则，但仅支持FREQ、BYDAY、BYHOUR、BYMINUTE、INTERVAL等参数，其中FREQ仅支持WEEKLY和DAILY，BYDAY支持一周七天（MO、TU、WE、TH、FR、SA、SU），BYHOUR支持0-23小时，BYMINUTE支持0-59分钟，并且间隔不能小于一小时，一天最大24个时间点。例如，周一到周天，每天UTC时间的14:00调度，其规则为：&#39;FREQ&#x3D;WEEKLY;BYDAY&#x3D;MO,TU,WE,TH,FR,SA,SU;BYHOUR&#x3D;14;BYMINUTE&#x3D;00&#39;。例如：某个地区的时间为 UTC+8，若在该地区每天14:00调度，则在14点基础上减8，其规则为&#39;FREQ&#x3D;DAILY;INTERVAL&#x3D;1;BYHOUR&#x3D;6;BYMINUTE&#x3D;00&#39;。
        :type pattern: list[str]
        """
        
        

        self._pattern = None
        self.discriminator = None

        self.pattern = pattern

    @property
    def pattern(self):
        """Gets the pattern of this PolicyTriggerPropertiesReq.

        调度规则。限制24条规则。调度器的调度规则，可参照iCalendar RFC 2445规范中的事件规则，但仅支持FREQ、BYDAY、BYHOUR、BYMINUTE、INTERVAL等参数，其中FREQ仅支持WEEKLY和DAILY，BYDAY支持一周七天（MO、TU、WE、TH、FR、SA、SU），BYHOUR支持0-23小时，BYMINUTE支持0-59分钟，并且间隔不能小于一小时，一天最大24个时间点。例如，周一到周天，每天UTC时间的14:00调度，其规则为：'FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR,SA,SU;BYHOUR=14;BYMINUTE=00'。例如：某个地区的时间为 UTC+8，若在该地区每天14:00调度，则在14点基础上减8，其规则为'FREQ=DAILY;INTERVAL=1;BYHOUR=6;BYMINUTE=00'。

        :return: The pattern of this PolicyTriggerPropertiesReq.
        :rtype: list[str]
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this PolicyTriggerPropertiesReq.

        调度规则。限制24条规则。调度器的调度规则，可参照iCalendar RFC 2445规范中的事件规则，但仅支持FREQ、BYDAY、BYHOUR、BYMINUTE、INTERVAL等参数，其中FREQ仅支持WEEKLY和DAILY，BYDAY支持一周七天（MO、TU、WE、TH、FR、SA、SU），BYHOUR支持0-23小时，BYMINUTE支持0-59分钟，并且间隔不能小于一小时，一天最大24个时间点。例如，周一到周天，每天UTC时间的14:00调度，其规则为：'FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR,SA,SU;BYHOUR=14;BYMINUTE=00'。例如：某个地区的时间为 UTC+8，若在该地区每天14:00调度，则在14点基础上减8，其规则为'FREQ=DAILY;INTERVAL=1;BYHOUR=6;BYMINUTE=00'。

        :param pattern: The pattern of this PolicyTriggerPropertiesReq.
        :type pattern: list[str]
        """
        self._pattern = pattern

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
        if not isinstance(other, PolicyTriggerPropertiesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
