# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDataPreviewRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'guid': 'str',
        'data_connection_id': 'str',
        'data_type': 'str',
        'database': 'str',
        'schema': 'str',
        'table': 'str',
        'datasource_workspace_id': 'str',
        'partitions_condition': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'guid': 'guid',
        'data_connection_id': 'data_connection_id',
        'data_type': 'data_type',
        'database': 'database',
        'schema': 'schema',
        'table': 'table',
        'datasource_workspace_id': 'datasource_workspace_id',
        'partitions_condition': 'partitions_condition'
    }

    def __init__(self, workspace=None, guid=None, data_connection_id=None, data_type=None, database=None, schema=None, table=None, datasource_workspace_id=None, partitions_condition=None):
        r"""ShowDataPreviewRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param guid: 资产guid，获取方法请参见[数据资产guid](dataartsstudio_02_0351.xml)。
        :type guid: str
        :param data_connection_id: 连接id
        :type data_connection_id: str
        :param data_type: 数据源表类型，取值范围：hive_table、dws_table、dli_table、dli_table_managed、dli_table_external、dli_table_view、mysql_table、gbase_table、postgre_table、hbase_table、dm_table、doris_table、sqlserver_table。
        :type data_type: str
        :param database: database名称
        :type database: str
        :param schema: schema名称
        :type schema: str
        :param table: table名称
        :type table: str
        :param datasource_workspace_id: 数据源空间id
        :type datasource_workspace_id: str
        :param partitions_condition: 分区名称，hive类型数据源可使用预览分区中数据
        :type partitions_condition: str
        """
        
        

        self._workspace = None
        self._guid = None
        self._data_connection_id = None
        self._data_type = None
        self._database = None
        self._schema = None
        self._table = None
        self._datasource_workspace_id = None
        self._partitions_condition = None
        self.discriminator = None

        self.workspace = workspace
        self.guid = guid
        if data_connection_id is not None:
            self.data_connection_id = data_connection_id
        if data_type is not None:
            self.data_type = data_type
        if database is not None:
            self.database = database
        if schema is not None:
            self.schema = schema
        if table is not None:
            self.table = table
        if datasource_workspace_id is not None:
            self.datasource_workspace_id = datasource_workspace_id
        if partitions_condition is not None:
            self.partitions_condition = partitions_condition

    @property
    def workspace(self):
        r"""Gets the workspace of this ShowDataPreviewRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this ShowDataPreviewRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ShowDataPreviewRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this ShowDataPreviewRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def guid(self):
        r"""Gets the guid of this ShowDataPreviewRequest.

        资产guid，获取方法请参见[数据资产guid](dataartsstudio_02_0351.xml)。

        :return: The guid of this ShowDataPreviewRequest.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        r"""Sets the guid of this ShowDataPreviewRequest.

        资产guid，获取方法请参见[数据资产guid](dataartsstudio_02_0351.xml)。

        :param guid: The guid of this ShowDataPreviewRequest.
        :type guid: str
        """
        self._guid = guid

    @property
    def data_connection_id(self):
        r"""Gets the data_connection_id of this ShowDataPreviewRequest.

        连接id

        :return: The data_connection_id of this ShowDataPreviewRequest.
        :rtype: str
        """
        return self._data_connection_id

    @data_connection_id.setter
    def data_connection_id(self, data_connection_id):
        r"""Sets the data_connection_id of this ShowDataPreviewRequest.

        连接id

        :param data_connection_id: The data_connection_id of this ShowDataPreviewRequest.
        :type data_connection_id: str
        """
        self._data_connection_id = data_connection_id

    @property
    def data_type(self):
        r"""Gets the data_type of this ShowDataPreviewRequest.

        数据源表类型，取值范围：hive_table、dws_table、dli_table、dli_table_managed、dli_table_external、dli_table_view、mysql_table、gbase_table、postgre_table、hbase_table、dm_table、doris_table、sqlserver_table。

        :return: The data_type of this ShowDataPreviewRequest.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        r"""Sets the data_type of this ShowDataPreviewRequest.

        数据源表类型，取值范围：hive_table、dws_table、dli_table、dli_table_managed、dli_table_external、dli_table_view、mysql_table、gbase_table、postgre_table、hbase_table、dm_table、doris_table、sqlserver_table。

        :param data_type: The data_type of this ShowDataPreviewRequest.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def database(self):
        r"""Gets the database of this ShowDataPreviewRequest.

        database名称

        :return: The database of this ShowDataPreviewRequest.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this ShowDataPreviewRequest.

        database名称

        :param database: The database of this ShowDataPreviewRequest.
        :type database: str
        """
        self._database = database

    @property
    def schema(self):
        r"""Gets the schema of this ShowDataPreviewRequest.

        schema名称

        :return: The schema of this ShowDataPreviewRequest.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this ShowDataPreviewRequest.

        schema名称

        :param schema: The schema of this ShowDataPreviewRequest.
        :type schema: str
        """
        self._schema = schema

    @property
    def table(self):
        r"""Gets the table of this ShowDataPreviewRequest.

        table名称

        :return: The table of this ShowDataPreviewRequest.
        :rtype: str
        """
        return self._table

    @table.setter
    def table(self, table):
        r"""Sets the table of this ShowDataPreviewRequest.

        table名称

        :param table: The table of this ShowDataPreviewRequest.
        :type table: str
        """
        self._table = table

    @property
    def datasource_workspace_id(self):
        r"""Gets the datasource_workspace_id of this ShowDataPreviewRequest.

        数据源空间id

        :return: The datasource_workspace_id of this ShowDataPreviewRequest.
        :rtype: str
        """
        return self._datasource_workspace_id

    @datasource_workspace_id.setter
    def datasource_workspace_id(self, datasource_workspace_id):
        r"""Sets the datasource_workspace_id of this ShowDataPreviewRequest.

        数据源空间id

        :param datasource_workspace_id: The datasource_workspace_id of this ShowDataPreviewRequest.
        :type datasource_workspace_id: str
        """
        self._datasource_workspace_id = datasource_workspace_id

    @property
    def partitions_condition(self):
        r"""Gets the partitions_condition of this ShowDataPreviewRequest.

        分区名称，hive类型数据源可使用预览分区中数据

        :return: The partitions_condition of this ShowDataPreviewRequest.
        :rtype: str
        """
        return self._partitions_condition

    @partitions_condition.setter
    def partitions_condition(self, partitions_condition):
        r"""Sets the partitions_condition of this ShowDataPreviewRequest.

        分区名称，hive类型数据源可使用预览分区中数据

        :param partitions_condition: The partitions_condition of this ShowDataPreviewRequest.
        :type partitions_condition: str
        """
        self._partitions_condition = partitions_condition

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
        if not isinstance(other, ShowDataPreviewRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
