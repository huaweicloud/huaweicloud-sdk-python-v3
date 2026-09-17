# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateChannelRequestDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'channel_id': 'str',
        'channel': 'str',
        'name': 'str',
        'description': 'str',
        'endpoint': 'str',
        'mqtt_channel_detail': 'CreateMqttChannelDetail',
        'iotdb_channel_detail': 'CreateIoTDBChannelDetail',
        'influxdb2_channel_detail': 'CreateInfluxDB2ChannelDetail',
        'pulsar_channel_detail': 'CreatePulsarChannelDetail'
    }

    attribute_map = {
        'channel_id': 'channel_id',
        'channel': 'channel',
        'name': 'name',
        'description': 'description',
        'endpoint': 'endpoint',
        'mqtt_channel_detail': 'mqtt_channel_detail',
        'iotdb_channel_detail': 'iotdb_channel_detail',
        'influxdb2_channel_detail': 'influxdb2_channel_detail',
        'pulsar_channel_detail': 'pulsar_channel_detail'
    }

    def __init__(self, channel_id=None, channel=None, name=None, description=None, endpoint=None, mqtt_channel_detail=None, iotdb_channel_detail=None, influxdb2_channel_detail=None, pulsar_channel_detail=None):
        r"""CreateChannelRequestDTO

        The model defined in huaweicloud sdk

        :param channel_id: 推送通道ID,非必填，若用户不填，则系统自动生成
        :type channel_id: str
        :param channel: 通道
        :type channel: str
        :param name: 推送通道名称
        :type name: str
        :param description: 推送通道描述
        :type description: str
        :param endpoint: 推送的地址
        :type endpoint: str
        :param mqtt_channel_detail: 
        :type mqtt_channel_detail: :class:`huaweicloudsdkiotedge.v2.CreateMqttChannelDetail`
        :param iotdb_channel_detail: 
        :type iotdb_channel_detail: :class:`huaweicloudsdkiotedge.v2.CreateIoTDBChannelDetail`
        :param influxdb2_channel_detail: 
        :type influxdb2_channel_detail: :class:`huaweicloudsdkiotedge.v2.CreateInfluxDB2ChannelDetail`
        :param pulsar_channel_detail: 
        :type pulsar_channel_detail: :class:`huaweicloudsdkiotedge.v2.CreatePulsarChannelDetail`
        """
        
        

        self._channel_id = None
        self._channel = None
        self._name = None
        self._description = None
        self._endpoint = None
        self._mqtt_channel_detail = None
        self._iotdb_channel_detail = None
        self._influxdb2_channel_detail = None
        self._pulsar_channel_detail = None
        self.discriminator = None

        if channel_id is not None:
            self.channel_id = channel_id
        self.channel = channel
        self.name = name
        if description is not None:
            self.description = description
        self.endpoint = endpoint
        if mqtt_channel_detail is not None:
            self.mqtt_channel_detail = mqtt_channel_detail
        if iotdb_channel_detail is not None:
            self.iotdb_channel_detail = iotdb_channel_detail
        if influxdb2_channel_detail is not None:
            self.influxdb2_channel_detail = influxdb2_channel_detail
        if pulsar_channel_detail is not None:
            self.pulsar_channel_detail = pulsar_channel_detail

    @property
    def channel_id(self):
        r"""Gets the channel_id of this CreateChannelRequestDTO.

        推送通道ID,非必填，若用户不填，则系统自动生成

        :return: The channel_id of this CreateChannelRequestDTO.
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        r"""Sets the channel_id of this CreateChannelRequestDTO.

        推送通道ID,非必填，若用户不填，则系统自动生成

        :param channel_id: The channel_id of this CreateChannelRequestDTO.
        :type channel_id: str
        """
        self._channel_id = channel_id

    @property
    def channel(self):
        r"""Gets the channel of this CreateChannelRequestDTO.

        通道

        :return: The channel of this CreateChannelRequestDTO.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        r"""Sets the channel of this CreateChannelRequestDTO.

        通道

        :param channel: The channel of this CreateChannelRequestDTO.
        :type channel: str
        """
        self._channel = channel

    @property
    def name(self):
        r"""Gets the name of this CreateChannelRequestDTO.

        推送通道名称

        :return: The name of this CreateChannelRequestDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateChannelRequestDTO.

        推送通道名称

        :param name: The name of this CreateChannelRequestDTO.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateChannelRequestDTO.

        推送通道描述

        :return: The description of this CreateChannelRequestDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateChannelRequestDTO.

        推送通道描述

        :param description: The description of this CreateChannelRequestDTO.
        :type description: str
        """
        self._description = description

    @property
    def endpoint(self):
        r"""Gets the endpoint of this CreateChannelRequestDTO.

        推送的地址

        :return: The endpoint of this CreateChannelRequestDTO.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        r"""Sets the endpoint of this CreateChannelRequestDTO.

        推送的地址

        :param endpoint: The endpoint of this CreateChannelRequestDTO.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def mqtt_channel_detail(self):
        r"""Gets the mqtt_channel_detail of this CreateChannelRequestDTO.

        :return: The mqtt_channel_detail of this CreateChannelRequestDTO.
        :rtype: :class:`huaweicloudsdkiotedge.v2.CreateMqttChannelDetail`
        """
        return self._mqtt_channel_detail

    @mqtt_channel_detail.setter
    def mqtt_channel_detail(self, mqtt_channel_detail):
        r"""Sets the mqtt_channel_detail of this CreateChannelRequestDTO.

        :param mqtt_channel_detail: The mqtt_channel_detail of this CreateChannelRequestDTO.
        :type mqtt_channel_detail: :class:`huaweicloudsdkiotedge.v2.CreateMqttChannelDetail`
        """
        self._mqtt_channel_detail = mqtt_channel_detail

    @property
    def iotdb_channel_detail(self):
        r"""Gets the iotdb_channel_detail of this CreateChannelRequestDTO.

        :return: The iotdb_channel_detail of this CreateChannelRequestDTO.
        :rtype: :class:`huaweicloudsdkiotedge.v2.CreateIoTDBChannelDetail`
        """
        return self._iotdb_channel_detail

    @iotdb_channel_detail.setter
    def iotdb_channel_detail(self, iotdb_channel_detail):
        r"""Sets the iotdb_channel_detail of this CreateChannelRequestDTO.

        :param iotdb_channel_detail: The iotdb_channel_detail of this CreateChannelRequestDTO.
        :type iotdb_channel_detail: :class:`huaweicloudsdkiotedge.v2.CreateIoTDBChannelDetail`
        """
        self._iotdb_channel_detail = iotdb_channel_detail

    @property
    def influxdb2_channel_detail(self):
        r"""Gets the influxdb2_channel_detail of this CreateChannelRequestDTO.

        :return: The influxdb2_channel_detail of this CreateChannelRequestDTO.
        :rtype: :class:`huaweicloudsdkiotedge.v2.CreateInfluxDB2ChannelDetail`
        """
        return self._influxdb2_channel_detail

    @influxdb2_channel_detail.setter
    def influxdb2_channel_detail(self, influxdb2_channel_detail):
        r"""Sets the influxdb2_channel_detail of this CreateChannelRequestDTO.

        :param influxdb2_channel_detail: The influxdb2_channel_detail of this CreateChannelRequestDTO.
        :type influxdb2_channel_detail: :class:`huaweicloudsdkiotedge.v2.CreateInfluxDB2ChannelDetail`
        """
        self._influxdb2_channel_detail = influxdb2_channel_detail

    @property
    def pulsar_channel_detail(self):
        r"""Gets the pulsar_channel_detail of this CreateChannelRequestDTO.

        :return: The pulsar_channel_detail of this CreateChannelRequestDTO.
        :rtype: :class:`huaweicloudsdkiotedge.v2.CreatePulsarChannelDetail`
        """
        return self._pulsar_channel_detail

    @pulsar_channel_detail.setter
    def pulsar_channel_detail(self, pulsar_channel_detail):
        r"""Sets the pulsar_channel_detail of this CreateChannelRequestDTO.

        :param pulsar_channel_detail: The pulsar_channel_detail of this CreateChannelRequestDTO.
        :type pulsar_channel_detail: :class:`huaweicloudsdkiotedge.v2.CreatePulsarChannelDetail`
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
        if not isinstance(other, CreateChannelRequestDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
