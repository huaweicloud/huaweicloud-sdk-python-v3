# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StreamingErrorBrokens:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_stream_failed': 'list[float]',
        'hand_shake_failed': 'list[float]',
        'parse_file_failed': 'list[float]',
        'parse_flv_file_failed': 'list[float]',
        'play_failed': 'list[float]',
        'publish_failed': 'list[float]',
        'retry_failed': 'list[float]',
        'rtmp_connect_failed': 'list[float]',
        'tcp_connect_failed': 'list[float]'
    }

    attribute_map = {
        'create_stream_failed': 'createStreamFailed',
        'hand_shake_failed': 'handShakeFailed',
        'parse_file_failed': 'parseFileFailed',
        'parse_flv_file_failed': 'parseFlvFileFailed',
        'play_failed': 'playFailed',
        'publish_failed': 'publishFailed',
        'retry_failed': 'retryFailed',
        'rtmp_connect_failed': 'rtmpConnectFailed',
        'tcp_connect_failed': 'tcpConnectFailed'
    }

    def __init__(self, create_stream_failed=None, hand_shake_failed=None, parse_file_failed=None, parse_flv_file_failed=None, play_failed=None, publish_failed=None, retry_failed=None, rtmp_connect_failed=None, tcp_connect_failed=None):
        """StreamingErrorBrokens

        The model defined in huaweicloud sdk

        :param create_stream_failed: 创建流媒体失败数
        :type create_stream_failed: list[float]
        :param hand_shake_failed: 建立握手失败数
        :type hand_shake_failed: list[float]
        :param parse_file_failed: 文件解析失败数
        :type parse_file_failed: list[float]
        :param parse_flv_file_failed: FLV文件解析失败数
        :type parse_flv_file_failed: list[float]
        :param play_failed: 播放失败数
        :type play_failed: list[float]
        :param publish_failed: 发布失败数
        :type publish_failed: list[float]
        :param retry_failed: 重试失败数
        :type retry_failed: list[float]
        :param rtmp_connect_failed: RTMP连接失败数
        :type rtmp_connect_failed: list[float]
        :param tcp_connect_failed: TCP连接失败数
        :type tcp_connect_failed: list[float]
        """
        
        

        self._create_stream_failed = None
        self._hand_shake_failed = None
        self._parse_file_failed = None
        self._parse_flv_file_failed = None
        self._play_failed = None
        self._publish_failed = None
        self._retry_failed = None
        self._rtmp_connect_failed = None
        self._tcp_connect_failed = None
        self.discriminator = None

        if create_stream_failed is not None:
            self.create_stream_failed = create_stream_failed
        if hand_shake_failed is not None:
            self.hand_shake_failed = hand_shake_failed
        if parse_file_failed is not None:
            self.parse_file_failed = parse_file_failed
        if parse_flv_file_failed is not None:
            self.parse_flv_file_failed = parse_flv_file_failed
        if play_failed is not None:
            self.play_failed = play_failed
        if publish_failed is not None:
            self.publish_failed = publish_failed
        if retry_failed is not None:
            self.retry_failed = retry_failed
        if rtmp_connect_failed is not None:
            self.rtmp_connect_failed = rtmp_connect_failed
        if tcp_connect_failed is not None:
            self.tcp_connect_failed = tcp_connect_failed

    @property
    def create_stream_failed(self):
        """Gets the create_stream_failed of this StreamingErrorBrokens.

        创建流媒体失败数

        :return: The create_stream_failed of this StreamingErrorBrokens.
        :rtype: list[float]
        """
        return self._create_stream_failed

    @create_stream_failed.setter
    def create_stream_failed(self, create_stream_failed):
        """Sets the create_stream_failed of this StreamingErrorBrokens.

        创建流媒体失败数

        :param create_stream_failed: The create_stream_failed of this StreamingErrorBrokens.
        :type create_stream_failed: list[float]
        """
        self._create_stream_failed = create_stream_failed

    @property
    def hand_shake_failed(self):
        """Gets the hand_shake_failed of this StreamingErrorBrokens.

        建立握手失败数

        :return: The hand_shake_failed of this StreamingErrorBrokens.
        :rtype: list[float]
        """
        return self._hand_shake_failed

    @hand_shake_failed.setter
    def hand_shake_failed(self, hand_shake_failed):
        """Sets the hand_shake_failed of this StreamingErrorBrokens.

        建立握手失败数

        :param hand_shake_failed: The hand_shake_failed of this StreamingErrorBrokens.
        :type hand_shake_failed: list[float]
        """
        self._hand_shake_failed = hand_shake_failed

    @property
    def parse_file_failed(self):
        """Gets the parse_file_failed of this StreamingErrorBrokens.

        文件解析失败数

        :return: The parse_file_failed of this StreamingErrorBrokens.
        :rtype: list[float]
        """
        return self._parse_file_failed

    @parse_file_failed.setter
    def parse_file_failed(self, parse_file_failed):
        """Sets the parse_file_failed of this StreamingErrorBrokens.

        文件解析失败数

        :param parse_file_failed: The parse_file_failed of this StreamingErrorBrokens.
        :type parse_file_failed: list[float]
        """
        self._parse_file_failed = parse_file_failed

    @property
    def parse_flv_file_failed(self):
        """Gets the parse_flv_file_failed of this StreamingErrorBrokens.

        FLV文件解析失败数

        :return: The parse_flv_file_failed of this StreamingErrorBrokens.
        :rtype: list[float]
        """
        return self._parse_flv_file_failed

    @parse_flv_file_failed.setter
    def parse_flv_file_failed(self, parse_flv_file_failed):
        """Sets the parse_flv_file_failed of this StreamingErrorBrokens.

        FLV文件解析失败数

        :param parse_flv_file_failed: The parse_flv_file_failed of this StreamingErrorBrokens.
        :type parse_flv_file_failed: list[float]
        """
        self._parse_flv_file_failed = parse_flv_file_failed

    @property
    def play_failed(self):
        """Gets the play_failed of this StreamingErrorBrokens.

        播放失败数

        :return: The play_failed of this StreamingErrorBrokens.
        :rtype: list[float]
        """
        return self._play_failed

    @play_failed.setter
    def play_failed(self, play_failed):
        """Sets the play_failed of this StreamingErrorBrokens.

        播放失败数

        :param play_failed: The play_failed of this StreamingErrorBrokens.
        :type play_failed: list[float]
        """
        self._play_failed = play_failed

    @property
    def publish_failed(self):
        """Gets the publish_failed of this StreamingErrorBrokens.

        发布失败数

        :return: The publish_failed of this StreamingErrorBrokens.
        :rtype: list[float]
        """
        return self._publish_failed

    @publish_failed.setter
    def publish_failed(self, publish_failed):
        """Sets the publish_failed of this StreamingErrorBrokens.

        发布失败数

        :param publish_failed: The publish_failed of this StreamingErrorBrokens.
        :type publish_failed: list[float]
        """
        self._publish_failed = publish_failed

    @property
    def retry_failed(self):
        """Gets the retry_failed of this StreamingErrorBrokens.

        重试失败数

        :return: The retry_failed of this StreamingErrorBrokens.
        :rtype: list[float]
        """
        return self._retry_failed

    @retry_failed.setter
    def retry_failed(self, retry_failed):
        """Sets the retry_failed of this StreamingErrorBrokens.

        重试失败数

        :param retry_failed: The retry_failed of this StreamingErrorBrokens.
        :type retry_failed: list[float]
        """
        self._retry_failed = retry_failed

    @property
    def rtmp_connect_failed(self):
        """Gets the rtmp_connect_failed of this StreamingErrorBrokens.

        RTMP连接失败数

        :return: The rtmp_connect_failed of this StreamingErrorBrokens.
        :rtype: list[float]
        """
        return self._rtmp_connect_failed

    @rtmp_connect_failed.setter
    def rtmp_connect_failed(self, rtmp_connect_failed):
        """Sets the rtmp_connect_failed of this StreamingErrorBrokens.

        RTMP连接失败数

        :param rtmp_connect_failed: The rtmp_connect_failed of this StreamingErrorBrokens.
        :type rtmp_connect_failed: list[float]
        """
        self._rtmp_connect_failed = rtmp_connect_failed

    @property
    def tcp_connect_failed(self):
        """Gets the tcp_connect_failed of this StreamingErrorBrokens.

        TCP连接失败数

        :return: The tcp_connect_failed of this StreamingErrorBrokens.
        :rtype: list[float]
        """
        return self._tcp_connect_failed

    @tcp_connect_failed.setter
    def tcp_connect_failed(self, tcp_connect_failed):
        """Sets the tcp_connect_failed of this StreamingErrorBrokens.

        TCP连接失败数

        :param tcp_connect_failed: The tcp_connect_failed of this StreamingErrorBrokens.
        :type tcp_connect_failed: list[float]
        """
        self._tcp_connect_failed = tcp_connect_failed

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
        if not isinstance(other, StreamingErrorBrokens):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
