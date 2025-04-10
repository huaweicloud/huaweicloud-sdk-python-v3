# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInspectionHistoriesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'inspection_reports': 'list[InspectionReports]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'inspection_reports': 'inspection_reports'
    }

    def __init__(self, total_count=None, inspection_reports=None):
        r"""ListInspectionHistoriesResponse

        The model defined in huaweicloud sdk

        :param total_count: 总记录数。
        :type total_count: int
        :param inspection_reports: 检查报告信息。
        :type inspection_reports: list[:class:`huaweicloudsdkrds.v3.InspectionReports`]
        """
        
        super(ListInspectionHistoriesResponse, self).__init__()

        self._total_count = None
        self._inspection_reports = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if inspection_reports is not None:
            self.inspection_reports = inspection_reports

    @property
    def total_count(self):
        r"""Gets the total_count of this ListInspectionHistoriesResponse.

        总记录数。

        :return: The total_count of this ListInspectionHistoriesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListInspectionHistoriesResponse.

        总记录数。

        :param total_count: The total_count of this ListInspectionHistoriesResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def inspection_reports(self):
        r"""Gets the inspection_reports of this ListInspectionHistoriesResponse.

        检查报告信息。

        :return: The inspection_reports of this ListInspectionHistoriesResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.InspectionReports`]
        """
        return self._inspection_reports

    @inspection_reports.setter
    def inspection_reports(self, inspection_reports):
        r"""Sets the inspection_reports of this ListInspectionHistoriesResponse.

        检查报告信息。

        :param inspection_reports: The inspection_reports of this ListInspectionHistoriesResponse.
        :type inspection_reports: list[:class:`huaweicloudsdkrds.v3.InspectionReports`]
        """
        self._inspection_reports = inspection_reports

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
        if not isinstance(other, ListInspectionHistoriesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
