# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutoIncrementUsageRespAutoIncrementUsageList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database': 'str',
        'table': 'str',
        'column': 'str',
        'current_value': 'str',
        'max_value': 'str',
        'ratio': 'str'
    }

    attribute_map = {
        'database': 'database',
        'table': 'table',
        'column': 'column',
        'current_value': 'current_value',
        'max_value': 'max_value',
        'ratio': 'ratio'
    }

    def __init__(self, database=None, table=None, column=None, current_value=None, max_value=None, ratio=None):
        r"""AutoIncrementUsageRespAutoIncrementUsageList

        The model defined in huaweicloud sdk

        :param database: 数据库名
        :type database: str
        :param table: 表名
        :type table: str
        :param column: 列名
        :type column: str
        :param current_value: 自增ID当前值
        :type current_value: str
        :param max_value: 该数据类型的自增 ID 支持的最大值。
        :type max_value: str
        :param ratio: 自增ID使用比例
        :type ratio: str
        """
        
        

        self._database = None
        self._table = None
        self._column = None
        self._current_value = None
        self._max_value = None
        self._ratio = None
        self.discriminator = None

        self.database = database
        self.table = table
        self.column = column
        self.current_value = current_value
        self.max_value = max_value
        self.ratio = ratio

    @property
    def database(self):
        r"""Gets the database of this AutoIncrementUsageRespAutoIncrementUsageList.

        数据库名

        :return: The database of this AutoIncrementUsageRespAutoIncrementUsageList.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this AutoIncrementUsageRespAutoIncrementUsageList.

        数据库名

        :param database: The database of this AutoIncrementUsageRespAutoIncrementUsageList.
        :type database: str
        """
        self._database = database

    @property
    def table(self):
        r"""Gets the table of this AutoIncrementUsageRespAutoIncrementUsageList.

        表名

        :return: The table of this AutoIncrementUsageRespAutoIncrementUsageList.
        :rtype: str
        """
        return self._table

    @table.setter
    def table(self, table):
        r"""Sets the table of this AutoIncrementUsageRespAutoIncrementUsageList.

        表名

        :param table: The table of this AutoIncrementUsageRespAutoIncrementUsageList.
        :type table: str
        """
        self._table = table

    @property
    def column(self):
        r"""Gets the column of this AutoIncrementUsageRespAutoIncrementUsageList.

        列名

        :return: The column of this AutoIncrementUsageRespAutoIncrementUsageList.
        :rtype: str
        """
        return self._column

    @column.setter
    def column(self, column):
        r"""Sets the column of this AutoIncrementUsageRespAutoIncrementUsageList.

        列名

        :param column: The column of this AutoIncrementUsageRespAutoIncrementUsageList.
        :type column: str
        """
        self._column = column

    @property
    def current_value(self):
        r"""Gets the current_value of this AutoIncrementUsageRespAutoIncrementUsageList.

        自增ID当前值

        :return: The current_value of this AutoIncrementUsageRespAutoIncrementUsageList.
        :rtype: str
        """
        return self._current_value

    @current_value.setter
    def current_value(self, current_value):
        r"""Sets the current_value of this AutoIncrementUsageRespAutoIncrementUsageList.

        自增ID当前值

        :param current_value: The current_value of this AutoIncrementUsageRespAutoIncrementUsageList.
        :type current_value: str
        """
        self._current_value = current_value

    @property
    def max_value(self):
        r"""Gets the max_value of this AutoIncrementUsageRespAutoIncrementUsageList.

        该数据类型的自增 ID 支持的最大值。

        :return: The max_value of this AutoIncrementUsageRespAutoIncrementUsageList.
        :rtype: str
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        r"""Sets the max_value of this AutoIncrementUsageRespAutoIncrementUsageList.

        该数据类型的自增 ID 支持的最大值。

        :param max_value: The max_value of this AutoIncrementUsageRespAutoIncrementUsageList.
        :type max_value: str
        """
        self._max_value = max_value

    @property
    def ratio(self):
        r"""Gets the ratio of this AutoIncrementUsageRespAutoIncrementUsageList.

        自增ID使用比例

        :return: The ratio of this AutoIncrementUsageRespAutoIncrementUsageList.
        :rtype: str
        """
        return self._ratio

    @ratio.setter
    def ratio(self, ratio):
        r"""Sets the ratio of this AutoIncrementUsageRespAutoIncrementUsageList.

        自增ID使用比例

        :param ratio: The ratio of this AutoIncrementUsageRespAutoIncrementUsageList.
        :type ratio: str
        """
        self._ratio = ratio

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
        if not isinstance(other, AutoIncrementUsageRespAutoIncrementUsageList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
