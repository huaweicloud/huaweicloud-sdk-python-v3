# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductCoverDetailInfo:

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
        'cover_url': 'str',
        'thumbnail_url': 'str'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'cover_url': 'cover_url',
        'thumbnail_url': 'thumbnail_url'
    }

    def __init__(self, asset_id=None, cover_url=None, thumbnail_url=None):
        r"""ProductCoverDetailInfo

        The model defined in huaweicloud sdk

        :param asset_id: 资产ID
        :type asset_id: str
        :param cover_url: 封面图片路径。
        :type cover_url: str
        :param thumbnail_url: 缩略图路径。
        :type thumbnail_url: str
        """
        
        

        self._asset_id = None
        self._cover_url = None
        self._thumbnail_url = None
        self.discriminator = None

        if asset_id is not None:
            self.asset_id = asset_id
        if cover_url is not None:
            self.cover_url = cover_url
        if thumbnail_url is not None:
            self.thumbnail_url = thumbnail_url

    @property
    def asset_id(self):
        r"""Gets the asset_id of this ProductCoverDetailInfo.

        资产ID

        :return: The asset_id of this ProductCoverDetailInfo.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this ProductCoverDetailInfo.

        资产ID

        :param asset_id: The asset_id of this ProductCoverDetailInfo.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def cover_url(self):
        r"""Gets the cover_url of this ProductCoverDetailInfo.

        封面图片路径。

        :return: The cover_url of this ProductCoverDetailInfo.
        :rtype: str
        """
        return self._cover_url

    @cover_url.setter
    def cover_url(self, cover_url):
        r"""Sets the cover_url of this ProductCoverDetailInfo.

        封面图片路径。

        :param cover_url: The cover_url of this ProductCoverDetailInfo.
        :type cover_url: str
        """
        self._cover_url = cover_url

    @property
    def thumbnail_url(self):
        r"""Gets the thumbnail_url of this ProductCoverDetailInfo.

        缩略图路径。

        :return: The thumbnail_url of this ProductCoverDetailInfo.
        :rtype: str
        """
        return self._thumbnail_url

    @thumbnail_url.setter
    def thumbnail_url(self, thumbnail_url):
        r"""Sets the thumbnail_url of this ProductCoverDetailInfo.

        缩略图路径。

        :param thumbnail_url: The thumbnail_url of this ProductCoverDetailInfo.
        :type thumbnail_url: str
        """
        self._thumbnail_url = thumbnail_url

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
        if not isinstance(other, ProductCoverDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
