# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSessionStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'statistics_list': 'list[DimensionListResult]'
    }

    attribute_map = {
        'total': 'total',
        'statistics_list': 'statistics_list'
    }

    def __init__(self, total=None, statistics_list=None):
        r"""ListSessionStatisticsResponse

        The model defined in huaweicloud sdk

        :param total: **参数解释**: 总数。 **取值范围**: 不涉及。
        :type total: int
        :param statistics_list: **参数解释**: 会话统计列表。
        :type statistics_list: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.DimensionListResult`]
        """
        
        super(ListSessionStatisticsResponse, self).__init__()

        self._total = None
        self._statistics_list = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if statistics_list is not None:
            self.statistics_list = statistics_list

    @property
    def total(self):
        r"""Gets the total of this ListSessionStatisticsResponse.

        **参数解释**: 总数。 **取值范围**: 不涉及。

        :return: The total of this ListSessionStatisticsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListSessionStatisticsResponse.

        **参数解释**: 总数。 **取值范围**: 不涉及。

        :param total: The total of this ListSessionStatisticsResponse.
        :type total: int
        """
        self._total = total

    @property
    def statistics_list(self):
        r"""Gets the statistics_list of this ListSessionStatisticsResponse.

        **参数解释**: 会话统计列表。

        :return: The statistics_list of this ListSessionStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.DimensionListResult`]
        """
        return self._statistics_list

    @statistics_list.setter
    def statistics_list(self, statistics_list):
        r"""Sets the statistics_list of this ListSessionStatisticsResponse.

        **参数解释**: 会话统计列表。

        :param statistics_list: The statistics_list of this ListSessionStatisticsResponse.
        :type statistics_list: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.DimensionListResult`]
        """
        self._statistics_list = statistics_list

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
        if not isinstance(other, ListSessionStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
