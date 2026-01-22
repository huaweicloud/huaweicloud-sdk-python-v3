# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDiagnosisReportsForRocketMqResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'diagnosis_report_list': 'list[DiagnosisReportResp]',
        'total_num': 'object'
    }

    attribute_map = {
        'diagnosis_report_list': 'diagnosis_report_list',
        'total_num': 'total_num'
    }

    def __init__(self, diagnosis_report_list=None, total_num=None):
        r"""ListDiagnosisReportsForRocketMqResponse

        The model defined in huaweicloud sdk

        :param diagnosis_report_list: **参数解释**： 诊断报告列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type diagnosis_report_list: list[:class:`huaweicloudsdkrocketmq.v2.DiagnosisReportResp`]
        :param total_num: **参数解释**： 报告数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type total_num: object
        """
        
        super().__init__()

        self._diagnosis_report_list = None
        self._total_num = None
        self.discriminator = None

        if diagnosis_report_list is not None:
            self.diagnosis_report_list = diagnosis_report_list
        if total_num is not None:
            self.total_num = total_num

    @property
    def diagnosis_report_list(self):
        r"""Gets the diagnosis_report_list of this ListDiagnosisReportsForRocketMqResponse.

        **参数解释**： 诊断报告列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The diagnosis_report_list of this ListDiagnosisReportsForRocketMqResponse.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.DiagnosisReportResp`]
        """
        return self._diagnosis_report_list

    @diagnosis_report_list.setter
    def diagnosis_report_list(self, diagnosis_report_list):
        r"""Sets the diagnosis_report_list of this ListDiagnosisReportsForRocketMqResponse.

        **参数解释**： 诊断报告列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param diagnosis_report_list: The diagnosis_report_list of this ListDiagnosisReportsForRocketMqResponse.
        :type diagnosis_report_list: list[:class:`huaweicloudsdkrocketmq.v2.DiagnosisReportResp`]
        """
        self._diagnosis_report_list = diagnosis_report_list

    @property
    def total_num(self):
        r"""Gets the total_num of this ListDiagnosisReportsForRocketMqResponse.

        **参数解释**： 报告数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The total_num of this ListDiagnosisReportsForRocketMqResponse.
        :rtype: object
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ListDiagnosisReportsForRocketMqResponse.

        **参数解释**： 报告数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param total_num: The total_num of this ListDiagnosisReportsForRocketMqResponse.
        :type total_num: object
        """
        self._total_num = total_num

    def to_dict(self):
        import warnings
        warnings.warn("ListDiagnosisReportsForRocketMqResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListDiagnosisReportsForRocketMqResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
