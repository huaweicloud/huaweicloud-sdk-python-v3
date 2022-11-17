# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDiagnosisTasksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'diagnosis_report_list': 'list[DiagnosisReportInfo]',
        'total_num': 'int'
    }

    attribute_map = {
        'diagnosis_report_list': 'diagnosis_report_list',
        'total_num': 'total_num'
    }

    def __init__(self, diagnosis_report_list=None, total_num=None):
        """ListDiagnosisTasksResponse

        The model defined in huaweicloud sdk

        :param diagnosis_report_list: 诊断报告列表
        :type diagnosis_report_list: list[:class:`huaweicloudsdkdcs.v2.DiagnosisReportInfo`]
        :param total_num: 诊断报告总数
        :type total_num: int
        """
        
        super(ListDiagnosisTasksResponse, self).__init__()

        self._diagnosis_report_list = None
        self._total_num = None
        self.discriminator = None

        if diagnosis_report_list is not None:
            self.diagnosis_report_list = diagnosis_report_list
        if total_num is not None:
            self.total_num = total_num

    @property
    def diagnosis_report_list(self):
        """Gets the diagnosis_report_list of this ListDiagnosisTasksResponse.

        诊断报告列表

        :return: The diagnosis_report_list of this ListDiagnosisTasksResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.DiagnosisReportInfo`]
        """
        return self._diagnosis_report_list

    @diagnosis_report_list.setter
    def diagnosis_report_list(self, diagnosis_report_list):
        """Sets the diagnosis_report_list of this ListDiagnosisTasksResponse.

        诊断报告列表

        :param diagnosis_report_list: The diagnosis_report_list of this ListDiagnosisTasksResponse.
        :type diagnosis_report_list: list[:class:`huaweicloudsdkdcs.v2.DiagnosisReportInfo`]
        """
        self._diagnosis_report_list = diagnosis_report_list

    @property
    def total_num(self):
        """Gets the total_num of this ListDiagnosisTasksResponse.

        诊断报告总数

        :return: The total_num of this ListDiagnosisTasksResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        """Sets the total_num of this ListDiagnosisTasksResponse.

        诊断报告总数

        :param total_num: The total_num of this ListDiagnosisTasksResponse.
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
        if not isinstance(other, ListDiagnosisTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
