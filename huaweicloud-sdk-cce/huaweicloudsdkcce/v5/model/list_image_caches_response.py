# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImageCachesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_caches': 'list[ImageCacheDetail]'
    }

    attribute_map = {
        'image_caches': 'image_caches'
    }

    def __init__(self, image_caches=None):
        r"""ListImageCachesResponse

        The model defined in huaweicloud sdk

        :param image_caches: 镜像缓存列表。
        :type image_caches: list[:class:`huaweicloudsdkcce.v5.ImageCacheDetail`]
        """
        
        super(ListImageCachesResponse, self).__init__()

        self._image_caches = None
        self.discriminator = None

        if image_caches is not None:
            self.image_caches = image_caches

    @property
    def image_caches(self):
        r"""Gets the image_caches of this ListImageCachesResponse.

        镜像缓存列表。

        :return: The image_caches of this ListImageCachesResponse.
        :rtype: list[:class:`huaweicloudsdkcce.v5.ImageCacheDetail`]
        """
        return self._image_caches

    @image_caches.setter
    def image_caches(self, image_caches):
        r"""Sets the image_caches of this ListImageCachesResponse.

        镜像缓存列表。

        :param image_caches: The image_caches of this ListImageCachesResponse.
        :type image_caches: list[:class:`huaweicloudsdkcce.v5.ImageCacheDetail`]
        """
        self._image_caches = image_caches

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
        if not isinstance(other, ListImageCachesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
