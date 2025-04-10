# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteImageCacheRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_cache_id': 'str'
    }

    attribute_map = {
        'image_cache_id': 'image_cache_id'
    }

    def __init__(self, image_cache_id=None):
        r"""DeleteImageCacheRequest

        The model defined in huaweicloud sdk

        :param image_cache_id: **参数解释：** 镜像缓存ID。 **约束限制：** 不涉及 **取值范围：** 镜像缓存ID。 **默认取值：** 不涉及 
        :type image_cache_id: str
        """
        
        

        self._image_cache_id = None
        self.discriminator = None

        self.image_cache_id = image_cache_id

    @property
    def image_cache_id(self):
        r"""Gets the image_cache_id of this DeleteImageCacheRequest.

        **参数解释：** 镜像缓存ID。 **约束限制：** 不涉及 **取值范围：** 镜像缓存ID。 **默认取值：** 不涉及 

        :return: The image_cache_id of this DeleteImageCacheRequest.
        :rtype: str
        """
        return self._image_cache_id

    @image_cache_id.setter
    def image_cache_id(self, image_cache_id):
        r"""Sets the image_cache_id of this DeleteImageCacheRequest.

        **参数解释：** 镜像缓存ID。 **约束限制：** 不涉及 **取值范围：** 镜像缓存ID。 **默认取值：** 不涉及 

        :param image_cache_id: The image_cache_id of this DeleteImageCacheRequest.
        :type image_cache_id: str
        """
        self._image_cache_id = image_cache_id

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
        if not isinstance(other, DeleteImageCacheRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
