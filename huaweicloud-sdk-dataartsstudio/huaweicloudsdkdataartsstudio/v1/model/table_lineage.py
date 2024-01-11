# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TableLineage:

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
        'input_tables': 'list[TableInfo]',
        'output_tables': 'list[TableInfo]',
        'source_connection_id': 'str',
        'target_connection_id': 'str',
        'column_lineages': 'list[ColumnLineage]'
    }

    attribute_map = {
        'name': 'name',
        'input_tables': 'input_tables',
        'output_tables': 'output_tables',
        'source_connection_id': 'source_connection_id',
        'target_connection_id': 'target_connection_id',
        'column_lineages': 'column_lineages'
    }

    def __init__(self, name=None, input_tables=None, output_tables=None, source_connection_id=None, target_connection_id=None, column_lineages=None):
        """TableLineage

        The model defined in huaweicloud sdk

        :param name: 作业算子名称
        :type name: str
        :param input_tables: 上游血缘表列表，列表大小：1至100
        :type input_tables: list[:class:`huaweicloudsdkdataartsstudio.v1.TableInfo`]
        :param output_tables: 下游血缘表列表，列表大小：1至100
        :type output_tables: list[:class:`huaweicloudsdkdataartsstudio.v1.TableInfo`]
        :param source_connection_id: 源数据连接id
        :type source_connection_id: str
        :param target_connection_id: 目标数据连接id
        :type target_connection_id: str
        :param column_lineages: 字段血缘列表，列表大小：0至100
        :type column_lineages: list[:class:`huaweicloudsdkdataartsstudio.v1.ColumnLineage`]
        """
        
        

        self._name = None
        self._input_tables = None
        self._output_tables = None
        self._source_connection_id = None
        self._target_connection_id = None
        self._column_lineages = None
        self.discriminator = None

        self.name = name
        self.input_tables = input_tables
        self.output_tables = output_tables
        self.source_connection_id = source_connection_id
        if target_connection_id is not None:
            self.target_connection_id = target_connection_id
        if column_lineages is not None:
            self.column_lineages = column_lineages

    @property
    def name(self):
        """Gets the name of this TableLineage.

        作业算子名称

        :return: The name of this TableLineage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TableLineage.

        作业算子名称

        :param name: The name of this TableLineage.
        :type name: str
        """
        self._name = name

    @property
    def input_tables(self):
        """Gets the input_tables of this TableLineage.

        上游血缘表列表，列表大小：1至100

        :return: The input_tables of this TableLineage.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.TableInfo`]
        """
        return self._input_tables

    @input_tables.setter
    def input_tables(self, input_tables):
        """Sets the input_tables of this TableLineage.

        上游血缘表列表，列表大小：1至100

        :param input_tables: The input_tables of this TableLineage.
        :type input_tables: list[:class:`huaweicloudsdkdataartsstudio.v1.TableInfo`]
        """
        self._input_tables = input_tables

    @property
    def output_tables(self):
        """Gets the output_tables of this TableLineage.

        下游血缘表列表，列表大小：1至100

        :return: The output_tables of this TableLineage.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.TableInfo`]
        """
        return self._output_tables

    @output_tables.setter
    def output_tables(self, output_tables):
        """Sets the output_tables of this TableLineage.

        下游血缘表列表，列表大小：1至100

        :param output_tables: The output_tables of this TableLineage.
        :type output_tables: list[:class:`huaweicloudsdkdataartsstudio.v1.TableInfo`]
        """
        self._output_tables = output_tables

    @property
    def source_connection_id(self):
        """Gets the source_connection_id of this TableLineage.

        源数据连接id

        :return: The source_connection_id of this TableLineage.
        :rtype: str
        """
        return self._source_connection_id

    @source_connection_id.setter
    def source_connection_id(self, source_connection_id):
        """Sets the source_connection_id of this TableLineage.

        源数据连接id

        :param source_connection_id: The source_connection_id of this TableLineage.
        :type source_connection_id: str
        """
        self._source_connection_id = source_connection_id

    @property
    def target_connection_id(self):
        """Gets the target_connection_id of this TableLineage.

        目标数据连接id

        :return: The target_connection_id of this TableLineage.
        :rtype: str
        """
        return self._target_connection_id

    @target_connection_id.setter
    def target_connection_id(self, target_connection_id):
        """Sets the target_connection_id of this TableLineage.

        目标数据连接id

        :param target_connection_id: The target_connection_id of this TableLineage.
        :type target_connection_id: str
        """
        self._target_connection_id = target_connection_id

    @property
    def column_lineages(self):
        """Gets the column_lineages of this TableLineage.

        字段血缘列表，列表大小：0至100

        :return: The column_lineages of this TableLineage.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ColumnLineage`]
        """
        return self._column_lineages

    @column_lineages.setter
    def column_lineages(self, column_lineages):
        """Sets the column_lineages of this TableLineage.

        字段血缘列表，列表大小：0至100

        :param column_lineages: The column_lineages of this TableLineage.
        :type column_lineages: list[:class:`huaweicloudsdkdataartsstudio.v1.ColumnLineage`]
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
        if not isinstance(other, TableLineage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
