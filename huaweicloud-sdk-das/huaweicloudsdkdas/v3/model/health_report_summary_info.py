# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HealthReportSummaryInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'analysis_results': 'list[HealthReportAnalysisResult]'
    }

    attribute_map = {
        'analysis_results': 'analysis_results'
    }

    def __init__(self, analysis_results=None):
        r"""HealthReportSummaryInfo

        The model defined in huaweicloud sdk

        :param analysis_results: 分析结果列表
        :type analysis_results: list[:class:`huaweicloudsdkdas.v3.HealthReportAnalysisResult`]
        """
        
        

        self._analysis_results = None
        self.discriminator = None

        self.analysis_results = analysis_results

    @property
    def analysis_results(self):
        r"""Gets the analysis_results of this HealthReportSummaryInfo.

        分析结果列表

        :return: The analysis_results of this HealthReportSummaryInfo.
        :rtype: list[:class:`huaweicloudsdkdas.v3.HealthReportAnalysisResult`]
        """
        return self._analysis_results

    @analysis_results.setter
    def analysis_results(self, analysis_results):
        r"""Sets the analysis_results of this HealthReportSummaryInfo.

        分析结果列表

        :param analysis_results: The analysis_results of this HealthReportSummaryInfo.
        :type analysis_results: list[:class:`huaweicloudsdkdas.v3.HealthReportAnalysisResult`]
        """
        self._analysis_results = analysis_results

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
        if not isinstance(other, HealthReportSummaryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
