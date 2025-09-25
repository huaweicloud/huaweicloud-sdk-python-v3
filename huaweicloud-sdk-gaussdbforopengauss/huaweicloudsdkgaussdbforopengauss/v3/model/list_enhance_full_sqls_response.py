# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEnhanceFullSqlsResponse(SdkResponse):

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
        'full_sqls': 'list[FullSqlResult]',
        'limit_count': 'int'
    }

    attribute_map = {
        'total_count': 'total_count',
        'full_sqls': 'full_sqls',
        'limit_count': 'limit_count'
    }

    def __init__(self, total_count=None, full_sqls=None, limit_count=None):
        r"""ListEnhanceFullSqlsResponse

        The model defined in huaweicloud sdk

        :param total_count: **参数解释**: 总记录数量。 **取值范围**: 不涉及。
        :type total_count: int
        :param full_sqls: **参数解释**: 全量SQL列表。
        :type full_sqls: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.FullSqlResult`]
        :param limit_count: **参数解释**: 最大查询记录数量。主要供前端交互控制使用。 **取值范围**: 不涉及。
        :type limit_count: int
        """
        
        super(ListEnhanceFullSqlsResponse, self).__init__()

        self._total_count = None
        self._full_sqls = None
        self._limit_count = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if full_sqls is not None:
            self.full_sqls = full_sqls
        if limit_count is not None:
            self.limit_count = limit_count

    @property
    def total_count(self):
        r"""Gets the total_count of this ListEnhanceFullSqlsResponse.

        **参数解释**: 总记录数量。 **取值范围**: 不涉及。

        :return: The total_count of this ListEnhanceFullSqlsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListEnhanceFullSqlsResponse.

        **参数解释**: 总记录数量。 **取值范围**: 不涉及。

        :param total_count: The total_count of this ListEnhanceFullSqlsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def full_sqls(self):
        r"""Gets the full_sqls of this ListEnhanceFullSqlsResponse.

        **参数解释**: 全量SQL列表。

        :return: The full_sqls of this ListEnhanceFullSqlsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.FullSqlResult`]
        """
        return self._full_sqls

    @full_sqls.setter
    def full_sqls(self, full_sqls):
        r"""Sets the full_sqls of this ListEnhanceFullSqlsResponse.

        **参数解释**: 全量SQL列表。

        :param full_sqls: The full_sqls of this ListEnhanceFullSqlsResponse.
        :type full_sqls: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.FullSqlResult`]
        """
        self._full_sqls = full_sqls

    @property
    def limit_count(self):
        r"""Gets the limit_count of this ListEnhanceFullSqlsResponse.

        **参数解释**: 最大查询记录数量。主要供前端交互控制使用。 **取值范围**: 不涉及。

        :return: The limit_count of this ListEnhanceFullSqlsResponse.
        :rtype: int
        """
        return self._limit_count

    @limit_count.setter
    def limit_count(self, limit_count):
        r"""Sets the limit_count of this ListEnhanceFullSqlsResponse.

        **参数解释**: 最大查询记录数量。主要供前端交互控制使用。 **取值范围**: 不涉及。

        :param limit_count: The limit_count of this ListEnhanceFullSqlsResponse.
        :type limit_count: int
        """
        self._limit_count = limit_count

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
        if not isinstance(other, ListEnhanceFullSqlsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
