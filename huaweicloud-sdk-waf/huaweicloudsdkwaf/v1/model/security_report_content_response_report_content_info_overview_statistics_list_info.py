# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityReportContentResponseReportContentInfoOverviewStatisticsListInfo:

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
        'top_domains': 'list[SecurityReportContentResponseReportContentInfoTopDomains]'
    }

    attribute_map = {
        'key': 'key',
        'num': 'num',
        'top_domains': 'top_domains'
    }

    def __init__(self, key=None, num=None, top_domains=None):
        r"""SecurityReportContentResponseReportContentInfoOverviewStatisticsListInfo

        The model defined in huaweicloud sdk

        :param key: **参数解释：** 统计维度标识（如ACCESS表示访问类统计）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type key: str
        :param num: **参数解释：** 该统计维度的总数量。 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 0
        :type num: int
        :param top_domains: **参数解释：** TOP域名列表，按统计数量排序的域名信息。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type top_domains: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoTopDomains`]
        """
        
        

        self._key = None
        self._num = None
        self._top_domains = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if num is not None:
            self.num = num
        if top_domains is not None:
            self.top_domains = top_domains

    @property
    def key(self):
        r"""Gets the key of this SecurityReportContentResponseReportContentInfoOverviewStatisticsListInfo.

        **参数解释：** 统计维度标识（如ACCESS表示访问类统计）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The key of this SecurityReportContentResponseReportContentInfoOverviewStatisticsListInfo.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this SecurityReportContentResponseReportContentInfoOverviewStatisticsListInfo.

        **参数解释：** 统计维度标识（如ACCESS表示访问类统计）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param key: The key of this SecurityReportContentResponseReportContentInfoOverviewStatisticsListInfo.
        :type key: str
        """
        self._key = key

    @property
    def num(self):
        r"""Gets the num of this SecurityReportContentResponseReportContentInfoOverviewStatisticsListInfo.

        **参数解释：** 该统计维度的总数量。 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 0

        :return: The num of this SecurityReportContentResponseReportContentInfoOverviewStatisticsListInfo.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        r"""Sets the num of this SecurityReportContentResponseReportContentInfoOverviewStatisticsListInfo.

        **参数解释：** 该统计维度的总数量。 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 0

        :param num: The num of this SecurityReportContentResponseReportContentInfoOverviewStatisticsListInfo.
        :type num: int
        """
        self._num = num

    @property
    def top_domains(self):
        r"""Gets the top_domains of this SecurityReportContentResponseReportContentInfoOverviewStatisticsListInfo.

        **参数解释：** TOP域名列表，按统计数量排序的域名信息。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The top_domains of this SecurityReportContentResponseReportContentInfoOverviewStatisticsListInfo.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoTopDomains`]
        """
        return self._top_domains

    @top_domains.setter
    def top_domains(self, top_domains):
        r"""Sets the top_domains of this SecurityReportContentResponseReportContentInfoOverviewStatisticsListInfo.

        **参数解释：** TOP域名列表，按统计数量排序的域名信息。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param top_domains: The top_domains of this SecurityReportContentResponseReportContentInfoOverviewStatisticsListInfo.
        :type top_domains: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoTopDomains`]
        """
        self._top_domains = top_domains

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
        if not isinstance(other, SecurityReportContentResponseReportContentInfoOverviewStatisticsListInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
