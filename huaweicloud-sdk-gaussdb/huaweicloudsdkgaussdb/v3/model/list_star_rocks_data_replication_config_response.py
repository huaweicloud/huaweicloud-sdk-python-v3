# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStarRocksDataReplicationConfigResponse(SdkResponse):

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
        'database_info': 'DataBaseInfo',
        'table_infos': 'list[TableConfigCheckResult]',
        'table_repl_config': 'TableReplConfig',
        'new_table_repl_config': 'TableReplConfig',
        'target_database_name': 'str',
        'is_tables_change': 'bool',
        'last_error_of_alter_table': 'str'
    }

    attribute_map = {
        'source_instance_id': 'source_instance_id',
        'source_node_id': 'source_node_id',
        'database_info': 'database_info',
        'table_infos': 'table_infos',
        'table_repl_config': 'table_repl_config',
        'new_table_repl_config': 'new_table_repl_config',
        'target_database_name': 'target_database_name',
        'is_tables_change': 'is_tables_change',
        'last_error_of_alter_table': 'last_error_of_alter_table'
    }

    def __init__(self, source_instance_id=None, source_node_id=None, database_info=None, table_infos=None, table_repl_config=None, new_table_repl_config=None, target_database_name=None, is_tables_change=None, last_error_of_alter_table=None):
        """ListStarRocksDataReplicationConfigResponse

        The model defined in huaweicloud sdk

        :param source_instance_id: GaussDB(for MySQL)实例ID。
        :type source_instance_id: str
        :param source_node_id: GaussDB(for MySQL)节点ID。
        :type source_node_id: str
        :param database_info: 
        :type database_info: :class:`huaweicloudsdkgaussdb.v3.DataBaseInfo`
        :param table_infos: 表配置信息。
        :type table_infos: list[:class:`huaweicloudsdkgaussdb.v3.TableConfigCheckResult`]
        :param table_repl_config: 
        :type table_repl_config: :class:`huaweicloudsdkgaussdb.v3.TableReplConfig`
        :param new_table_repl_config: 
        :type new_table_repl_config: :class:`huaweicloudsdkgaussdb.v3.TableReplConfig`
        :param target_database_name: 目标数据库名。
        :type target_database_name: str
        :param is_tables_change: 同步任务表是否变化。
        :type is_tables_change: bool
        :param last_error_of_alter_table: 最近一次alter table的异常信息。
        :type last_error_of_alter_table: str
        """
        
        super(ListStarRocksDataReplicationConfigResponse, self).__init__()

        self._source_instance_id = None
        self._source_node_id = None
        self._database_info = None
        self._table_infos = None
        self._table_repl_config = None
        self._new_table_repl_config = None
        self._target_database_name = None
        self._is_tables_change = None
        self._last_error_of_alter_table = None
        self.discriminator = None

        if source_instance_id is not None:
            self.source_instance_id = source_instance_id
        if source_node_id is not None:
            self.source_node_id = source_node_id
        if database_info is not None:
            self.database_info = database_info
        if table_infos is not None:
            self.table_infos = table_infos
        if table_repl_config is not None:
            self.table_repl_config = table_repl_config
        if new_table_repl_config is not None:
            self.new_table_repl_config = new_table_repl_config
        if target_database_name is not None:
            self.target_database_name = target_database_name
        if is_tables_change is not None:
            self.is_tables_change = is_tables_change
        if last_error_of_alter_table is not None:
            self.last_error_of_alter_table = last_error_of_alter_table

    @property
    def source_instance_id(self):
        """Gets the source_instance_id of this ListStarRocksDataReplicationConfigResponse.

        GaussDB(for MySQL)实例ID。

        :return: The source_instance_id of this ListStarRocksDataReplicationConfigResponse.
        :rtype: str
        """
        return self._source_instance_id

    @source_instance_id.setter
    def source_instance_id(self, source_instance_id):
        """Sets the source_instance_id of this ListStarRocksDataReplicationConfigResponse.

        GaussDB(for MySQL)实例ID。

        :param source_instance_id: The source_instance_id of this ListStarRocksDataReplicationConfigResponse.
        :type source_instance_id: str
        """
        self._source_instance_id = source_instance_id

    @property
    def source_node_id(self):
        """Gets the source_node_id of this ListStarRocksDataReplicationConfigResponse.

        GaussDB(for MySQL)节点ID。

        :return: The source_node_id of this ListStarRocksDataReplicationConfigResponse.
        :rtype: str
        """
        return self._source_node_id

    @source_node_id.setter
    def source_node_id(self, source_node_id):
        """Sets the source_node_id of this ListStarRocksDataReplicationConfigResponse.

        GaussDB(for MySQL)节点ID。

        :param source_node_id: The source_node_id of this ListStarRocksDataReplicationConfigResponse.
        :type source_node_id: str
        """
        self._source_node_id = source_node_id

    @property
    def database_info(self):
        """Gets the database_info of this ListStarRocksDataReplicationConfigResponse.

        :return: The database_info of this ListStarRocksDataReplicationConfigResponse.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DataBaseInfo`
        """
        return self._database_info

    @database_info.setter
    def database_info(self, database_info):
        """Sets the database_info of this ListStarRocksDataReplicationConfigResponse.

        :param database_info: The database_info of this ListStarRocksDataReplicationConfigResponse.
        :type database_info: :class:`huaweicloudsdkgaussdb.v3.DataBaseInfo`
        """
        self._database_info = database_info

    @property
    def table_infos(self):
        """Gets the table_infos of this ListStarRocksDataReplicationConfigResponse.

        表配置信息。

        :return: The table_infos of this ListStarRocksDataReplicationConfigResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.TableConfigCheckResult`]
        """
        return self._table_infos

    @table_infos.setter
    def table_infos(self, table_infos):
        """Sets the table_infos of this ListStarRocksDataReplicationConfigResponse.

        表配置信息。

        :param table_infos: The table_infos of this ListStarRocksDataReplicationConfigResponse.
        :type table_infos: list[:class:`huaweicloudsdkgaussdb.v3.TableConfigCheckResult`]
        """
        self._table_infos = table_infos

    @property
    def table_repl_config(self):
        """Gets the table_repl_config of this ListStarRocksDataReplicationConfigResponse.

        :return: The table_repl_config of this ListStarRocksDataReplicationConfigResponse.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.TableReplConfig`
        """
        return self._table_repl_config

    @table_repl_config.setter
    def table_repl_config(self, table_repl_config):
        """Sets the table_repl_config of this ListStarRocksDataReplicationConfigResponse.

        :param table_repl_config: The table_repl_config of this ListStarRocksDataReplicationConfigResponse.
        :type table_repl_config: :class:`huaweicloudsdkgaussdb.v3.TableReplConfig`
        """
        self._table_repl_config = table_repl_config

    @property
    def new_table_repl_config(self):
        """Gets the new_table_repl_config of this ListStarRocksDataReplicationConfigResponse.

        :return: The new_table_repl_config of this ListStarRocksDataReplicationConfigResponse.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.TableReplConfig`
        """
        return self._new_table_repl_config

    @new_table_repl_config.setter
    def new_table_repl_config(self, new_table_repl_config):
        """Sets the new_table_repl_config of this ListStarRocksDataReplicationConfigResponse.

        :param new_table_repl_config: The new_table_repl_config of this ListStarRocksDataReplicationConfigResponse.
        :type new_table_repl_config: :class:`huaweicloudsdkgaussdb.v3.TableReplConfig`
        """
        self._new_table_repl_config = new_table_repl_config

    @property
    def target_database_name(self):
        """Gets the target_database_name of this ListStarRocksDataReplicationConfigResponse.

        目标数据库名。

        :return: The target_database_name of this ListStarRocksDataReplicationConfigResponse.
        :rtype: str
        """
        return self._target_database_name

    @target_database_name.setter
    def target_database_name(self, target_database_name):
        """Sets the target_database_name of this ListStarRocksDataReplicationConfigResponse.

        目标数据库名。

        :param target_database_name: The target_database_name of this ListStarRocksDataReplicationConfigResponse.
        :type target_database_name: str
        """
        self._target_database_name = target_database_name

    @property
    def is_tables_change(self):
        """Gets the is_tables_change of this ListStarRocksDataReplicationConfigResponse.

        同步任务表是否变化。

        :return: The is_tables_change of this ListStarRocksDataReplicationConfigResponse.
        :rtype: bool
        """
        return self._is_tables_change

    @is_tables_change.setter
    def is_tables_change(self, is_tables_change):
        """Sets the is_tables_change of this ListStarRocksDataReplicationConfigResponse.

        同步任务表是否变化。

        :param is_tables_change: The is_tables_change of this ListStarRocksDataReplicationConfigResponse.
        :type is_tables_change: bool
        """
        self._is_tables_change = is_tables_change

    @property
    def last_error_of_alter_table(self):
        """Gets the last_error_of_alter_table of this ListStarRocksDataReplicationConfigResponse.

        最近一次alter table的异常信息。

        :return: The last_error_of_alter_table of this ListStarRocksDataReplicationConfigResponse.
        :rtype: str
        """
        return self._last_error_of_alter_table

    @last_error_of_alter_table.setter
    def last_error_of_alter_table(self, last_error_of_alter_table):
        """Sets the last_error_of_alter_table of this ListStarRocksDataReplicationConfigResponse.

        最近一次alter table的异常信息。

        :param last_error_of_alter_table: The last_error_of_alter_table of this ListStarRocksDataReplicationConfigResponse.
        :type last_error_of_alter_table: str
        """
        self._last_error_of_alter_table = last_error_of_alter_table

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
        if not isinstance(other, ListStarRocksDataReplicationConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
