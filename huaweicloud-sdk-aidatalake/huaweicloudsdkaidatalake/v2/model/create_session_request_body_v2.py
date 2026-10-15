# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSessionRequestBodyV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'endpoint_name': 'str',
        'agency_name': 'str',
        'catalog_context': 'CatalogContext',
        'wait_timeout': 'int',
        'max_retry_times': 'int',
        'priority': 'int',
        'cpu': 'int',
        'memory': 'int'
    }

    attribute_map = {
        'endpoint_name': 'endpoint_name',
        'agency_name': 'agency_name',
        'catalog_context': 'catalog_context',
        'wait_timeout': 'wait_timeout',
        'max_retry_times': 'max_retry_times',
        'priority': 'priority',
        'cpu': 'cpu',
        'memory': 'memory'
    }

    def __init__(self, endpoint_name=None, agency_name=None, catalog_context=None, wait_timeout=None, max_retry_times=None, priority=None, cpu=None, memory=None):
        r"""CreateSessionRequestBodyV2

        The model defined in huaweicloud sdk

        :param endpoint_name: **参数解释**：Endpoint名称。 **约束限制**：不涉及。 **取值范围**：长度为1~128个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。
        :type endpoint_name: str
        :param agency_name: **参数解释**：委托名称。 **约束限制**：具体请参见[[配置Aura委托](https://support.huaweicloud.com/usermanual-aidatalake/aidatalake_01_0078.html#section4)](tag:HEC)[[配置Aura委托](https://support.huaweicloud.com/intl/zh-cn/usermanual-aidatalake/aidatalake_01_0078.html#section4)](tag:hws_hk)。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type agency_name: str
        :param catalog_context: 
        :type catalog_context: :class:`huaweicloudsdkaidatalake.v2.CatalogContext`
        :param wait_timeout: **参数解释**：创建session排队等待时间，单位：秒。 **约束限制**：不涉及。 **取值范围**：300~86400。 **默认取值**：不涉及。
        :type wait_timeout: int
        :param max_retry_times: **参数解释**：资源不足时重试次数。 **约束限制**：不涉及。 **取值范围**：1~2147483647。 **默认取值**：不涉及。
        :type max_retry_times: int
        :param priority: **参数解释**：优先级（1~9，9为最高优先级）。 **约束限制**：不涉及。 **取值范围**：1~9。 **默认取值**：5。
        :type priority: int
        :param cpu: **参数解释**：会话维度指定的 CN（计算节点）CPU 资源规格，单位：毫核（millicores）。 **约束限制**：可选；不传时回退到全局配置 getCnCpuLimit； INNER_SESSION/维护语句场景不消费该字段，资源规格继承父会话 CN； 上限 48000 毫核（48 核），超上限返回 400 INVALID_PARAMETER。 **取值范围**：(0, 48000] 毫核。 **默认取值**：不传时取全局配置兜底值（如 4000 毫核）。
        :type cpu: int
        :param memory: **参数解释**：会话维度指定的 CN（计算节点）Memory 资源规格，单位：MB。 **约束限制**：可选；不传时回退到全局配置 getCnMemoryLimit； INNER_SESSION/维护语句场景不消费该字段，资源规格继承父会话 CN； 上限 393216 MB（384 GB），超上限返回 400 INVALID_PARAMETER。 **取值范围**：(0, 393216] MB。 **默认取值**：不传时取全局配置兜底值（如 16384 MB）。
        :type memory: int
        """
        
        

        self._endpoint_name = None
        self._agency_name = None
        self._catalog_context = None
        self._wait_timeout = None
        self._max_retry_times = None
        self._priority = None
        self._cpu = None
        self._memory = None
        self.discriminator = None

        self.endpoint_name = endpoint_name
        if agency_name is not None:
            self.agency_name = agency_name
        self.catalog_context = catalog_context
        if wait_timeout is not None:
            self.wait_timeout = wait_timeout
        if max_retry_times is not None:
            self.max_retry_times = max_retry_times
        if priority is not None:
            self.priority = priority
        if cpu is not None:
            self.cpu = cpu
        if memory is not None:
            self.memory = memory

    @property
    def endpoint_name(self):
        r"""Gets the endpoint_name of this CreateSessionRequestBodyV2.

        **参数解释**：Endpoint名称。 **约束限制**：不涉及。 **取值范围**：长度为1~128个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :return: The endpoint_name of this CreateSessionRequestBodyV2.
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        r"""Sets the endpoint_name of this CreateSessionRequestBodyV2.

        **参数解释**：Endpoint名称。 **约束限制**：不涉及。 **取值范围**：长度为1~128个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :param endpoint_name: The endpoint_name of this CreateSessionRequestBodyV2.
        :type endpoint_name: str
        """
        self._endpoint_name = endpoint_name

    @property
    def agency_name(self):
        r"""Gets the agency_name of this CreateSessionRequestBodyV2.

        **参数解释**：委托名称。 **约束限制**：具体请参见[[配置Aura委托](https://support.huaweicloud.com/usermanual-aidatalake/aidatalake_01_0078.html#section4)](tag:HEC)[[配置Aura委托](https://support.huaweicloud.com/intl/zh-cn/usermanual-aidatalake/aidatalake_01_0078.html#section4)](tag:hws_hk)。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The agency_name of this CreateSessionRequestBodyV2.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this CreateSessionRequestBodyV2.

        **参数解释**：委托名称。 **约束限制**：具体请参见[[配置Aura委托](https://support.huaweicloud.com/usermanual-aidatalake/aidatalake_01_0078.html#section4)](tag:HEC)[[配置Aura委托](https://support.huaweicloud.com/intl/zh-cn/usermanual-aidatalake/aidatalake_01_0078.html#section4)](tag:hws_hk)。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param agency_name: The agency_name of this CreateSessionRequestBodyV2.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def catalog_context(self):
        r"""Gets the catalog_context of this CreateSessionRequestBodyV2.

        :return: The catalog_context of this CreateSessionRequestBodyV2.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.CatalogContext`
        """
        return self._catalog_context

    @catalog_context.setter
    def catalog_context(self, catalog_context):
        r"""Sets the catalog_context of this CreateSessionRequestBodyV2.

        :param catalog_context: The catalog_context of this CreateSessionRequestBodyV2.
        :type catalog_context: :class:`huaweicloudsdkaidatalake.v2.CatalogContext`
        """
        self._catalog_context = catalog_context

    @property
    def wait_timeout(self):
        r"""Gets the wait_timeout of this CreateSessionRequestBodyV2.

        **参数解释**：创建session排队等待时间，单位：秒。 **约束限制**：不涉及。 **取值范围**：300~86400。 **默认取值**：不涉及。

        :return: The wait_timeout of this CreateSessionRequestBodyV2.
        :rtype: int
        """
        return self._wait_timeout

    @wait_timeout.setter
    def wait_timeout(self, wait_timeout):
        r"""Sets the wait_timeout of this CreateSessionRequestBodyV2.

        **参数解释**：创建session排队等待时间，单位：秒。 **约束限制**：不涉及。 **取值范围**：300~86400。 **默认取值**：不涉及。

        :param wait_timeout: The wait_timeout of this CreateSessionRequestBodyV2.
        :type wait_timeout: int
        """
        self._wait_timeout = wait_timeout

    @property
    def max_retry_times(self):
        r"""Gets the max_retry_times of this CreateSessionRequestBodyV2.

        **参数解释**：资源不足时重试次数。 **约束限制**：不涉及。 **取值范围**：1~2147483647。 **默认取值**：不涉及。

        :return: The max_retry_times of this CreateSessionRequestBodyV2.
        :rtype: int
        """
        return self._max_retry_times

    @max_retry_times.setter
    def max_retry_times(self, max_retry_times):
        r"""Sets the max_retry_times of this CreateSessionRequestBodyV2.

        **参数解释**：资源不足时重试次数。 **约束限制**：不涉及。 **取值范围**：1~2147483647。 **默认取值**：不涉及。

        :param max_retry_times: The max_retry_times of this CreateSessionRequestBodyV2.
        :type max_retry_times: int
        """
        self._max_retry_times = max_retry_times

    @property
    def priority(self):
        r"""Gets the priority of this CreateSessionRequestBodyV2.

        **参数解释**：优先级（1~9，9为最高优先级）。 **约束限制**：不涉及。 **取值范围**：1~9。 **默认取值**：5。

        :return: The priority of this CreateSessionRequestBodyV2.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this CreateSessionRequestBodyV2.

        **参数解释**：优先级（1~9，9为最高优先级）。 **约束限制**：不涉及。 **取值范围**：1~9。 **默认取值**：5。

        :param priority: The priority of this CreateSessionRequestBodyV2.
        :type priority: int
        """
        self._priority = priority

    @property
    def cpu(self):
        r"""Gets the cpu of this CreateSessionRequestBodyV2.

        **参数解释**：会话维度指定的 CN（计算节点）CPU 资源规格，单位：毫核（millicores）。 **约束限制**：可选；不传时回退到全局配置 getCnCpuLimit； INNER_SESSION/维护语句场景不消费该字段，资源规格继承父会话 CN； 上限 48000 毫核（48 核），超上限返回 400 INVALID_PARAMETER。 **取值范围**：(0, 48000] 毫核。 **默认取值**：不传时取全局配置兜底值（如 4000 毫核）。

        :return: The cpu of this CreateSessionRequestBodyV2.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this CreateSessionRequestBodyV2.

        **参数解释**：会话维度指定的 CN（计算节点）CPU 资源规格，单位：毫核（millicores）。 **约束限制**：可选；不传时回退到全局配置 getCnCpuLimit； INNER_SESSION/维护语句场景不消费该字段，资源规格继承父会话 CN； 上限 48000 毫核（48 核），超上限返回 400 INVALID_PARAMETER。 **取值范围**：(0, 48000] 毫核。 **默认取值**：不传时取全局配置兜底值（如 4000 毫核）。

        :param cpu: The cpu of this CreateSessionRequestBodyV2.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def memory(self):
        r"""Gets the memory of this CreateSessionRequestBodyV2.

        **参数解释**：会话维度指定的 CN（计算节点）Memory 资源规格，单位：MB。 **约束限制**：可选；不传时回退到全局配置 getCnMemoryLimit； INNER_SESSION/维护语句场景不消费该字段，资源规格继承父会话 CN； 上限 393216 MB（384 GB），超上限返回 400 INVALID_PARAMETER。 **取值范围**：(0, 393216] MB。 **默认取值**：不传时取全局配置兜底值（如 16384 MB）。

        :return: The memory of this CreateSessionRequestBodyV2.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this CreateSessionRequestBodyV2.

        **参数解释**：会话维度指定的 CN（计算节点）Memory 资源规格，单位：MB。 **约束限制**：可选；不传时回退到全局配置 getCnMemoryLimit； INNER_SESSION/维护语句场景不消费该字段，资源规格继承父会话 CN； 上限 393216 MB（384 GB），超上限返回 400 INVALID_PARAMETER。 **取值范围**：(0, 393216] MB。 **默认取值**：不传时取全局配置兜底值（如 16384 MB）。

        :param memory: The memory of this CreateSessionRequestBodyV2.
        :type memory: int
        """
        self._memory = memory

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
        if not isinstance(other, CreateSessionRequestBodyV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
