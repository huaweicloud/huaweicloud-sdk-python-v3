# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecordDownloadUrlDO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'token': 'str',
        'file_type': 'str',
        'url': 'str'
    }

    attribute_map = {
        'token': 'token',
        'file_type': 'fileType',
        'url': 'url'
    }

    def __init__(self, token=None, file_type=None, url=None):
        r"""RecordDownloadUrlDO

        The model defined in huaweicloud sdk

        :param token: 下载鉴权token，下载文件时，使用该token鉴权。（一小时内有效，使用后立即失效）。
        :type token: str
        :param file_type: 文件类型。 * Aux：辅流（会议中的共享画面；分辨率为720p） * Hd：高清（会议中的视频画面；分辨率和会议中视频画面的分辨率一致，1080p或者720p） * Sd：标清（会议中视频画面和共享画面的合成画面，视频画面是大画面，共享画面是小画面，共享画面布局在右下方；分辨率为4CIF） &gt; 单个MP4文件大小不超过1GB。 
        :type file_type: str
        :param url: 文件下载url，最大1000个字符。
        :type url: str
        """
        
        

        self._token = None
        self._file_type = None
        self._url = None
        self.discriminator = None

        if token is not None:
            self.token = token
        if file_type is not None:
            self.file_type = file_type
        if url is not None:
            self.url = url

    @property
    def token(self):
        r"""Gets the token of this RecordDownloadUrlDO.

        下载鉴权token，下载文件时，使用该token鉴权。（一小时内有效，使用后立即失效）。

        :return: The token of this RecordDownloadUrlDO.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        r"""Sets the token of this RecordDownloadUrlDO.

        下载鉴权token，下载文件时，使用该token鉴权。（一小时内有效，使用后立即失效）。

        :param token: The token of this RecordDownloadUrlDO.
        :type token: str
        """
        self._token = token

    @property
    def file_type(self):
        r"""Gets the file_type of this RecordDownloadUrlDO.

        文件类型。 * Aux：辅流（会议中的共享画面；分辨率为720p） * Hd：高清（会议中的视频画面；分辨率和会议中视频画面的分辨率一致，1080p或者720p） * Sd：标清（会议中视频画面和共享画面的合成画面，视频画面是大画面，共享画面是小画面，共享画面布局在右下方；分辨率为4CIF） > 单个MP4文件大小不超过1GB。 

        :return: The file_type of this RecordDownloadUrlDO.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this RecordDownloadUrlDO.

        文件类型。 * Aux：辅流（会议中的共享画面；分辨率为720p） * Hd：高清（会议中的视频画面；分辨率和会议中视频画面的分辨率一致，1080p或者720p） * Sd：标清（会议中视频画面和共享画面的合成画面，视频画面是大画面，共享画面是小画面，共享画面布局在右下方；分辨率为4CIF） > 单个MP4文件大小不超过1GB。 

        :param file_type: The file_type of this RecordDownloadUrlDO.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def url(self):
        r"""Gets the url of this RecordDownloadUrlDO.

        文件下载url，最大1000个字符。

        :return: The url of this RecordDownloadUrlDO.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this RecordDownloadUrlDO.

        文件下载url，最大1000个字符。

        :param url: The url of this RecordDownloadUrlDO.
        :type url: str
        """
        self._url = url

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
        if not isinstance(other, RecordDownloadUrlDO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
