# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateClientNodeRequest:

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
        'body': 'UpdateNodeChannelRequestDTO'
    }

    attribute_map = {
        'channel_id': 'channel_id',
        'node_id': 'node_id',
        'body': 'body'
    }

    def __init__(self, channel_id=None, node_id=None, body=None):
        r"""UpdateClientNodeRequest

        The model defined in huaweicloud sdk

        :param channel_id: 边缘推送通道ID
        :type channel_id: str
        :param node_id: 边缘节点ID
        :type node_id: str
        :param body: Body of the UpdateClientNodeRequest
        :type body: :class:`huaweicloudsdkiotedge.v2.UpdateNodeChannelRequestDTO`
        """
        
        

        self._channel_id = None
        self._node_id = None
        self._body = None
        self.discriminator = None

        self.channel_id = channel_id
        self.node_id = node_id
        if body is not None:
            self.body = body

    @property
    def channel_id(self):
        r"""Gets the channel_id of this UpdateClientNodeRequest.

        边缘推送通道ID

        :return: The channel_id of this UpdateClientNodeRequest.
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        r"""Sets the channel_id of this UpdateClientNodeRequest.

        边缘推送通道ID

        :param channel_id: The channel_id of this UpdateClientNodeRequest.
        :type channel_id: str
        """
        self._channel_id = channel_id

    @property
    def node_id(self):
        r"""Gets the node_id of this UpdateClientNodeRequest.

        边缘节点ID

        :return: The node_id of this UpdateClientNodeRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this UpdateClientNodeRequest.

        边缘节点ID

        :param node_id: The node_id of this UpdateClientNodeRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def body(self):
        r"""Gets the body of this UpdateClientNodeRequest.

        :return: The body of this UpdateClientNodeRequest.
        :rtype: :class:`huaweicloudsdkiotedge.v2.UpdateNodeChannelRequestDTO`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateClientNodeRequest.

        :param body: The body of this UpdateClientNodeRequest.
        :type body: :class:`huaweicloudsdkiotedge.v2.UpdateNodeChannelRequestDTO`
        """
        self._body = body

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
        if not isinstance(other, UpdateClientNodeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
