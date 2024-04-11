# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BrowserCacheRules:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'condition': 'BrowserCacheRulesCondition',
        'cache_type': 'str',
        'ttl': 'int',
        'ttl_unit': 'str'
    }

    attribute_map = {
        'condition': 'condition',
        'cache_type': 'cache_type',
        'ttl': 'ttl',
        'ttl_unit': 'ttl_unit'
    }

    def __init__(self, condition=None, cache_type=None, ttl=None, ttl_unit=None):
        """BrowserCacheRules

        The model defined in huaweicloud sdk

        :param condition: 
        :type condition: :class:`huaweicloudsdkcdn.v2.BrowserCacheRulesCondition`
        :param cache_type: 缓存生效类型：   - follow_origin：遵循源站的缓存策略，即Cache-Control头部的设置，   - ttl：浏览器缓存遵循当前规则设置的过期时间，   - never：浏览器不缓存资源。
        :type cache_type: str
        :param ttl: 缓存过期时间，最大支持365天。   &gt; 当缓存生效类型为ttl时必填。
        :type ttl: int
        :param ttl_unit: 缓存过期时间单位，s：秒；m：分种；h：小时；d：天。   &gt; 当缓存生效类型为ttl时必填。
        :type ttl_unit: str
        """
        
        

        self._condition = None
        self._cache_type = None
        self._ttl = None
        self._ttl_unit = None
        self.discriminator = None

        self.condition = condition
        self.cache_type = cache_type
        if ttl is not None:
            self.ttl = ttl
        if ttl_unit is not None:
            self.ttl_unit = ttl_unit

    @property
    def condition(self):
        """Gets the condition of this BrowserCacheRules.

        :return: The condition of this BrowserCacheRules.
        :rtype: :class:`huaweicloudsdkcdn.v2.BrowserCacheRulesCondition`
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this BrowserCacheRules.

        :param condition: The condition of this BrowserCacheRules.
        :type condition: :class:`huaweicloudsdkcdn.v2.BrowserCacheRulesCondition`
        """
        self._condition = condition

    @property
    def cache_type(self):
        """Gets the cache_type of this BrowserCacheRules.

        缓存生效类型：   - follow_origin：遵循源站的缓存策略，即Cache-Control头部的设置，   - ttl：浏览器缓存遵循当前规则设置的过期时间，   - never：浏览器不缓存资源。

        :return: The cache_type of this BrowserCacheRules.
        :rtype: str
        """
        return self._cache_type

    @cache_type.setter
    def cache_type(self, cache_type):
        """Sets the cache_type of this BrowserCacheRules.

        缓存生效类型：   - follow_origin：遵循源站的缓存策略，即Cache-Control头部的设置，   - ttl：浏览器缓存遵循当前规则设置的过期时间，   - never：浏览器不缓存资源。

        :param cache_type: The cache_type of this BrowserCacheRules.
        :type cache_type: str
        """
        self._cache_type = cache_type

    @property
    def ttl(self):
        """Gets the ttl of this BrowserCacheRules.

        缓存过期时间，最大支持365天。   > 当缓存生效类型为ttl时必填。

        :return: The ttl of this BrowserCacheRules.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this BrowserCacheRules.

        缓存过期时间，最大支持365天。   > 当缓存生效类型为ttl时必填。

        :param ttl: The ttl of this BrowserCacheRules.
        :type ttl: int
        """
        self._ttl = ttl

    @property
    def ttl_unit(self):
        """Gets the ttl_unit of this BrowserCacheRules.

        缓存过期时间单位，s：秒；m：分种；h：小时；d：天。   > 当缓存生效类型为ttl时必填。

        :return: The ttl_unit of this BrowserCacheRules.
        :rtype: str
        """
        return self._ttl_unit

    @ttl_unit.setter
    def ttl_unit(self, ttl_unit):
        """Sets the ttl_unit of this BrowserCacheRules.

        缓存过期时间单位，s：秒；m：分种；h：小时；d：天。   > 当缓存生效类型为ttl时必填。

        :param ttl_unit: The ttl_unit of this BrowserCacheRules.
        :type ttl_unit: str
        """
        self._ttl_unit = ttl_unit

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
        if not isinstance(other, BrowserCacheRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
