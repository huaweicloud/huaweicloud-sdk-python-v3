# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteSecurityReportRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'report_id': 'int'
    }

    attribute_map = {
        'report_id': 'report_id'
    }

    def __init__(self, report_id=None):
        r"""DeleteSecurityReportRequestInfo

        The model defined in huaweicloud sdk

        :param report_id: **参数解释**： 报告ID **约束限制**： 必填 **取值范围**： 最小值0，最大值2147483647 **默认取值**： 不涉及 
        :type report_id: int
        """
        
        

        self._report_id = None
        self.discriminator = None

        self.report_id = report_id

    @property
    def report_id(self):
        r"""Gets the report_id of this DeleteSecurityReportRequestInfo.

        **参数解释**： 报告ID **约束限制**： 必填 **取值范围**： 最小值0，最大值2147483647 **默认取值**： 不涉及 

        :return: The report_id of this DeleteSecurityReportRequestInfo.
        :rtype: int
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        r"""Sets the report_id of this DeleteSecurityReportRequestInfo.

        **参数解释**： 报告ID **约束限制**： 必填 **取值范围**： 最小值0，最大值2147483647 **默认取值**： 不涉及 

        :param report_id: The report_id of this DeleteSecurityReportRequestInfo.
        :type report_id: int
        """
        self._report_id = report_id

    def to_dict(self):
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
        if not isinstance(other, DeleteSecurityReportRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
