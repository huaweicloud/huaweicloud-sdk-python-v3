# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WafCustomCondition:

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
        'contents': 'list[str]'
    }

    attribute_map = {
        'category': 'category',
        'index': 'index',
        'logic_operation': 'logic_operation',
        'contents': 'contents'
    }

    def __init__(self, category=None, index=None, logic_operation=None, contents=None):
        r"""WafCustomCondition

        The model defined in huaweicloud sdk

        :param category: 字段类型 枚举值： url：路径 ip：IPv4 user-agent: User Agent method: Method referer: Referer params：Params cookie：Cookie header：Header request_line: Request Line request: Request
        :type category: str
        :param index: 子字段 - 当字段类型为url，user-agent、refer、request_line、method、request时，不需要传index参数 - 当字段类型为ip或ipv6时，index必填且必须为以下值：    client-ip：客户端IP    x-forwarded-for：X-Forwarded-For    TCP连接IP: $remote_addr - 当字段类型（category）选择“params”、“cookie”、“header”时，请根据实际需求配置子字段且该参数必填。 - 当匹配逻辑为num_greater、num_less、num_equal、num_not_equal时，子字段必须为空 - 当子字段不为空时，最大长度不超过2048
        :type index: str
        :param logic_operation: 条件列表匹配逻辑。 如果字段类型category是url、user-agent或者referer， 匹配逻辑可以为：contain、 not_contain、 equal、 not_equal、 prefix、 not_prefix、 suffix、 not_suffix、 len_greater、 len_less、len_equal或者len_not_equal 如果字段类型category是ip、ipv6或method，匹配逻辑可以为： equal、not_equal 如果字段类型category是request_line或者request, 匹配逻辑可以为： len_greater、len_less、len_equal或者len_not_equal 如果字段类型category是params、cookie或者header, 匹配逻辑可以为：contain、 not_contain、 equal、 not_equal、 prefix、 not_prefix、 suffix、 not_suffix、 len_greater、 len_less、len_equal、len_not_equal、num_greater、num_less、num_equal、num_not_equal、exist或者not_exist
        :type logic_operation: str
        :param contents: 条件列表逻辑匹配内容。 - 当匹配逻辑为exist或not_exist时，contents必须为空，其他情况下contents必填且长度不超过2048 - 当匹配逻辑包含\&quot;len\&quot;时，contents必须为0~65535的整数；当匹配逻辑包含\&quot;num\&quot;时，contents必须为0~512的整数 - 当category为method时, contents必须是1-64位大写字母
        :type contents: list[str]
        """
        
        

        self._category = None
        self._index = None
        self._logic_operation = None
        self._contents = None
        self.discriminator = None

        self.category = category
        if index is not None:
            self.index = index
        self.logic_operation = logic_operation
        self.contents = contents

    @property
    def category(self):
        r"""Gets the category of this WafCustomCondition.

        字段类型 枚举值： url：路径 ip：IPv4 user-agent: User Agent method: Method referer: Referer params：Params cookie：Cookie header：Header request_line: Request Line request: Request

        :return: The category of this WafCustomCondition.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this WafCustomCondition.

        字段类型 枚举值： url：路径 ip：IPv4 user-agent: User Agent method: Method referer: Referer params：Params cookie：Cookie header：Header request_line: Request Line request: Request

        :param category: The category of this WafCustomCondition.
        :type category: str
        """
        self._category = category

    @property
    def index(self):
        r"""Gets the index of this WafCustomCondition.

        子字段 - 当字段类型为url，user-agent、refer、request_line、method、request时，不需要传index参数 - 当字段类型为ip或ipv6时，index必填且必须为以下值：    client-ip：客户端IP    x-forwarded-for：X-Forwarded-For    TCP连接IP: $remote_addr - 当字段类型（category）选择“params”、“cookie”、“header”时，请根据实际需求配置子字段且该参数必填。 - 当匹配逻辑为num_greater、num_less、num_equal、num_not_equal时，子字段必须为空 - 当子字段不为空时，最大长度不超过2048

        :return: The index of this WafCustomCondition.
        :rtype: str
        """
        return self._index

    @index.setter
    def index(self, index):
        r"""Sets the index of this WafCustomCondition.

        子字段 - 当字段类型为url，user-agent、refer、request_line、method、request时，不需要传index参数 - 当字段类型为ip或ipv6时，index必填且必须为以下值：    client-ip：客户端IP    x-forwarded-for：X-Forwarded-For    TCP连接IP: $remote_addr - 当字段类型（category）选择“params”、“cookie”、“header”时，请根据实际需求配置子字段且该参数必填。 - 当匹配逻辑为num_greater、num_less、num_equal、num_not_equal时，子字段必须为空 - 当子字段不为空时，最大长度不超过2048

        :param index: The index of this WafCustomCondition.
        :type index: str
        """
        self._index = index

    @property
    def logic_operation(self):
        r"""Gets the logic_operation of this WafCustomCondition.

        条件列表匹配逻辑。 如果字段类型category是url、user-agent或者referer， 匹配逻辑可以为：contain、 not_contain、 equal、 not_equal、 prefix、 not_prefix、 suffix、 not_suffix、 len_greater、 len_less、len_equal或者len_not_equal 如果字段类型category是ip、ipv6或method，匹配逻辑可以为： equal、not_equal 如果字段类型category是request_line或者request, 匹配逻辑可以为： len_greater、len_less、len_equal或者len_not_equal 如果字段类型category是params、cookie或者header, 匹配逻辑可以为：contain、 not_contain、 equal、 not_equal、 prefix、 not_prefix、 suffix、 not_suffix、 len_greater、 len_less、len_equal、len_not_equal、num_greater、num_less、num_equal、num_not_equal、exist或者not_exist

        :return: The logic_operation of this WafCustomCondition.
        :rtype: str
        """
        return self._logic_operation

    @logic_operation.setter
    def logic_operation(self, logic_operation):
        r"""Sets the logic_operation of this WafCustomCondition.

        条件列表匹配逻辑。 如果字段类型category是url、user-agent或者referer， 匹配逻辑可以为：contain、 not_contain、 equal、 not_equal、 prefix、 not_prefix、 suffix、 not_suffix、 len_greater、 len_less、len_equal或者len_not_equal 如果字段类型category是ip、ipv6或method，匹配逻辑可以为： equal、not_equal 如果字段类型category是request_line或者request, 匹配逻辑可以为： len_greater、len_less、len_equal或者len_not_equal 如果字段类型category是params、cookie或者header, 匹配逻辑可以为：contain、 not_contain、 equal、 not_equal、 prefix、 not_prefix、 suffix、 not_suffix、 len_greater、 len_less、len_equal、len_not_equal、num_greater、num_less、num_equal、num_not_equal、exist或者not_exist

        :param logic_operation: The logic_operation of this WafCustomCondition.
        :type logic_operation: str
        """
        self._logic_operation = logic_operation

    @property
    def contents(self):
        r"""Gets the contents of this WafCustomCondition.

        条件列表逻辑匹配内容。 - 当匹配逻辑为exist或not_exist时，contents必须为空，其他情况下contents必填且长度不超过2048 - 当匹配逻辑包含\"len\"时，contents必须为0~65535的整数；当匹配逻辑包含\"num\"时，contents必须为0~512的整数 - 当category为method时, contents必须是1-64位大写字母

        :return: The contents of this WafCustomCondition.
        :rtype: list[str]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        r"""Sets the contents of this WafCustomCondition.

        条件列表逻辑匹配内容。 - 当匹配逻辑为exist或not_exist时，contents必须为空，其他情况下contents必填且长度不超过2048 - 当匹配逻辑包含\"len\"时，contents必须为0~65535的整数；当匹配逻辑包含\"num\"时，contents必须为0~512的整数 - 当category为method时, contents必须是1-64位大写字母

        :param contents: The contents of this WafCustomCondition.
        :type contents: list[str]
        """
        self._contents = contents

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
        if not isinstance(other, WafCustomCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
