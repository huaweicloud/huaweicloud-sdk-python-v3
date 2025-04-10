# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateImageCacheResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_cache': 'ImageCacheDetail'
    }

    attribute_map = {
        'image_cache': 'image_cache'
    }

    def __init__(self, image_cache=None):
        r"""CreateImageCacheResponse

        The model defined in huaweicloud sdk

        :param image_cache: 
        :type image_cache: :class:`huaweicloudsdkcce.v5.ImageCacheDetail`
        """
        
        super(CreateImageCacheResponse, self).__init__()

        self._image_cache = None
        self.discriminator = None

        if image_cache is not None:
            self.image_cache = image_cache

    @property
    def image_cache(self):
        r"""Gets the image_cache of this CreateImageCacheResponse.

        :return: The image_cache of this CreateImageCacheResponse.
        :rtype: :class:`huaweicloudsdkcce.v5.ImageCacheDetail`
        """
        return self._image_cache

    @image_cache.setter
    def image_cache(self, image_cache):
        r"""Sets the image_cache of this CreateImageCacheResponse.

        :param image_cache: The image_cache of this CreateImageCacheResponse.
        :type image_cache: :class:`huaweicloudsdkcce.v5.ImageCacheDetail`
        """
        self._image_cache = image_cache

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
        if not isinstance(other, CreateImageCacheResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
