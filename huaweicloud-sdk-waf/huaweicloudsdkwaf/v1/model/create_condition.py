# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCondition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'index': 'str',
        'logic_operation': 'str',
        'contents': 'list[str]',
        'check_all_indexes_logic': 'int',
        'value_list_id': 'str'
    }

    attribute_map = {
        'category': 'category',
        'index': 'index',
        'logic_operation': 'logic_operation',
        'contents': 'contents',
        'check_all_indexes_logic': 'check_all_indexes_logic',
        'value_list_id': 'value_list_id'
    }

    def __init__(self, category=None, index=None, logic_operation=None, contents=None, check_all_indexes_logic=None, value_list_id=None):
        r"""CreateCondition

        The model defined in huaweicloud sdk

        :param category: **参数解释：** 字段类型 **约束限制：** 不涉及 **取值范围：** - url: 路径 - custom_geoip: 客户端IP所属的地理位置 - robot: 已知特征爬虫 - user-agent: User Agent - ip: IPv4 - ipv6: IPv6 - params: Params - cookie: Cookie - referer: Referer - header: Header - method: Method - request_line: Request Line - request: Request - protocol: Protocol - request_body: Request Body  **默认取值：** 不涉及
        :type category: str
        :param index: **参数解释：** 子字段 **约束限制：** 随字段类型变化 **取值范围：** - custom_geoip:    - v4：ipv4   - v6：ipv6   - any：ipv4或ipv6 - ip/ipv6:    - null：客户端IP   - x-forwarded-for：请求header中X-Forwarded-For记录的IP   - $remote_addr：TCP连接IP   - $remote_sockaddr：3层源IP - params/cookie/header：   - check_all_indexes_logic为null： 可自定义子字段名称   - check_all_indexes_logic不为null：必须为null - 其他字段类型：不支持，默认为null  **默认取值：** 不涉及
        :type index: str
        :param logic_operation: **参数解释：** 匹配逻辑 **约束限制：** 匹配逻辑根据字段类型变化 **取值范围：** - url/user-agent/referer:    - contain_any: 包含任意一个   - not_contain_all: 不包含全部   - equal_any: 等于任意一个   - not_equal_all: 不等于全部   - prefix_any: 前缀匹配任意一个   - not_prefix_all: 前缀不匹配全部   - suffix_any: 后缀匹配任意一个   - not_suffix_all: 后缀不匹配全部   - contain: 包含   - not_contain: 不包含   - equal: 等于   - not_equal: 不等于   - prefix: 前缀匹配   - not_prefix: 前缀不匹配   - suffix: 后缀匹配   - not_suffix: 后缀不匹配   - len_equal: 长度等于   - len_not_equal: 长度不等于   - len_greater: 长度大于   - len_less: 长度小于   - len_greater_equal: 长度大于等于   - len_less_equal: 长度小于等于   - regular_match: 正则匹配   - regular_not_match: 正则不匹配 - custom_geoip:    - belong: 属于   - not_belong: 不属于 - robot:    - match: 匹配   - not_match: 不匹配 - ip/ipv6:   - equal_any: 等于任意一个   - not_equal_all: 不等于全部   - equal: 等于   - not_equal: 不等于 - params/cookie/header:   - contain_any: 包含任意一个   - not_contain_all: 不包含全部   - equal_any: 等于任意一个   - not_equal_all: 不等于全部   - prefix_any: 前缀匹配任意一个   - not_prefix_all: 前缀不匹配全部   - suffix_any: 后缀匹配任意一个   - not_suffix_all: 后缀不匹配全部   - contain: 包含   - not_contain: 不包含   - equal: 等于   - not_equal: 不等于   - prefix: 前缀匹配   - not_prefix: 前缀不匹配   - suffix: 后缀匹配   - not_suffix: 后缀不匹配   - len_equal: 长度等于   - len_not_equal: 长度不等于   - len_greater: 长度大于   - len_less: 长度小于   - len_greater_equal: 长度大于等于   - len_less_equal: 长度小于等于   - num_equal: 数字等于   - num_not_equal: 数字不等于   - num_greater: 数字大于   - num_less: 数字小于   - exist: 存在   - not_exist: 不存在   - regular_match: 正则匹配   - regular_not_match: 正则不匹配 - method/protocol:   - equal: 等于   - not_equal: 不等于 - request_line:   - len_equal: 长度等于   - len_not_equal: 长度不等于   - len_greater: 长度大于   - len_less: 长度小于   - len_greater_equal: 长度大于等于   - len_less_equal: 长度小于等于 - request:   - len_equal: 长度等于   - len_not_equal: 长度不等于   - len_greater: 长度大于   - len_less: 长度小于   - len_greater_equal: 长度大于等于   - len_less_equal: 长度小于等于   - regular_match: 正则匹配   - regular_not_match: 正则不匹配 - request_body:   - contain: 包含   - contain_any: 包含任意一个   - not_contain: 不包含   - not_contain_all: 不包含全部   - regular_match: 正则匹配   - regular_not_match: 正则不匹配  **默认取值：** 不涉及
        :type logic_operation: str
        :param contents: **参数解释：** 条件列表逻辑匹配内容 **约束限制：** 当logic_operation参数不以any或者all结尾时，需要传该参数 **取值范围：** 匹配内容字符串长度范围：[1, 4096] 内容格式根据参数category和logic_operation变化： - logic_operation为数值比较类型：纯数字 - url: URL格式；仅支持单个匹配内容 - custom_geoip: 客户端IP所属国家或省份，多个位置以|分隔，比如：\&quot;BJ|SH\&quot; - robot: 已知特征爬虫列表，可选择多个   - crawler_engine：搜索引擎   - crawler_scanner：扫描器   - crawler_script：脚本工具   - crawler_other：其他爬虫 - ip: IPv4 - ipv6: IPv6 - referer: 例如：http://test.com - params：不包含&amp; - user-agent/cookie/header/request_body: 无限制 - method: HTTP协议支持的method，字母大写 - protocol:    - http   - https  **默认取值：** 不涉及
        :type contents: list[str]
        :param check_all_indexes_logic: **参数解释：** 需要检查所有子字段或检查任意子字段时传此参数 **约束限制：** 仅当category为params/cookie/header时支持 **取值范围：** - 1：所有子字段 - 2：任意子字段  **默认取值：** 不涉及
        :type check_all_indexes_logic: int
        :param value_list_id: **参数解释：** 引用表ID **约束限制：** 当logic_operation参数以any或者all结尾时，需要传该参数；引用表类型要与category类型保持一致 **取值范围：** 通过ListValueList接口获取引用表ID  **默认取值：** 不涉及
        :type value_list_id: str
        """
        
        

        self._category = None
        self._index = None
        self._logic_operation = None
        self._contents = None
        self._check_all_indexes_logic = None
        self._value_list_id = None
        self.discriminator = None

        self.category = category
        if index is not None:
            self.index = index
        self.logic_operation = logic_operation
        if contents is not None:
            self.contents = contents
        if check_all_indexes_logic is not None:
            self.check_all_indexes_logic = check_all_indexes_logic
        if value_list_id is not None:
            self.value_list_id = value_list_id

    @property
    def category(self):
        r"""Gets the category of this CreateCondition.

        **参数解释：** 字段类型 **约束限制：** 不涉及 **取值范围：** - url: 路径 - custom_geoip: 客户端IP所属的地理位置 - robot: 已知特征爬虫 - user-agent: User Agent - ip: IPv4 - ipv6: IPv6 - params: Params - cookie: Cookie - referer: Referer - header: Header - method: Method - request_line: Request Line - request: Request - protocol: Protocol - request_body: Request Body  **默认取值：** 不涉及

        :return: The category of this CreateCondition.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this CreateCondition.

        **参数解释：** 字段类型 **约束限制：** 不涉及 **取值范围：** - url: 路径 - custom_geoip: 客户端IP所属的地理位置 - robot: 已知特征爬虫 - user-agent: User Agent - ip: IPv4 - ipv6: IPv6 - params: Params - cookie: Cookie - referer: Referer - header: Header - method: Method - request_line: Request Line - request: Request - protocol: Protocol - request_body: Request Body  **默认取值：** 不涉及

        :param category: The category of this CreateCondition.
        :type category: str
        """
        self._category = category

    @property
    def index(self):
        r"""Gets the index of this CreateCondition.

        **参数解释：** 子字段 **约束限制：** 随字段类型变化 **取值范围：** - custom_geoip:    - v4：ipv4   - v6：ipv6   - any：ipv4或ipv6 - ip/ipv6:    - null：客户端IP   - x-forwarded-for：请求header中X-Forwarded-For记录的IP   - $remote_addr：TCP连接IP   - $remote_sockaddr：3层源IP - params/cookie/header：   - check_all_indexes_logic为null： 可自定义子字段名称   - check_all_indexes_logic不为null：必须为null - 其他字段类型：不支持，默认为null  **默认取值：** 不涉及

        :return: The index of this CreateCondition.
        :rtype: str
        """
        return self._index

    @index.setter
    def index(self, index):
        r"""Sets the index of this CreateCondition.

        **参数解释：** 子字段 **约束限制：** 随字段类型变化 **取值范围：** - custom_geoip:    - v4：ipv4   - v6：ipv6   - any：ipv4或ipv6 - ip/ipv6:    - null：客户端IP   - x-forwarded-for：请求header中X-Forwarded-For记录的IP   - $remote_addr：TCP连接IP   - $remote_sockaddr：3层源IP - params/cookie/header：   - check_all_indexes_logic为null： 可自定义子字段名称   - check_all_indexes_logic不为null：必须为null - 其他字段类型：不支持，默认为null  **默认取值：** 不涉及

        :param index: The index of this CreateCondition.
        :type index: str
        """
        self._index = index

    @property
    def logic_operation(self):
        r"""Gets the logic_operation of this CreateCondition.

        **参数解释：** 匹配逻辑 **约束限制：** 匹配逻辑根据字段类型变化 **取值范围：** - url/user-agent/referer:    - contain_any: 包含任意一个   - not_contain_all: 不包含全部   - equal_any: 等于任意一个   - not_equal_all: 不等于全部   - prefix_any: 前缀匹配任意一个   - not_prefix_all: 前缀不匹配全部   - suffix_any: 后缀匹配任意一个   - not_suffix_all: 后缀不匹配全部   - contain: 包含   - not_contain: 不包含   - equal: 等于   - not_equal: 不等于   - prefix: 前缀匹配   - not_prefix: 前缀不匹配   - suffix: 后缀匹配   - not_suffix: 后缀不匹配   - len_equal: 长度等于   - len_not_equal: 长度不等于   - len_greater: 长度大于   - len_less: 长度小于   - len_greater_equal: 长度大于等于   - len_less_equal: 长度小于等于   - regular_match: 正则匹配   - regular_not_match: 正则不匹配 - custom_geoip:    - belong: 属于   - not_belong: 不属于 - robot:    - match: 匹配   - not_match: 不匹配 - ip/ipv6:   - equal_any: 等于任意一个   - not_equal_all: 不等于全部   - equal: 等于   - not_equal: 不等于 - params/cookie/header:   - contain_any: 包含任意一个   - not_contain_all: 不包含全部   - equal_any: 等于任意一个   - not_equal_all: 不等于全部   - prefix_any: 前缀匹配任意一个   - not_prefix_all: 前缀不匹配全部   - suffix_any: 后缀匹配任意一个   - not_suffix_all: 后缀不匹配全部   - contain: 包含   - not_contain: 不包含   - equal: 等于   - not_equal: 不等于   - prefix: 前缀匹配   - not_prefix: 前缀不匹配   - suffix: 后缀匹配   - not_suffix: 后缀不匹配   - len_equal: 长度等于   - len_not_equal: 长度不等于   - len_greater: 长度大于   - len_less: 长度小于   - len_greater_equal: 长度大于等于   - len_less_equal: 长度小于等于   - num_equal: 数字等于   - num_not_equal: 数字不等于   - num_greater: 数字大于   - num_less: 数字小于   - exist: 存在   - not_exist: 不存在   - regular_match: 正则匹配   - regular_not_match: 正则不匹配 - method/protocol:   - equal: 等于   - not_equal: 不等于 - request_line:   - len_equal: 长度等于   - len_not_equal: 长度不等于   - len_greater: 长度大于   - len_less: 长度小于   - len_greater_equal: 长度大于等于   - len_less_equal: 长度小于等于 - request:   - len_equal: 长度等于   - len_not_equal: 长度不等于   - len_greater: 长度大于   - len_less: 长度小于   - len_greater_equal: 长度大于等于   - len_less_equal: 长度小于等于   - regular_match: 正则匹配   - regular_not_match: 正则不匹配 - request_body:   - contain: 包含   - contain_any: 包含任意一个   - not_contain: 不包含   - not_contain_all: 不包含全部   - regular_match: 正则匹配   - regular_not_match: 正则不匹配  **默认取值：** 不涉及

        :return: The logic_operation of this CreateCondition.
        :rtype: str
        """
        return self._logic_operation

    @logic_operation.setter
    def logic_operation(self, logic_operation):
        r"""Sets the logic_operation of this CreateCondition.

        **参数解释：** 匹配逻辑 **约束限制：** 匹配逻辑根据字段类型变化 **取值范围：** - url/user-agent/referer:    - contain_any: 包含任意一个   - not_contain_all: 不包含全部   - equal_any: 等于任意一个   - not_equal_all: 不等于全部   - prefix_any: 前缀匹配任意一个   - not_prefix_all: 前缀不匹配全部   - suffix_any: 后缀匹配任意一个   - not_suffix_all: 后缀不匹配全部   - contain: 包含   - not_contain: 不包含   - equal: 等于   - not_equal: 不等于   - prefix: 前缀匹配   - not_prefix: 前缀不匹配   - suffix: 后缀匹配   - not_suffix: 后缀不匹配   - len_equal: 长度等于   - len_not_equal: 长度不等于   - len_greater: 长度大于   - len_less: 长度小于   - len_greater_equal: 长度大于等于   - len_less_equal: 长度小于等于   - regular_match: 正则匹配   - regular_not_match: 正则不匹配 - custom_geoip:    - belong: 属于   - not_belong: 不属于 - robot:    - match: 匹配   - not_match: 不匹配 - ip/ipv6:   - equal_any: 等于任意一个   - not_equal_all: 不等于全部   - equal: 等于   - not_equal: 不等于 - params/cookie/header:   - contain_any: 包含任意一个   - not_contain_all: 不包含全部   - equal_any: 等于任意一个   - not_equal_all: 不等于全部   - prefix_any: 前缀匹配任意一个   - not_prefix_all: 前缀不匹配全部   - suffix_any: 后缀匹配任意一个   - not_suffix_all: 后缀不匹配全部   - contain: 包含   - not_contain: 不包含   - equal: 等于   - not_equal: 不等于   - prefix: 前缀匹配   - not_prefix: 前缀不匹配   - suffix: 后缀匹配   - not_suffix: 后缀不匹配   - len_equal: 长度等于   - len_not_equal: 长度不等于   - len_greater: 长度大于   - len_less: 长度小于   - len_greater_equal: 长度大于等于   - len_less_equal: 长度小于等于   - num_equal: 数字等于   - num_not_equal: 数字不等于   - num_greater: 数字大于   - num_less: 数字小于   - exist: 存在   - not_exist: 不存在   - regular_match: 正则匹配   - regular_not_match: 正则不匹配 - method/protocol:   - equal: 等于   - not_equal: 不等于 - request_line:   - len_equal: 长度等于   - len_not_equal: 长度不等于   - len_greater: 长度大于   - len_less: 长度小于   - len_greater_equal: 长度大于等于   - len_less_equal: 长度小于等于 - request:   - len_equal: 长度等于   - len_not_equal: 长度不等于   - len_greater: 长度大于   - len_less: 长度小于   - len_greater_equal: 长度大于等于   - len_less_equal: 长度小于等于   - regular_match: 正则匹配   - regular_not_match: 正则不匹配 - request_body:   - contain: 包含   - contain_any: 包含任意一个   - not_contain: 不包含   - not_contain_all: 不包含全部   - regular_match: 正则匹配   - regular_not_match: 正则不匹配  **默认取值：** 不涉及

        :param logic_operation: The logic_operation of this CreateCondition.
        :type logic_operation: str
        """
        self._logic_operation = logic_operation

    @property
    def contents(self):
        r"""Gets the contents of this CreateCondition.

        **参数解释：** 条件列表逻辑匹配内容 **约束限制：** 当logic_operation参数不以any或者all结尾时，需要传该参数 **取值范围：** 匹配内容字符串长度范围：[1, 4096] 内容格式根据参数category和logic_operation变化： - logic_operation为数值比较类型：纯数字 - url: URL格式；仅支持单个匹配内容 - custom_geoip: 客户端IP所属国家或省份，多个位置以|分隔，比如：\"BJ|SH\" - robot: 已知特征爬虫列表，可选择多个   - crawler_engine：搜索引擎   - crawler_scanner：扫描器   - crawler_script：脚本工具   - crawler_other：其他爬虫 - ip: IPv4 - ipv6: IPv6 - referer: 例如：http://test.com - params：不包含& - user-agent/cookie/header/request_body: 无限制 - method: HTTP协议支持的method，字母大写 - protocol:    - http   - https  **默认取值：** 不涉及

        :return: The contents of this CreateCondition.
        :rtype: list[str]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        r"""Sets the contents of this CreateCondition.

        **参数解释：** 条件列表逻辑匹配内容 **约束限制：** 当logic_operation参数不以any或者all结尾时，需要传该参数 **取值范围：** 匹配内容字符串长度范围：[1, 4096] 内容格式根据参数category和logic_operation变化： - logic_operation为数值比较类型：纯数字 - url: URL格式；仅支持单个匹配内容 - custom_geoip: 客户端IP所属国家或省份，多个位置以|分隔，比如：\"BJ|SH\" - robot: 已知特征爬虫列表，可选择多个   - crawler_engine：搜索引擎   - crawler_scanner：扫描器   - crawler_script：脚本工具   - crawler_other：其他爬虫 - ip: IPv4 - ipv6: IPv6 - referer: 例如：http://test.com - params：不包含& - user-agent/cookie/header/request_body: 无限制 - method: HTTP协议支持的method，字母大写 - protocol:    - http   - https  **默认取值：** 不涉及

        :param contents: The contents of this CreateCondition.
        :type contents: list[str]
        """
        self._contents = contents

    @property
    def check_all_indexes_logic(self):
        r"""Gets the check_all_indexes_logic of this CreateCondition.

        **参数解释：** 需要检查所有子字段或检查任意子字段时传此参数 **约束限制：** 仅当category为params/cookie/header时支持 **取值范围：** - 1：所有子字段 - 2：任意子字段  **默认取值：** 不涉及

        :return: The check_all_indexes_logic of this CreateCondition.
        :rtype: int
        """
        return self._check_all_indexes_logic

    @check_all_indexes_logic.setter
    def check_all_indexes_logic(self, check_all_indexes_logic):
        r"""Sets the check_all_indexes_logic of this CreateCondition.

        **参数解释：** 需要检查所有子字段或检查任意子字段时传此参数 **约束限制：** 仅当category为params/cookie/header时支持 **取值范围：** - 1：所有子字段 - 2：任意子字段  **默认取值：** 不涉及

        :param check_all_indexes_logic: The check_all_indexes_logic of this CreateCondition.
        :type check_all_indexes_logic: int
        """
        self._check_all_indexes_logic = check_all_indexes_logic

    @property
    def value_list_id(self):
        r"""Gets the value_list_id of this CreateCondition.

        **参数解释：** 引用表ID **约束限制：** 当logic_operation参数以any或者all结尾时，需要传该参数；引用表类型要与category类型保持一致 **取值范围：** 通过ListValueList接口获取引用表ID  **默认取值：** 不涉及

        :return: The value_list_id of this CreateCondition.
        :rtype: str
        """
        return self._value_list_id

    @value_list_id.setter
    def value_list_id(self, value_list_id):
        r"""Sets the value_list_id of this CreateCondition.

        **参数解释：** 引用表ID **约束限制：** 当logic_operation参数以any或者all结尾时，需要传该参数；引用表类型要与category类型保持一致 **取值范围：** 通过ListValueList接口获取引用表ID  **默认取值：** 不涉及

        :param value_list_id: The value_list_id of this CreateCondition.
        :type value_list_id: str
        """
        self._value_list_id = value_list_id

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
        if not isinstance(other, CreateCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
