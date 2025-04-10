# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PlayDomainStreamInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'play_domain': 'str',
        'stream': 'str',
        'protocol': 'str',
        'bandwidth': 'int',
        'online': 'int'
    }

    attribute_map = {
        'play_domain': 'play_domain',
        'stream': 'stream',
        'protocol': 'protocol',
        'bandwidth': 'bandwidth',
        'online': 'online'
    }

    def __init__(self, play_domain=None, stream=None, protocol=None, bandwidth=None, online=None):
        r"""PlayDomainStreamInfo

        The model defined in huaweicloud sdk

        :param play_domain: 播放域名
        :type play_domain: str
        :param stream: 播放流名
        :type stream: str
        :param protocol: 播放的协议，支持flv,hls,rtmp。
        :type protocol: str
        :param bandwidth: 1分钟粒度的带宽值，单位为bps。
        :type bandwidth: int
        :param online: 1分钟粒度的在线人数。
        :type online: int
        """
        
        

        self._play_domain = None
        self._stream = None
        self._protocol = None
        self._bandwidth = None
        self._online = None
        self.discriminator = None

        if play_domain is not None:
            self.play_domain = play_domain
        if stream is not None:
            self.stream = stream
        if protocol is not None:
            self.protocol = protocol
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if online is not None:
            self.online = online

    @property
    def play_domain(self):
        r"""Gets the play_domain of this PlayDomainStreamInfo.

        播放域名

        :return: The play_domain of this PlayDomainStreamInfo.
        :rtype: str
        """
        return self._play_domain

    @play_domain.setter
    def play_domain(self, play_domain):
        r"""Sets the play_domain of this PlayDomainStreamInfo.

        播放域名

        :param play_domain: The play_domain of this PlayDomainStreamInfo.
        :type play_domain: str
        """
        self._play_domain = play_domain

    @property
    def stream(self):
        r"""Gets the stream of this PlayDomainStreamInfo.

        播放流名

        :return: The stream of this PlayDomainStreamInfo.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        r"""Sets the stream of this PlayDomainStreamInfo.

        播放流名

        :param stream: The stream of this PlayDomainStreamInfo.
        :type stream: str
        """
        self._stream = stream

    @property
    def protocol(self):
        r"""Gets the protocol of this PlayDomainStreamInfo.

        播放的协议，支持flv,hls,rtmp。

        :return: The protocol of this PlayDomainStreamInfo.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this PlayDomainStreamInfo.

        播放的协议，支持flv,hls,rtmp。

        :param protocol: The protocol of this PlayDomainStreamInfo.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def bandwidth(self):
        r"""Gets the bandwidth of this PlayDomainStreamInfo.

        1分钟粒度的带宽值，单位为bps。

        :return: The bandwidth of this PlayDomainStreamInfo.
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        r"""Sets the bandwidth of this PlayDomainStreamInfo.

        1分钟粒度的带宽值，单位为bps。

        :param bandwidth: The bandwidth of this PlayDomainStreamInfo.
        :type bandwidth: int
        """
        self._bandwidth = bandwidth

    @property
    def online(self):
        r"""Gets the online of this PlayDomainStreamInfo.

        1分钟粒度的在线人数。

        :return: The online of this PlayDomainStreamInfo.
        :rtype: int
        """
        return self._online

    @online.setter
    def online(self, online):
        r"""Sets the online of this PlayDomainStreamInfo.

        1分钟粒度的在线人数。

        :param online: The online of this PlayDomainStreamInfo.
        :type online: int
        """
        self._online = online

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
        if not isinstance(other, PlayDomainStreamInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
