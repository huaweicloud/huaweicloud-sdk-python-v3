# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateClientNodeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'channel': 'str',
        'description': 'str',
        'endpoint': 'str',
        'mqtt_channel_detail': 'MqttNodeChannelDetailDTO',
        'iotdb_channel_detail': 'IoTDBNodeChannelDetailDTO',
        'influxdb2_channel_detail': 'InfluxDB2NodeChannelDetailDTO',
        'pulsar_channel_detail': 'PulsarNodeChannelDetailDTO',
        'create_time': 'str',
        'update_time': 'str',
        'synchronized_time': 'str',
        'synchronized_status': 'bool'
    }

    attribute_map = {
        'channel': 'channel',
        'description': 'description',
        'endpoint': 'endpoint',
        'mqtt_channel_detail': 'mqtt_channel_detail',
        'iotdb_channel_detail': 'iotdb_channel_detail',
        'influxdb2_channel_detail': 'influxdb2_channel_detail',
        'pulsar_channel_detail': 'pulsar_channel_detail',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'synchronized_time': 'synchronized_time',
        'synchronized_status': 'synchronized_status'
    }

    def __init__(self, channel=None, description=None, endpoint=None, mqtt_channel_detail=None, iotdb_channel_detail=None, influxdb2_channel_detail=None, pulsar_channel_detail=None, create_time=None, update_time=None, synchronized_time=None, synchronized_status=None):
        r"""UpdateClientNodeResponse

        The model defined in huaweicloud sdk

        :param channel: 通道
        :type channel: str
        :param description: 推送通道描述
        :type description: str
        :param endpoint: 推送的地址
        :type endpoint: str
        :param mqtt_channel_detail: 
        :type mqtt_channel_detail: :class:`huaweicloudsdkiotedge.v2.MqttNodeChannelDetailDTO`
        :param iotdb_channel_detail: 
        :type iotdb_channel_detail: :class:`huaweicloudsdkiotedge.v2.IoTDBNodeChannelDetailDTO`
        :param influxdb2_channel_detail: 
        :type influxdb2_channel_detail: :class:`huaweicloudsdkiotedge.v2.InfluxDB2NodeChannelDetailDTO`
        :param pulsar_channel_detail: 
        :type pulsar_channel_detail: :class:`huaweicloudsdkiotedge.v2.PulsarNodeChannelDetailDTO`
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        :param synchronized_time: 下发时间，表示通道是否已经同步到了节点
        :type synchronized_time: str
        :param synchronized_status: 下发状态，表示是否已同步到了节点
        :type synchronized_status: bool
        """
        
        super().__init__()

        self._channel = None
        self._description = None
        self._endpoint = None
        self._mqtt_channel_detail = None
        self._iotdb_channel_detail = None
        self._influxdb2_channel_detail = None
        self._pulsar_channel_detail = None
        self._create_time = None
        self._update_time = None
        self._synchronized_time = None
        self._synchronized_status = None
        self.discriminator = None

        if channel is not None:
            self.channel = channel
        if description is not None:
            self.description = description
        if endpoint is not None:
            self.endpoint = endpoint
        if mqtt_channel_detail is not None:
            self.mqtt_channel_detail = mqtt_channel_detail
        if iotdb_channel_detail is not None:
            self.iotdb_channel_detail = iotdb_channel_detail
        if influxdb2_channel_detail is not None:
            self.influxdb2_channel_detail = influxdb2_channel_detail
        if pulsar_channel_detail is not None:
            self.pulsar_channel_detail = pulsar_channel_detail
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if synchronized_time is not None:
            self.synchronized_time = synchronized_time
        if synchronized_status is not None:
            self.synchronized_status = synchronized_status

    @property
    def channel(self):
        r"""Gets the channel of this UpdateClientNodeResponse.

        通道

        :return: The channel of this UpdateClientNodeResponse.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        r"""Sets the channel of this UpdateClientNodeResponse.

        通道

        :param channel: The channel of this UpdateClientNodeResponse.
        :type channel: str
        """
        self._channel = channel

    @property
    def description(self):
        r"""Gets the description of this UpdateClientNodeResponse.

        推送通道描述

        :return: The description of this UpdateClientNodeResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateClientNodeResponse.

        推送通道描述

        :param description: The description of this UpdateClientNodeResponse.
        :type description: str
        """
        self._description = description

    @property
    def endpoint(self):
        r"""Gets the endpoint of this UpdateClientNodeResponse.

        推送的地址

        :return: The endpoint of this UpdateClientNodeResponse.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        r"""Sets the endpoint of this UpdateClientNodeResponse.

        推送的地址

        :param endpoint: The endpoint of this UpdateClientNodeResponse.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def mqtt_channel_detail(self):
        r"""Gets the mqtt_channel_detail of this UpdateClientNodeResponse.

        :return: The mqtt_channel_detail of this UpdateClientNodeResponse.
        :rtype: :class:`huaweicloudsdkiotedge.v2.MqttNodeChannelDetailDTO`
        """
        return self._mqtt_channel_detail

    @mqtt_channel_detail.setter
    def mqtt_channel_detail(self, mqtt_channel_detail):
        r"""Sets the mqtt_channel_detail of this UpdateClientNodeResponse.

        :param mqtt_channel_detail: The mqtt_channel_detail of this UpdateClientNodeResponse.
        :type mqtt_channel_detail: :class:`huaweicloudsdkiotedge.v2.MqttNodeChannelDetailDTO`
        """
        self._mqtt_channel_detail = mqtt_channel_detail

    @property
    def iotdb_channel_detail(self):
        r"""Gets the iotdb_channel_detail of this UpdateClientNodeResponse.

        :return: The iotdb_channel_detail of this UpdateClientNodeResponse.
        :rtype: :class:`huaweicloudsdkiotedge.v2.IoTDBNodeChannelDetailDTO`
        """
        return self._iotdb_channel_detail

    @iotdb_channel_detail.setter
    def iotdb_channel_detail(self, iotdb_channel_detail):
        r"""Sets the iotdb_channel_detail of this UpdateClientNodeResponse.

        :param iotdb_channel_detail: The iotdb_channel_detail of this UpdateClientNodeResponse.
        :type iotdb_channel_detail: :class:`huaweicloudsdkiotedge.v2.IoTDBNodeChannelDetailDTO`
        """
        self._iotdb_channel_detail = iotdb_channel_detail

    @property
    def influxdb2_channel_detail(self):
        r"""Gets the influxdb2_channel_detail of this UpdateClientNodeResponse.

        :return: The influxdb2_channel_detail of this UpdateClientNodeResponse.
        :rtype: :class:`huaweicloudsdkiotedge.v2.InfluxDB2NodeChannelDetailDTO`
        """
        return self._influxdb2_channel_detail

    @influxdb2_channel_detail.setter
    def influxdb2_channel_detail(self, influxdb2_channel_detail):
        r"""Sets the influxdb2_channel_detail of this UpdateClientNodeResponse.

        :param influxdb2_channel_detail: The influxdb2_channel_detail of this UpdateClientNodeResponse.
        :type influxdb2_channel_detail: :class:`huaweicloudsdkiotedge.v2.InfluxDB2NodeChannelDetailDTO`
        """
        self._influxdb2_channel_detail = influxdb2_channel_detail

    @property
    def pulsar_channel_detail(self):
        r"""Gets the pulsar_channel_detail of this UpdateClientNodeResponse.

        :return: The pulsar_channel_detail of this UpdateClientNodeResponse.
        :rtype: :class:`huaweicloudsdkiotedge.v2.PulsarNodeChannelDetailDTO`
        """
        return self._pulsar_channel_detail

    @pulsar_channel_detail.setter
    def pulsar_channel_detail(self, pulsar_channel_detail):
        r"""Sets the pulsar_channel_detail of this UpdateClientNodeResponse.

        :param pulsar_channel_detail: The pulsar_channel_detail of this UpdateClientNodeResponse.
        :type pulsar_channel_detail: :class:`huaweicloudsdkiotedge.v2.PulsarNodeChannelDetailDTO`
        """
        self._pulsar_channel_detail = pulsar_channel_detail

    @property
    def create_time(self):
        r"""Gets the create_time of this UpdateClientNodeResponse.

        创建时间

        :return: The create_time of this UpdateClientNodeResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this UpdateClientNodeResponse.

        创建时间

        :param create_time: The create_time of this UpdateClientNodeResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this UpdateClientNodeResponse.

        更新时间

        :return: The update_time of this UpdateClientNodeResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this UpdateClientNodeResponse.

        更新时间

        :param update_time: The update_time of this UpdateClientNodeResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def synchronized_time(self):
        r"""Gets the synchronized_time of this UpdateClientNodeResponse.

        下发时间，表示通道是否已经同步到了节点

        :return: The synchronized_time of this UpdateClientNodeResponse.
        :rtype: str
        """
        return self._synchronized_time

    @synchronized_time.setter
    def synchronized_time(self, synchronized_time):
        r"""Sets the synchronized_time of this UpdateClientNodeResponse.

        下发时间，表示通道是否已经同步到了节点

        :param synchronized_time: The synchronized_time of this UpdateClientNodeResponse.
        :type synchronized_time: str
        """
        self._synchronized_time = synchronized_time

    @property
    def synchronized_status(self):
        r"""Gets the synchronized_status of this UpdateClientNodeResponse.

        下发状态，表示是否已同步到了节点

        :return: The synchronized_status of this UpdateClientNodeResponse.
        :rtype: bool
        """
        return self._synchronized_status

    @synchronized_status.setter
    def synchronized_status(self, synchronized_status):
        r"""Sets the synchronized_status of this UpdateClientNodeResponse.

        下发状态，表示是否已同步到了节点

        :param synchronized_status: The synchronized_status of this UpdateClientNodeResponse.
        :type synchronized_status: bool
        """
        self._synchronized_status = synchronized_status

    def to_dict(self):
        import warnings
        warnings.warn("UpdateClientNodeResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, UpdateClientNodeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
