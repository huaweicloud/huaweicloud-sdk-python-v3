# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HistoryStreamInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'app': 'str',
        'stream': 'str',
        'type': 'int',
        'video_codec': 'str',
        'audio_codec': 'str',
        'client_ip': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'app': 'app',
        'stream': 'stream',
        'type': 'type',
        'video_codec': 'video_codec',
        'audio_codec': 'audio_codec',
        'client_ip': 'client_ip',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, domain=None, app=None, stream=None, type=None, video_codec=None, audio_codec=None, client_ip=None, start_time=None, end_time=None):
        r"""HistoryStreamInfo

        The model defined in huaweicloud sdk

        :param domain: 推流域名。  - type为0表主播推流域名。  - type为1表示第三方推流域名 
        :type domain: str
        :param app: 应用名称。
        :type app: str
        :param stream: 流名。
        :type stream: str
        :param type: 推流类型，取值如下：  - 0：表示主播推流  - 1：表示第三方推流 
        :type type: int
        :param video_codec: 视频编码格式。
        :type video_codec: str
        :param audio_codec: 音频编码格式。
        :type audio_codec: str
        :param client_ip: 主播ip。
        :type client_ip: str
        :param start_time: 采样开始时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。
        :type start_time: str
        :param end_time: 采样结束时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。
        :type end_time: str
        """
        
        

        self._domain = None
        self._app = None
        self._stream = None
        self._type = None
        self._video_codec = None
        self._audio_codec = None
        self._client_ip = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if app is not None:
            self.app = app
        if stream is not None:
            self.stream = stream
        if type is not None:
            self.type = type
        if video_codec is not None:
            self.video_codec = video_codec
        if audio_codec is not None:
            self.audio_codec = audio_codec
        if client_ip is not None:
            self.client_ip = client_ip
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def domain(self):
        r"""Gets the domain of this HistoryStreamInfo.

        推流域名。  - type为0表主播推流域名。  - type为1表示第三方推流域名 

        :return: The domain of this HistoryStreamInfo.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this HistoryStreamInfo.

        推流域名。  - type为0表主播推流域名。  - type为1表示第三方推流域名 

        :param domain: The domain of this HistoryStreamInfo.
        :type domain: str
        """
        self._domain = domain

    @property
    def app(self):
        r"""Gets the app of this HistoryStreamInfo.

        应用名称。

        :return: The app of this HistoryStreamInfo.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        r"""Sets the app of this HistoryStreamInfo.

        应用名称。

        :param app: The app of this HistoryStreamInfo.
        :type app: str
        """
        self._app = app

    @property
    def stream(self):
        r"""Gets the stream of this HistoryStreamInfo.

        流名。

        :return: The stream of this HistoryStreamInfo.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        r"""Sets the stream of this HistoryStreamInfo.

        流名。

        :param stream: The stream of this HistoryStreamInfo.
        :type stream: str
        """
        self._stream = stream

    @property
    def type(self):
        r"""Gets the type of this HistoryStreamInfo.

        推流类型，取值如下：  - 0：表示主播推流  - 1：表示第三方推流 

        :return: The type of this HistoryStreamInfo.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this HistoryStreamInfo.

        推流类型，取值如下：  - 0：表示主播推流  - 1：表示第三方推流 

        :param type: The type of this HistoryStreamInfo.
        :type type: int
        """
        self._type = type

    @property
    def video_codec(self):
        r"""Gets the video_codec of this HistoryStreamInfo.

        视频编码格式。

        :return: The video_codec of this HistoryStreamInfo.
        :rtype: str
        """
        return self._video_codec

    @video_codec.setter
    def video_codec(self, video_codec):
        r"""Sets the video_codec of this HistoryStreamInfo.

        视频编码格式。

        :param video_codec: The video_codec of this HistoryStreamInfo.
        :type video_codec: str
        """
        self._video_codec = video_codec

    @property
    def audio_codec(self):
        r"""Gets the audio_codec of this HistoryStreamInfo.

        音频编码格式。

        :return: The audio_codec of this HistoryStreamInfo.
        :rtype: str
        """
        return self._audio_codec

    @audio_codec.setter
    def audio_codec(self, audio_codec):
        r"""Sets the audio_codec of this HistoryStreamInfo.

        音频编码格式。

        :param audio_codec: The audio_codec of this HistoryStreamInfo.
        :type audio_codec: str
        """
        self._audio_codec = audio_codec

    @property
    def client_ip(self):
        r"""Gets the client_ip of this HistoryStreamInfo.

        主播ip。

        :return: The client_ip of this HistoryStreamInfo.
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        r"""Sets the client_ip of this HistoryStreamInfo.

        主播ip。

        :param client_ip: The client_ip of this HistoryStreamInfo.
        :type client_ip: str
        """
        self._client_ip = client_ip

    @property
    def start_time(self):
        r"""Gets the start_time of this HistoryStreamInfo.

        采样开始时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。

        :return: The start_time of this HistoryStreamInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this HistoryStreamInfo.

        采样开始时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。

        :param start_time: The start_time of this HistoryStreamInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this HistoryStreamInfo.

        采样结束时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。

        :return: The end_time of this HistoryStreamInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this HistoryStreamInfo.

        采样结束时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。

        :param end_time: The end_time of this HistoryStreamInfo.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, HistoryStreamInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
