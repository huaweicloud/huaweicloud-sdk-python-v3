# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoModerationResultRequestParamsData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'frame_interval': 'int'
    }

    attribute_map = {
        'url': 'url',
        'frame_interval': 'frame_interval'
    }

    def __init__(self, url=None, frame_interval=None):
        """VideoModerationResultRequestParamsData

        The model defined in huaweicloud sdk

        :param url: 创建作业时传的url参数
        :type url: str
        :param frame_interval: 创建作业时传的frame_interval参数，默认为5秒截取一帧
        :type frame_interval: int
        """
        
        

        self._url = None
        self._frame_interval = None
        self.discriminator = None

        self.url = url
        if frame_interval is not None:
            self.frame_interval = frame_interval

    @property
    def url(self):
        """Gets the url of this VideoModerationResultRequestParamsData.

        创建作业时传的url参数

        :return: The url of this VideoModerationResultRequestParamsData.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this VideoModerationResultRequestParamsData.

        创建作业时传的url参数

        :param url: The url of this VideoModerationResultRequestParamsData.
        :type url: str
        """
        self._url = url

    @property
    def frame_interval(self):
        """Gets the frame_interval of this VideoModerationResultRequestParamsData.

        创建作业时传的frame_interval参数，默认为5秒截取一帧

        :return: The frame_interval of this VideoModerationResultRequestParamsData.
        :rtype: int
        """
        return self._frame_interval

    @frame_interval.setter
    def frame_interval(self, frame_interval):
        """Sets the frame_interval of this VideoModerationResultRequestParamsData.

        创建作业时传的frame_interval参数，默认为5秒截取一帧

        :param frame_interval: The frame_interval of this VideoModerationResultRequestParamsData.
        :type frame_interval: int
        """
        self._frame_interval = frame_interval

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
        if not isinstance(other, VideoModerationResultRequestParamsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
