# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSqlPlanActionResponse(SdkResponse):

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
        'sql_plan_bind_state_list': 'list[SqlPlanStateListResponseSqlPlanBindStateList]'
    }

    attribute_map = {
        'total': 'total',
        'sql_plan_bind_state_list': 'sql_plan_bind_state_list'
    }

    def __init__(self, total=None, sql_plan_bind_state_list=None):
        r"""ListSqlPlanActionResponse

        The model defined in huaweicloud sdk

        :param total: **参数解释**: sql执行计划总数。 **取值范围**: 不涉及。
        :type total: int
        :param sql_plan_bind_state_list: **参数解释**: 执行计划列表。 **取值范围**: 不涉及。
        :type sql_plan_bind_state_list: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.SqlPlanStateListResponseSqlPlanBindStateList`]
        """
        
        super().__init__()

        self._total = None
        self._sql_plan_bind_state_list = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if sql_plan_bind_state_list is not None:
            self.sql_plan_bind_state_list = sql_plan_bind_state_list

    @property
    def total(self):
        r"""Gets the total of this ListSqlPlanActionResponse.

        **参数解释**: sql执行计划总数。 **取值范围**: 不涉及。

        :return: The total of this ListSqlPlanActionResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListSqlPlanActionResponse.

        **参数解释**: sql执行计划总数。 **取值范围**: 不涉及。

        :param total: The total of this ListSqlPlanActionResponse.
        :type total: int
        """
        self._total = total

    @property
    def sql_plan_bind_state_list(self):
        r"""Gets the sql_plan_bind_state_list of this ListSqlPlanActionResponse.

        **参数解释**: 执行计划列表。 **取值范围**: 不涉及。

        :return: The sql_plan_bind_state_list of this ListSqlPlanActionResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.SqlPlanStateListResponseSqlPlanBindStateList`]
        """
        return self._sql_plan_bind_state_list

    @sql_plan_bind_state_list.setter
    def sql_plan_bind_state_list(self, sql_plan_bind_state_list):
        r"""Sets the sql_plan_bind_state_list of this ListSqlPlanActionResponse.

        **参数解释**: 执行计划列表。 **取值范围**: 不涉及。

        :param sql_plan_bind_state_list: The sql_plan_bind_state_list of this ListSqlPlanActionResponse.
        :type sql_plan_bind_state_list: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.SqlPlanStateListResponseSqlPlanBindStateList`]
        """
        self._sql_plan_bind_state_list = sql_plan_bind_state_list

    def to_dict(self):
        import warnings
        warnings.warn("ListSqlPlanActionResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListSqlPlanActionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
