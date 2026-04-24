# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmnTopicRequest:

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
        'urn': 'str',
        'notify_method': 'str',
        'protocol': 'str',
        'other_persons': 'str',
        'max_send_times': 'int',
        'send_interval': 'int',
        'duty_schedule_name': 'str',
        'smn_config_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'urn': 'urn',
        'notify_method': 'notify_method',
        'protocol': 'protocol',
        'other_persons': 'other_persons',
        'max_send_times': 'max_send_times',
        'send_interval': 'send_interval',
        'duty_schedule_name': 'duty_schedule_name',
        'smn_config_name': 'smn_config_name'
    }

    def __init__(self, name=None, urn=None, notify_method=None, protocol=None, other_persons=None, max_send_times=None, send_interval=None, duty_schedule_name=None, smn_config_name=None):
        r"""SmnTopicRequest

        The model defined in huaweicloud sdk

        :param name: 主题名称。
        :type name: str
        :param urn: smn urn，可以在SMN服务查看对应主题的urn。
        :type urn: str
        :param notify_method: 告警方式：主题、责任人、值班表和钉钉机器人，取值如下： - SUBJECT: 主题 - OWNER： 责任人 - DUTY_SCHEDULE: 值班表 - DINGDING: 钉钉机器人
        :type notify_method: str
        :param protocol: 告警协议：短信、邮件、电话，示例：[\&quot;email\&quot;] \&quot;email\&quot;：邮件传输协议,\&quot;sms\&quot;：短信传输协议,\&quot;callnotify\&quot;:语音, \&quot;dingding\&quot;:个人钉钉。
        :type protocol: str
        :param other_persons: 抄送人，示例：[\&quot;lin\&quot;,\&quot;hua\&quot;]。
        :type other_persons: str
        :param max_send_times: 最大告警次数，取值为 [1, 50]。
        :type max_send_times: int
        :param send_interval: 告警间隔，取值为[5, 60]，单位：分钟。
        :type send_interval: int
        :param duty_schedule_name: 值班表名称。
        :type duty_schedule_name: str
        :param smn_config_name: 机器人名称。
        :type smn_config_name: str
        """
        
        

        self._name = None
        self._urn = None
        self._notify_method = None
        self._protocol = None
        self._other_persons = None
        self._max_send_times = None
        self._send_interval = None
        self._duty_schedule_name = None
        self._smn_config_name = None
        self.discriminator = None

        self.name = name
        self.urn = urn
        self.notify_method = notify_method
        if protocol is not None:
            self.protocol = protocol
        if other_persons is not None:
            self.other_persons = other_persons
        self.max_send_times = max_send_times
        self.send_interval = send_interval
        if duty_schedule_name is not None:
            self.duty_schedule_name = duty_schedule_name
        if smn_config_name is not None:
            self.smn_config_name = smn_config_name

    @property
    def name(self):
        r"""Gets the name of this SmnTopicRequest.

        主题名称。

        :return: The name of this SmnTopicRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SmnTopicRequest.

        主题名称。

        :param name: The name of this SmnTopicRequest.
        :type name: str
        """
        self._name = name

    @property
    def urn(self):
        r"""Gets the urn of this SmnTopicRequest.

        smn urn，可以在SMN服务查看对应主题的urn。

        :return: The urn of this SmnTopicRequest.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        r"""Sets the urn of this SmnTopicRequest.

        smn urn，可以在SMN服务查看对应主题的urn。

        :param urn: The urn of this SmnTopicRequest.
        :type urn: str
        """
        self._urn = urn

    @property
    def notify_method(self):
        r"""Gets the notify_method of this SmnTopicRequest.

        告警方式：主题、责任人、值班表和钉钉机器人，取值如下： - SUBJECT: 主题 - OWNER： 责任人 - DUTY_SCHEDULE: 值班表 - DINGDING: 钉钉机器人

        :return: The notify_method of this SmnTopicRequest.
        :rtype: str
        """
        return self._notify_method

    @notify_method.setter
    def notify_method(self, notify_method):
        r"""Sets the notify_method of this SmnTopicRequest.

        告警方式：主题、责任人、值班表和钉钉机器人，取值如下： - SUBJECT: 主题 - OWNER： 责任人 - DUTY_SCHEDULE: 值班表 - DINGDING: 钉钉机器人

        :param notify_method: The notify_method of this SmnTopicRequest.
        :type notify_method: str
        """
        self._notify_method = notify_method

    @property
    def protocol(self):
        r"""Gets the protocol of this SmnTopicRequest.

        告警协议：短信、邮件、电话，示例：[\"email\"] \"email\"：邮件传输协议,\"sms\"：短信传输协议,\"callnotify\":语音, \"dingding\":个人钉钉。

        :return: The protocol of this SmnTopicRequest.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this SmnTopicRequest.

        告警协议：短信、邮件、电话，示例：[\"email\"] \"email\"：邮件传输协议,\"sms\"：短信传输协议,\"callnotify\":语音, \"dingding\":个人钉钉。

        :param protocol: The protocol of this SmnTopicRequest.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def other_persons(self):
        r"""Gets the other_persons of this SmnTopicRequest.

        抄送人，示例：[\"lin\",\"hua\"]。

        :return: The other_persons of this SmnTopicRequest.
        :rtype: str
        """
        return self._other_persons

    @other_persons.setter
    def other_persons(self, other_persons):
        r"""Sets the other_persons of this SmnTopicRequest.

        抄送人，示例：[\"lin\",\"hua\"]。

        :param other_persons: The other_persons of this SmnTopicRequest.
        :type other_persons: str
        """
        self._other_persons = other_persons

    @property
    def max_send_times(self):
        r"""Gets the max_send_times of this SmnTopicRequest.

        最大告警次数，取值为 [1, 50]。

        :return: The max_send_times of this SmnTopicRequest.
        :rtype: int
        """
        return self._max_send_times

    @max_send_times.setter
    def max_send_times(self, max_send_times):
        r"""Sets the max_send_times of this SmnTopicRequest.

        最大告警次数，取值为 [1, 50]。

        :param max_send_times: The max_send_times of this SmnTopicRequest.
        :type max_send_times: int
        """
        self._max_send_times = max_send_times

    @property
    def send_interval(self):
        r"""Gets the send_interval of this SmnTopicRequest.

        告警间隔，取值为[5, 60]，单位：分钟。

        :return: The send_interval of this SmnTopicRequest.
        :rtype: int
        """
        return self._send_interval

    @send_interval.setter
    def send_interval(self, send_interval):
        r"""Sets the send_interval of this SmnTopicRequest.

        告警间隔，取值为[5, 60]，单位：分钟。

        :param send_interval: The send_interval of this SmnTopicRequest.
        :type send_interval: int
        """
        self._send_interval = send_interval

    @property
    def duty_schedule_name(self):
        r"""Gets the duty_schedule_name of this SmnTopicRequest.

        值班表名称。

        :return: The duty_schedule_name of this SmnTopicRequest.
        :rtype: str
        """
        return self._duty_schedule_name

    @duty_schedule_name.setter
    def duty_schedule_name(self, duty_schedule_name):
        r"""Sets the duty_schedule_name of this SmnTopicRequest.

        值班表名称。

        :param duty_schedule_name: The duty_schedule_name of this SmnTopicRequest.
        :type duty_schedule_name: str
        """
        self._duty_schedule_name = duty_schedule_name

    @property
    def smn_config_name(self):
        r"""Gets the smn_config_name of this SmnTopicRequest.

        机器人名称。

        :return: The smn_config_name of this SmnTopicRequest.
        :rtype: str
        """
        return self._smn_config_name

    @smn_config_name.setter
    def smn_config_name(self, smn_config_name):
        r"""Sets the smn_config_name of this SmnTopicRequest.

        机器人名称。

        :param smn_config_name: The smn_config_name of this SmnTopicRequest.
        :type smn_config_name: str
        """
        self._smn_config_name = smn_config_name

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
        if not isinstance(other, SmnTopicRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
