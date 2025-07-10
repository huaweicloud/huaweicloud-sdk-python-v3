# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CacheRulesEngine:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ttl': 'int',
        'ttl_unit': 'str',
        'follow_origin': 'str',
        'force_cache': 'str'
    }

    attribute_map = {
        'ttl': 'ttl',
        'ttl_unit': 'ttl_unit',
        'follow_origin': 'follow_origin',
        'force_cache': 'force_cache'
    }

    def __init__(self, ttl=None, ttl_unit=None, follow_origin=None, force_cache=None):
        r"""CacheRulesEngine

        The model defined in huaweicloud sdk

        :param ttl: **参数解释：** 资源在CDN节点的缓存过期时间 **约束限制：** 最大支持365天 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type ttl: int
        :param ttl_unit: **参数解释：** 缓存过期时间单位 **约束限制：** 不涉及 **取值范围：** - s: 秒 - m: 分 - h: 小时 - d: 天 **默认取值：** 不涉及
        :type ttl_unit: str
        :param follow_origin: **参数解释：** 缓存过期时间来源，设置CDN节点的缓存遵循源站还是CDN侧的配置 **约束限制：** 不涉及 **取值范围：** - on: CDN节点的缓存过期时间遵循源站的设置 - off: CDN节点的缓存过期时间遵循“缓存规则”中的“缓存过期时间” - min_ttl: CDN节点的缓存过期时间取缓存规则和源站二者的最小值 **默认取值：** off: CDN节点的缓存过期时间遵循“缓存规则”中的“缓存过期时间”
        :type follow_origin: str
        :param force_cache: **参数解释：** 强制缓存：CDN节点缓存过期时间是否忽略源站响应头Cache-Control中的no-cache、private、no-store字段 **约束限制：** 强制缓存与缓存过期时间来源功能配合使用，具体使用限制及配置效果请参考CDN用户指南的配置节点缓存规则章节 **取值范围：** - on: 打开强制缓存 - off: 关闭强制缓存 **默认取值：** off: 关闭强制缓存
        :type force_cache: str
        """
        
        

        self._ttl = None
        self._ttl_unit = None
        self._follow_origin = None
        self._force_cache = None
        self.discriminator = None

        self.ttl = ttl
        self.ttl_unit = ttl_unit
        self.follow_origin = follow_origin
        if force_cache is not None:
            self.force_cache = force_cache

    @property
    def ttl(self):
        r"""Gets the ttl of this CacheRulesEngine.

        **参数解释：** 资源在CDN节点的缓存过期时间 **约束限制：** 最大支持365天 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The ttl of this CacheRulesEngine.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        r"""Sets the ttl of this CacheRulesEngine.

        **参数解释：** 资源在CDN节点的缓存过期时间 **约束限制：** 最大支持365天 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param ttl: The ttl of this CacheRulesEngine.
        :type ttl: int
        """
        self._ttl = ttl

    @property
    def ttl_unit(self):
        r"""Gets the ttl_unit of this CacheRulesEngine.

        **参数解释：** 缓存过期时间单位 **约束限制：** 不涉及 **取值范围：** - s: 秒 - m: 分 - h: 小时 - d: 天 **默认取值：** 不涉及

        :return: The ttl_unit of this CacheRulesEngine.
        :rtype: str
        """
        return self._ttl_unit

    @ttl_unit.setter
    def ttl_unit(self, ttl_unit):
        r"""Sets the ttl_unit of this CacheRulesEngine.

        **参数解释：** 缓存过期时间单位 **约束限制：** 不涉及 **取值范围：** - s: 秒 - m: 分 - h: 小时 - d: 天 **默认取值：** 不涉及

        :param ttl_unit: The ttl_unit of this CacheRulesEngine.
        :type ttl_unit: str
        """
        self._ttl_unit = ttl_unit

    @property
    def follow_origin(self):
        r"""Gets the follow_origin of this CacheRulesEngine.

        **参数解释：** 缓存过期时间来源，设置CDN节点的缓存遵循源站还是CDN侧的配置 **约束限制：** 不涉及 **取值范围：** - on: CDN节点的缓存过期时间遵循源站的设置 - off: CDN节点的缓存过期时间遵循“缓存规则”中的“缓存过期时间” - min_ttl: CDN节点的缓存过期时间取缓存规则和源站二者的最小值 **默认取值：** off: CDN节点的缓存过期时间遵循“缓存规则”中的“缓存过期时间”

        :return: The follow_origin of this CacheRulesEngine.
        :rtype: str
        """
        return self._follow_origin

    @follow_origin.setter
    def follow_origin(self, follow_origin):
        r"""Sets the follow_origin of this CacheRulesEngine.

        **参数解释：** 缓存过期时间来源，设置CDN节点的缓存遵循源站还是CDN侧的配置 **约束限制：** 不涉及 **取值范围：** - on: CDN节点的缓存过期时间遵循源站的设置 - off: CDN节点的缓存过期时间遵循“缓存规则”中的“缓存过期时间” - min_ttl: CDN节点的缓存过期时间取缓存规则和源站二者的最小值 **默认取值：** off: CDN节点的缓存过期时间遵循“缓存规则”中的“缓存过期时间”

        :param follow_origin: The follow_origin of this CacheRulesEngine.
        :type follow_origin: str
        """
        self._follow_origin = follow_origin

    @property
    def force_cache(self):
        r"""Gets the force_cache of this CacheRulesEngine.

        **参数解释：** 强制缓存：CDN节点缓存过期时间是否忽略源站响应头Cache-Control中的no-cache、private、no-store字段 **约束限制：** 强制缓存与缓存过期时间来源功能配合使用，具体使用限制及配置效果请参考CDN用户指南的配置节点缓存规则章节 **取值范围：** - on: 打开强制缓存 - off: 关闭强制缓存 **默认取值：** off: 关闭强制缓存

        :return: The force_cache of this CacheRulesEngine.
        :rtype: str
        """
        return self._force_cache

    @force_cache.setter
    def force_cache(self, force_cache):
        r"""Sets the force_cache of this CacheRulesEngine.

        **参数解释：** 强制缓存：CDN节点缓存过期时间是否忽略源站响应头Cache-Control中的no-cache、private、no-store字段 **约束限制：** 强制缓存与缓存过期时间来源功能配合使用，具体使用限制及配置效果请参考CDN用户指南的配置节点缓存规则章节 **取值范围：** - on: 打开强制缓存 - off: 关闭强制缓存 **默认取值：** off: 关闭强制缓存

        :param force_cache: The force_cache of this CacheRulesEngine.
        :type force_cache: str
        """
        self._force_cache = force_cache

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
        if not isinstance(other, CacheRulesEngine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
