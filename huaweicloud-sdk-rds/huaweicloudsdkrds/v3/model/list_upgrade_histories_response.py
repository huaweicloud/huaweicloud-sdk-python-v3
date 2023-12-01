# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUpgradeHistoriesResponse(SdkResponse):

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
        'upgrade_reports': 'list[UpgradeReports]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'upgrade_reports': 'upgrade_reports'
    }

    def __init__(self, total_count=None, upgrade_reports=None):
        """ListUpgradeHistoriesResponse

        The model defined in huaweicloud sdk

        :param total_count: 总记录数。
        :type total_count: int
        :param upgrade_reports: 升级报告信息。
        :type upgrade_reports: list[:class:`huaweicloudsdkrds.v3.UpgradeReports`]
        """
        
        super(ListUpgradeHistoriesResponse, self).__init__()

        self._total_count = None
        self._upgrade_reports = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if upgrade_reports is not None:
            self.upgrade_reports = upgrade_reports

    @property
    def total_count(self):
        """Gets the total_count of this ListUpgradeHistoriesResponse.

        总记录数。

        :return: The total_count of this ListUpgradeHistoriesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListUpgradeHistoriesResponse.

        总记录数。

        :param total_count: The total_count of this ListUpgradeHistoriesResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def upgrade_reports(self):
        """Gets the upgrade_reports of this ListUpgradeHistoriesResponse.

        升级报告信息。

        :return: The upgrade_reports of this ListUpgradeHistoriesResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.UpgradeReports`]
        """
        return self._upgrade_reports

    @upgrade_reports.setter
    def upgrade_reports(self, upgrade_reports):
        """Sets the upgrade_reports of this ListUpgradeHistoriesResponse.

        升级报告信息。

        :param upgrade_reports: The upgrade_reports of this ListUpgradeHistoriesResponse.
        :type upgrade_reports: list[:class:`huaweicloudsdkrds.v3.UpgradeReports`]
        """
        self._upgrade_reports = upgrade_reports

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
        if not isinstance(other, ListUpgradeHistoriesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
