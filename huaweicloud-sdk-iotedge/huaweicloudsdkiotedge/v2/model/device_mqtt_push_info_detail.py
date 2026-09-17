# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeviceMqttPushInfoDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topic': 'str',
        'format': 'str',
        'qos': 'int'
    }

    attribute_map = {
        'topic': 'topic',
        'format': 'format',
        'qos': 'qos'
    }

    def __init__(self, topic=None, format=None, qos=None):
        r"""DeviceMqttPushInfoDetail

        The model defined in huaweicloud sdk

        :param topic: client推送的topic
        :type topic: str
        :param format: 数据格式转换类型
        :type format: str
        :param qos: MQTT的服务质量
        :type qos: int
        """
        
        

        self._topic = None
        self._format = None
        self._qos = None
        self.discriminator = None

        if topic is not None:
            self.topic = topic
        if format is not None:
            self.format = format
        if qos is not None:
            self.qos = qos

    @property
    def topic(self):
        r"""Gets the topic of this DeviceMqttPushInfoDetail.

        client推送的topic

        :return: The topic of this DeviceMqttPushInfoDetail.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this DeviceMqttPushInfoDetail.

        client推送的topic

        :param topic: The topic of this DeviceMqttPushInfoDetail.
        :type topic: str
        """
        self._topic = topic

    @property
    def format(self):
        r"""Gets the format of this DeviceMqttPushInfoDetail.

        数据格式转换类型

        :return: The format of this DeviceMqttPushInfoDetail.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this DeviceMqttPushInfoDetail.

        数据格式转换类型

        :param format: The format of this DeviceMqttPushInfoDetail.
        :type format: str
        """
        self._format = format

    @property
    def qos(self):
        r"""Gets the qos of this DeviceMqttPushInfoDetail.

        MQTT的服务质量

        :return: The qos of this DeviceMqttPushInfoDetail.
        :rtype: int
        """
        return self._qos

    @qos.setter
    def qos(self, qos):
        r"""Sets the qos of this DeviceMqttPushInfoDetail.

        MQTT的服务质量

        :param qos: The qos of this DeviceMqttPushInfoDetail.
        :type qos: int
        """
        self._qos = qos

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
        if not isinstance(other, DeviceMqttPushInfoDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
