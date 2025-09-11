# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSlowSqlDetailsResponse(SdkResponse):

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
        'slow_sql_details': 'list[SlowSqlDetailResult]'
    }

    attribute_map = {
        'total': 'total',
        'slow_sql_details': 'slow_sql_details'
    }

    def __init__(self, total=None, slow_sql_details=None):
        r"""ListSlowSqlDetailsResponse

        The model defined in huaweicloud sdk

        :param total: **参数解释**: 总条数。 **取值范围**: 不涉及。
        :type total: int
        :param slow_sql_details: **参数解释**: 慢SQL详情信息列表。
        :type slow_sql_details: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.SlowSqlDetailResult`]
        """
        
        super(ListSlowSqlDetailsResponse, self).__init__()

        self._total = None
        self._slow_sql_details = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if slow_sql_details is not None:
            self.slow_sql_details = slow_sql_details

    @property
    def total(self):
        r"""Gets the total of this ListSlowSqlDetailsResponse.

        **参数解释**: 总条数。 **取值范围**: 不涉及。

        :return: The total of this ListSlowSqlDetailsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListSlowSqlDetailsResponse.

        **参数解释**: 总条数。 **取值范围**: 不涉及。

        :param total: The total of this ListSlowSqlDetailsResponse.
        :type total: int
        """
        self._total = total

    @property
    def slow_sql_details(self):
        r"""Gets the slow_sql_details of this ListSlowSqlDetailsResponse.

        **参数解释**: 慢SQL详情信息列表。

        :return: The slow_sql_details of this ListSlowSqlDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.SlowSqlDetailResult`]
        """
        return self._slow_sql_details

    @slow_sql_details.setter
    def slow_sql_details(self, slow_sql_details):
        r"""Sets the slow_sql_details of this ListSlowSqlDetailsResponse.

        **参数解释**: 慢SQL详情信息列表。

        :param slow_sql_details: The slow_sql_details of this ListSlowSqlDetailsResponse.
        :type slow_sql_details: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.SlowSqlDetailResult`]
        """
        self._slow_sql_details = slow_sql_details

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
        if not isinstance(other, ListSlowSqlDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
