# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SendSecurityReportRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'report_id': 'int',
        'report_sub_id': 'int'
    }

    attribute_map = {
        'report_id': 'report_id',
        'report_sub_id': 'report_sub_id'
    }

    def __init__(self, report_id=None, report_sub_id=None):
        r"""SendSecurityReportRequestInfo

        The model defined in huaweicloud sdk

        :param report_id: **参数解释**: 报告ID **取值范围**: 字符长度10-2147483647位 
        :type report_id: int
        :param report_sub_id: **参数解释**: 报告子ID **取值范围**: 字符长度10-2147483647位 
        :type report_sub_id: int
        """
        
        

        self._report_id = None
        self._report_sub_id = None
        self.discriminator = None

        self.report_id = report_id
        self.report_sub_id = report_sub_id

    @property
    def report_id(self):
        r"""Gets the report_id of this SendSecurityReportRequestInfo.

        **参数解释**: 报告ID **取值范围**: 字符长度10-2147483647位 

        :return: The report_id of this SendSecurityReportRequestInfo.
        :rtype: int
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        r"""Sets the report_id of this SendSecurityReportRequestInfo.

        **参数解释**: 报告ID **取值范围**: 字符长度10-2147483647位 

        :param report_id: The report_id of this SendSecurityReportRequestInfo.
        :type report_id: int
        """
        self._report_id = report_id

    @property
    def report_sub_id(self):
        r"""Gets the report_sub_id of this SendSecurityReportRequestInfo.

        **参数解释**: 报告子ID **取值范围**: 字符长度10-2147483647位 

        :return: The report_sub_id of this SendSecurityReportRequestInfo.
        :rtype: int
        """
        return self._report_sub_id

    @report_sub_id.setter
    def report_sub_id(self, report_sub_id):
        r"""Sets the report_sub_id of this SendSecurityReportRequestInfo.

        **参数解释**: 报告子ID **取值范围**: 字符长度10-2147483647位 

        :param report_sub_id: The report_sub_id of this SendSecurityReportRequestInfo.
        :type report_sub_id: int
        """
        self._report_sub_id = report_sub_id

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
        if not isinstance(other, SendSecurityReportRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
