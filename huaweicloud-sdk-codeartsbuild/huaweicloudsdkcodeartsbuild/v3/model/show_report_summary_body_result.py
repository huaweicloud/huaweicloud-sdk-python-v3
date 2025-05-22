# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowReportSummaryBodyResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'summary': 'ShowReportSummary',
        'sub_summarys': 'list[ShowReportSummary]'
    }

    attribute_map = {
        'summary': 'summary',
        'sub_summarys': 'sub_summarys'
    }

    def __init__(self, summary=None, sub_summarys=None):
        r"""ShowReportSummaryBodyResult

        The model defined in huaweicloud sdk

        :param summary: 
        :type summary: :class:`huaweicloudsdkcodeartsbuild.v3.ShowReportSummary`
        :param sub_summarys: 单元测试报告列表
        :type sub_summarys: list[:class:`huaweicloudsdkcodeartsbuild.v3.ShowReportSummary`]
        """
        
        

        self._summary = None
        self._sub_summarys = None
        self.discriminator = None

        if summary is not None:
            self.summary = summary
        if sub_summarys is not None:
            self.sub_summarys = sub_summarys

    @property
    def summary(self):
        r"""Gets the summary of this ShowReportSummaryBodyResult.

        :return: The summary of this ShowReportSummaryBodyResult.
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowReportSummary`
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        r"""Sets the summary of this ShowReportSummaryBodyResult.

        :param summary: The summary of this ShowReportSummaryBodyResult.
        :type summary: :class:`huaweicloudsdkcodeartsbuild.v3.ShowReportSummary`
        """
        self._summary = summary

    @property
    def sub_summarys(self):
        r"""Gets the sub_summarys of this ShowReportSummaryBodyResult.

        单元测试报告列表

        :return: The sub_summarys of this ShowReportSummaryBodyResult.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.ShowReportSummary`]
        """
        return self._sub_summarys

    @sub_summarys.setter
    def sub_summarys(self, sub_summarys):
        r"""Sets the sub_summarys of this ShowReportSummaryBodyResult.

        单元测试报告列表

        :param sub_summarys: The sub_summarys of this ShowReportSummaryBodyResult.
        :type sub_summarys: list[:class:`huaweicloudsdkcodeartsbuild.v3.ShowReportSummary`]
        """
        self._sub_summarys = sub_summarys

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
        if not isinstance(other, ShowReportSummaryBodyResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
