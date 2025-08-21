# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubNodeLineageConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'sql_statement': 'str',
        'input_tables': 'list[TableConfig]',
        'output_table': 'TableConfig',
        'column_lineages': 'list[ColumnLineageConfig]'
    }

    attribute_map = {
        'name': 'name',
        'sql_statement': 'sql_statement',
        'input_tables': 'input_tables',
        'output_table': 'output_table',
        'column_lineages': 'column_lineages'
    }

    def __init__(self, name=None, sql_statement=None, input_tables=None, output_table=None, column_lineages=None):
        r"""SubNodeLineageConfig

        The model defined in huaweicloud sdk

        :param name: 节点名称。
        :type name: str
        :param sql_statement: 待接续sql语句。
        :type sql_statement: str
        :param input_tables: 输入表。
        :type input_tables: list[:class:`huaweicloudsdkdataartsstudio.v1.TableConfig`]
        :param output_table: 
        :type output_table: :class:`huaweicloudsdkdataartsstudio.v1.TableConfig`
        :param column_lineages: 字段血缘信息。
        :type column_lineages: list[:class:`huaweicloudsdkdataartsstudio.v1.ColumnLineageConfig`]
        """
        
        

        self._name = None
        self._sql_statement = None
        self._input_tables = None
        self._output_table = None
        self._column_lineages = None
        self.discriminator = None

        self.name = name
        if sql_statement is not None:
            self.sql_statement = sql_statement
        self.input_tables = input_tables
        self.output_table = output_table
        if column_lineages is not None:
            self.column_lineages = column_lineages

    @property
    def name(self):
        r"""Gets the name of this SubNodeLineageConfig.

        节点名称。

        :return: The name of this SubNodeLineageConfig.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SubNodeLineageConfig.

        节点名称。

        :param name: The name of this SubNodeLineageConfig.
        :type name: str
        """
        self._name = name

    @property
    def sql_statement(self):
        r"""Gets the sql_statement of this SubNodeLineageConfig.

        待接续sql语句。

        :return: The sql_statement of this SubNodeLineageConfig.
        :rtype: str
        """
        return self._sql_statement

    @sql_statement.setter
    def sql_statement(self, sql_statement):
        r"""Sets the sql_statement of this SubNodeLineageConfig.

        待接续sql语句。

        :param sql_statement: The sql_statement of this SubNodeLineageConfig.
        :type sql_statement: str
        """
        self._sql_statement = sql_statement

    @property
    def input_tables(self):
        r"""Gets the input_tables of this SubNodeLineageConfig.

        输入表。

        :return: The input_tables of this SubNodeLineageConfig.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.TableConfig`]
        """
        return self._input_tables

    @input_tables.setter
    def input_tables(self, input_tables):
        r"""Sets the input_tables of this SubNodeLineageConfig.

        输入表。

        :param input_tables: The input_tables of this SubNodeLineageConfig.
        :type input_tables: list[:class:`huaweicloudsdkdataartsstudio.v1.TableConfig`]
        """
        self._input_tables = input_tables

    @property
    def output_table(self):
        r"""Gets the output_table of this SubNodeLineageConfig.

        :return: The output_table of this SubNodeLineageConfig.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.TableConfig`
        """
        return self._output_table

    @output_table.setter
    def output_table(self, output_table):
        r"""Sets the output_table of this SubNodeLineageConfig.

        :param output_table: The output_table of this SubNodeLineageConfig.
        :type output_table: :class:`huaweicloudsdkdataartsstudio.v1.TableConfig`
        """
        self._output_table = output_table

    @property
    def column_lineages(self):
        r"""Gets the column_lineages of this SubNodeLineageConfig.

        字段血缘信息。

        :return: The column_lineages of this SubNodeLineageConfig.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ColumnLineageConfig`]
        """
        return self._column_lineages

    @column_lineages.setter
    def column_lineages(self, column_lineages):
        r"""Sets the column_lineages of this SubNodeLineageConfig.

        字段血缘信息。

        :param column_lineages: The column_lineages of this SubNodeLineageConfig.
        :type column_lineages: list[:class:`huaweicloudsdkdataartsstudio.v1.ColumnLineageConfig`]
        """
        self._column_lineages = column_lineages

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
        if not isinstance(other, SubNodeLineageConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
