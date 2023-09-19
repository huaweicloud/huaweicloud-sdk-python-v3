# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OutputAssetInfo:

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
        'asset_name': 'str',
        'cover_url': 'str',
        'preview_video_url': 'str'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'asset_name': 'asset_name',
        'cover_url': 'cover_url',
        'preview_video_url': 'preview_video_url'
    }

    def __init__(self, asset_id=None, asset_name=None, cover_url=None, preview_video_url=None):
        """OutputAssetInfo

        The model defined in huaweicloud sdk

        :param asset_id: 输出视频资产ID。
        :type asset_id: str
        :param asset_name: 输出视频资产名称。
        :type asset_name: str
        :param cover_url: 视频封面URL。
        :type cover_url: str
        :param preview_video_url: 预览视频下载URL。URL有效期24小时。 &gt; * 分数数字人视频制作不支持预览。
        :type preview_video_url: str
        """
        
        

        self._asset_id = None
        self._asset_name = None
        self._cover_url = None
        self._preview_video_url = None
        self.discriminator = None

        self.asset_id = asset_id
        self.asset_name = asset_name
        if cover_url is not None:
            self.cover_url = cover_url
        if preview_video_url is not None:
            self.preview_video_url = preview_video_url

    @property
    def asset_id(self):
        """Gets the asset_id of this OutputAssetInfo.

        输出视频资产ID。

        :return: The asset_id of this OutputAssetInfo.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this OutputAssetInfo.

        输出视频资产ID。

        :param asset_id: The asset_id of this OutputAssetInfo.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def asset_name(self):
        """Gets the asset_name of this OutputAssetInfo.

        输出视频资产名称。

        :return: The asset_name of this OutputAssetInfo.
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        """Sets the asset_name of this OutputAssetInfo.

        输出视频资产名称。

        :param asset_name: The asset_name of this OutputAssetInfo.
        :type asset_name: str
        """
        self._asset_name = asset_name

    @property
    def cover_url(self):
        """Gets the cover_url of this OutputAssetInfo.

        视频封面URL。

        :return: The cover_url of this OutputAssetInfo.
        :rtype: str
        """
        return self._cover_url

    @cover_url.setter
    def cover_url(self, cover_url):
        """Sets the cover_url of this OutputAssetInfo.

        视频封面URL。

        :param cover_url: The cover_url of this OutputAssetInfo.
        :type cover_url: str
        """
        self._cover_url = cover_url

    @property
    def preview_video_url(self):
        """Gets the preview_video_url of this OutputAssetInfo.

        预览视频下载URL。URL有效期24小时。 > * 分数数字人视频制作不支持预览。

        :return: The preview_video_url of this OutputAssetInfo.
        :rtype: str
        """
        return self._preview_video_url

    @preview_video_url.setter
    def preview_video_url(self, preview_video_url):
        """Sets the preview_video_url of this OutputAssetInfo.

        预览视频下载URL。URL有效期24小时。 > * 分数数字人视频制作不支持预览。

        :param preview_video_url: The preview_video_url of this OutputAssetInfo.
        :type preview_video_url: str
        """
        self._preview_video_url = preview_video_url

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
        if not isinstance(other, OutputAssetInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
