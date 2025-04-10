# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowNextflowJobReportsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'report_files': 'list[NextflowJobReportFile]'
    }

    attribute_map = {
        'report_files': 'report_files'
    }

    def __init__(self, report_files=None):
        r"""ShowNextflowJobReportsResponse

        The model defined in huaweicloud sdk

        :param report_files: 作业报告文件列表
        :type report_files: list[:class:`huaweicloudsdkeihealth.v1.NextflowJobReportFile`]
        """
        
        super(ShowNextflowJobReportsResponse, self).__init__()

        self._report_files = None
        self.discriminator = None

        if report_files is not None:
            self.report_files = report_files

    @property
    def report_files(self):
        r"""Gets the report_files of this ShowNextflowJobReportsResponse.

        作业报告文件列表

        :return: The report_files of this ShowNextflowJobReportsResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.NextflowJobReportFile`]
        """
        return self._report_files

    @report_files.setter
    def report_files(self, report_files):
        r"""Sets the report_files of this ShowNextflowJobReportsResponse.

        作业报告文件列表

        :param report_files: The report_files of this ShowNextflowJobReportsResponse.
        :type report_files: list[:class:`huaweicloudsdkeihealth.v1.NextflowJobReportFile`]
        """
        self._report_files = report_files

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
        if not isinstance(other, ShowNextflowJobReportsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
