# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HealthReportInspectionStat:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'inspection_score': 'list[HealthReportInspectionScore]',
        'analyze_success': 'bool',
        'error_message': 'str'
    }

    attribute_map = {
        'inspection_score': 'inspection_score',
        'analyze_success': 'analyze_success',
        'error_message': 'error_message'
    }

    def __init__(self, inspection_score=None, analyze_success=None, error_message=None):
        r"""HealthReportInspectionStat

        The model defined in huaweicloud sdk

        :param inspection_score: 巡检评分。
        :type inspection_score: list[:class:`huaweicloudsdkdas.v3.HealthReportInspectionScore`]
        :param analyze_success: 统计分析是否成功。
        :type analyze_success: bool
        :param error_message: 错误信息。
        :type error_message: str
        """
        
        

        self._inspection_score = None
        self._analyze_success = None
        self._error_message = None
        self.discriminator = None

        self.inspection_score = inspection_score
        self.analyze_success = analyze_success
        self.error_message = error_message

    @property
    def inspection_score(self):
        r"""Gets the inspection_score of this HealthReportInspectionStat.

        巡检评分。

        :return: The inspection_score of this HealthReportInspectionStat.
        :rtype: list[:class:`huaweicloudsdkdas.v3.HealthReportInspectionScore`]
        """
        return self._inspection_score

    @inspection_score.setter
    def inspection_score(self, inspection_score):
        r"""Sets the inspection_score of this HealthReportInspectionStat.

        巡检评分。

        :param inspection_score: The inspection_score of this HealthReportInspectionStat.
        :type inspection_score: list[:class:`huaweicloudsdkdas.v3.HealthReportInspectionScore`]
        """
        self._inspection_score = inspection_score

    @property
    def analyze_success(self):
        r"""Gets the analyze_success of this HealthReportInspectionStat.

        统计分析是否成功。

        :return: The analyze_success of this HealthReportInspectionStat.
        :rtype: bool
        """
        return self._analyze_success

    @analyze_success.setter
    def analyze_success(self, analyze_success):
        r"""Sets the analyze_success of this HealthReportInspectionStat.

        统计分析是否成功。

        :param analyze_success: The analyze_success of this HealthReportInspectionStat.
        :type analyze_success: bool
        """
        self._analyze_success = analyze_success

    @property
    def error_message(self):
        r"""Gets the error_message of this HealthReportInspectionStat.

        错误信息。

        :return: The error_message of this HealthReportInspectionStat.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this HealthReportInspectionStat.

        错误信息。

        :param error_message: The error_message of this HealthReportInspectionStat.
        :type error_message: str
        """
        self._error_message = error_message

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
        if not isinstance(other, HealthReportInspectionStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
