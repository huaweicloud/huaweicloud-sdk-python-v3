# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CacheConfigRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cache_config': 'CacheConfigRequest'
    }

    attribute_map = {
        'cache_config': 'cache_config'
    }

    def __init__(self, cache_config=None):
        r"""CacheConfigRequestBody

        The model defined in huaweicloud sdk

        :param cache_config: 
        :type cache_config: :class:`huaweicloudsdkcdn.v1.CacheConfigRequest`
        """
        
        

        self._cache_config = None
        self.discriminator = None

        self.cache_config = cache_config

    @property
    def cache_config(self):
        r"""Gets the cache_config of this CacheConfigRequestBody.

        :return: The cache_config of this CacheConfigRequestBody.
        :rtype: :class:`huaweicloudsdkcdn.v1.CacheConfigRequest`
        """
        return self._cache_config

    @cache_config.setter
    def cache_config(self, cache_config):
        r"""Sets the cache_config of this CacheConfigRequestBody.

        :param cache_config: The cache_config of this CacheConfigRequestBody.
        :type cache_config: :class:`huaweicloudsdkcdn.v1.CacheConfigRequest`
        """
        self._cache_config = cache_config

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
        if not isinstance(other, CacheConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
