# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDiagnosisReportsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'diagnosis_report_list': 'list[DiagnosisReportResp]'
    }

    attribute_map = {
        'diagnosis_report_list': 'diagnosis_report_list'
    }

    def __init__(self, diagnosis_report_list=None):
        r"""ListDiagnosisReportsResponse

        The model defined in huaweicloud sdk

        :param diagnosis_report_list: **参数解释**： 诊断报告列表。 **取值范围**： 不涉及。
        :type diagnosis_report_list: list[:class:`huaweicloudsdkrocketmq.v2.DiagnosisReportResp`]
        """
        
        super(ListDiagnosisReportsResponse, self).__init__()

        self._diagnosis_report_list = None
        self.discriminator = None

        if diagnosis_report_list is not None:
            self.diagnosis_report_list = diagnosis_report_list

    @property
    def diagnosis_report_list(self):
        r"""Gets the diagnosis_report_list of this ListDiagnosisReportsResponse.

        **参数解释**： 诊断报告列表。 **取值范围**： 不涉及。

        :return: The diagnosis_report_list of this ListDiagnosisReportsResponse.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.DiagnosisReportResp`]
        """
        return self._diagnosis_report_list

    @diagnosis_report_list.setter
    def diagnosis_report_list(self, diagnosis_report_list):
        r"""Sets the diagnosis_report_list of this ListDiagnosisReportsResponse.

        **参数解释**： 诊断报告列表。 **取值范围**： 不涉及。

        :param diagnosis_report_list: The diagnosis_report_list of this ListDiagnosisReportsResponse.
        :type diagnosis_report_list: list[:class:`huaweicloudsdkrocketmq.v2.DiagnosisReportResp`]
        """
        self._diagnosis_report_list = diagnosis_report_list

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
        if not isinstance(other, ListDiagnosisReportsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
