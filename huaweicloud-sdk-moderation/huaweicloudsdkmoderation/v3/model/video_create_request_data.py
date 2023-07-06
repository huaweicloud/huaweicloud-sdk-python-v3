# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoCreateRequestData:

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
        'frame_interval': 'int',
        'language': 'str'
    }

    attribute_map = {
        'url': 'url',
        'frame_interval': 'frame_interval',
        'language': 'language'
    }

    def __init__(self, url=None, frame_interval=None, language=None):
        """VideoCreateRequestData

        The model defined in huaweicloud sdk

        :param url: 视频url地址
        :type url: str
        :param frame_interval: 截帧频率间隔，单位为秒，取值范围为1~60s；若不传递默认5s截帧一次
        :type frame_interval: int
        :param language: 支持的语言，默认为zh zh：中文
        :type language: str
        """
        
        

        self._url = None
        self._frame_interval = None
        self._language = None
        self.discriminator = None

        self.url = url
        if frame_interval is not None:
            self.frame_interval = frame_interval
        if language is not None:
            self.language = language

    @property
    def url(self):
        """Gets the url of this VideoCreateRequestData.

        视频url地址

        :return: The url of this VideoCreateRequestData.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this VideoCreateRequestData.

        视频url地址

        :param url: The url of this VideoCreateRequestData.
        :type url: str
        """
        self._url = url

    @property
    def frame_interval(self):
        """Gets the frame_interval of this VideoCreateRequestData.

        截帧频率间隔，单位为秒，取值范围为1~60s；若不传递默认5s截帧一次

        :return: The frame_interval of this VideoCreateRequestData.
        :rtype: int
        """
        return self._frame_interval

    @frame_interval.setter
    def frame_interval(self, frame_interval):
        """Sets the frame_interval of this VideoCreateRequestData.

        截帧频率间隔，单位为秒，取值范围为1~60s；若不传递默认5s截帧一次

        :param frame_interval: The frame_interval of this VideoCreateRequestData.
        :type frame_interval: int
        """
        self._frame_interval = frame_interval

    @property
    def language(self):
        """Gets the language of this VideoCreateRequestData.

        支持的语言，默认为zh zh：中文

        :return: The language of this VideoCreateRequestData.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this VideoCreateRequestData.

        支持的语言，默认为zh zh：中文

        :param language: The language of this VideoCreateRequestData.
        :type language: str
        """
        self._language = language

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
        if not isinstance(other, VideoCreateRequestData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
