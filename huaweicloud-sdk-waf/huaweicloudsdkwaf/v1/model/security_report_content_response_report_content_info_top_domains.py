# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityReportContentResponseReportContentInfoTopDomains:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'num': 'int',
        'host': 'str',
        'web_tag': 'str',
        'block_num': 'int',
        'only_log_num': 'int'
    }

    attribute_map = {
        'key': 'key',
        'num': 'num',
        'host': 'host',
        'web_tag': 'web_tag',
        'block_num': 'block_num',
        'only_log_num': 'only_log_num'
    }

    def __init__(self, key=None, num=None, host=None, web_tag=None, block_num=None, only_log_num=None):
        r"""SecurityReportContentResponseReportContentInfoTopDomains

        The model defined in huaweicloud sdk

        :param key: **参数解释：** 域名标识。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type key: str
        :param num: **参数解释：** 该域名在对应统计维度下的数量。 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 0
        :type num: int
        :param host: **参数解释：** 域名标识，包含域名及关联标识。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type host: str
        :param web_tag: **参数解释：** 域名的Web标签。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type web_tag: str
        :param block_num: **参数解释：** 该域名拦截数量。 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 不涉及
        :type block_num: int
        :param only_log_num: **参数解释：** 该域名仅记录数量。 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 不涉及
        :type only_log_num: int
        """
        
        

        self._key = None
        self._num = None
        self._host = None
        self._web_tag = None
        self._block_num = None
        self._only_log_num = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if num is not None:
            self.num = num
        if host is not None:
            self.host = host
        if web_tag is not None:
            self.web_tag = web_tag
        if block_num is not None:
            self.block_num = block_num
        if only_log_num is not None:
            self.only_log_num = only_log_num

    @property
    def key(self):
        r"""Gets the key of this SecurityReportContentResponseReportContentInfoTopDomains.

        **参数解释：** 域名标识。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The key of this SecurityReportContentResponseReportContentInfoTopDomains.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this SecurityReportContentResponseReportContentInfoTopDomains.

        **参数解释：** 域名标识。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param key: The key of this SecurityReportContentResponseReportContentInfoTopDomains.
        :type key: str
        """
        self._key = key

    @property
    def num(self):
        r"""Gets the num of this SecurityReportContentResponseReportContentInfoTopDomains.

        **参数解释：** 该域名在对应统计维度下的数量。 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 0

        :return: The num of this SecurityReportContentResponseReportContentInfoTopDomains.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        r"""Sets the num of this SecurityReportContentResponseReportContentInfoTopDomains.

        **参数解释：** 该域名在对应统计维度下的数量。 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 0

        :param num: The num of this SecurityReportContentResponseReportContentInfoTopDomains.
        :type num: int
        """
        self._num = num

    @property
    def host(self):
        r"""Gets the host of this SecurityReportContentResponseReportContentInfoTopDomains.

        **参数解释：** 域名标识，包含域名及关联标识。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The host of this SecurityReportContentResponseReportContentInfoTopDomains.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this SecurityReportContentResponseReportContentInfoTopDomains.

        **参数解释：** 域名标识，包含域名及关联标识。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param host: The host of this SecurityReportContentResponseReportContentInfoTopDomains.
        :type host: str
        """
        self._host = host

    @property
    def web_tag(self):
        r"""Gets the web_tag of this SecurityReportContentResponseReportContentInfoTopDomains.

        **参数解释：** 域名的Web标签。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The web_tag of this SecurityReportContentResponseReportContentInfoTopDomains.
        :rtype: str
        """
        return self._web_tag

    @web_tag.setter
    def web_tag(self, web_tag):
        r"""Sets the web_tag of this SecurityReportContentResponseReportContentInfoTopDomains.

        **参数解释：** 域名的Web标签。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param web_tag: The web_tag of this SecurityReportContentResponseReportContentInfoTopDomains.
        :type web_tag: str
        """
        self._web_tag = web_tag

    @property
    def block_num(self):
        r"""Gets the block_num of this SecurityReportContentResponseReportContentInfoTopDomains.

        **参数解释：** 该域名拦截数量。 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 不涉及

        :return: The block_num of this SecurityReportContentResponseReportContentInfoTopDomains.
        :rtype: int
        """
        return self._block_num

    @block_num.setter
    def block_num(self, block_num):
        r"""Sets the block_num of this SecurityReportContentResponseReportContentInfoTopDomains.

        **参数解释：** 该域名拦截数量。 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 不涉及

        :param block_num: The block_num of this SecurityReportContentResponseReportContentInfoTopDomains.
        :type block_num: int
        """
        self._block_num = block_num

    @property
    def only_log_num(self):
        r"""Gets the only_log_num of this SecurityReportContentResponseReportContentInfoTopDomains.

        **参数解释：** 该域名仅记录数量。 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 不涉及

        :return: The only_log_num of this SecurityReportContentResponseReportContentInfoTopDomains.
        :rtype: int
        """
        return self._only_log_num

    @only_log_num.setter
    def only_log_num(self, only_log_num):
        r"""Sets the only_log_num of this SecurityReportContentResponseReportContentInfoTopDomains.

        **参数解释：** 该域名仅记录数量。 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 不涉及

        :param only_log_num: The only_log_num of this SecurityReportContentResponseReportContentInfoTopDomains.
        :type only_log_num: int
        """
        self._only_log_num = only_log_num

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
        if not isinstance(other, SecurityReportContentResponseReportContentInfoTopDomains):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
