# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReportSummaryVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'case_success_rate': 'str',
        'case_complete_rate': 'str'
    }

    attribute_map = {
        'case_success_rate': 'case_success_rate',
        'case_complete_rate': 'case_complete_rate'
    }

    def __init__(self, case_success_rate=None, case_complete_rate=None):
        """ReportSummaryVo

        The model defined in huaweicloud sdk

        :param case_success_rate: 用例通过率
        :type case_success_rate: str
        :param case_complete_rate: 用例完成率
        :type case_complete_rate: str
        """
        
        

        self._case_success_rate = None
        self._case_complete_rate = None
        self.discriminator = None

        if case_success_rate is not None:
            self.case_success_rate = case_success_rate
        if case_complete_rate is not None:
            self.case_complete_rate = case_complete_rate

    @property
    def case_success_rate(self):
        """Gets the case_success_rate of this ReportSummaryVo.

        用例通过率

        :return: The case_success_rate of this ReportSummaryVo.
        :rtype: str
        """
        return self._case_success_rate

    @case_success_rate.setter
    def case_success_rate(self, case_success_rate):
        """Sets the case_success_rate of this ReportSummaryVo.

        用例通过率

        :param case_success_rate: The case_success_rate of this ReportSummaryVo.
        :type case_success_rate: str
        """
        self._case_success_rate = case_success_rate

    @property
    def case_complete_rate(self):
        """Gets the case_complete_rate of this ReportSummaryVo.

        用例完成率

        :return: The case_complete_rate of this ReportSummaryVo.
        :rtype: str
        """
        return self._case_complete_rate

    @case_complete_rate.setter
    def case_complete_rate(self, case_complete_rate):
        """Sets the case_complete_rate of this ReportSummaryVo.

        用例完成率

        :param case_complete_rate: The case_complete_rate of this ReportSummaryVo.
        :type case_complete_rate: str
        """
        self._case_complete_rate = case_complete_rate

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
        if not isinstance(other, ReportSummaryVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
