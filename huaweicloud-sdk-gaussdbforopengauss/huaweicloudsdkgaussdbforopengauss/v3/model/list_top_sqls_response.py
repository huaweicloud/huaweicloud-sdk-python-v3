# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTopSqlsResponse(SdkResponse):

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
        'top_sql_infos': 'list[TopSQLInfoResult]'
    }

    attribute_map = {
        'total': 'total',
        'top_sql_infos': 'top_sql_infos'
    }

    def __init__(self, total=None, top_sql_infos=None):
        r"""ListTopSqlsResponse

        The model defined in huaweicloud sdk

        :param total: **参数解释**: Top SQL总条数。 **取值范围**: 不涉及。
        :type total: int
        :param top_sql_infos: **参数解释**: Top SQL信息列表。
        :type top_sql_infos: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.TopSQLInfoResult`]
        """
        
        super(ListTopSqlsResponse, self).__init__()

        self._total = None
        self._top_sql_infos = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if top_sql_infos is not None:
            self.top_sql_infos = top_sql_infos

    @property
    def total(self):
        r"""Gets the total of this ListTopSqlsResponse.

        **参数解释**: Top SQL总条数。 **取值范围**: 不涉及。

        :return: The total of this ListTopSqlsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListTopSqlsResponse.

        **参数解释**: Top SQL总条数。 **取值范围**: 不涉及。

        :param total: The total of this ListTopSqlsResponse.
        :type total: int
        """
        self._total = total

    @property
    def top_sql_infos(self):
        r"""Gets the top_sql_infos of this ListTopSqlsResponse.

        **参数解释**: Top SQL信息列表。

        :return: The top_sql_infos of this ListTopSqlsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.TopSQLInfoResult`]
        """
        return self._top_sql_infos

    @top_sql_infos.setter
    def top_sql_infos(self, top_sql_infos):
        r"""Sets the top_sql_infos of this ListTopSqlsResponse.

        **参数解释**: Top SQL信息列表。

        :param top_sql_infos: The top_sql_infos of this ListTopSqlsResponse.
        :type top_sql_infos: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.TopSQLInfoResult`]
        """
        self._top_sql_infos = top_sql_infos

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
        if not isinstance(other, ListTopSqlsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
