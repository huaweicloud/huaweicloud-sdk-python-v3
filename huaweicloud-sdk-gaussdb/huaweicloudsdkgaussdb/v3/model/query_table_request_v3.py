# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryTableRequestV3:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database_tables': 'list[DatabaseTablesInfo]',
        'source_instance_id': 'str',
        'selected_tables': 'list[DatabaseTablesInfo]',
        'filter_type': 'str'
    }

    attribute_map = {
        'database_tables': 'database_tables',
        'source_instance_id': 'source_instance_id',
        'selected_tables': 'selected_tables',
        'filter_type': 'filter_type'
    }

    def __init__(self, database_tables=None, source_instance_id=None, selected_tables=None, filter_type=None):
        r"""QueryTableRequestV3

        The model defined in huaweicloud sdk

        :param database_tables: **参数解释**：  查询的数据库及表名称的列表。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type database_tables: list[:class:`huaweicloudsdkgaussdb.v3.DatabaseTablesInfo`]
        :param source_instance_id: **参数解释**：  需要查询数据库的源实例ID，严格匹配UUID规则。  **约束限制**：  只能由英文字母、数字组成，且长度为36个字符。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type source_instance_id: str
        :param selected_tables: **参数解释**：  已选择的数据库及表名称的列表。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type selected_tables: list[:class:`huaweicloudsdkgaussdb.v3.DatabaseTablesInfo`]
        :param filter_type: **参数解释**：  表黑白名单设置。include_tables：白名单，exclude_tables：黑名单。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type filter_type: str
        """
        
        

        self._database_tables = None
        self._source_instance_id = None
        self._selected_tables = None
        self._filter_type = None
        self.discriminator = None

        if database_tables is not None:
            self.database_tables = database_tables
        if source_instance_id is not None:
            self.source_instance_id = source_instance_id
        if selected_tables is not None:
            self.selected_tables = selected_tables
        if filter_type is not None:
            self.filter_type = filter_type

    @property
    def database_tables(self):
        r"""Gets the database_tables of this QueryTableRequestV3.

        **参数解释**：  查询的数据库及表名称的列表。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The database_tables of this QueryTableRequestV3.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.DatabaseTablesInfo`]
        """
        return self._database_tables

    @database_tables.setter
    def database_tables(self, database_tables):
        r"""Sets the database_tables of this QueryTableRequestV3.

        **参数解释**：  查询的数据库及表名称的列表。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param database_tables: The database_tables of this QueryTableRequestV3.
        :type database_tables: list[:class:`huaweicloudsdkgaussdb.v3.DatabaseTablesInfo`]
        """
        self._database_tables = database_tables

    @property
    def source_instance_id(self):
        r"""Gets the source_instance_id of this QueryTableRequestV3.

        **参数解释**：  需要查询数据库的源实例ID，严格匹配UUID规则。  **约束限制**：  只能由英文字母、数字组成，且长度为36个字符。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The source_instance_id of this QueryTableRequestV3.
        :rtype: str
        """
        return self._source_instance_id

    @source_instance_id.setter
    def source_instance_id(self, source_instance_id):
        r"""Sets the source_instance_id of this QueryTableRequestV3.

        **参数解释**：  需要查询数据库的源实例ID，严格匹配UUID规则。  **约束限制**：  只能由英文字母、数字组成，且长度为36个字符。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param source_instance_id: The source_instance_id of this QueryTableRequestV3.
        :type source_instance_id: str
        """
        self._source_instance_id = source_instance_id

    @property
    def selected_tables(self):
        r"""Gets the selected_tables of this QueryTableRequestV3.

        **参数解释**：  已选择的数据库及表名称的列表。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The selected_tables of this QueryTableRequestV3.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.DatabaseTablesInfo`]
        """
        return self._selected_tables

    @selected_tables.setter
    def selected_tables(self, selected_tables):
        r"""Sets the selected_tables of this QueryTableRequestV3.

        **参数解释**：  已选择的数据库及表名称的列表。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param selected_tables: The selected_tables of this QueryTableRequestV3.
        :type selected_tables: list[:class:`huaweicloudsdkgaussdb.v3.DatabaseTablesInfo`]
        """
        self._selected_tables = selected_tables

    @property
    def filter_type(self):
        r"""Gets the filter_type of this QueryTableRequestV3.

        **参数解释**：  表黑白名单设置。include_tables：白名单，exclude_tables：黑名单。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The filter_type of this QueryTableRequestV3.
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        r"""Sets the filter_type of this QueryTableRequestV3.

        **参数解释**：  表黑白名单设置。include_tables：白名单，exclude_tables：黑名单。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param filter_type: The filter_type of this QueryTableRequestV3.
        :type filter_type: str
        """
        self._filter_type = filter_type

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
        if not isinstance(other, QueryTableRequestV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
