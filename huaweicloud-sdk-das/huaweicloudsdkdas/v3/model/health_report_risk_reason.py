# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HealthReportRiskReason:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'reason_code': 'str',
        'reason_content': 'str',
        'suggestions': 'list[HealthReportRiskSuggestion]'
    }

    attribute_map = {
        'reason_code': 'reason_code',
        'reason_content': 'reason_content',
        'suggestions': 'suggestions'
    }

    def __init__(self, reason_code=None, reason_content=None, suggestions=None):
        r"""HealthReportRiskReason

        The model defined in huaweicloud sdk

        :param reason_code: 可能原因编码。
        :type reason_code: str
        :param reason_content: 可能原因内容。
        :type reason_content: str
        :param suggestions: 建议优化措施列表。
        :type suggestions: list[:class:`huaweicloudsdkdas.v3.HealthReportRiskSuggestion`]
        """
        
        

        self._reason_code = None
        self._reason_content = None
        self._suggestions = None
        self.discriminator = None

        self.reason_code = reason_code
        self.reason_content = reason_content
        self.suggestions = suggestions

    @property
    def reason_code(self):
        r"""Gets the reason_code of this HealthReportRiskReason.

        可能原因编码。

        :return: The reason_code of this HealthReportRiskReason.
        :rtype: str
        """
        return self._reason_code

    @reason_code.setter
    def reason_code(self, reason_code):
        r"""Sets the reason_code of this HealthReportRiskReason.

        可能原因编码。

        :param reason_code: The reason_code of this HealthReportRiskReason.
        :type reason_code: str
        """
        self._reason_code = reason_code

    @property
    def reason_content(self):
        r"""Gets the reason_content of this HealthReportRiskReason.

        可能原因内容。

        :return: The reason_content of this HealthReportRiskReason.
        :rtype: str
        """
        return self._reason_content

    @reason_content.setter
    def reason_content(self, reason_content):
        r"""Sets the reason_content of this HealthReportRiskReason.

        可能原因内容。

        :param reason_content: The reason_content of this HealthReportRiskReason.
        :type reason_content: str
        """
        self._reason_content = reason_content

    @property
    def suggestions(self):
        r"""Gets the suggestions of this HealthReportRiskReason.

        建议优化措施列表。

        :return: The suggestions of this HealthReportRiskReason.
        :rtype: list[:class:`huaweicloudsdkdas.v3.HealthReportRiskSuggestion`]
        """
        return self._suggestions

    @suggestions.setter
    def suggestions(self, suggestions):
        r"""Sets the suggestions of this HealthReportRiskReason.

        建议优化措施列表。

        :param suggestions: The suggestions of this HealthReportRiskReason.
        :type suggestions: list[:class:`huaweicloudsdkdas.v3.HealthReportRiskSuggestion`]
        """
        self._suggestions = suggestions

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
        if not isinstance(other, HealthReportRiskReason):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
