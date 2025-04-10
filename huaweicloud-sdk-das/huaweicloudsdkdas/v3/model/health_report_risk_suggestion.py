# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HealthReportRiskSuggestion:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'suggestion_code': 'str',
        'suggestion_content': 'str'
    }

    attribute_map = {
        'suggestion_code': 'suggestion_code',
        'suggestion_content': 'suggestion_content'
    }

    def __init__(self, suggestion_code=None, suggestion_content=None):
        r"""HealthReportRiskSuggestion

        The model defined in huaweicloud sdk

        :param suggestion_code: 建议优化措施编码。
        :type suggestion_code: str
        :param suggestion_content: 建议优化措施。
        :type suggestion_content: str
        """
        
        

        self._suggestion_code = None
        self._suggestion_content = None
        self.discriminator = None

        self.suggestion_code = suggestion_code
        self.suggestion_content = suggestion_content

    @property
    def suggestion_code(self):
        r"""Gets the suggestion_code of this HealthReportRiskSuggestion.

        建议优化措施编码。

        :return: The suggestion_code of this HealthReportRiskSuggestion.
        :rtype: str
        """
        return self._suggestion_code

    @suggestion_code.setter
    def suggestion_code(self, suggestion_code):
        r"""Sets the suggestion_code of this HealthReportRiskSuggestion.

        建议优化措施编码。

        :param suggestion_code: The suggestion_code of this HealthReportRiskSuggestion.
        :type suggestion_code: str
        """
        self._suggestion_code = suggestion_code

    @property
    def suggestion_content(self):
        r"""Gets the suggestion_content of this HealthReportRiskSuggestion.

        建议优化措施。

        :return: The suggestion_content of this HealthReportRiskSuggestion.
        :rtype: str
        """
        return self._suggestion_content

    @suggestion_content.setter
    def suggestion_content(self, suggestion_content):
        r"""Sets the suggestion_content of this HealthReportRiskSuggestion.

        建议优化措施。

        :param suggestion_content: The suggestion_content of this HealthReportRiskSuggestion.
        :type suggestion_content: str
        """
        self._suggestion_content = suggestion_content

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
        if not isinstance(other, HealthReportRiskSuggestion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
