# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFullSqlSwitchesResponse(SdkResponse):

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
        'full_sql_switchs': 'list[FullSqlSwitchResult]',
        'allowed_sql_types': 'list[SqlTypeRangeConfigResult]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'full_sql_switchs': 'full_sql_switchs',
        'allowed_sql_types': 'allowed_sql_types'
    }

    def __init__(self, total_count=None, full_sql_switchs=None, allowed_sql_types=None):
        r"""ListFullSqlSwitchesResponse

        The model defined in huaweicloud sdk

        :param total_count: **参数解释**: 总记录数量。 **取值范围**: 不涉及。
        :type total_count: int
        :param full_sql_switchs: **参数解释**: 开关记录列表。
        :type full_sql_switchs: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.FullSqlSwitchResult`]
        :param allowed_sql_types: **参数解释**: 可选择的SQL采集类别清单列表。供开启全量SQL时做配置下发参考。
        :type allowed_sql_types: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.SqlTypeRangeConfigResult`]
        """
        
        super(ListFullSqlSwitchesResponse, self).__init__()

        self._total_count = None
        self._full_sql_switchs = None
        self._allowed_sql_types = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if full_sql_switchs is not None:
            self.full_sql_switchs = full_sql_switchs
        if allowed_sql_types is not None:
            self.allowed_sql_types = allowed_sql_types

    @property
    def total_count(self):
        r"""Gets the total_count of this ListFullSqlSwitchesResponse.

        **参数解释**: 总记录数量。 **取值范围**: 不涉及。

        :return: The total_count of this ListFullSqlSwitchesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListFullSqlSwitchesResponse.

        **参数解释**: 总记录数量。 **取值范围**: 不涉及。

        :param total_count: The total_count of this ListFullSqlSwitchesResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def full_sql_switchs(self):
        r"""Gets the full_sql_switchs of this ListFullSqlSwitchesResponse.

        **参数解释**: 开关记录列表。

        :return: The full_sql_switchs of this ListFullSqlSwitchesResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.FullSqlSwitchResult`]
        """
        return self._full_sql_switchs

    @full_sql_switchs.setter
    def full_sql_switchs(self, full_sql_switchs):
        r"""Sets the full_sql_switchs of this ListFullSqlSwitchesResponse.

        **参数解释**: 开关记录列表。

        :param full_sql_switchs: The full_sql_switchs of this ListFullSqlSwitchesResponse.
        :type full_sql_switchs: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.FullSqlSwitchResult`]
        """
        self._full_sql_switchs = full_sql_switchs

    @property
    def allowed_sql_types(self):
        r"""Gets the allowed_sql_types of this ListFullSqlSwitchesResponse.

        **参数解释**: 可选择的SQL采集类别清单列表。供开启全量SQL时做配置下发参考。

        :return: The allowed_sql_types of this ListFullSqlSwitchesResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.SqlTypeRangeConfigResult`]
        """
        return self._allowed_sql_types

    @allowed_sql_types.setter
    def allowed_sql_types(self, allowed_sql_types):
        r"""Sets the allowed_sql_types of this ListFullSqlSwitchesResponse.

        **参数解释**: 可选择的SQL采集类别清单列表。供开启全量SQL时做配置下发参考。

        :param allowed_sql_types: The allowed_sql_types of this ListFullSqlSwitchesResponse.
        :type allowed_sql_types: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.SqlTypeRangeConfigResult`]
        """
        self._allowed_sql_types = allowed_sql_types

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
        if not isinstance(other, ListFullSqlSwitchesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
