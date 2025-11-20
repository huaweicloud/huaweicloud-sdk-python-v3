# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportTaskInfoRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'operational_report_data': 'ExportTaskInfoRequestBodyOperationalReportData'
    }

    attribute_map = {
        'type': 'type',
        'operational_report_data': 'operational_report_data'
    }

    def __init__(self, type=None, operational_report_data=None):
        r"""ExportTaskInfoRequestBody

        The model defined in huaweicloud sdk

        :param type: **参数解释**: 导出的类型 **约束限制**: 不涉及 **取值范围**: - operational-report：月度运营报告  **默认取值**: 不涉及 
        :type type: str
        :param operational_report_data: 
        :type operational_report_data: :class:`huaweicloudsdkhss.v5.ExportTaskInfoRequestBodyOperationalReportData`
        """
        
        

        self._type = None
        self._operational_report_data = None
        self.discriminator = None

        self.type = type
        self.operational_report_data = operational_report_data

    @property
    def type(self):
        r"""Gets the type of this ExportTaskInfoRequestBody.

        **参数解释**: 导出的类型 **约束限制**: 不涉及 **取值范围**: - operational-report：月度运营报告  **默认取值**: 不涉及 

        :return: The type of this ExportTaskInfoRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ExportTaskInfoRequestBody.

        **参数解释**: 导出的类型 **约束限制**: 不涉及 **取值范围**: - operational-report：月度运营报告  **默认取值**: 不涉及 

        :param type: The type of this ExportTaskInfoRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def operational_report_data(self):
        r"""Gets the operational_report_data of this ExportTaskInfoRequestBody.

        :return: The operational_report_data of this ExportTaskInfoRequestBody.
        :rtype: :class:`huaweicloudsdkhss.v5.ExportTaskInfoRequestBodyOperationalReportData`
        """
        return self._operational_report_data

    @operational_report_data.setter
    def operational_report_data(self, operational_report_data):
        r"""Sets the operational_report_data of this ExportTaskInfoRequestBody.

        :param operational_report_data: The operational_report_data of this ExportTaskInfoRequestBody.
        :type operational_report_data: :class:`huaweicloudsdkhss.v5.ExportTaskInfoRequestBodyOperationalReportData`
        """
        self._operational_report_data = operational_report_data

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
        if not isinstance(other, ExportTaskInfoRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
