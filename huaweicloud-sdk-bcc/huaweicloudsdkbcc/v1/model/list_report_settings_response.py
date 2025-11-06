# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListReportSettingsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'report_settings': 'list[ReportSettingEntity]'
    }

    attribute_map = {
        'count': 'count',
        'report_settings': 'report_settings'
    }

    def __init__(self, count=None, report_settings=None):
        r"""ListReportSettingsResponse

        The model defined in huaweicloud sdk

        :param count: 报告配置总条数
        :type count: int
        :param report_settings: 配置列表
        :type report_settings: list[:class:`huaweicloudsdkbcc.v1.ReportSettingEntity`]
        """
        
        super().__init__()

        self._count = None
        self._report_settings = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if report_settings is not None:
            self.report_settings = report_settings

    @property
    def count(self):
        r"""Gets the count of this ListReportSettingsResponse.

        报告配置总条数

        :return: The count of this ListReportSettingsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListReportSettingsResponse.

        报告配置总条数

        :param count: The count of this ListReportSettingsResponse.
        :type count: int
        """
        self._count = count

    @property
    def report_settings(self):
        r"""Gets the report_settings of this ListReportSettingsResponse.

        配置列表

        :return: The report_settings of this ListReportSettingsResponse.
        :rtype: list[:class:`huaweicloudsdkbcc.v1.ReportSettingEntity`]
        """
        return self._report_settings

    @report_settings.setter
    def report_settings(self, report_settings):
        r"""Sets the report_settings of this ListReportSettingsResponse.

        配置列表

        :param report_settings: The report_settings of this ListReportSettingsResponse.
        :type report_settings: list[:class:`huaweicloudsdkbcc.v1.ReportSettingEntity`]
        """
        self._report_settings = report_settings

    def to_dict(self):
        import warnings
        warnings.warn("ListReportSettingsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListReportSettingsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
