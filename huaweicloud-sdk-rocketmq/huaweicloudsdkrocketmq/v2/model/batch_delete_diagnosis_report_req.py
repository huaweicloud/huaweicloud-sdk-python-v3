# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteDiagnosisReportReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'report_id_list': 'list[str]'
    }

    attribute_map = {
        'report_id_list': 'report_id_list'
    }

    def __init__(self, report_id_list=None):
        r"""BatchDeleteDiagnosisReportReq

        The model defined in huaweicloud sdk

        :param report_id_list: **参数解释**： 诊断报告ID列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type report_id_list: list[str]
        """
        
        

        self._report_id_list = None
        self.discriminator = None

        if report_id_list is not None:
            self.report_id_list = report_id_list

    @property
    def report_id_list(self):
        r"""Gets the report_id_list of this BatchDeleteDiagnosisReportReq.

        **参数解释**： 诊断报告ID列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The report_id_list of this BatchDeleteDiagnosisReportReq.
        :rtype: list[str]
        """
        return self._report_id_list

    @report_id_list.setter
    def report_id_list(self, report_id_list):
        r"""Sets the report_id_list of this BatchDeleteDiagnosisReportReq.

        **参数解释**： 诊断报告ID列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param report_id_list: The report_id_list of this BatchDeleteDiagnosisReportReq.
        :type report_id_list: list[str]
        """
        self._report_id_list = report_id_list

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
        if not isinstance(other, BatchDeleteDiagnosisReportReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
