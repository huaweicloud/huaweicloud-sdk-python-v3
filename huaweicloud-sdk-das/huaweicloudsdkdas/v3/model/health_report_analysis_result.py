# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HealthReportAnalysisResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'risk_code': 'str',
        'risk_level': 'str',
        'risk_content': 'str',
        'reasons': 'list[HealthReportRiskReason]'
    }

    attribute_map = {
        'risk_code': 'risk_code',
        'risk_level': 'risk_level',
        'risk_content': 'risk_content',
        'reasons': 'reasons'
    }

    def __init__(self, risk_code=None, risk_level=None, risk_content=None, reasons=None):
        r"""HealthReportAnalysisResult

        The model defined in huaweicloud sdk

        :param risk_code: 风险点编码。
        :type risk_code: str
        :param risk_level: 风险点级别。
        :type risk_level: str
        :param risk_content: 风险点内容。
        :type risk_content: str
        :param reasons: 可能原因列表。
        :type reasons: list[:class:`huaweicloudsdkdas.v3.HealthReportRiskReason`]
        """
        
        

        self._risk_code = None
        self._risk_level = None
        self._risk_content = None
        self._reasons = None
        self.discriminator = None

        self.risk_code = risk_code
        self.risk_level = risk_level
        self.risk_content = risk_content
        self.reasons = reasons

    @property
    def risk_code(self):
        r"""Gets the risk_code of this HealthReportAnalysisResult.

        风险点编码。

        :return: The risk_code of this HealthReportAnalysisResult.
        :rtype: str
        """
        return self._risk_code

    @risk_code.setter
    def risk_code(self, risk_code):
        r"""Sets the risk_code of this HealthReportAnalysisResult.

        风险点编码。

        :param risk_code: The risk_code of this HealthReportAnalysisResult.
        :type risk_code: str
        """
        self._risk_code = risk_code

    @property
    def risk_level(self):
        r"""Gets the risk_level of this HealthReportAnalysisResult.

        风险点级别。

        :return: The risk_level of this HealthReportAnalysisResult.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        r"""Sets the risk_level of this HealthReportAnalysisResult.

        风险点级别。

        :param risk_level: The risk_level of this HealthReportAnalysisResult.
        :type risk_level: str
        """
        self._risk_level = risk_level

    @property
    def risk_content(self):
        r"""Gets the risk_content of this HealthReportAnalysisResult.

        风险点内容。

        :return: The risk_content of this HealthReportAnalysisResult.
        :rtype: str
        """
        return self._risk_content

    @risk_content.setter
    def risk_content(self, risk_content):
        r"""Sets the risk_content of this HealthReportAnalysisResult.

        风险点内容。

        :param risk_content: The risk_content of this HealthReportAnalysisResult.
        :type risk_content: str
        """
        self._risk_content = risk_content

    @property
    def reasons(self):
        r"""Gets the reasons of this HealthReportAnalysisResult.

        可能原因列表。

        :return: The reasons of this HealthReportAnalysisResult.
        :rtype: list[:class:`huaweicloudsdkdas.v3.HealthReportRiskReason`]
        """
        return self._reasons

    @reasons.setter
    def reasons(self, reasons):
        r"""Sets the reasons of this HealthReportAnalysisResult.

        可能原因列表。

        :param reasons: The reasons of this HealthReportAnalysisResult.
        :type reasons: list[:class:`huaweicloudsdkdas.v3.HealthReportRiskReason`]
        """
        self._reasons = reasons

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
        if not isinstance(other, HealthReportAnalysisResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
