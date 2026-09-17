# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateNodeChannelRequestDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mqtt_channel_detail': 'UpdateMqttNodeChannelDetail',
        'pulsar_channel_detail': 'UpdatePulsarNodeChannelDetail'
    }

    attribute_map = {
        'mqtt_channel_detail': 'mqtt_channel_detail',
        'pulsar_channel_detail': 'pulsar_channel_detail'
    }

    def __init__(self, mqtt_channel_detail=None, pulsar_channel_detail=None):
        r"""UpdateNodeChannelRequestDTO

        The model defined in huaweicloud sdk

        :param mqtt_channel_detail: 
        :type mqtt_channel_detail: :class:`huaweicloudsdkiotedge.v2.UpdateMqttNodeChannelDetail`
        :param pulsar_channel_detail: 
        :type pulsar_channel_detail: :class:`huaweicloudsdkiotedge.v2.UpdatePulsarNodeChannelDetail`
        """
        
        

        self._mqtt_channel_detail = None
        self._pulsar_channel_detail = None
        self.discriminator = None

        if mqtt_channel_detail is not None:
            self.mqtt_channel_detail = mqtt_channel_detail
        if pulsar_channel_detail is not None:
            self.pulsar_channel_detail = pulsar_channel_detail

    @property
    def mqtt_channel_detail(self):
        r"""Gets the mqtt_channel_detail of this UpdateNodeChannelRequestDTO.

        :return: The mqtt_channel_detail of this UpdateNodeChannelRequestDTO.
        :rtype: :class:`huaweicloudsdkiotedge.v2.UpdateMqttNodeChannelDetail`
        """
        return self._mqtt_channel_detail

    @mqtt_channel_detail.setter
    def mqtt_channel_detail(self, mqtt_channel_detail):
        r"""Sets the mqtt_channel_detail of this UpdateNodeChannelRequestDTO.

        :param mqtt_channel_detail: The mqtt_channel_detail of this UpdateNodeChannelRequestDTO.
        :type mqtt_channel_detail: :class:`huaweicloudsdkiotedge.v2.UpdateMqttNodeChannelDetail`
        """
        self._mqtt_channel_detail = mqtt_channel_detail

    @property
    def pulsar_channel_detail(self):
        r"""Gets the pulsar_channel_detail of this UpdateNodeChannelRequestDTO.

        :return: The pulsar_channel_detail of this UpdateNodeChannelRequestDTO.
        :rtype: :class:`huaweicloudsdkiotedge.v2.UpdatePulsarNodeChannelDetail`
        """
        return self._pulsar_channel_detail

    @pulsar_channel_detail.setter
    def pulsar_channel_detail(self, pulsar_channel_detail):
        r"""Sets the pulsar_channel_detail of this UpdateNodeChannelRequestDTO.

        :param pulsar_channel_detail: The pulsar_channel_detail of this UpdateNodeChannelRequestDTO.
        :type pulsar_channel_detail: :class:`huaweicloudsdkiotedge.v2.UpdatePulsarNodeChannelDetail`
        """
        self._pulsar_channel_detail = pulsar_channel_detail

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
        if not isinstance(other, UpdateNodeChannelRequestDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
