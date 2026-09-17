# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClientNodeResponse(SdkResponse):

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
        'node_id': 'str',
        'allotted_time': 'str',
        'update_time': 'str',
        'synchronized_time': 'str',
        'synchronized_status': 'bool'
    }

    attribute_map = {
        'channel_id': 'channel_id',
        'node_id': 'node_id',
        'allotted_time': 'allotted_time',
        'update_time': 'update_time',
        'synchronized_time': 'synchronized_time',
        'synchronized_status': 'synchronized_status'
    }

    def __init__(self, channel_id=None, node_id=None, allotted_time=None, update_time=None, synchronized_time=None, synchronized_status=None):
        r"""CreateClientNodeResponse

        The model defined in huaweicloud sdk

        :param channel_id: 推送通道ID
        :type channel_id: str
        :param node_id: 节点ID
        :type node_id: str
        :param allotted_time: 路由分配到节点的时间
        :type allotted_time: str
        :param update_time: 节点实例化后通道的连接和推送信息的修改时间
        :type update_time: str
        :param synchronized_time: 下发时间，表示通道是否已经同步到了节点
        :type synchronized_time: str
        :param synchronized_status: 下发状态，表示是否已同步到了节点
        :type synchronized_status: bool
        """
        
        super().__init__()

        self._channel_id = None
        self._node_id = None
        self._allotted_time = None
        self._update_time = None
        self._synchronized_time = None
        self._synchronized_status = None
        self.discriminator = None

        if channel_id is not None:
            self.channel_id = channel_id
        if node_id is not None:
            self.node_id = node_id
        if allotted_time is not None:
            self.allotted_time = allotted_time
        if update_time is not None:
            self.update_time = update_time
        if synchronized_time is not None:
            self.synchronized_time = synchronized_time
        if synchronized_status is not None:
            self.synchronized_status = synchronized_status

    @property
    def channel_id(self):
        r"""Gets the channel_id of this CreateClientNodeResponse.

        推送通道ID

        :return: The channel_id of this CreateClientNodeResponse.
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        r"""Sets the channel_id of this CreateClientNodeResponse.

        推送通道ID

        :param channel_id: The channel_id of this CreateClientNodeResponse.
        :type channel_id: str
        """
        self._channel_id = channel_id

    @property
    def node_id(self):
        r"""Gets the node_id of this CreateClientNodeResponse.

        节点ID

        :return: The node_id of this CreateClientNodeResponse.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this CreateClientNodeResponse.

        节点ID

        :param node_id: The node_id of this CreateClientNodeResponse.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def allotted_time(self):
        r"""Gets the allotted_time of this CreateClientNodeResponse.

        路由分配到节点的时间

        :return: The allotted_time of this CreateClientNodeResponse.
        :rtype: str
        """
        return self._allotted_time

    @allotted_time.setter
    def allotted_time(self, allotted_time):
        r"""Sets the allotted_time of this CreateClientNodeResponse.

        路由分配到节点的时间

        :param allotted_time: The allotted_time of this CreateClientNodeResponse.
        :type allotted_time: str
        """
        self._allotted_time = allotted_time

    @property
    def update_time(self):
        r"""Gets the update_time of this CreateClientNodeResponse.

        节点实例化后通道的连接和推送信息的修改时间

        :return: The update_time of this CreateClientNodeResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CreateClientNodeResponse.

        节点实例化后通道的连接和推送信息的修改时间

        :param update_time: The update_time of this CreateClientNodeResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def synchronized_time(self):
        r"""Gets the synchronized_time of this CreateClientNodeResponse.

        下发时间，表示通道是否已经同步到了节点

        :return: The synchronized_time of this CreateClientNodeResponse.
        :rtype: str
        """
        return self._synchronized_time

    @synchronized_time.setter
    def synchronized_time(self, synchronized_time):
        r"""Sets the synchronized_time of this CreateClientNodeResponse.

        下发时间，表示通道是否已经同步到了节点

        :param synchronized_time: The synchronized_time of this CreateClientNodeResponse.
        :type synchronized_time: str
        """
        self._synchronized_time = synchronized_time

    @property
    def synchronized_status(self):
        r"""Gets the synchronized_status of this CreateClientNodeResponse.

        下发状态，表示是否已同步到了节点

        :return: The synchronized_status of this CreateClientNodeResponse.
        :rtype: bool
        """
        return self._synchronized_status

    @synchronized_status.setter
    def synchronized_status(self, synchronized_status):
        r"""Sets the synchronized_status of this CreateClientNodeResponse.

        下发状态，表示是否已同步到了节点

        :param synchronized_status: The synchronized_status of this CreateClientNodeResponse.
        :type synchronized_status: bool
        """
        self._synchronized_status = synchronized_status

    def to_dict(self):
        import warnings
        warnings.warn("CreateClientNodeResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateClientNodeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
