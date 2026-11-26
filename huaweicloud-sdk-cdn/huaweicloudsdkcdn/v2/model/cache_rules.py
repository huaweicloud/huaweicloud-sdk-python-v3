# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CacheRules:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'match_type': 'str',
        'match_value': 'str',
        'ttl': 'int',
        'ttl_unit': 'str',
        'priority': 'int',
        'follow_origin': 'str',
        'force_cache': 'str',
        'url_parameter_type': 'str',
        'url_parameter_value': 'str',
        'stale_while_revalidate': 'str'
    }

    attribute_map = {
        'match_type': 'match_type',
        'match_value': 'match_value',
        'ttl': 'ttl',
        'ttl_unit': 'ttl_unit',
        'priority': 'priority',
        'follow_origin': 'follow_origin',
        'force_cache': 'force_cache',
        'url_parameter_type': 'url_parameter_type',
        'url_parameter_value': 'url_parameter_value',
        'stale_while_revalidate': 'stale_while_revalidate'
    }

    def __init__(self, match_type=None, match_value=None, ttl=None, ttl_unit=None, priority=None, follow_origin=None, force_cache=None, url_parameter_type=None, url_parameter_value=None, stale_while_revalidate=None):
        r"""CacheRules

        The model defined in huaweicloud sdk

        :param match_type: **参数解释：** 匹配类型 **约束限制：** 不涉及 **取值范围：** - all: 匹配所有文件 - file_extension: 按文件后缀匹配 - catalog: 按目录匹配 - full_path: 全路径匹配 - home_page: 按首页匹配  **默认取值：** 不涉及
        :type match_type: str
        :param match_value: **参数解释：** 缓存规则匹配内容 **约束限制：** - 当match_type为all时，置空 - 当match_type为file_extension时，为文件后缀，输入首字符为“.”，以“,”或“;”分隔，如.jpg,.zip,.exe，并且输入的文件名后缀总数不超过100个，总字符不超过1000 - 当match_type为catalog时，为目录路径，输入要求以“/”作为首字符， 以“,”或“;”分隔，如/test/folder01,/test/folder02，并且输入的目录路径总数不超过20个，总字符不超过255 - 当match_type为full_path时，为全路径，输入要求以“/”作为首字符，支持匹配指定目录下的具体文件，或者带通配符“\\*”的文件，单条全路径缓存规则里仅支持配置一个全路径，如/test/index.html或/test/\\*.jpg，不可配置/* - 当match_type为home_page时，置空  **取值范围：** 不涉及 **默认取值：** 不涉及
        :type match_value: str
        :param ttl: **参数解释：** 资源在CDN节点的缓存过期时间，单位由ttl_unit参数指定 **约束限制：** 最大支持365天 **取值范围：** 不涉及 **默认取值：** 0
        :type ttl: int
        :param ttl_unit: **参数解释：** 缓存过期时间单位 **约束限制：** 不涉及 **取值范围：** - s: 秒 - m: 分 - h: 小时 - d: 天  **默认取值：** 不涉及
        :type ttl_unit: str
        :param priority: **参数解释：** 缓存规则的优先级，数值越大，优先级越高 **约束限制：** 优先级不能相同 **取值范围：** 1-1000 **默认取值：** 不涉及
        :type priority: int
        :param follow_origin: **参数解释：** 缓存过期时间来源，设置CDN节点的缓存遵循源站还是CDN侧的配置 **约束限制：** 不涉及 **取值范围：** - on: CDN节点的缓存过期时间遵循源站的设置 - off: CDN节点的缓存过期时间遵循“缓存规则”中的“缓存过期时间” - min_ttl: CDN节点的缓存过期时间取缓存规则和源站二者的最小值  **默认取值：** off: CDN节点的缓存过期时间遵循“缓存规则”中的“缓存过期时间”
        :type follow_origin: str
        :param force_cache: **参数解释：** 强制缓存：CDN节点缓存过期时间是否忽略源站响应头Cache-Control中的no-cache、private、no-store字段 **约束限制：** 强制缓存与缓存过期时间来源功能配合使用，具体使用限制及配置效果请参考CDN用户指南的配置节点缓存规则章节 **取值范围：** - on: 打开强制缓存 - off: 关闭强制缓存  **默认取值：** off: 关闭强制缓存
        :type force_cache: str
        :param url_parameter_type: **参数解释：** URL参数 **约束限制：** 不涉及 **取值范围：** - del_params: 忽略指定URL参数 - reserve_params: 保留指定URL参数 - ignore_url_params: 忽略全部URL参数 - full_url: 使用完整URL参数  **默认取值：** full_url: 使用完整URL参数
        :type url_parameter_type: str
        :param url_parameter_value: **参数解释：** URL参数值 **约束限制：** - 最多配置30条参数值 - 以“,”或“;”分隔 - 当url_parameter_type为del_params或reserve_params时必填  **取值范围：** 不涉及 **默认取值：** 不涉及
        :type url_parameter_value: str
        :param stale_while_revalidate: **参数解释：** 如果您的源站的Cache-Control头部设置了stale-while-revalidate&#x3D;***（***为时间），可以在CDN侧开启SWR开关，当CDN节点缓存的资源过期后，如果客户端请求该资源时过期时间没有超过stale-while-revalidate设置的时间，浏览器仍然返回已缓存的资源，同时cdn节点会回源请求最新的资源并缓存，用户再次请求时就会得到最新的资源。 **约束限制：** 不涉及 **取值范围：** - on: 开启 - off: 关闭  **默认取值：** off: 关闭
        :type stale_while_revalidate: str
        """
        
        

        self._match_type = None
        self._match_value = None
        self._ttl = None
        self._ttl_unit = None
        self._priority = None
        self._follow_origin = None
        self._force_cache = None
        self._url_parameter_type = None
        self._url_parameter_value = None
        self._stale_while_revalidate = None
        self.discriminator = None

        self.match_type = match_type
        if match_value is not None:
            self.match_value = match_value
        if ttl is not None:
            self.ttl = ttl
        self.ttl_unit = ttl_unit
        self.priority = priority
        if follow_origin is not None:
            self.follow_origin = follow_origin
        if force_cache is not None:
            self.force_cache = force_cache
        if url_parameter_type is not None:
            self.url_parameter_type = url_parameter_type
        if url_parameter_value is not None:
            self.url_parameter_value = url_parameter_value
        if stale_while_revalidate is not None:
            self.stale_while_revalidate = stale_while_revalidate

    @property
    def match_type(self):
        r"""Gets the match_type of this CacheRules.

        **参数解释：** 匹配类型 **约束限制：** 不涉及 **取值范围：** - all: 匹配所有文件 - file_extension: 按文件后缀匹配 - catalog: 按目录匹配 - full_path: 全路径匹配 - home_page: 按首页匹配  **默认取值：** 不涉及

        :return: The match_type of this CacheRules.
        :rtype: str
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        r"""Sets the match_type of this CacheRules.

        **参数解释：** 匹配类型 **约束限制：** 不涉及 **取值范围：** - all: 匹配所有文件 - file_extension: 按文件后缀匹配 - catalog: 按目录匹配 - full_path: 全路径匹配 - home_page: 按首页匹配  **默认取值：** 不涉及

        :param match_type: The match_type of this CacheRules.
        :type match_type: str
        """
        self._match_type = match_type

    @property
    def match_value(self):
        r"""Gets the match_value of this CacheRules.

        **参数解释：** 缓存规则匹配内容 **约束限制：** - 当match_type为all时，置空 - 当match_type为file_extension时，为文件后缀，输入首字符为“.”，以“,”或“;”分隔，如.jpg,.zip,.exe，并且输入的文件名后缀总数不超过100个，总字符不超过1000 - 当match_type为catalog时，为目录路径，输入要求以“/”作为首字符， 以“,”或“;”分隔，如/test/folder01,/test/folder02，并且输入的目录路径总数不超过20个，总字符不超过255 - 当match_type为full_path时，为全路径，输入要求以“/”作为首字符，支持匹配指定目录下的具体文件，或者带通配符“\\*”的文件，单条全路径缓存规则里仅支持配置一个全路径，如/test/index.html或/test/\\*.jpg，不可配置/* - 当match_type为home_page时，置空  **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The match_value of this CacheRules.
        :rtype: str
        """
        return self._match_value

    @match_value.setter
    def match_value(self, match_value):
        r"""Sets the match_value of this CacheRules.

        **参数解释：** 缓存规则匹配内容 **约束限制：** - 当match_type为all时，置空 - 当match_type为file_extension时，为文件后缀，输入首字符为“.”，以“,”或“;”分隔，如.jpg,.zip,.exe，并且输入的文件名后缀总数不超过100个，总字符不超过1000 - 当match_type为catalog时，为目录路径，输入要求以“/”作为首字符， 以“,”或“;”分隔，如/test/folder01,/test/folder02，并且输入的目录路径总数不超过20个，总字符不超过255 - 当match_type为full_path时，为全路径，输入要求以“/”作为首字符，支持匹配指定目录下的具体文件，或者带通配符“\\*”的文件，单条全路径缓存规则里仅支持配置一个全路径，如/test/index.html或/test/\\*.jpg，不可配置/* - 当match_type为home_page时，置空  **取值范围：** 不涉及 **默认取值：** 不涉及

        :param match_value: The match_value of this CacheRules.
        :type match_value: str
        """
        self._match_value = match_value

    @property
    def ttl(self):
        r"""Gets the ttl of this CacheRules.

        **参数解释：** 资源在CDN节点的缓存过期时间，单位由ttl_unit参数指定 **约束限制：** 最大支持365天 **取值范围：** 不涉及 **默认取值：** 0

        :return: The ttl of this CacheRules.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        r"""Sets the ttl of this CacheRules.

        **参数解释：** 资源在CDN节点的缓存过期时间，单位由ttl_unit参数指定 **约束限制：** 最大支持365天 **取值范围：** 不涉及 **默认取值：** 0

        :param ttl: The ttl of this CacheRules.
        :type ttl: int
        """
        self._ttl = ttl

    @property
    def ttl_unit(self):
        r"""Gets the ttl_unit of this CacheRules.

        **参数解释：** 缓存过期时间单位 **约束限制：** 不涉及 **取值范围：** - s: 秒 - m: 分 - h: 小时 - d: 天  **默认取值：** 不涉及

        :return: The ttl_unit of this CacheRules.
        :rtype: str
        """
        return self._ttl_unit

    @ttl_unit.setter
    def ttl_unit(self, ttl_unit):
        r"""Sets the ttl_unit of this CacheRules.

        **参数解释：** 缓存过期时间单位 **约束限制：** 不涉及 **取值范围：** - s: 秒 - m: 分 - h: 小时 - d: 天  **默认取值：** 不涉及

        :param ttl_unit: The ttl_unit of this CacheRules.
        :type ttl_unit: str
        """
        self._ttl_unit = ttl_unit

    @property
    def priority(self):
        r"""Gets the priority of this CacheRules.

        **参数解释：** 缓存规则的优先级，数值越大，优先级越高 **约束限制：** 优先级不能相同 **取值范围：** 1-1000 **默认取值：** 不涉及

        :return: The priority of this CacheRules.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this CacheRules.

        **参数解释：** 缓存规则的优先级，数值越大，优先级越高 **约束限制：** 优先级不能相同 **取值范围：** 1-1000 **默认取值：** 不涉及

        :param priority: The priority of this CacheRules.
        :type priority: int
        """
        self._priority = priority

    @property
    def follow_origin(self):
        r"""Gets the follow_origin of this CacheRules.

        **参数解释：** 缓存过期时间来源，设置CDN节点的缓存遵循源站还是CDN侧的配置 **约束限制：** 不涉及 **取值范围：** - on: CDN节点的缓存过期时间遵循源站的设置 - off: CDN节点的缓存过期时间遵循“缓存规则”中的“缓存过期时间” - min_ttl: CDN节点的缓存过期时间取缓存规则和源站二者的最小值  **默认取值：** off: CDN节点的缓存过期时间遵循“缓存规则”中的“缓存过期时间”

        :return: The follow_origin of this CacheRules.
        :rtype: str
        """
        return self._follow_origin

    @follow_origin.setter
    def follow_origin(self, follow_origin):
        r"""Sets the follow_origin of this CacheRules.

        **参数解释：** 缓存过期时间来源，设置CDN节点的缓存遵循源站还是CDN侧的配置 **约束限制：** 不涉及 **取值范围：** - on: CDN节点的缓存过期时间遵循源站的设置 - off: CDN节点的缓存过期时间遵循“缓存规则”中的“缓存过期时间” - min_ttl: CDN节点的缓存过期时间取缓存规则和源站二者的最小值  **默认取值：** off: CDN节点的缓存过期时间遵循“缓存规则”中的“缓存过期时间”

        :param follow_origin: The follow_origin of this CacheRules.
        :type follow_origin: str
        """
        self._follow_origin = follow_origin

    @property
    def force_cache(self):
        r"""Gets the force_cache of this CacheRules.

        **参数解释：** 强制缓存：CDN节点缓存过期时间是否忽略源站响应头Cache-Control中的no-cache、private、no-store字段 **约束限制：** 强制缓存与缓存过期时间来源功能配合使用，具体使用限制及配置效果请参考CDN用户指南的配置节点缓存规则章节 **取值范围：** - on: 打开强制缓存 - off: 关闭强制缓存  **默认取值：** off: 关闭强制缓存

        :return: The force_cache of this CacheRules.
        :rtype: str
        """
        return self._force_cache

    @force_cache.setter
    def force_cache(self, force_cache):
        r"""Sets the force_cache of this CacheRules.

        **参数解释：** 强制缓存：CDN节点缓存过期时间是否忽略源站响应头Cache-Control中的no-cache、private、no-store字段 **约束限制：** 强制缓存与缓存过期时间来源功能配合使用，具体使用限制及配置效果请参考CDN用户指南的配置节点缓存规则章节 **取值范围：** - on: 打开强制缓存 - off: 关闭强制缓存  **默认取值：** off: 关闭强制缓存

        :param force_cache: The force_cache of this CacheRules.
        :type force_cache: str
        """
        self._force_cache = force_cache

    @property
    def url_parameter_type(self):
        r"""Gets the url_parameter_type of this CacheRules.

        **参数解释：** URL参数 **约束限制：** 不涉及 **取值范围：** - del_params: 忽略指定URL参数 - reserve_params: 保留指定URL参数 - ignore_url_params: 忽略全部URL参数 - full_url: 使用完整URL参数  **默认取值：** full_url: 使用完整URL参数

        :return: The url_parameter_type of this CacheRules.
        :rtype: str
        """
        return self._url_parameter_type

    @url_parameter_type.setter
    def url_parameter_type(self, url_parameter_type):
        r"""Sets the url_parameter_type of this CacheRules.

        **参数解释：** URL参数 **约束限制：** 不涉及 **取值范围：** - del_params: 忽略指定URL参数 - reserve_params: 保留指定URL参数 - ignore_url_params: 忽略全部URL参数 - full_url: 使用完整URL参数  **默认取值：** full_url: 使用完整URL参数

        :param url_parameter_type: The url_parameter_type of this CacheRules.
        :type url_parameter_type: str
        """
        self._url_parameter_type = url_parameter_type

    @property
    def url_parameter_value(self):
        r"""Gets the url_parameter_value of this CacheRules.

        **参数解释：** URL参数值 **约束限制：** - 最多配置30条参数值 - 以“,”或“;”分隔 - 当url_parameter_type为del_params或reserve_params时必填  **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The url_parameter_value of this CacheRules.
        :rtype: str
        """
        return self._url_parameter_value

    @url_parameter_value.setter
    def url_parameter_value(self, url_parameter_value):
        r"""Sets the url_parameter_value of this CacheRules.

        **参数解释：** URL参数值 **约束限制：** - 最多配置30条参数值 - 以“,”或“;”分隔 - 当url_parameter_type为del_params或reserve_params时必填  **取值范围：** 不涉及 **默认取值：** 不涉及

        :param url_parameter_value: The url_parameter_value of this CacheRules.
        :type url_parameter_value: str
        """
        self._url_parameter_value = url_parameter_value

    @property
    def stale_while_revalidate(self):
        r"""Gets the stale_while_revalidate of this CacheRules.

        **参数解释：** 如果您的源站的Cache-Control头部设置了stale-while-revalidate=***（***为时间），可以在CDN侧开启SWR开关，当CDN节点缓存的资源过期后，如果客户端请求该资源时过期时间没有超过stale-while-revalidate设置的时间，浏览器仍然返回已缓存的资源，同时cdn节点会回源请求最新的资源并缓存，用户再次请求时就会得到最新的资源。 **约束限制：** 不涉及 **取值范围：** - on: 开启 - off: 关闭  **默认取值：** off: 关闭

        :return: The stale_while_revalidate of this CacheRules.
        :rtype: str
        """
        return self._stale_while_revalidate

    @stale_while_revalidate.setter
    def stale_while_revalidate(self, stale_while_revalidate):
        r"""Sets the stale_while_revalidate of this CacheRules.

        **参数解释：** 如果您的源站的Cache-Control头部设置了stale-while-revalidate=***（***为时间），可以在CDN侧开启SWR开关，当CDN节点缓存的资源过期后，如果客户端请求该资源时过期时间没有超过stale-while-revalidate设置的时间，浏览器仍然返回已缓存的资源，同时cdn节点会回源请求最新的资源并缓存，用户再次请求时就会得到最新的资源。 **约束限制：** 不涉及 **取值范围：** - on: 开启 - off: 关闭  **默认取值：** off: 关闭

        :param stale_while_revalidate: The stale_while_revalidate of this CacheRules.
        :type stale_while_revalidate: str
        """
        self._stale_while_revalidate = stale_while_revalidate

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CacheRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
