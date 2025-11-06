# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowReportSettingResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'report_setting': 'ReportSettingEntity'
    }

    attribute_map = {
        'report_setting': 'report_setting'
    }

    def __init__(self, report_setting=None):
        r"""ShowReportSettingResponse

        The model defined in huaweicloud sdk

        :param report_setting: 
        :type report_setting: :class:`huaweicloudsdkbcc.v1.ReportSettingEntity`
        """
        
        super().__init__()

        self._report_setting = None
        self.discriminator = None

        if report_setting is not None:
            self.report_setting = report_setting

    @property
    def report_setting(self):
        r"""Gets the report_setting of this ShowReportSettingResponse.

        :return: The report_setting of this ShowReportSettingResponse.
        :rtype: :class:`huaweicloudsdkbcc.v1.ReportSettingEntity`
        """
        return self._report_setting

    @report_setting.setter
    def report_setting(self, report_setting):
        r"""Sets the report_setting of this ShowReportSettingResponse.

        :param report_setting: The report_setting of this ShowReportSettingResponse.
        :type report_setting: :class:`huaweicloudsdkbcc.v1.ReportSettingEntity`
        """
        self._report_setting = report_setting

    def to_dict(self):
        import warnings
        warnings.warn("ShowReportSettingResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowReportSettingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
