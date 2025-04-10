# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCacheRulesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cache_config': 'CacheConfig',
        'x_request_id': 'str'
    }

    attribute_map = {
        'cache_config': 'cache_config',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, cache_config=None, x_request_id=None):
        r"""UpdateCacheRulesResponse

        The model defined in huaweicloud sdk

        :param cache_config: 
        :type cache_config: :class:`huaweicloudsdkcdn.v1.CacheConfig`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(UpdateCacheRulesResponse, self).__init__()

        self._cache_config = None
        self._x_request_id = None
        self.discriminator = None

        if cache_config is not None:
            self.cache_config = cache_config
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def cache_config(self):
        r"""Gets the cache_config of this UpdateCacheRulesResponse.

        :return: The cache_config of this UpdateCacheRulesResponse.
        :rtype: :class:`huaweicloudsdkcdn.v1.CacheConfig`
        """
        return self._cache_config

    @cache_config.setter
    def cache_config(self, cache_config):
        r"""Sets the cache_config of this UpdateCacheRulesResponse.

        :param cache_config: The cache_config of this UpdateCacheRulesResponse.
        :type cache_config: :class:`huaweicloudsdkcdn.v1.CacheConfig`
        """
        self._cache_config = cache_config

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this UpdateCacheRulesResponse.

        :return: The x_request_id of this UpdateCacheRulesResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this UpdateCacheRulesResponse.

        :param x_request_id: The x_request_id of this UpdateCacheRulesResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, UpdateCacheRulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
