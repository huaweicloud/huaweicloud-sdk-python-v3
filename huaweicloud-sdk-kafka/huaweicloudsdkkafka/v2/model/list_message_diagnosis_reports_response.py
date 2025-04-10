# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMessageDiagnosisReportsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'report_list': 'list[KafkaMessageDiagnosisReportInfoEntity]',
        'total_num': 'int'
    }

    attribute_map = {
        'report_list': 'report_list',
        'total_num': 'total_num'
    }

    def __init__(self, report_list=None, total_num=None):
        r"""ListMessageDiagnosisReportsResponse

        The model defined in huaweicloud sdk

        :param report_list: 诊断报告列表
        :type report_list: list[:class:`huaweicloudsdkkafka.v2.KafkaMessageDiagnosisReportInfoEntity`]
        :param total_num: 诊断报告总数
        :type total_num: int
        """
        
        super(ListMessageDiagnosisReportsResponse, self).__init__()

        self._report_list = None
        self._total_num = None
        self.discriminator = None

        if report_list is not None:
            self.report_list = report_list
        if total_num is not None:
            self.total_num = total_num

    @property
    def report_list(self):
        r"""Gets the report_list of this ListMessageDiagnosisReportsResponse.

        诊断报告列表

        :return: The report_list of this ListMessageDiagnosisReportsResponse.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.KafkaMessageDiagnosisReportInfoEntity`]
        """
        return self._report_list

    @report_list.setter
    def report_list(self, report_list):
        r"""Sets the report_list of this ListMessageDiagnosisReportsResponse.

        诊断报告列表

        :param report_list: The report_list of this ListMessageDiagnosisReportsResponse.
        :type report_list: list[:class:`huaweicloudsdkkafka.v2.KafkaMessageDiagnosisReportInfoEntity`]
        """
        self._report_list = report_list

    @property
    def total_num(self):
        r"""Gets the total_num of this ListMessageDiagnosisReportsResponse.

        诊断报告总数

        :return: The total_num of this ListMessageDiagnosisReportsResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ListMessageDiagnosisReportsResponse.

        诊断报告总数

        :param total_num: The total_num of this ListMessageDiagnosisReportsResponse.
        :type total_num: int
        """
        self._total_num = total_num

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
        if not isinstance(other, ListMessageDiagnosisReportsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
