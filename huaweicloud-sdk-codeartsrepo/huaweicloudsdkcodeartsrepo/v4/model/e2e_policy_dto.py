# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class E2ePolicyDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auto_extract': 'bool',
        'prefix_symbol': 'str',
        'separator': 'str',
        'suffix_symbol': 'str'
    }

    attribute_map = {
        'auto_extract': 'auto_extract',
        'prefix_symbol': 'prefix_symbol',
        'separator': 'separator',
        'suffix_symbol': 'suffix_symbol'
    }

    def __init__(self, auto_extract=None, prefix_symbol=None, separator=None, suffix_symbol=None):
        r"""E2ePolicyDto

        The model defined in huaweicloud sdk

        :param auto_extract: **参数解释：** 是否开启单号自动提取。 **取值范围：** true：开启单号自动提取，false：未开启单号自动提取。
        :type auto_extract: bool
        :param prefix_symbol: **参数解释：** 自动提取时的单号前缀合集，英文逗号分隔。 **取值范围：** 单个前缀长度最多200个字符，最多允许配置10个前缀。
        :type prefix_symbol: str
        :param separator: **参数解释：** 自动提取时的分隔符。
        :type separator: str
        :param suffix_symbol: **参数解释：** 自动提取时的单号后缀。
        :type suffix_symbol: str
        """
        
        

        self._auto_extract = None
        self._prefix_symbol = None
        self._separator = None
        self._suffix_symbol = None
        self.discriminator = None

        if auto_extract is not None:
            self.auto_extract = auto_extract
        if prefix_symbol is not None:
            self.prefix_symbol = prefix_symbol
        if separator is not None:
            self.separator = separator
        if suffix_symbol is not None:
            self.suffix_symbol = suffix_symbol

    @property
    def auto_extract(self):
        r"""Gets the auto_extract of this E2ePolicyDto.

        **参数解释：** 是否开启单号自动提取。 **取值范围：** true：开启单号自动提取，false：未开启单号自动提取。

        :return: The auto_extract of this E2ePolicyDto.
        :rtype: bool
        """
        return self._auto_extract

    @auto_extract.setter
    def auto_extract(self, auto_extract):
        r"""Sets the auto_extract of this E2ePolicyDto.

        **参数解释：** 是否开启单号自动提取。 **取值范围：** true：开启单号自动提取，false：未开启单号自动提取。

        :param auto_extract: The auto_extract of this E2ePolicyDto.
        :type auto_extract: bool
        """
        self._auto_extract = auto_extract

    @property
    def prefix_symbol(self):
        r"""Gets the prefix_symbol of this E2ePolicyDto.

        **参数解释：** 自动提取时的单号前缀合集，英文逗号分隔。 **取值范围：** 单个前缀长度最多200个字符，最多允许配置10个前缀。

        :return: The prefix_symbol of this E2ePolicyDto.
        :rtype: str
        """
        return self._prefix_symbol

    @prefix_symbol.setter
    def prefix_symbol(self, prefix_symbol):
        r"""Sets the prefix_symbol of this E2ePolicyDto.

        **参数解释：** 自动提取时的单号前缀合集，英文逗号分隔。 **取值范围：** 单个前缀长度最多200个字符，最多允许配置10个前缀。

        :param prefix_symbol: The prefix_symbol of this E2ePolicyDto.
        :type prefix_symbol: str
        """
        self._prefix_symbol = prefix_symbol

    @property
    def separator(self):
        r"""Gets the separator of this E2ePolicyDto.

        **参数解释：** 自动提取时的分隔符。

        :return: The separator of this E2ePolicyDto.
        :rtype: str
        """
        return self._separator

    @separator.setter
    def separator(self, separator):
        r"""Sets the separator of this E2ePolicyDto.

        **参数解释：** 自动提取时的分隔符。

        :param separator: The separator of this E2ePolicyDto.
        :type separator: str
        """
        self._separator = separator

    @property
    def suffix_symbol(self):
        r"""Gets the suffix_symbol of this E2ePolicyDto.

        **参数解释：** 自动提取时的单号后缀。

        :return: The suffix_symbol of this E2ePolicyDto.
        :rtype: str
        """
        return self._suffix_symbol

    @suffix_symbol.setter
    def suffix_symbol(self, suffix_symbol):
        r"""Sets the suffix_symbol of this E2ePolicyDto.

        **参数解释：** 自动提取时的单号后缀。

        :param suffix_symbol: The suffix_symbol of this E2ePolicyDto.
        :type suffix_symbol: str
        """
        self._suffix_symbol = suffix_symbol

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
        if not isinstance(other, E2ePolicyDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
