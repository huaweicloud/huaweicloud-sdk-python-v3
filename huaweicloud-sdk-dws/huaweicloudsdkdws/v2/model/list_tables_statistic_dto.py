# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTablesStatisticDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_name': 'str',
        'schema_name': 'str',
        'table_name': 'str',
        'table_owner': 'str',
        'table_size': 'str',
        'skew_rate': 'float',
        'dirty_page_rate': 'float'
    }

    attribute_map = {
        'db_name': 'db_name',
        'schema_name': 'schema_name',
        'table_name': 'table_name',
        'table_owner': 'table_owner',
        'table_size': 'table_size',
        'skew_rate': 'skew_rate',
        'dirty_page_rate': 'dirty_page_rate'
    }

    def __init__(self, db_name=None, schema_name=None, table_name=None, table_owner=None, table_size=None, skew_rate=None, dirty_page_rate=None):
        r"""ListTablesStatisticDto

        The model defined in huaweicloud sdk

        :param db_name: **参数解释**： 数据库名称。 **取值范围**： 不涉及。
        :type db_name: str
        :param schema_name: **参数解释**： 模式名称。 **取值范围**： 不涉及。
        :type schema_name: str
        :param table_name: **参数解释**： 表名。 **取值范围**： 不涉及。
        :type table_name: str
        :param table_owner: **参数解释**： 所属用户。 **取值范围**： 不涉及。
        :type table_owner: str
        :param table_size: **参数解释**： 表大小。 **取值范围**： 不涉及。
        :type table_size: str
        :param skew_rate: **参数解释**： 表倾斜率。 **取值范围**： 不涉及。
        :type skew_rate: float
        :param dirty_page_rate: **参数解释**： 脏页率。 **取值范围**： 不涉及。
        :type dirty_page_rate: float
        """
        
        

        self._db_name = None
        self._schema_name = None
        self._table_name = None
        self._table_owner = None
        self._table_size = None
        self._skew_rate = None
        self._dirty_page_rate = None
        self.discriminator = None

        if db_name is not None:
            self.db_name = db_name
        if schema_name is not None:
            self.schema_name = schema_name
        if table_name is not None:
            self.table_name = table_name
        if table_owner is not None:
            self.table_owner = table_owner
        if table_size is not None:
            self.table_size = table_size
        if skew_rate is not None:
            self.skew_rate = skew_rate
        if dirty_page_rate is not None:
            self.dirty_page_rate = dirty_page_rate

    @property
    def db_name(self):
        r"""Gets the db_name of this ListTablesStatisticDto.

        **参数解释**： 数据库名称。 **取值范围**： 不涉及。

        :return: The db_name of this ListTablesStatisticDto.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this ListTablesStatisticDto.

        **参数解释**： 数据库名称。 **取值范围**： 不涉及。

        :param db_name: The db_name of this ListTablesStatisticDto.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def schema_name(self):
        r"""Gets the schema_name of this ListTablesStatisticDto.

        **参数解释**： 模式名称。 **取值范围**： 不涉及。

        :return: The schema_name of this ListTablesStatisticDto.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this ListTablesStatisticDto.

        **参数解释**： 模式名称。 **取值范围**： 不涉及。

        :param schema_name: The schema_name of this ListTablesStatisticDto.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def table_name(self):
        r"""Gets the table_name of this ListTablesStatisticDto.

        **参数解释**： 表名。 **取值范围**： 不涉及。

        :return: The table_name of this ListTablesStatisticDto.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this ListTablesStatisticDto.

        **参数解释**： 表名。 **取值范围**： 不涉及。

        :param table_name: The table_name of this ListTablesStatisticDto.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def table_owner(self):
        r"""Gets the table_owner of this ListTablesStatisticDto.

        **参数解释**： 所属用户。 **取值范围**： 不涉及。

        :return: The table_owner of this ListTablesStatisticDto.
        :rtype: str
        """
        return self._table_owner

    @table_owner.setter
    def table_owner(self, table_owner):
        r"""Sets the table_owner of this ListTablesStatisticDto.

        **参数解释**： 所属用户。 **取值范围**： 不涉及。

        :param table_owner: The table_owner of this ListTablesStatisticDto.
        :type table_owner: str
        """
        self._table_owner = table_owner

    @property
    def table_size(self):
        r"""Gets the table_size of this ListTablesStatisticDto.

        **参数解释**： 表大小。 **取值范围**： 不涉及。

        :return: The table_size of this ListTablesStatisticDto.
        :rtype: str
        """
        return self._table_size

    @table_size.setter
    def table_size(self, table_size):
        r"""Sets the table_size of this ListTablesStatisticDto.

        **参数解释**： 表大小。 **取值范围**： 不涉及。

        :param table_size: The table_size of this ListTablesStatisticDto.
        :type table_size: str
        """
        self._table_size = table_size

    @property
    def skew_rate(self):
        r"""Gets the skew_rate of this ListTablesStatisticDto.

        **参数解释**： 表倾斜率。 **取值范围**： 不涉及。

        :return: The skew_rate of this ListTablesStatisticDto.
        :rtype: float
        """
        return self._skew_rate

    @skew_rate.setter
    def skew_rate(self, skew_rate):
        r"""Sets the skew_rate of this ListTablesStatisticDto.

        **参数解释**： 表倾斜率。 **取值范围**： 不涉及。

        :param skew_rate: The skew_rate of this ListTablesStatisticDto.
        :type skew_rate: float
        """
        self._skew_rate = skew_rate

    @property
    def dirty_page_rate(self):
        r"""Gets the dirty_page_rate of this ListTablesStatisticDto.

        **参数解释**： 脏页率。 **取值范围**： 不涉及。

        :return: The dirty_page_rate of this ListTablesStatisticDto.
        :rtype: float
        """
        return self._dirty_page_rate

    @dirty_page_rate.setter
    def dirty_page_rate(self, dirty_page_rate):
        r"""Sets the dirty_page_rate of this ListTablesStatisticDto.

        **参数解释**： 脏页率。 **取值范围**： 不涉及。

        :param dirty_page_rate: The dirty_page_rate of this ListTablesStatisticDto.
        :type dirty_page_rate: float
        """
        self._dirty_page_rate = dirty_page_rate

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
        if not isinstance(other, ListTablesStatisticDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
