# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Condition:

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
        'contents': 'list[str]',
        'index': 'str',
        'logic_operation': 'str'
    }

    attribute_map = {
        'category': 'category',
        'contents': 'contents',
        'index': 'index',
        'logic_operation': 'logic_operation'
    }

    def __init__(self, category=None, contents=None, index=None, logic_operation=None):
        r"""Condition

        The model defined in huaweicloud sdk

        :param category: 字段类型 url：路径 ip：IPv4 ipv6：IPv6 params：Params cookie：Cookie header：Header response_code：Response Code
        :type category: str
        :param contents: 条件列表逻辑匹配内容。 当匹配逻辑为exist或not_exist时，contents必须为空，其他情况下contents必填且长度不超过2048 当category为response_code时，contents状态码为200~599，正则为 ^(?:[2-5]\\d{2})$ 当匹配逻辑包含\&quot;len\&quot;时，contents必须为0~65535的整数；当匹配逻辑包含\&quot;num\&quot;时，contents必须为0~512的整数
        :type contents: list[str]
        :param index: 子字段 当字段类型为ip或ipv6时，index必填且必须为：client-ip：客户端IP、x-forwarded-for：X-Forwarded-For、TCP连接IP: $remote_addr 当字段类型（category）选择“params”、“cookie”、“header”时，请根据实际需求配置子字段且该参数必填。 当匹配逻辑为num_greater、num_less、num_equal、num_not_equal时，子字段必须为空 当子字段不为空时，最大长度不超过2048
        :type index: str
        :param logic_operation: 条件列表匹配逻辑。 如果字段类型category是url，匹配逻辑可以为：contain、 not_contain、 equal、 not_equal、 prefix、 not_prefix、 suffix、 not_suffix、 len_greater、 len_less、len_equal或者len_not_equal 如果字段类型category是ip、ipv6或response_code，匹配逻辑可以为： equal、not_equal 如果字段类型category是params、cookie或者header, 匹配逻辑可以为：contain、 not_contain、 equal、 not_equal、 prefix、 not_prefix、 suffix、 not_suffix、 len_greater、 len_less、len_equal、len_not_equal、num_greater、num_less、num_equal、num_not_equal、exist或者not_exist
        :type logic_operation: str
        """
        
        

        self._category = None
        self._contents = None
        self._index = None
        self._logic_operation = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if contents is not None:
            self.contents = contents
        if index is not None:
            self.index = index
        if logic_operation is not None:
            self.logic_operation = logic_operation

    @property
    def category(self):
        r"""Gets the category of this Condition.

        字段类型 url：路径 ip：IPv4 ipv6：IPv6 params：Params cookie：Cookie header：Header response_code：Response Code

        :return: The category of this Condition.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this Condition.

        字段类型 url：路径 ip：IPv4 ipv6：IPv6 params：Params cookie：Cookie header：Header response_code：Response Code

        :param category: The category of this Condition.
        :type category: str
        """
        self._category = category

    @property
    def contents(self):
        r"""Gets the contents of this Condition.

        条件列表逻辑匹配内容。 当匹配逻辑为exist或not_exist时，contents必须为空，其他情况下contents必填且长度不超过2048 当category为response_code时，contents状态码为200~599，正则为 ^(?:[2-5]\\d{2})$ 当匹配逻辑包含\"len\"时，contents必须为0~65535的整数；当匹配逻辑包含\"num\"时，contents必须为0~512的整数

        :return: The contents of this Condition.
        :rtype: list[str]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        r"""Sets the contents of this Condition.

        条件列表逻辑匹配内容。 当匹配逻辑为exist或not_exist时，contents必须为空，其他情况下contents必填且长度不超过2048 当category为response_code时，contents状态码为200~599，正则为 ^(?:[2-5]\\d{2})$ 当匹配逻辑包含\"len\"时，contents必须为0~65535的整数；当匹配逻辑包含\"num\"时，contents必须为0~512的整数

        :param contents: The contents of this Condition.
        :type contents: list[str]
        """
        self._contents = contents

    @property
    def index(self):
        r"""Gets the index of this Condition.

        子字段 当字段类型为ip或ipv6时，index必填且必须为：client-ip：客户端IP、x-forwarded-for：X-Forwarded-For、TCP连接IP: $remote_addr 当字段类型（category）选择“params”、“cookie”、“header”时，请根据实际需求配置子字段且该参数必填。 当匹配逻辑为num_greater、num_less、num_equal、num_not_equal时，子字段必须为空 当子字段不为空时，最大长度不超过2048

        :return: The index of this Condition.
        :rtype: str
        """
        return self._index

    @index.setter
    def index(self, index):
        r"""Sets the index of this Condition.

        子字段 当字段类型为ip或ipv6时，index必填且必须为：client-ip：客户端IP、x-forwarded-for：X-Forwarded-For、TCP连接IP: $remote_addr 当字段类型（category）选择“params”、“cookie”、“header”时，请根据实际需求配置子字段且该参数必填。 当匹配逻辑为num_greater、num_less、num_equal、num_not_equal时，子字段必须为空 当子字段不为空时，最大长度不超过2048

        :param index: The index of this Condition.
        :type index: str
        """
        self._index = index

    @property
    def logic_operation(self):
        r"""Gets the logic_operation of this Condition.

        条件列表匹配逻辑。 如果字段类型category是url，匹配逻辑可以为：contain、 not_contain、 equal、 not_equal、 prefix、 not_prefix、 suffix、 not_suffix、 len_greater、 len_less、len_equal或者len_not_equal 如果字段类型category是ip、ipv6或response_code，匹配逻辑可以为： equal、not_equal 如果字段类型category是params、cookie或者header, 匹配逻辑可以为：contain、 not_contain、 equal、 not_equal、 prefix、 not_prefix、 suffix、 not_suffix、 len_greater、 len_less、len_equal、len_not_equal、num_greater、num_less、num_equal、num_not_equal、exist或者not_exist

        :return: The logic_operation of this Condition.
        :rtype: str
        """
        return self._logic_operation

    @logic_operation.setter
    def logic_operation(self, logic_operation):
        r"""Sets the logic_operation of this Condition.

        条件列表匹配逻辑。 如果字段类型category是url，匹配逻辑可以为：contain、 not_contain、 equal、 not_equal、 prefix、 not_prefix、 suffix、 not_suffix、 len_greater、 len_less、len_equal或者len_not_equal 如果字段类型category是ip、ipv6或response_code，匹配逻辑可以为： equal、not_equal 如果字段类型category是params、cookie或者header, 匹配逻辑可以为：contain、 not_contain、 equal、 not_equal、 prefix、 not_prefix、 suffix、 not_suffix、 len_greater、 len_less、len_equal、len_not_equal、num_greater、num_less、num_equal、num_not_equal、exist或者not_exist

        :param logic_operation: The logic_operation of this Condition.
        :type logic_operation: str
        """
        self._logic_operation = logic_operation

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
        if not isinstance(other, Condition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
