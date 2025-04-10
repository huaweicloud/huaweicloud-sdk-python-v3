# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSingleStreamDetailResponse(SdkResponse):

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
        'video_framerate': 'list[StreamDetail]',
        'video_bitrate': 'list[StreamDetail]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'publish_domain': 'publish_domain',
        'app': 'app',
        'stream': 'stream',
        'video_framerate': 'video_framerate',
        'video_bitrate': 'video_bitrate',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, publish_domain=None, app=None, stream=None, video_framerate=None, video_bitrate=None, x_request_id=None):
        r"""ListSingleStreamDetailResponse

        The model defined in huaweicloud sdk

        :param publish_domain: 推流域名
        :type publish_domain: str
        :param app: 应用名
        :type app: str
        :param stream: 流名
        :type stream: str
        :param video_framerate: 展示流视频帧率情况，帧率单位为fps。  如果出现断流则会出现多个时间段流信息，如： &#x60;&#x60;&#x60; \&quot;video_framerate\&quot;: [     {       \&quot;start_time\&quot;: \&quot;2022-02-04T07:00:00Z\&quot;,       \&quot;end_time\&quot;: \&quot;2022-02-04T07:00:02Z\&quot;,       \&quot;data_list\&quot;: [         21,         22       ]     },     {       \&quot;start_time\&quot;: \&quot;2022-02-04T07:00:05Z\&quot;,       \&quot;end_time\&quot;: \&quot;2022-02-04T07:00:07Z\&quot;,       \&quot;data_list\&quot;: [         13,         34,         21       ]     }   ] 
        :type video_framerate: list[:class:`huaweicloudsdklive.v2.StreamDetail`]
        :param video_bitrate: 展示流视频码率情况，码率单位为Kbps。  如果出现断流则会出现多个时间段流信息，如： &#x60;&#x60;&#x60; \&quot;video_bitrate\&quot;: [     {       \&quot;start_time\&quot;: \&quot;2022-02-04T07:00:00Z\&quot;,       \&quot;end_time\&quot;: \&quot;2022-02-04T07:00:02Z\&quot;,       \&quot;data_list\&quot;: [         1326,         1268,         775       ]     },     {       \&quot;start_time\&quot;: \&quot;2022-02-04T07:00:05Z\&quot;,       \&quot;end_time\&quot;: \&quot;2022-02-04T07:00:07Z\&quot;,       \&quot;data_list\&quot;: [         1021,         2022       ]     }   ] 
        :type video_bitrate: list[:class:`huaweicloudsdklive.v2.StreamDetail`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListSingleStreamDetailResponse, self).__init__()

        self._publish_domain = None
        self._app = None
        self._stream = None
        self._video_framerate = None
        self._video_bitrate = None
        self._x_request_id = None
        self.discriminator = None

        if publish_domain is not None:
            self.publish_domain = publish_domain
        if app is not None:
            self.app = app
        if stream is not None:
            self.stream = stream
        if video_framerate is not None:
            self.video_framerate = video_framerate
        if video_bitrate is not None:
            self.video_bitrate = video_bitrate
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def publish_domain(self):
        r"""Gets the publish_domain of this ListSingleStreamDetailResponse.

        推流域名

        :return: The publish_domain of this ListSingleStreamDetailResponse.
        :rtype: str
        """
        return self._publish_domain

    @publish_domain.setter
    def publish_domain(self, publish_domain):
        r"""Sets the publish_domain of this ListSingleStreamDetailResponse.

        推流域名

        :param publish_domain: The publish_domain of this ListSingleStreamDetailResponse.
        :type publish_domain: str
        """
        self._publish_domain = publish_domain

    @property
    def app(self):
        r"""Gets the app of this ListSingleStreamDetailResponse.

        应用名

        :return: The app of this ListSingleStreamDetailResponse.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        r"""Sets the app of this ListSingleStreamDetailResponse.

        应用名

        :param app: The app of this ListSingleStreamDetailResponse.
        :type app: str
        """
        self._app = app

    @property
    def stream(self):
        r"""Gets the stream of this ListSingleStreamDetailResponse.

        流名

        :return: The stream of this ListSingleStreamDetailResponse.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        r"""Sets the stream of this ListSingleStreamDetailResponse.

        流名

        :param stream: The stream of this ListSingleStreamDetailResponse.
        :type stream: str
        """
        self._stream = stream

    @property
    def video_framerate(self):
        r"""Gets the video_framerate of this ListSingleStreamDetailResponse.

        展示流视频帧率情况，帧率单位为fps。  如果出现断流则会出现多个时间段流信息，如： ``` \"video_framerate\": [     {       \"start_time\": \"2022-02-04T07:00:00Z\",       \"end_time\": \"2022-02-04T07:00:02Z\",       \"data_list\": [         21,         22       ]     },     {       \"start_time\": \"2022-02-04T07:00:05Z\",       \"end_time\": \"2022-02-04T07:00:07Z\",       \"data_list\": [         13,         34,         21       ]     }   ] 

        :return: The video_framerate of this ListSingleStreamDetailResponse.
        :rtype: list[:class:`huaweicloudsdklive.v2.StreamDetail`]
        """
        return self._video_framerate

    @video_framerate.setter
    def video_framerate(self, video_framerate):
        r"""Sets the video_framerate of this ListSingleStreamDetailResponse.

        展示流视频帧率情况，帧率单位为fps。  如果出现断流则会出现多个时间段流信息，如： ``` \"video_framerate\": [     {       \"start_time\": \"2022-02-04T07:00:00Z\",       \"end_time\": \"2022-02-04T07:00:02Z\",       \"data_list\": [         21,         22       ]     },     {       \"start_time\": \"2022-02-04T07:00:05Z\",       \"end_time\": \"2022-02-04T07:00:07Z\",       \"data_list\": [         13,         34,         21       ]     }   ] 

        :param video_framerate: The video_framerate of this ListSingleStreamDetailResponse.
        :type video_framerate: list[:class:`huaweicloudsdklive.v2.StreamDetail`]
        """
        self._video_framerate = video_framerate

    @property
    def video_bitrate(self):
        r"""Gets the video_bitrate of this ListSingleStreamDetailResponse.

        展示流视频码率情况，码率单位为Kbps。  如果出现断流则会出现多个时间段流信息，如： ``` \"video_bitrate\": [     {       \"start_time\": \"2022-02-04T07:00:00Z\",       \"end_time\": \"2022-02-04T07:00:02Z\",       \"data_list\": [         1326,         1268,         775       ]     },     {       \"start_time\": \"2022-02-04T07:00:05Z\",       \"end_time\": \"2022-02-04T07:00:07Z\",       \"data_list\": [         1021,         2022       ]     }   ] 

        :return: The video_bitrate of this ListSingleStreamDetailResponse.
        :rtype: list[:class:`huaweicloudsdklive.v2.StreamDetail`]
        """
        return self._video_bitrate

    @video_bitrate.setter
    def video_bitrate(self, video_bitrate):
        r"""Sets the video_bitrate of this ListSingleStreamDetailResponse.

        展示流视频码率情况，码率单位为Kbps。  如果出现断流则会出现多个时间段流信息，如： ``` \"video_bitrate\": [     {       \"start_time\": \"2022-02-04T07:00:00Z\",       \"end_time\": \"2022-02-04T07:00:02Z\",       \"data_list\": [         1326,         1268,         775       ]     },     {       \"start_time\": \"2022-02-04T07:00:05Z\",       \"end_time\": \"2022-02-04T07:00:07Z\",       \"data_list\": [         1021,         2022       ]     }   ] 

        :param video_bitrate: The video_bitrate of this ListSingleStreamDetailResponse.
        :type video_bitrate: list[:class:`huaweicloudsdklive.v2.StreamDetail`]
        """
        self._video_bitrate = video_bitrate

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListSingleStreamDetailResponse.

        :return: The x_request_id of this ListSingleStreamDetailResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListSingleStreamDetailResponse.

        :param x_request_id: The x_request_id of this ListSingleStreamDetailResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListSingleStreamDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
