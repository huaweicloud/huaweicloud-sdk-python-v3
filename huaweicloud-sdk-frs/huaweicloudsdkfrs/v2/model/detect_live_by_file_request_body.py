# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DetectLiveByFileRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'video_file': 'file',
        'actions': 'str',
        'action_time': 'str'
    }

    attribute_map = {
        'video_file': 'video_file',
        'actions': 'actions',
        'action_time': 'action_time'
    }

    def __init__(self, video_file=None, actions=None, action_time=None):
        """DetectLiveByFileRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._video_file = None
        self._actions = None
        self._action_time = None
        self.discriminator = None

        self.video_file = video_file
        self.actions = actions
        if action_time is not None:
            self.action_time = action_time

    @property
    def video_file(self):
        """Gets the video_file of this DetectLiveByFileRequestBody.

        本地视频文件。上传文件时，请求格式为multipart。 视频要求： • 视频文件大小不超过8MB，建议客户端压缩到200KB~2MB。 • 限制视频时长1～15秒。 • 建议帧率10fps～30fps。 • 封装格式：mp4、avi、flv、webm、asf、mov。 • 视频编码格式： h261、h263、h264、hevc、vc1、vp8、vp9、wmv3。

        :return: The video_file of this DetectLiveByFileRequestBody.
        :rtype: file
        """
        return self._video_file

    @video_file.setter
    def video_file(self, video_file):
        """Sets the video_file of this DetectLiveByFileRequestBody.

        本地视频文件。上传文件时，请求格式为multipart。 视频要求： • 视频文件大小不超过8MB，建议客户端压缩到200KB~2MB。 • 限制视频时长1～15秒。 • 建议帧率10fps～30fps。 • 封装格式：mp4、avi、flv、webm、asf、mov。 • 视频编码格式： h261、h263、h264、hevc、vc1、vp8、vp9、wmv3。

        :param video_file: The video_file of this DetectLiveByFileRequestBody.
        :type: file
        """
        self._video_file = video_file

    @property
    def actions(self):
        """Gets the actions of this DetectLiveByFileRequestBody.

        动作代码顺序列表，英文逗号（,）分隔。建议单动作，目前支持的动作有： • 1：左摇头 • 2：右摇头 • 3：点头 • 4：嘴部动作

        :return: The actions of this DetectLiveByFileRequestBody.
        :rtype: str
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this DetectLiveByFileRequestBody.

        动作代码顺序列表，英文逗号（,）分隔。建议单动作，目前支持的动作有： • 1：左摇头 • 2：右摇头 • 3：点头 • 4：嘴部动作

        :param actions: The actions of this DetectLiveByFileRequestBody.
        :type: str
        """
        self._actions = actions

    @property
    def action_time(self):
        """Gets the action_time of this DetectLiveByFileRequestBody.

        该参数为动作时间数组拼接的字符串，数组的长度和actions的数量一致，每一项代表了对应次序动作的起始时间和结束时间，单位为距视频开始的毫秒数。

        :return: The action_time of this DetectLiveByFileRequestBody.
        :rtype: str
        """
        return self._action_time

    @action_time.setter
    def action_time(self, action_time):
        """Sets the action_time of this DetectLiveByFileRequestBody.

        该参数为动作时间数组拼接的字符串，数组的长度和actions的数量一致，每一项代表了对应次序动作的起始时间和结束时间，单位为距视频开始的毫秒数。

        :param action_time: The action_time of this DetectLiveByFileRequestBody.
        :type: str
        """
        self._action_time = action_time

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
        if not isinstance(other, DetectLiveByFileRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other