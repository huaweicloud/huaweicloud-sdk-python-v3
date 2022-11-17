# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAssetDetailResponse(SdkResponse):

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
        'base_info': 'BaseInfo',
        'transcode_info': 'TranscodeInfo',
        'thumbnail_info': 'ThumbnailInfo',
        'review_info': 'ReviewInfo'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'base_info': 'base_info',
        'transcode_info': 'transcode_info',
        'thumbnail_info': 'thumbnail_info',
        'review_info': 'review_info'
    }

    def __init__(self, asset_id=None, base_info=None, transcode_info=None, thumbnail_info=None, review_info=None):
        """ShowAssetDetailResponse

        The model defined in huaweicloud sdk

        :param asset_id: 媒资ID。
        :type asset_id: str
        :param base_info: 
        :type base_info: :class:`huaweicloudsdkvod.v1.BaseInfo`
        :param transcode_info: 
        :type transcode_info: :class:`huaweicloudsdkvod.v1.TranscodeInfo`
        :param thumbnail_info: 
        :type thumbnail_info: :class:`huaweicloudsdkvod.v1.ThumbnailInfo`
        :param review_info: 
        :type review_info: :class:`huaweicloudsdkvod.v1.ReviewInfo`
        """
        
        super(ShowAssetDetailResponse, self).__init__()

        self._asset_id = None
        self._base_info = None
        self._transcode_info = None
        self._thumbnail_info = None
        self._review_info = None
        self.discriminator = None

        if asset_id is not None:
            self.asset_id = asset_id
        if base_info is not None:
            self.base_info = base_info
        if transcode_info is not None:
            self.transcode_info = transcode_info
        if thumbnail_info is not None:
            self.thumbnail_info = thumbnail_info
        if review_info is not None:
            self.review_info = review_info

    @property
    def asset_id(self):
        """Gets the asset_id of this ShowAssetDetailResponse.

        媒资ID。

        :return: The asset_id of this ShowAssetDetailResponse.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this ShowAssetDetailResponse.

        媒资ID。

        :param asset_id: The asset_id of this ShowAssetDetailResponse.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def base_info(self):
        """Gets the base_info of this ShowAssetDetailResponse.

        :return: The base_info of this ShowAssetDetailResponse.
        :rtype: :class:`huaweicloudsdkvod.v1.BaseInfo`
        """
        return self._base_info

    @base_info.setter
    def base_info(self, base_info):
        """Sets the base_info of this ShowAssetDetailResponse.

        :param base_info: The base_info of this ShowAssetDetailResponse.
        :type base_info: :class:`huaweicloudsdkvod.v1.BaseInfo`
        """
        self._base_info = base_info

    @property
    def transcode_info(self):
        """Gets the transcode_info of this ShowAssetDetailResponse.

        :return: The transcode_info of this ShowAssetDetailResponse.
        :rtype: :class:`huaweicloudsdkvod.v1.TranscodeInfo`
        """
        return self._transcode_info

    @transcode_info.setter
    def transcode_info(self, transcode_info):
        """Sets the transcode_info of this ShowAssetDetailResponse.

        :param transcode_info: The transcode_info of this ShowAssetDetailResponse.
        :type transcode_info: :class:`huaweicloudsdkvod.v1.TranscodeInfo`
        """
        self._transcode_info = transcode_info

    @property
    def thumbnail_info(self):
        """Gets the thumbnail_info of this ShowAssetDetailResponse.

        :return: The thumbnail_info of this ShowAssetDetailResponse.
        :rtype: :class:`huaweicloudsdkvod.v1.ThumbnailInfo`
        """
        return self._thumbnail_info

    @thumbnail_info.setter
    def thumbnail_info(self, thumbnail_info):
        """Sets the thumbnail_info of this ShowAssetDetailResponse.

        :param thumbnail_info: The thumbnail_info of this ShowAssetDetailResponse.
        :type thumbnail_info: :class:`huaweicloudsdkvod.v1.ThumbnailInfo`
        """
        self._thumbnail_info = thumbnail_info

    @property
    def review_info(self):
        """Gets the review_info of this ShowAssetDetailResponse.

        :return: The review_info of this ShowAssetDetailResponse.
        :rtype: :class:`huaweicloudsdkvod.v1.ReviewInfo`
        """
        return self._review_info

    @review_info.setter
    def review_info(self, review_info):
        """Sets the review_info of this ShowAssetDetailResponse.

        :param review_info: The review_info of this ShowAssetDetailResponse.
        :type review_info: :class:`huaweicloudsdkvod.v1.ReviewInfo`
        """
        self._review_info = review_info

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
        if not isinstance(other, ShowAssetDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
