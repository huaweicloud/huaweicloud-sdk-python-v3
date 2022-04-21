# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAssetResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'asset_id': 'str',
        'video_upload_url': 'str',
        'cover_upload_url': 'str',
        'subtitle_upload_urls': 'list[str]'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'video_upload_url': 'video_upload_url',
        'cover_upload_url': 'cover_upload_url',
        'subtitle_upload_urls': 'subtitle_upload_urls'
    }

    def __init__(self, asset_id=None, video_upload_url=None, cover_upload_url=None, subtitle_upload_urls=None):
        """UpdateAssetResponse

        The model defined in huaweicloud sdk

        :param asset_id: 媒资ID。
        :type asset_id: str
        :param video_upload_url: 视频上传地址。  用于客户端上传不超过20MB的小视频文件（&lt;&#x3D;20MB）。该URL中携带了临时授权信息，当文件大于20MB时，需要采用分段方式上传。  &gt; 您可以使用PUT请求向“**video_upload_url**”中上传视频文件。其中，“**Content-Type**”需要根据上传的视频文件类型进行设置，如下所示：视频文件：video/视频格式，如：“video/mp4”。
        :type video_upload_url: str
        :param cover_upload_url: 封面上传地址，用于上传封面文件。  &gt; 您可以使用PUT请求向“**cover_upload_url**”中上传封面图片。其中，“**Content-Type**”需要根据上传的封面文件类型进行设置，如下所示：图片文件：image/图片格式，如：“image/png”。
        :type cover_upload_url: str
        :param subtitle_upload_urls: 字幕上传地址，用于上传字幕。  &gt; 您可以使用PUT请求向“**subtitle_upload_urls**”中上传字幕文件。其中，“**Content-Type**”需要根据上传的字幕文件类型进行设置，如下所示：字幕文件：application/octet-stream。
        :type subtitle_upload_urls: list[str]
        """
        
        super(UpdateAssetResponse, self).__init__()

        self._asset_id = None
        self._video_upload_url = None
        self._cover_upload_url = None
        self._subtitle_upload_urls = None
        self.discriminator = None

        if asset_id is not None:
            self.asset_id = asset_id
        if video_upload_url is not None:
            self.video_upload_url = video_upload_url
        if cover_upload_url is not None:
            self.cover_upload_url = cover_upload_url
        if subtitle_upload_urls is not None:
            self.subtitle_upload_urls = subtitle_upload_urls

    @property
    def asset_id(self):
        """Gets the asset_id of this UpdateAssetResponse.

        媒资ID。

        :return: The asset_id of this UpdateAssetResponse.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this UpdateAssetResponse.

        媒资ID。

        :param asset_id: The asset_id of this UpdateAssetResponse.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def video_upload_url(self):
        """Gets the video_upload_url of this UpdateAssetResponse.

        视频上传地址。  用于客户端上传不超过20MB的小视频文件（<=20MB）。该URL中携带了临时授权信息，当文件大于20MB时，需要采用分段方式上传。  > 您可以使用PUT请求向“**video_upload_url**”中上传视频文件。其中，“**Content-Type**”需要根据上传的视频文件类型进行设置，如下所示：视频文件：video/视频格式，如：“video/mp4”。

        :return: The video_upload_url of this UpdateAssetResponse.
        :rtype: str
        """
        return self._video_upload_url

    @video_upload_url.setter
    def video_upload_url(self, video_upload_url):
        """Sets the video_upload_url of this UpdateAssetResponse.

        视频上传地址。  用于客户端上传不超过20MB的小视频文件（<=20MB）。该URL中携带了临时授权信息，当文件大于20MB时，需要采用分段方式上传。  > 您可以使用PUT请求向“**video_upload_url**”中上传视频文件。其中，“**Content-Type**”需要根据上传的视频文件类型进行设置，如下所示：视频文件：video/视频格式，如：“video/mp4”。

        :param video_upload_url: The video_upload_url of this UpdateAssetResponse.
        :type video_upload_url: str
        """
        self._video_upload_url = video_upload_url

    @property
    def cover_upload_url(self):
        """Gets the cover_upload_url of this UpdateAssetResponse.

        封面上传地址，用于上传封面文件。  > 您可以使用PUT请求向“**cover_upload_url**”中上传封面图片。其中，“**Content-Type**”需要根据上传的封面文件类型进行设置，如下所示：图片文件：image/图片格式，如：“image/png”。

        :return: The cover_upload_url of this UpdateAssetResponse.
        :rtype: str
        """
        return self._cover_upload_url

    @cover_upload_url.setter
    def cover_upload_url(self, cover_upload_url):
        """Sets the cover_upload_url of this UpdateAssetResponse.

        封面上传地址，用于上传封面文件。  > 您可以使用PUT请求向“**cover_upload_url**”中上传封面图片。其中，“**Content-Type**”需要根据上传的封面文件类型进行设置，如下所示：图片文件：image/图片格式，如：“image/png”。

        :param cover_upload_url: The cover_upload_url of this UpdateAssetResponse.
        :type cover_upload_url: str
        """
        self._cover_upload_url = cover_upload_url

    @property
    def subtitle_upload_urls(self):
        """Gets the subtitle_upload_urls of this UpdateAssetResponse.

        字幕上传地址，用于上传字幕。  > 您可以使用PUT请求向“**subtitle_upload_urls**”中上传字幕文件。其中，“**Content-Type**”需要根据上传的字幕文件类型进行设置，如下所示：字幕文件：application/octet-stream。

        :return: The subtitle_upload_urls of this UpdateAssetResponse.
        :rtype: list[str]
        """
        return self._subtitle_upload_urls

    @subtitle_upload_urls.setter
    def subtitle_upload_urls(self, subtitle_upload_urls):
        """Sets the subtitle_upload_urls of this UpdateAssetResponse.

        字幕上传地址，用于上传字幕。  > 您可以使用PUT请求向“**subtitle_upload_urls**”中上传字幕文件。其中，“**Content-Type**”需要根据上传的字幕文件类型进行设置，如下所示：字幕文件：application/octet-stream。

        :param subtitle_upload_urls: The subtitle_upload_urls of this UpdateAssetResponse.
        :type subtitle_upload_urls: list[str]
        """
        self._subtitle_upload_urls = subtitle_upload_urls

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
        if not isinstance(other, UpdateAssetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
