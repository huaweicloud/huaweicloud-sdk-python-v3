# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NetworkConnection:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'peer_connection_list': 'list[PeerConnectionItem]'
    }

    attribute_map = {
        'peer_connection_list': 'peerConnectionList'
    }

    def __init__(self, peer_connection_list=None):
        r"""NetworkConnection

        The model defined in huaweicloud sdk

        :param peer_connection_list: **参数解释**：Peer方式打通网络列表。
        :type peer_connection_list: list[:class:`huaweicloudsdkmodelarts.v1.PeerConnectionItem`]
        """
        
        

        self._peer_connection_list = None
        self.discriminator = None

        if peer_connection_list is not None:
            self.peer_connection_list = peer_connection_list

    @property
    def peer_connection_list(self):
        r"""Gets the peer_connection_list of this NetworkConnection.

        **参数解释**：Peer方式打通网络列表。

        :return: The peer_connection_list of this NetworkConnection.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.PeerConnectionItem`]
        """
        return self._peer_connection_list

    @peer_connection_list.setter
    def peer_connection_list(self, peer_connection_list):
        r"""Sets the peer_connection_list of this NetworkConnection.

        **参数解释**：Peer方式打通网络列表。

        :param peer_connection_list: The peer_connection_list of this NetworkConnection.
        :type peer_connection_list: list[:class:`huaweicloudsdkmodelarts.v1.PeerConnectionItem`]
        """
        self._peer_connection_list = peer_connection_list

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
        if not isinstance(other, NetworkConnection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
