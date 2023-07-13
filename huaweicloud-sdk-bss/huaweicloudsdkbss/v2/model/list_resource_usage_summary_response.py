# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceUsageSummaryResponse(SdkResponse):

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
        'summary_usage_info_list': 'list[StatUsageSummaryInfo]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'summary_usage_info_list': 'summary_usage_info_list'
    }

    def __init__(self, total_count=None, summary_usage_info_list=None):
        """ListResourceUsageSummaryResponse

        The model defined in huaweicloud sdk

        :param total_count: 总条数。
        :type total_count: int
        :param summary_usage_info_list: 统计值，按照资源ID维度返回的月度统计结果。具体请参见表3。  说明： 每月2日20点后可查询上月数据；若查询当月数据，则只返回资源ID。
        :type summary_usage_info_list: list[:class:`huaweicloudsdkbss.v2.StatUsageSummaryInfo`]
        """
        
        super(ListResourceUsageSummaryResponse, self).__init__()

        self._total_count = None
        self._summary_usage_info_list = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if summary_usage_info_list is not None:
            self.summary_usage_info_list = summary_usage_info_list

    @property
    def total_count(self):
        """Gets the total_count of this ListResourceUsageSummaryResponse.

        总条数。

        :return: The total_count of this ListResourceUsageSummaryResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListResourceUsageSummaryResponse.

        总条数。

        :param total_count: The total_count of this ListResourceUsageSummaryResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def summary_usage_info_list(self):
        """Gets the summary_usage_info_list of this ListResourceUsageSummaryResponse.

        统计值，按照资源ID维度返回的月度统计结果。具体请参见表3。  说明： 每月2日20点后可查询上月数据；若查询当月数据，则只返回资源ID。

        :return: The summary_usage_info_list of this ListResourceUsageSummaryResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.StatUsageSummaryInfo`]
        """
        return self._summary_usage_info_list

    @summary_usage_info_list.setter
    def summary_usage_info_list(self, summary_usage_info_list):
        """Sets the summary_usage_info_list of this ListResourceUsageSummaryResponse.

        统计值，按照资源ID维度返回的月度统计结果。具体请参见表3。  说明： 每月2日20点后可查询上月数据；若查询当月数据，则只返回资源ID。

        :param summary_usage_info_list: The summary_usage_info_list of this ListResourceUsageSummaryResponse.
        :type summary_usage_info_list: list[:class:`huaweicloudsdkbss.v2.StatUsageSummaryInfo`]
        """
        self._summary_usage_info_list = summary_usage_info_list

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
        if not isinstance(other, ListResourceUsageSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
