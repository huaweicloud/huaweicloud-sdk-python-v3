# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuerySqlPlanStateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql_id': 'str',
        'page_size': 'str',
        'offset': 'str'
    }

    attribute_map = {
        'sql_id': 'sql_id',
        'page_size': 'page_size',
        'offset': 'offset'
    }

    def __init__(self, sql_id=None, page_size=None, offset=None):
        r"""QuerySqlPlanStateRequest

        The model defined in huaweicloud sdk

        :param sql_id: **参数解释**: 归一化的SQL ID **约束限制**: 不涉及。
        :type sql_id: str
        :param page_size: **参数解释**: SQL执行计划每页显示数量。 **约束限制**: 不涉及。 **取值范围**: 整数，1~100。 **默认取值**: 不涉及。
        :type page_size: str
        :param offset: **参数解释**: SQL执行计划起始页码。 **约束限制**: 不涉及。 **取值范围**: 大于等于0的整数。 **默认取值**: 不涉及。
        :type offset: str
        """
        
        

        self._sql_id = None
        self._page_size = None
        self._offset = None
        self.discriminator = None

        self.sql_id = sql_id
        self.page_size = page_size
        self.offset = offset

    @property
    def sql_id(self):
        r"""Gets the sql_id of this QuerySqlPlanStateRequest.

        **参数解释**: 归一化的SQL ID **约束限制**: 不涉及。

        :return: The sql_id of this QuerySqlPlanStateRequest.
        :rtype: str
        """
        return self._sql_id

    @sql_id.setter
    def sql_id(self, sql_id):
        r"""Sets the sql_id of this QuerySqlPlanStateRequest.

        **参数解释**: 归一化的SQL ID **约束限制**: 不涉及。

        :param sql_id: The sql_id of this QuerySqlPlanStateRequest.
        :type sql_id: str
        """
        self._sql_id = sql_id

    @property
    def page_size(self):
        r"""Gets the page_size of this QuerySqlPlanStateRequest.

        **参数解释**: SQL执行计划每页显示数量。 **约束限制**: 不涉及。 **取值范围**: 整数，1~100。 **默认取值**: 不涉及。

        :return: The page_size of this QuerySqlPlanStateRequest.
        :rtype: str
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this QuerySqlPlanStateRequest.

        **参数解释**: SQL执行计划每页显示数量。 **约束限制**: 不涉及。 **取值范围**: 整数，1~100。 **默认取值**: 不涉及。

        :param page_size: The page_size of this QuerySqlPlanStateRequest.
        :type page_size: str
        """
        self._page_size = page_size

    @property
    def offset(self):
        r"""Gets the offset of this QuerySqlPlanStateRequest.

        **参数解释**: SQL执行计划起始页码。 **约束限制**: 不涉及。 **取值范围**: 大于等于0的整数。 **默认取值**: 不涉及。

        :return: The offset of this QuerySqlPlanStateRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this QuerySqlPlanStateRequest.

        **参数解释**: SQL执行计划起始页码。 **约束限制**: 不涉及。 **取值范围**: 大于等于0的整数。 **默认取值**: 不涉及。

        :param offset: The offset of this QuerySqlPlanStateRequest.
        :type offset: str
        """
        self._offset = offset

    def to_dict(self):
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
        if not isinstance(other, QuerySqlPlanStateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
