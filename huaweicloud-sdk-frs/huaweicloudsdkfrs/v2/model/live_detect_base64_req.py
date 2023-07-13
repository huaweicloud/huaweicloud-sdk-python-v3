# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LiveDetectBase64Req:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'video_base64': 'str',
        'actions': 'str',
        'action_time': 'str',
        'nod_threshold': 'float'
    }

    attribute_map = {
        'video_base64': 'video_base64',
        'actions': 'actions',
        'action_time': 'action_time',
        'nod_threshold': 'nod_threshold'
    }

    def __init__(self, video_base64=None, actions=None, action_time=None, nod_threshold=None):
        """LiveDetectBase64Req

        The model defined in huaweicloud sdk

        :param video_base64: 视频数据，Base64编码，要求： • Base64编码后大小不超过8MB，建议客户端压缩到200KB~2MB。 • 限制视频时长1～15秒。 • 建议帧率10fps～30fps。 • 封装格式：mp4、avi、flv、webm、asf、mov。 • 视频编码格式： h261、h263、h264、hevc、vc1、vp8、vp9、wmv3。
        :type video_base64: str
        :param actions: 动作代码顺序列表，英文逗号（,）分隔。建议单动作，目前支持的动作有： • 1：左摇头 • 2：右摇头 • 3：点头 • 4：嘴部动作
        :type actions: str
        :param action_time: 该参数为动作时间数组拼接的字符串，数组的长度和actions的数量一致，每一项代表了对应次序动作的起始时间和结束时间，单位为距视频开始的毫秒数。
        :type action_time: str
        :param nod_threshold: 该参数为点头动作幅度的判断门限，取值范围：[1,90]，默认为10，单位为度。该值设置越大，则越难判断为点头。
        :type nod_threshold: float
        """
        
        

        self._video_base64 = None
        self._actions = None
        self._action_time = None
        self._nod_threshold = None
        self.discriminator = None

        self.video_base64 = video_base64
        self.actions = actions
        if action_time is not None:
            self.action_time = action_time
        if nod_threshold is not None:
            self.nod_threshold = nod_threshold

    @property
    def video_base64(self):
        """Gets the video_base64 of this LiveDetectBase64Req.

        视频数据，Base64编码，要求： • Base64编码后大小不超过8MB，建议客户端压缩到200KB~2MB。 • 限制视频时长1～15秒。 • 建议帧率10fps～30fps。 • 封装格式：mp4、avi、flv、webm、asf、mov。 • 视频编码格式： h261、h263、h264、hevc、vc1、vp8、vp9、wmv3。

        :return: The video_base64 of this LiveDetectBase64Req.
        :rtype: str
        """
        return self._video_base64

    @video_base64.setter
    def video_base64(self, video_base64):
        """Sets the video_base64 of this LiveDetectBase64Req.

        视频数据，Base64编码，要求： • Base64编码后大小不超过8MB，建议客户端压缩到200KB~2MB。 • 限制视频时长1～15秒。 • 建议帧率10fps～30fps。 • 封装格式：mp4、avi、flv、webm、asf、mov。 • 视频编码格式： h261、h263、h264、hevc、vc1、vp8、vp9、wmv3。

        :param video_base64: The video_base64 of this LiveDetectBase64Req.
        :type video_base64: str
        """
        self._video_base64 = video_base64

    @property
    def actions(self):
        """Gets the actions of this LiveDetectBase64Req.

        动作代码顺序列表，英文逗号（,）分隔。建议单动作，目前支持的动作有： • 1：左摇头 • 2：右摇头 • 3：点头 • 4：嘴部动作

        :return: The actions of this LiveDetectBase64Req.
        :rtype: str
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this LiveDetectBase64Req.

        动作代码顺序列表，英文逗号（,）分隔。建议单动作，目前支持的动作有： • 1：左摇头 • 2：右摇头 • 3：点头 • 4：嘴部动作

        :param actions: The actions of this LiveDetectBase64Req.
        :type actions: str
        """
        self._actions = actions

    @property
    def action_time(self):
        """Gets the action_time of this LiveDetectBase64Req.

        该参数为动作时间数组拼接的字符串，数组的长度和actions的数量一致，每一项代表了对应次序动作的起始时间和结束时间，单位为距视频开始的毫秒数。

        :return: The action_time of this LiveDetectBase64Req.
        :rtype: str
        """
        return self._action_time

    @action_time.setter
    def action_time(self, action_time):
        """Sets the action_time of this LiveDetectBase64Req.

        该参数为动作时间数组拼接的字符串，数组的长度和actions的数量一致，每一项代表了对应次序动作的起始时间和结束时间，单位为距视频开始的毫秒数。

        :param action_time: The action_time of this LiveDetectBase64Req.
        :type action_time: str
        """
        self._action_time = action_time

    @property
    def nod_threshold(self):
        """Gets the nod_threshold of this LiveDetectBase64Req.

        该参数为点头动作幅度的判断门限，取值范围：[1,90]，默认为10，单位为度。该值设置越大，则越难判断为点头。

        :return: The nod_threshold of this LiveDetectBase64Req.
        :rtype: float
        """
        return self._nod_threshold

    @nod_threshold.setter
    def nod_threshold(self, nod_threshold):
        """Sets the nod_threshold of this LiveDetectBase64Req.

        该参数为点头动作幅度的判断门限，取值范围：[1,90]，默认为10，单位为度。该值设置越大，则越难判断为点头。

        :param nod_threshold: The nod_threshold of this LiveDetectBase64Req.
        :type nod_threshold: float
        """
        self._nod_threshold = nod_threshold

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
        if not isinstance(other, LiveDetectBase64Req):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
