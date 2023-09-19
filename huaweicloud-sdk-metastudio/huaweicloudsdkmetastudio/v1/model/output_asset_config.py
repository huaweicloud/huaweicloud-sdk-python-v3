# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OutputAssetConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_name': 'str',
        'is_preview_video': 'bool'
    }

    attribute_map = {
        'asset_name': 'asset_name',
        'is_preview_video': 'is_preview_video'
    }

    def __init__(self, asset_name=None, is_preview_video=None):
        """OutputAssetConfig

        The model defined in huaweicloud sdk

        :param asset_name: 输出视频资产名称。
        :type asset_name: str
        :param is_preview_video: 是否是预览视频。如果是预览视频不存资产库。 &gt; * 分身数字人视频制作不支持预览。
        :type is_preview_video: bool
        """
        
        

        self._asset_name = None
        self._is_preview_video = None
        self.discriminator = None

        self.asset_name = asset_name
        if is_preview_video is not None:
            self.is_preview_video = is_preview_video

    @property
    def asset_name(self):
        """Gets the asset_name of this OutputAssetConfig.

        输出视频资产名称。

        :return: The asset_name of this OutputAssetConfig.
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        """Sets the asset_name of this OutputAssetConfig.

        输出视频资产名称。

        :param asset_name: The asset_name of this OutputAssetConfig.
        :type asset_name: str
        """
        self._asset_name = asset_name

    @property
    def is_preview_video(self):
        """Gets the is_preview_video of this OutputAssetConfig.

        是否是预览视频。如果是预览视频不存资产库。 > * 分身数字人视频制作不支持预览。

        :return: The is_preview_video of this OutputAssetConfig.
        :rtype: bool
        """
        return self._is_preview_video

    @is_preview_video.setter
    def is_preview_video(self, is_preview_video):
        """Sets the is_preview_video of this OutputAssetConfig.

        是否是预览视频。如果是预览视频不存资产库。 > * 分身数字人视频制作不支持预览。

        :param is_preview_video: The is_preview_video of this OutputAssetConfig.
        :type is_preview_video: bool
        """
        self._is_preview_video = is_preview_video

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
        if not isinstance(other, OutputAssetConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
