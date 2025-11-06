# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmTemplateSpecItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_template_name': 'str',
        'alarm_template_name_en': 'str',
        'desc': 'str',
        'desc_en': 'str',
        'alarm_template_spec_type': 'str',
        'metric_alarm_template_spec': 'MetricAlarmTemplateSpec',
        'event_alarm_template_spec': 'EventAlarmTemplateSpec'
    }

    attribute_map = {
        'alarm_template_name': 'alarm_template_name',
        'alarm_template_name_en': 'alarm_template_name_en',
        'desc': 'desc',
        'desc_en': 'desc_en',
        'alarm_template_spec_type': 'alarm_template_spec_type',
        'metric_alarm_template_spec': 'metric_alarm_template_spec',
        'event_alarm_template_spec': 'event_alarm_template_spec'
    }

    def __init__(self, alarm_template_name=None, alarm_template_name_en=None, desc=None, desc_en=None, alarm_template_spec_type=None, metric_alarm_template_spec=None, event_alarm_template_spec=None):
        r"""AlarmTemplateSpecItem

        The model defined in huaweicloud sdk

        :param alarm_template_name: 告警模板下单个告警规则名称。
        :type alarm_template_name: str
        :param alarm_template_name_en: 告警模板下单个告警规则英文名称。
        :type alarm_template_name_en: str
        :param desc: 告警模板下单个告警规则描述。
        :type desc: str
        :param desc_en: 告警模板下单个告警规则英文描述。
        :type desc_en: str
        :param alarm_template_spec_type: 告警模板下单个告警规则类型。 “metric”：指标告警 “event”：事件告警
        :type alarm_template_spec_type: str
        :param metric_alarm_template_spec: 
        :type metric_alarm_template_spec: :class:`huaweicloudsdkaom.v2.MetricAlarmTemplateSpec`
        :param event_alarm_template_spec: 
        :type event_alarm_template_spec: :class:`huaweicloudsdkaom.v2.EventAlarmTemplateSpec`
        """
        
        

        self._alarm_template_name = None
        self._alarm_template_name_en = None
        self._desc = None
        self._desc_en = None
        self._alarm_template_spec_type = None
        self._metric_alarm_template_spec = None
        self._event_alarm_template_spec = None
        self.discriminator = None

        self.alarm_template_name = alarm_template_name
        if alarm_template_name_en is not None:
            self.alarm_template_name_en = alarm_template_name_en
        if desc is not None:
            self.desc = desc
        if desc_en is not None:
            self.desc_en = desc_en
        self.alarm_template_spec_type = alarm_template_spec_type
        if metric_alarm_template_spec is not None:
            self.metric_alarm_template_spec = metric_alarm_template_spec
        if event_alarm_template_spec is not None:
            self.event_alarm_template_spec = event_alarm_template_spec

    @property
    def alarm_template_name(self):
        r"""Gets the alarm_template_name of this AlarmTemplateSpecItem.

        告警模板下单个告警规则名称。

        :return: The alarm_template_name of this AlarmTemplateSpecItem.
        :rtype: str
        """
        return self._alarm_template_name

    @alarm_template_name.setter
    def alarm_template_name(self, alarm_template_name):
        r"""Sets the alarm_template_name of this AlarmTemplateSpecItem.

        告警模板下单个告警规则名称。

        :param alarm_template_name: The alarm_template_name of this AlarmTemplateSpecItem.
        :type alarm_template_name: str
        """
        self._alarm_template_name = alarm_template_name

    @property
    def alarm_template_name_en(self):
        r"""Gets the alarm_template_name_en of this AlarmTemplateSpecItem.

        告警模板下单个告警规则英文名称。

        :return: The alarm_template_name_en of this AlarmTemplateSpecItem.
        :rtype: str
        """
        return self._alarm_template_name_en

    @alarm_template_name_en.setter
    def alarm_template_name_en(self, alarm_template_name_en):
        r"""Sets the alarm_template_name_en of this AlarmTemplateSpecItem.

        告警模板下单个告警规则英文名称。

        :param alarm_template_name_en: The alarm_template_name_en of this AlarmTemplateSpecItem.
        :type alarm_template_name_en: str
        """
        self._alarm_template_name_en = alarm_template_name_en

    @property
    def desc(self):
        r"""Gets the desc of this AlarmTemplateSpecItem.

        告警模板下单个告警规则描述。

        :return: The desc of this AlarmTemplateSpecItem.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this AlarmTemplateSpecItem.

        告警模板下单个告警规则描述。

        :param desc: The desc of this AlarmTemplateSpecItem.
        :type desc: str
        """
        self._desc = desc

    @property
    def desc_en(self):
        r"""Gets the desc_en of this AlarmTemplateSpecItem.

        告警模板下单个告警规则英文描述。

        :return: The desc_en of this AlarmTemplateSpecItem.
        :rtype: str
        """
        return self._desc_en

    @desc_en.setter
    def desc_en(self, desc_en):
        r"""Sets the desc_en of this AlarmTemplateSpecItem.

        告警模板下单个告警规则英文描述。

        :param desc_en: The desc_en of this AlarmTemplateSpecItem.
        :type desc_en: str
        """
        self._desc_en = desc_en

    @property
    def alarm_template_spec_type(self):
        r"""Gets the alarm_template_spec_type of this AlarmTemplateSpecItem.

        告警模板下单个告警规则类型。 “metric”：指标告警 “event”：事件告警

        :return: The alarm_template_spec_type of this AlarmTemplateSpecItem.
        :rtype: str
        """
        return self._alarm_template_spec_type

    @alarm_template_spec_type.setter
    def alarm_template_spec_type(self, alarm_template_spec_type):
        r"""Sets the alarm_template_spec_type of this AlarmTemplateSpecItem.

        告警模板下单个告警规则类型。 “metric”：指标告警 “event”：事件告警

        :param alarm_template_spec_type: The alarm_template_spec_type of this AlarmTemplateSpecItem.
        :type alarm_template_spec_type: str
        """
        self._alarm_template_spec_type = alarm_template_spec_type

    @property
    def metric_alarm_template_spec(self):
        r"""Gets the metric_alarm_template_spec of this AlarmTemplateSpecItem.

        :return: The metric_alarm_template_spec of this AlarmTemplateSpecItem.
        :rtype: :class:`huaweicloudsdkaom.v2.MetricAlarmTemplateSpec`
        """
        return self._metric_alarm_template_spec

    @metric_alarm_template_spec.setter
    def metric_alarm_template_spec(self, metric_alarm_template_spec):
        r"""Sets the metric_alarm_template_spec of this AlarmTemplateSpecItem.

        :param metric_alarm_template_spec: The metric_alarm_template_spec of this AlarmTemplateSpecItem.
        :type metric_alarm_template_spec: :class:`huaweicloudsdkaom.v2.MetricAlarmTemplateSpec`
        """
        self._metric_alarm_template_spec = metric_alarm_template_spec

    @property
    def event_alarm_template_spec(self):
        r"""Gets the event_alarm_template_spec of this AlarmTemplateSpecItem.

        :return: The event_alarm_template_spec of this AlarmTemplateSpecItem.
        :rtype: :class:`huaweicloudsdkaom.v2.EventAlarmTemplateSpec`
        """
        return self._event_alarm_template_spec

    @event_alarm_template_spec.setter
    def event_alarm_template_spec(self, event_alarm_template_spec):
        r"""Sets the event_alarm_template_spec of this AlarmTemplateSpecItem.

        :param event_alarm_template_spec: The event_alarm_template_spec of this AlarmTemplateSpecItem.
        :type event_alarm_template_spec: :class:`huaweicloudsdkaom.v2.EventAlarmTemplateSpec`
        """
        self._event_alarm_template_spec = event_alarm_template_spec

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
        if not isinstance(other, AlarmTemplateSpecItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
