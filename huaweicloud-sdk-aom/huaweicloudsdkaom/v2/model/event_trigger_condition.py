# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventTriggerCondition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_name': 'str',
        'trigger_type': 'str',
        'aggregation_window': 'int',
        'operator': 'str',
        'thresholds': 'dict(str, int)',
        'frequency': 'str'
    }

    attribute_map = {
        'event_name': 'event_name',
        'trigger_type': 'trigger_type',
        'aggregation_window': 'aggregation_window',
        'operator': 'operator',
        'thresholds': 'thresholds',
        'frequency': 'frequency'
    }

    def __init__(self, event_name=None, trigger_type=None, aggregation_window=None, operator=None, thresholds=None, frequency=None):
        r"""EventTriggerCondition

        The model defined in huaweicloud sdk

        :param event_name: 事件名称。
        :type event_name: str
        :param trigger_type: 触发方式： - “immediately”：立即触发 - “accumulative”：累计触发
        :type trigger_type: str
        :param aggregation_window: 统计周期。单位为秒，例如 1小时 填“3600”，当trigger_type为“immediately”时 不填。
        :type aggregation_window: int
        :param operator: 判断条件：“&gt;”,“&lt;”,“&#x3D;”,“&gt;&#x3D;”,“&lt;&#x3D;”，当trigger_type为“immediately”时 不填。
        :type operator: str
        :param thresholds: 键值对形式，键为告警级别，值为累计次数，当trigger_type为“immediately”时 值为空。
        :type thresholds: dict(str, int)
        :param frequency: 事件类告警频率。当trigger_type为“immediately”时 不填。 - “0”：只告警一次 - “300”：每5分钟 - “600”：每10分钟： - “900”：每15分钟： - “1800”：每30分钟： - “3600”：每1小时： - “10800”：每3小时： - “21600”：每6小时： - “43200”：每12小时： - “86400”：每天：
        :type frequency: str
        """
        
        

        self._event_name = None
        self._trigger_type = None
        self._aggregation_window = None
        self._operator = None
        self._thresholds = None
        self._frequency = None
        self.discriminator = None

        if event_name is not None:
            self.event_name = event_name
        if trigger_type is not None:
            self.trigger_type = trigger_type
        if aggregation_window is not None:
            self.aggregation_window = aggregation_window
        if operator is not None:
            self.operator = operator
        if thresholds is not None:
            self.thresholds = thresholds
        if frequency is not None:
            self.frequency = frequency

    @property
    def event_name(self):
        r"""Gets the event_name of this EventTriggerCondition.

        事件名称。

        :return: The event_name of this EventTriggerCondition.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        r"""Sets the event_name of this EventTriggerCondition.

        事件名称。

        :param event_name: The event_name of this EventTriggerCondition.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def trigger_type(self):
        r"""Gets the trigger_type of this EventTriggerCondition.

        触发方式： - “immediately”：立即触发 - “accumulative”：累计触发

        :return: The trigger_type of this EventTriggerCondition.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        r"""Sets the trigger_type of this EventTriggerCondition.

        触发方式： - “immediately”：立即触发 - “accumulative”：累计触发

        :param trigger_type: The trigger_type of this EventTriggerCondition.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

    @property
    def aggregation_window(self):
        r"""Gets the aggregation_window of this EventTriggerCondition.

        统计周期。单位为秒，例如 1小时 填“3600”，当trigger_type为“immediately”时 不填。

        :return: The aggregation_window of this EventTriggerCondition.
        :rtype: int
        """
        return self._aggregation_window

    @aggregation_window.setter
    def aggregation_window(self, aggregation_window):
        r"""Sets the aggregation_window of this EventTriggerCondition.

        统计周期。单位为秒，例如 1小时 填“3600”，当trigger_type为“immediately”时 不填。

        :param aggregation_window: The aggregation_window of this EventTriggerCondition.
        :type aggregation_window: int
        """
        self._aggregation_window = aggregation_window

    @property
    def operator(self):
        r"""Gets the operator of this EventTriggerCondition.

        判断条件：“>”,“<”,“=”,“>=”,“<=”，当trigger_type为“immediately”时 不填。

        :return: The operator of this EventTriggerCondition.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this EventTriggerCondition.

        判断条件：“>”,“<”,“=”,“>=”,“<=”，当trigger_type为“immediately”时 不填。

        :param operator: The operator of this EventTriggerCondition.
        :type operator: str
        """
        self._operator = operator

    @property
    def thresholds(self):
        r"""Gets the thresholds of this EventTriggerCondition.

        键值对形式，键为告警级别，值为累计次数，当trigger_type为“immediately”时 值为空。

        :return: The thresholds of this EventTriggerCondition.
        :rtype: dict(str, int)
        """
        return self._thresholds

    @thresholds.setter
    def thresholds(self, thresholds):
        r"""Sets the thresholds of this EventTriggerCondition.

        键值对形式，键为告警级别，值为累计次数，当trigger_type为“immediately”时 值为空。

        :param thresholds: The thresholds of this EventTriggerCondition.
        :type thresholds: dict(str, int)
        """
        self._thresholds = thresholds

    @property
    def frequency(self):
        r"""Gets the frequency of this EventTriggerCondition.

        事件类告警频率。当trigger_type为“immediately”时 不填。 - “0”：只告警一次 - “300”：每5分钟 - “600”：每10分钟： - “900”：每15分钟： - “1800”：每30分钟： - “3600”：每1小时： - “10800”：每3小时： - “21600”：每6小时： - “43200”：每12小时： - “86400”：每天：

        :return: The frequency of this EventTriggerCondition.
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        r"""Sets the frequency of this EventTriggerCondition.

        事件类告警频率。当trigger_type为“immediately”时 不填。 - “0”：只告警一次 - “300”：每5分钟 - “600”：每10分钟： - “900”：每15分钟： - “1800”：每30分钟： - “3600”：每1小时： - “10800”：每3小时： - “21600”：每6小时： - “43200”：每12小时： - “86400”：每天：

        :param frequency: The frequency of this EventTriggerCondition.
        :type frequency: str
        """
        self._frequency = frequency

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
        if not isinstance(other, EventTriggerCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
