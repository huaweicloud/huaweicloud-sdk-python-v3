# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PeerChannelInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'channel_name': 'str',
        'peers': 'dict(str, int)'
    }

    attribute_map = {
        'channel_name': 'channel_name',
        'peers': 'peers'
    }

    def __init__(self, channel_name=None, peers=None):
        r"""PeerChannelInfo

        The model defined in huaweicloud sdk

        :param channel_name: peer加入的通道名称
        :type channel_name: str
        :param peers: 加入通道peer名称和数量，key为组织名称，value为peer数量
        :type peers: dict(str, int)
        """
        
        

        self._channel_name = None
        self._peers = None
        self.discriminator = None

        self.channel_name = channel_name
        self.peers = peers

    @property
    def channel_name(self):
        r"""Gets the channel_name of this PeerChannelInfo.

        peer加入的通道名称

        :return: The channel_name of this PeerChannelInfo.
        :rtype: str
        """
        return self._channel_name

    @channel_name.setter
    def channel_name(self, channel_name):
        r"""Sets the channel_name of this PeerChannelInfo.

        peer加入的通道名称

        :param channel_name: The channel_name of this PeerChannelInfo.
        :type channel_name: str
        """
        self._channel_name = channel_name

    @property
    def peers(self):
        r"""Gets the peers of this PeerChannelInfo.

        加入通道peer名称和数量，key为组织名称，value为peer数量

        :return: The peers of this PeerChannelInfo.
        :rtype: dict(str, int)
        """
        return self._peers

    @peers.setter
    def peers(self, peers):
        r"""Sets the peers of this PeerChannelInfo.

        加入通道peer名称和数量，key为组织名称，value为peer数量

        :param peers: The peers of this PeerChannelInfo.
        :type peers: dict(str, int)
        """
        self._peers = peers

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PeerChannelInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
