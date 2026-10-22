# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoDocCountItems:

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
        'doc_count': 'int'
    }

    attribute_map = {
        'key': 'key',
        'doc_count': 'doc_count'
    }

    def __init__(self, key=None, doc_count=None):
        r"""SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoDocCountItems

        The model defined in huaweicloud sdk

        :param key: **参数解释：** 响应码标识。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type key: str
        :param doc_count: **参数解释：** 该响应码的文档计数。 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 0
        :type doc_count: int
        """
        
        

        self._key = None
        self._doc_count = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if doc_count is not None:
            self.doc_count = doc_count

    @property
    def key(self):
        r"""Gets the key of this SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoDocCountItems.

        **参数解释：** 响应码标识。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The key of this SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoDocCountItems.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoDocCountItems.

        **参数解释：** 响应码标识。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param key: The key of this SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoDocCountItems.
        :type key: str
        """
        self._key = key

    @property
    def doc_count(self):
        r"""Gets the doc_count of this SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoDocCountItems.

        **参数解释：** 该响应码的文档计数。 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 0

        :return: The doc_count of this SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoDocCountItems.
        :rtype: int
        """
        return self._doc_count

    @doc_count.setter
    def doc_count(self, doc_count):
        r"""Sets the doc_count of this SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoDocCountItems.

        **参数解释：** 该响应码的文档计数。 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 0

        :param doc_count: The doc_count of this SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoDocCountItems.
        :type doc_count: int
        """
        self._doc_count = doc_count

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
        if not isinstance(other, SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoDocCountItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
