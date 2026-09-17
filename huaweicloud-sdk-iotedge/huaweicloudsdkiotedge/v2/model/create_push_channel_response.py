# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePushChannelResponse(SdkResponse):

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
        'name': 'str',
        'channel': 'str',
        'description': 'str',
        'endpoint': 'str',
        'mqtt_channel_detail': 'MqttChannelDetailDTO',
        'iotdb_channel_detail': 'IoTDBChannelDetailDTO',
        'influxdb2_channel_detail': 'CreateInfluxDB2ChannelDetail',
        'pulsar_channel_detail': 'PulsarChannelDetailDTO',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'channel_id': 'channel_id',
        'name': 'name',
        'channel': 'channel',
        'description': 'description',
        'endpoint': 'endpoint',
        'mqtt_channel_detail': 'mqtt_channel_detail',
        'iotdb_channel_detail': 'iotdb_channel_detail',
        'influxdb2_channel_detail': 'influxdb2_channel_detail',
        'pulsar_channel_detail': 'pulsar_channel_detail',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, channel_id=None, name=None, channel=None, description=None, endpoint=None, mqtt_channel_detail=None, iotdb_channel_detail=None, influxdb2_channel_detail=None, pulsar_channel_detail=None, create_time=None, update_time=None):
        r"""CreatePushChannelResponse

        The model defined in huaweicloud sdk

        :param channel_id: 推送通道ID
        :type channel_id: str
        :param name: 推送通道名称
        :type name: str
        :param channel: 通道
        :type channel: str
        :param description: 推送通道描述
        :type description: str
        :param endpoint: 推送的地址
        :type endpoint: str
        :param mqtt_channel_detail: 
        :type mqtt_channel_detail: :class:`huaweicloudsdkiotedge.v2.MqttChannelDetailDTO`
        :param iotdb_channel_detail: 
        :type iotdb_channel_detail: :class:`huaweicloudsdkiotedge.v2.IoTDBChannelDetailDTO`
        :param influxdb2_channel_detail: 
        :type influxdb2_channel_detail: :class:`huaweicloudsdkiotedge.v2.CreateInfluxDB2ChannelDetail`
        :param pulsar_channel_detail: 
        :type pulsar_channel_detail: :class:`huaweicloudsdkiotedge.v2.PulsarChannelDetailDTO`
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        """
        
        super().__init__()

        self._channel_id = None
        self._name = None
        self._channel = None
        self._description = None
        self._endpoint = None
        self._mqtt_channel_detail = None
        self._iotdb_channel_detail = None
        self._influxdb2_channel_detail = None
        self._pulsar_channel_detail = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if channel_id is not None:
            self.channel_id = channel_id
        if name is not None:
            self.name = name
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

    @property
    def channel_id(self):
        r"""Gets the channel_id of this CreatePushChannelResponse.

        推送通道ID

        :return: The channel_id of this CreatePushChannelResponse.
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        r"""Sets the channel_id of this CreatePushChannelResponse.

        推送通道ID

        :param channel_id: The channel_id of this CreatePushChannelResponse.
        :type channel_id: str
        """
        self._channel_id = channel_id

    @property
    def name(self):
        r"""Gets the name of this CreatePushChannelResponse.

        推送通道名称

        :return: The name of this CreatePushChannelResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreatePushChannelResponse.

        推送通道名称

        :param name: The name of this CreatePushChannelResponse.
        :type name: str
        """
        self._name = name

    @property
    def channel(self):
        r"""Gets the channel of this CreatePushChannelResponse.

        通道

        :return: The channel of this CreatePushChannelResponse.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        r"""Sets the channel of this CreatePushChannelResponse.

        通道

        :param channel: The channel of this CreatePushChannelResponse.
        :type channel: str
        """
        self._channel = channel

    @property
    def description(self):
        r"""Gets the description of this CreatePushChannelResponse.

        推送通道描述

        :return: The description of this CreatePushChannelResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreatePushChannelResponse.

        推送通道描述

        :param description: The description of this CreatePushChannelResponse.
        :type description: str
        """
        self._description = description

    @property
    def endpoint(self):
        r"""Gets the endpoint of this CreatePushChannelResponse.

        推送的地址

        :return: The endpoint of this CreatePushChannelResponse.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        r"""Sets the endpoint of this CreatePushChannelResponse.

        推送的地址

        :param endpoint: The endpoint of this CreatePushChannelResponse.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def mqtt_channel_detail(self):
        r"""Gets the mqtt_channel_detail of this CreatePushChannelResponse.

        :return: The mqtt_channel_detail of this CreatePushChannelResponse.
        :rtype: :class:`huaweicloudsdkiotedge.v2.MqttChannelDetailDTO`
        """
        return self._mqtt_channel_detail

    @mqtt_channel_detail.setter
    def mqtt_channel_detail(self, mqtt_channel_detail):
        r"""Sets the mqtt_channel_detail of this CreatePushChannelResponse.

        :param mqtt_channel_detail: The mqtt_channel_detail of this CreatePushChannelResponse.
        :type mqtt_channel_detail: :class:`huaweicloudsdkiotedge.v2.MqttChannelDetailDTO`
        """
        self._mqtt_channel_detail = mqtt_channel_detail

    @property
    def iotdb_channel_detail(self):
        r"""Gets the iotdb_channel_detail of this CreatePushChannelResponse.

        :return: The iotdb_channel_detail of this CreatePushChannelResponse.
        :rtype: :class:`huaweicloudsdkiotedge.v2.IoTDBChannelDetailDTO`
        """
        return self._iotdb_channel_detail

    @iotdb_channel_detail.setter
    def iotdb_channel_detail(self, iotdb_channel_detail):
        r"""Sets the iotdb_channel_detail of this CreatePushChannelResponse.

        :param iotdb_channel_detail: The iotdb_channel_detail of this CreatePushChannelResponse.
        :type iotdb_channel_detail: :class:`huaweicloudsdkiotedge.v2.IoTDBChannelDetailDTO`
        """
        self._iotdb_channel_detail = iotdb_channel_detail

    @property
    def influxdb2_channel_detail(self):
        r"""Gets the influxdb2_channel_detail of this CreatePushChannelResponse.

        :return: The influxdb2_channel_detail of this CreatePushChannelResponse.
        :rtype: :class:`huaweicloudsdkiotedge.v2.CreateInfluxDB2ChannelDetail`
        """
        return self._influxdb2_channel_detail

    @influxdb2_channel_detail.setter
    def influxdb2_channel_detail(self, influxdb2_channel_detail):
        r"""Sets the influxdb2_channel_detail of this CreatePushChannelResponse.

        :param influxdb2_channel_detail: The influxdb2_channel_detail of this CreatePushChannelResponse.
        :type influxdb2_channel_detail: :class:`huaweicloudsdkiotedge.v2.CreateInfluxDB2ChannelDetail`
        """
        self._influxdb2_channel_detail = influxdb2_channel_detail

    @property
    def pulsar_channel_detail(self):
        r"""Gets the pulsar_channel_detail of this CreatePushChannelResponse.

        :return: The pulsar_channel_detail of this CreatePushChannelResponse.
        :rtype: :class:`huaweicloudsdkiotedge.v2.PulsarChannelDetailDTO`
        """
        return self._pulsar_channel_detail

    @pulsar_channel_detail.setter
    def pulsar_channel_detail(self, pulsar_channel_detail):
        r"""Sets the pulsar_channel_detail of this CreatePushChannelResponse.

        :param pulsar_channel_detail: The pulsar_channel_detail of this CreatePushChannelResponse.
        :type pulsar_channel_detail: :class:`huaweicloudsdkiotedge.v2.PulsarChannelDetailDTO`
        """
        self._pulsar_channel_detail = pulsar_channel_detail

    @property
    def create_time(self):
        r"""Gets the create_time of this CreatePushChannelResponse.

        创建时间

        :return: The create_time of this CreatePushChannelResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CreatePushChannelResponse.

        创建时间

        :param create_time: The create_time of this CreatePushChannelResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this CreatePushChannelResponse.

        更新时间

        :return: The update_time of this CreatePushChannelResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CreatePushChannelResponse.

        更新时间

        :param update_time: The update_time of this CreatePushChannelResponse.
        :type update_time: str
        """
        self._update_time = update_time

    def to_dict(self):
        import warnings
        warnings.warn("CreatePushChannelResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreatePushChannelResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
