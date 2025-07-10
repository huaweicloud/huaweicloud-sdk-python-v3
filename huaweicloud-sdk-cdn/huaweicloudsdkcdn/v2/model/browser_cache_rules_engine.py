# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BrowserCacheRulesEngine:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cache_type': 'str',
        'ttl': 'int',
        'ttl_unit': 'str'
    }

    attribute_map = {
        'cache_type': 'cache_type',
        'ttl': 'ttl',
        'ttl_unit': 'ttl_unit'
    }

    def __init__(self, cache_type=None, ttl=None, ttl_unit=None):
        r"""BrowserCacheRulesEngine

        The model defined in huaweicloud sdk

        :param cache_type: **参数解释：** 缓存生效类型 **约束限制：** 不涉及 **取值范围：** - follow_origin: 遵循源站的缓存策略，即Cache-Control头部的设置 - ttl: 浏览器缓存遵循当前规则设置的过期时间 - never: 浏览器不缓存资源 **默认取值：** 不涉及
        :type cache_type: str
        :param ttl: **参数解释：** 缓存过期时间 **约束限制：** - 最大支持365天 - 当缓存生效类型为ttl时必填 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type ttl: int
        :param ttl_unit: **参数解释：** 缓存过期时间单位 **约束限制：** 当缓存生效类型为ttl时必填 **取值范围：** - s：秒 - m：分种 - h：小时 - d：天 **默认取值：** 不涉及
        :type ttl_unit: str
        """
        
        

        self._cache_type = None
        self._ttl = None
        self._ttl_unit = None
        self.discriminator = None

        self.cache_type = cache_type
        if ttl is not None:
            self.ttl = ttl
        if ttl_unit is not None:
            self.ttl_unit = ttl_unit

    @property
    def cache_type(self):
        r"""Gets the cache_type of this BrowserCacheRulesEngine.

        **参数解释：** 缓存生效类型 **约束限制：** 不涉及 **取值范围：** - follow_origin: 遵循源站的缓存策略，即Cache-Control头部的设置 - ttl: 浏览器缓存遵循当前规则设置的过期时间 - never: 浏览器不缓存资源 **默认取值：** 不涉及

        :return: The cache_type of this BrowserCacheRulesEngine.
        :rtype: str
        """
        return self._cache_type

    @cache_type.setter
    def cache_type(self, cache_type):
        r"""Sets the cache_type of this BrowserCacheRulesEngine.

        **参数解释：** 缓存生效类型 **约束限制：** 不涉及 **取值范围：** - follow_origin: 遵循源站的缓存策略，即Cache-Control头部的设置 - ttl: 浏览器缓存遵循当前规则设置的过期时间 - never: 浏览器不缓存资源 **默认取值：** 不涉及

        :param cache_type: The cache_type of this BrowserCacheRulesEngine.
        :type cache_type: str
        """
        self._cache_type = cache_type

    @property
    def ttl(self):
        r"""Gets the ttl of this BrowserCacheRulesEngine.

        **参数解释：** 缓存过期时间 **约束限制：** - 最大支持365天 - 当缓存生效类型为ttl时必填 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The ttl of this BrowserCacheRulesEngine.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        r"""Sets the ttl of this BrowserCacheRulesEngine.

        **参数解释：** 缓存过期时间 **约束限制：** - 最大支持365天 - 当缓存生效类型为ttl时必填 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param ttl: The ttl of this BrowserCacheRulesEngine.
        :type ttl: int
        """
        self._ttl = ttl

    @property
    def ttl_unit(self):
        r"""Gets the ttl_unit of this BrowserCacheRulesEngine.

        **参数解释：** 缓存过期时间单位 **约束限制：** 当缓存生效类型为ttl时必填 **取值范围：** - s：秒 - m：分种 - h：小时 - d：天 **默认取值：** 不涉及

        :return: The ttl_unit of this BrowserCacheRulesEngine.
        :rtype: str
        """
        return self._ttl_unit

    @ttl_unit.setter
    def ttl_unit(self, ttl_unit):
        r"""Sets the ttl_unit of this BrowserCacheRulesEngine.

        **参数解释：** 缓存过期时间单位 **约束限制：** 当缓存生效类型为ttl时必填 **取值范围：** - s：秒 - m：分种 - h：小时 - d：天 **默认取值：** 不涉及

        :param ttl_unit: The ttl_unit of this BrowserCacheRulesEngine.
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
        if not isinstance(other, BrowserCacheRulesEngine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
