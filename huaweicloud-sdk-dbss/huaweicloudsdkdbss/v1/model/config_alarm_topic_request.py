# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigAlarmTopicRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_cpu': 'int',
        'alarm_disk': 'int',
        'alarm_memory': 'int',
        'alarm_num': 'int',
        'alarm_risk': 'list[str]',
        'alarm_switch': 'str',
        'alarm_topic_urn': 'str'
    }

    attribute_map = {
        'alarm_cpu': 'alarm_cpu',
        'alarm_disk': 'alarm_disk',
        'alarm_memory': 'alarm_memory',
        'alarm_num': 'alarm_num',
        'alarm_risk': 'alarm_risk',
        'alarm_switch': 'alarm_switch',
        'alarm_topic_urn': 'alarm_topic_urn'
    }

    def __init__(self, alarm_cpu=None, alarm_disk=None, alarm_memory=None, alarm_num=None, alarm_risk=None, alarm_switch=None, alarm_topic_urn=None):
        r"""ConfigAlarmTopicRequest

        The model defined in huaweicloud sdk

        :param alarm_cpu: CPU告警阈值(%)
        :type alarm_cpu: int
        :param alarm_disk: 磁盘告警阈值(%)
        :type alarm_disk: int
        :param alarm_memory: 内存告警阈值(%)
        :type alarm_memory: int
        :param alarm_num: 每天发送告警总条数
        :type alarm_num: int
        :param alarm_risk: 告警等级,默认为空。 - high：高  - medium：中  - low：低
        :type alarm_risk: list[str]
        :param alarm_switch: 通知开关 - ON：开启  - OFF：关闭
        :type alarm_switch: str
        :param alarm_topic_urn: 通知消息主题URN,调用SMN服务接口获取。当alarm_switch为ON时必填
        :type alarm_topic_urn: str
        """
        
        

        self._alarm_cpu = None
        self._alarm_disk = None
        self._alarm_memory = None
        self._alarm_num = None
        self._alarm_risk = None
        self._alarm_switch = None
        self._alarm_topic_urn = None
        self.discriminator = None

        self.alarm_cpu = alarm_cpu
        self.alarm_disk = alarm_disk
        self.alarm_memory = alarm_memory
        self.alarm_num = alarm_num
        if alarm_risk is not None:
            self.alarm_risk = alarm_risk
        self.alarm_switch = alarm_switch
        if alarm_topic_urn is not None:
            self.alarm_topic_urn = alarm_topic_urn

    @property
    def alarm_cpu(self):
        r"""Gets the alarm_cpu of this ConfigAlarmTopicRequest.

        CPU告警阈值(%)

        :return: The alarm_cpu of this ConfigAlarmTopicRequest.
        :rtype: int
        """
        return self._alarm_cpu

    @alarm_cpu.setter
    def alarm_cpu(self, alarm_cpu):
        r"""Sets the alarm_cpu of this ConfigAlarmTopicRequest.

        CPU告警阈值(%)

        :param alarm_cpu: The alarm_cpu of this ConfigAlarmTopicRequest.
        :type alarm_cpu: int
        """
        self._alarm_cpu = alarm_cpu

    @property
    def alarm_disk(self):
        r"""Gets the alarm_disk of this ConfigAlarmTopicRequest.

        磁盘告警阈值(%)

        :return: The alarm_disk of this ConfigAlarmTopicRequest.
        :rtype: int
        """
        return self._alarm_disk

    @alarm_disk.setter
    def alarm_disk(self, alarm_disk):
        r"""Sets the alarm_disk of this ConfigAlarmTopicRequest.

        磁盘告警阈值(%)

        :param alarm_disk: The alarm_disk of this ConfigAlarmTopicRequest.
        :type alarm_disk: int
        """
        self._alarm_disk = alarm_disk

    @property
    def alarm_memory(self):
        r"""Gets the alarm_memory of this ConfigAlarmTopicRequest.

        内存告警阈值(%)

        :return: The alarm_memory of this ConfigAlarmTopicRequest.
        :rtype: int
        """
        return self._alarm_memory

    @alarm_memory.setter
    def alarm_memory(self, alarm_memory):
        r"""Sets the alarm_memory of this ConfigAlarmTopicRequest.

        内存告警阈值(%)

        :param alarm_memory: The alarm_memory of this ConfigAlarmTopicRequest.
        :type alarm_memory: int
        """
        self._alarm_memory = alarm_memory

    @property
    def alarm_num(self):
        r"""Gets the alarm_num of this ConfigAlarmTopicRequest.

        每天发送告警总条数

        :return: The alarm_num of this ConfigAlarmTopicRequest.
        :rtype: int
        """
        return self._alarm_num

    @alarm_num.setter
    def alarm_num(self, alarm_num):
        r"""Sets the alarm_num of this ConfigAlarmTopicRequest.

        每天发送告警总条数

        :param alarm_num: The alarm_num of this ConfigAlarmTopicRequest.
        :type alarm_num: int
        """
        self._alarm_num = alarm_num

    @property
    def alarm_risk(self):
        r"""Gets the alarm_risk of this ConfigAlarmTopicRequest.

        告警等级,默认为空。 - high：高  - medium：中  - low：低

        :return: The alarm_risk of this ConfigAlarmTopicRequest.
        :rtype: list[str]
        """
        return self._alarm_risk

    @alarm_risk.setter
    def alarm_risk(self, alarm_risk):
        r"""Sets the alarm_risk of this ConfigAlarmTopicRequest.

        告警等级,默认为空。 - high：高  - medium：中  - low：低

        :param alarm_risk: The alarm_risk of this ConfigAlarmTopicRequest.
        :type alarm_risk: list[str]
        """
        self._alarm_risk = alarm_risk

    @property
    def alarm_switch(self):
        r"""Gets the alarm_switch of this ConfigAlarmTopicRequest.

        通知开关 - ON：开启  - OFF：关闭

        :return: The alarm_switch of this ConfigAlarmTopicRequest.
        :rtype: str
        """
        return self._alarm_switch

    @alarm_switch.setter
    def alarm_switch(self, alarm_switch):
        r"""Sets the alarm_switch of this ConfigAlarmTopicRequest.

        通知开关 - ON：开启  - OFF：关闭

        :param alarm_switch: The alarm_switch of this ConfigAlarmTopicRequest.
        :type alarm_switch: str
        """
        self._alarm_switch = alarm_switch

    @property
    def alarm_topic_urn(self):
        r"""Gets the alarm_topic_urn of this ConfigAlarmTopicRequest.

        通知消息主题URN,调用SMN服务接口获取。当alarm_switch为ON时必填

        :return: The alarm_topic_urn of this ConfigAlarmTopicRequest.
        :rtype: str
        """
        return self._alarm_topic_urn

    @alarm_topic_urn.setter
    def alarm_topic_urn(self, alarm_topic_urn):
        r"""Sets the alarm_topic_urn of this ConfigAlarmTopicRequest.

        通知消息主题URN,调用SMN服务接口获取。当alarm_switch为ON时必填

        :param alarm_topic_urn: The alarm_topic_urn of this ConfigAlarmTopicRequest.
        :type alarm_topic_urn: str
        """
        self._alarm_topic_urn = alarm_topic_urn

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
        if not isinstance(other, ConfigAlarmTopicRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
