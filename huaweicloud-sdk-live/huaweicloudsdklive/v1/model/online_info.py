# coding: utf-8

import pprint
import re

import six





class OnlineInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'publish_domain': 'str',
        'app': 'str',
        'stream': 'str',
        'video_codec': 'str',
        'audio_codec': 'str',
        'client_ip': 'str',
        'start_time': 'str'
    }

    attribute_map = {
        'publish_domain': 'publish_domain',
        'app': 'app',
        'stream': 'stream',
        'video_codec': 'video_codec',
        'audio_codec': 'audio_codec',
        'client_ip': 'client_ip',
        'start_time': 'start_time'
    }

    def __init__(self, publish_domain=None, app=None, stream=None, video_codec=None, audio_codec=None, client_ip=None, start_time=None):
        """OnlineInfo - a model defined in huaweicloud sdk"""
        
        

        self._publish_domain = None
        self._app = None
        self._stream = None
        self._video_codec = None
        self._audio_codec = None
        self._client_ip = None
        self._start_time = None
        self.discriminator = None

        self.publish_domain = publish_domain
        self.app = app
        self.stream = stream
        self.video_codec = video_codec
        self.audio_codec = audio_codec
        self.client_ip = client_ip
        self.start_time = start_time

    @property
    def publish_domain(self):
        """Gets the publish_domain of this OnlineInfo.

        域名

        :return: The publish_domain of this OnlineInfo.
        :rtype: str
        """
        return self._publish_domain

    @publish_domain.setter
    def publish_domain(self, publish_domain):
        """Sets the publish_domain of this OnlineInfo.

        域名

        :param publish_domain: The publish_domain of this OnlineInfo.
        :type: str
        """
        self._publish_domain = publish_domain

    @property
    def app(self):
        """Gets the app of this OnlineInfo.

        应用名

        :return: The app of this OnlineInfo.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this OnlineInfo.

        应用名

        :param app: The app of this OnlineInfo.
        :type: str
        """
        self._app = app

    @property
    def stream(self):
        """Gets the stream of this OnlineInfo.

        流名

        :return: The stream of this OnlineInfo.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this OnlineInfo.

        流名

        :param stream: The stream of this OnlineInfo.
        :type: str
        """
        self._stream = stream

    @property
    def video_codec(self):
        """Gets the video_codec of this OnlineInfo.

        视频编码方式 - H264 - H265 

        :return: The video_codec of this OnlineInfo.
        :rtype: str
        """
        return self._video_codec

    @video_codec.setter
    def video_codec(self, video_codec):
        """Sets the video_codec of this OnlineInfo.

        视频编码方式 - H264 - H265 

        :param video_codec: The video_codec of this OnlineInfo.
        :type: str
        """
        self._video_codec = video_codec

    @property
    def audio_codec(self):
        """Gets the audio_codec of this OnlineInfo.

        音频编码方式 - AAC 

        :return: The audio_codec of this OnlineInfo.
        :rtype: str
        """
        return self._audio_codec

    @audio_codec.setter
    def audio_codec(self, audio_codec):
        """Sets the audio_codec of this OnlineInfo.

        音频编码方式 - AAC 

        :param audio_codec: The audio_codec of this OnlineInfo.
        :type: str
        """
        self._audio_codec = audio_codec

    @property
    def client_ip(self):
        """Gets the client_ip of this OnlineInfo.

        推流设备的ip

        :return: The client_ip of this OnlineInfo.
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        """Sets the client_ip of this OnlineInfo.

        推流设备的ip

        :param client_ip: The client_ip of this OnlineInfo.
        :type: str
        """
        self._client_ip = client_ip

    @property
    def start_time(self):
        """Gets the start_time of this OnlineInfo.

        开始推流时刻 UTC格式 2006-01-02T15:04:05Z

        :return: The start_time of this OnlineInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this OnlineInfo.

        开始推流时刻 UTC格式 2006-01-02T15:04:05Z

        :param start_time: The start_time of this OnlineInfo.
        :type: str
        """
        self._start_time = start_time

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OnlineInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
