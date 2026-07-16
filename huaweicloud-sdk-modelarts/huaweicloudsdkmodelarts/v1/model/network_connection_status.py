# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NetworkConnectionStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'peer_connection_status': 'list[PeerConnectionStatus]',
        'sfs_turbo_status': 'list[SfsTurboConnectionStatus]'
    }

    attribute_map = {
        'peer_connection_status': 'peerConnectionStatus',
        'sfs_turbo_status': 'sfsTurboStatus'
    }

    def __init__(self, peer_connection_status=None, sfs_turbo_status=None):
        r"""NetworkConnectionStatus

        The model defined in huaweicloud sdk

        :param peer_connection_status: **参数解释**：Peer方式打通网络的状态信息列表。
        :type peer_connection_status: list[:class:`huaweicloudsdkmodelarts.v1.PeerConnectionStatus`]
        :param sfs_turbo_status: **参数解释**：网络可连通的SFS Turbo信息列表。
        :type sfs_turbo_status: list[:class:`huaweicloudsdkmodelarts.v1.SfsTurboConnectionStatus`]
        """
        
        

        self._peer_connection_status = None
        self._sfs_turbo_status = None
        self.discriminator = None

        if peer_connection_status is not None:
            self.peer_connection_status = peer_connection_status
        if sfs_turbo_status is not None:
            self.sfs_turbo_status = sfs_turbo_status

    @property
    def peer_connection_status(self):
        r"""Gets the peer_connection_status of this NetworkConnectionStatus.

        **参数解释**：Peer方式打通网络的状态信息列表。

        :return: The peer_connection_status of this NetworkConnectionStatus.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.PeerConnectionStatus`]
        """
        return self._peer_connection_status

    @peer_connection_status.setter
    def peer_connection_status(self, peer_connection_status):
        r"""Sets the peer_connection_status of this NetworkConnectionStatus.

        **参数解释**：Peer方式打通网络的状态信息列表。

        :param peer_connection_status: The peer_connection_status of this NetworkConnectionStatus.
        :type peer_connection_status: list[:class:`huaweicloudsdkmodelarts.v1.PeerConnectionStatus`]
        """
        self._peer_connection_status = peer_connection_status

    @property
    def sfs_turbo_status(self):
        r"""Gets the sfs_turbo_status of this NetworkConnectionStatus.

        **参数解释**：网络可连通的SFS Turbo信息列表。

        :return: The sfs_turbo_status of this NetworkConnectionStatus.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.SfsTurboConnectionStatus`]
        """
        return self._sfs_turbo_status

    @sfs_turbo_status.setter
    def sfs_turbo_status(self, sfs_turbo_status):
        r"""Sets the sfs_turbo_status of this NetworkConnectionStatus.

        **参数解释**：网络可连通的SFS Turbo信息列表。

        :param sfs_turbo_status: The sfs_turbo_status of this NetworkConnectionStatus.
        :type sfs_turbo_status: list[:class:`huaweicloudsdkmodelarts.v1.SfsTurboConnectionStatus`]
        """
        self._sfs_turbo_status = sfs_turbo_status

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
        if not isinstance(other, NetworkConnectionStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
