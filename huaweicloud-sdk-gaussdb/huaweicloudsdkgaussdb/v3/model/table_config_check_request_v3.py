# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TableConfigCheckRequestV3:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_instance_id': 'str',
        'source_node_id': 'str',
        'source_database_name': 'str',
        'task_name': 'str',
        'db_configs': 'list[DbConfig]',
        'tables_configs': 'list[TablesConfig]',
        'table_repl_config': 'TableReplConfig'
    }

    attribute_map = {
        'source_instance_id': 'source_instance_id',
        'source_node_id': 'source_node_id',
        'source_database_name': 'source_database_name',
        'task_name': 'task_name',
        'db_configs': 'db_configs',
        'tables_configs': 'tables_configs',
        'table_repl_config': 'table_repl_config'
    }

    def __init__(self, source_instance_id=None, source_node_id=None, source_database_name=None, task_name=None, db_configs=None, tables_configs=None, table_repl_config=None):
        """TableConfigCheckRequestV3

        The model defined in huaweicloud sdk

        :param source_instance_id: GaussDB(for MySQL)实例ID。
        :type source_instance_id: str
        :param source_node_id: GaussDB(for MySQL)只读节点ID。如为空，则取GaussDB(for MySQL)主节点ID
        :type source_node_id: str
        :param source_database_name: GaussDB(for MySQL)数据库名。
        :type source_database_name: str
        :param task_name: 同步任务名称。字符长度限制3~128位，仅支持英文大小写字母、数字以及下划线_。
        :type task_name: str
        :param db_configs: 库配置列表。
        :type db_configs: list[:class:`huaweicloudsdkgaussdb.v3.DbConfig`]
        :param tables_configs: 表配置信息。
        :type tables_configs: list[:class:`huaweicloudsdkgaussdb.v3.TablesConfig`]
        :param table_repl_config: 
        :type table_repl_config: :class:`huaweicloudsdkgaussdb.v3.TableReplConfig`
        """
        
        

        self._source_instance_id = None
        self._source_node_id = None
        self._source_database_name = None
        self._task_name = None
        self._db_configs = None
        self._tables_configs = None
        self._table_repl_config = None
        self.discriminator = None

        if source_instance_id is not None:
            self.source_instance_id = source_instance_id
        if source_node_id is not None:
            self.source_node_id = source_node_id
        if source_database_name is not None:
            self.source_database_name = source_database_name
        if task_name is not None:
            self.task_name = task_name
        if db_configs is not None:
            self.db_configs = db_configs
        if tables_configs is not None:
            self.tables_configs = tables_configs
        if table_repl_config is not None:
            self.table_repl_config = table_repl_config

    @property
    def source_instance_id(self):
        """Gets the source_instance_id of this TableConfigCheckRequestV3.

        GaussDB(for MySQL)实例ID。

        :return: The source_instance_id of this TableConfigCheckRequestV3.
        :rtype: str
        """
        return self._source_instance_id

    @source_instance_id.setter
    def source_instance_id(self, source_instance_id):
        """Sets the source_instance_id of this TableConfigCheckRequestV3.

        GaussDB(for MySQL)实例ID。

        :param source_instance_id: The source_instance_id of this TableConfigCheckRequestV3.
        :type source_instance_id: str
        """
        self._source_instance_id = source_instance_id

    @property
    def source_node_id(self):
        """Gets the source_node_id of this TableConfigCheckRequestV3.

        GaussDB(for MySQL)只读节点ID。如为空，则取GaussDB(for MySQL)主节点ID

        :return: The source_node_id of this TableConfigCheckRequestV3.
        :rtype: str
        """
        return self._source_node_id

    @source_node_id.setter
    def source_node_id(self, source_node_id):
        """Sets the source_node_id of this TableConfigCheckRequestV3.

        GaussDB(for MySQL)只读节点ID。如为空，则取GaussDB(for MySQL)主节点ID

        :param source_node_id: The source_node_id of this TableConfigCheckRequestV3.
        :type source_node_id: str
        """
        self._source_node_id = source_node_id

    @property
    def source_database_name(self):
        """Gets the source_database_name of this TableConfigCheckRequestV3.

        GaussDB(for MySQL)数据库名。

        :return: The source_database_name of this TableConfigCheckRequestV3.
        :rtype: str
        """
        return self._source_database_name

    @source_database_name.setter
    def source_database_name(self, source_database_name):
        """Sets the source_database_name of this TableConfigCheckRequestV3.

        GaussDB(for MySQL)数据库名。

        :param source_database_name: The source_database_name of this TableConfigCheckRequestV3.
        :type source_database_name: str
        """
        self._source_database_name = source_database_name

    @property
    def task_name(self):
        """Gets the task_name of this TableConfigCheckRequestV3.

        同步任务名称。字符长度限制3~128位，仅支持英文大小写字母、数字以及下划线_。

        :return: The task_name of this TableConfigCheckRequestV3.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this TableConfigCheckRequestV3.

        同步任务名称。字符长度限制3~128位，仅支持英文大小写字母、数字以及下划线_。

        :param task_name: The task_name of this TableConfigCheckRequestV3.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def db_configs(self):
        """Gets the db_configs of this TableConfigCheckRequestV3.

        库配置列表。

        :return: The db_configs of this TableConfigCheckRequestV3.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.DbConfig`]
        """
        return self._db_configs

    @db_configs.setter
    def db_configs(self, db_configs):
        """Sets the db_configs of this TableConfigCheckRequestV3.

        库配置列表。

        :param db_configs: The db_configs of this TableConfigCheckRequestV3.
        :type db_configs: list[:class:`huaweicloudsdkgaussdb.v3.DbConfig`]
        """
        self._db_configs = db_configs

    @property
    def tables_configs(self):
        """Gets the tables_configs of this TableConfigCheckRequestV3.

        表配置信息。

        :return: The tables_configs of this TableConfigCheckRequestV3.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.TablesConfig`]
        """
        return self._tables_configs

    @tables_configs.setter
    def tables_configs(self, tables_configs):
        """Sets the tables_configs of this TableConfigCheckRequestV3.

        表配置信息。

        :param tables_configs: The tables_configs of this TableConfigCheckRequestV3.
        :type tables_configs: list[:class:`huaweicloudsdkgaussdb.v3.TablesConfig`]
        """
        self._tables_configs = tables_configs

    @property
    def table_repl_config(self):
        """Gets the table_repl_config of this TableConfigCheckRequestV3.

        :return: The table_repl_config of this TableConfigCheckRequestV3.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.TableReplConfig`
        """
        return self._table_repl_config

    @table_repl_config.setter
    def table_repl_config(self, table_repl_config):
        """Sets the table_repl_config of this TableConfigCheckRequestV3.

        :param table_repl_config: The table_repl_config of this TableConfigCheckRequestV3.
        :type table_repl_config: :class:`huaweicloudsdkgaussdb.v3.TableReplConfig`
        """
        self._table_repl_config = table_repl_config

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
        if not isinstance(other, TableConfigCheckRequestV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
