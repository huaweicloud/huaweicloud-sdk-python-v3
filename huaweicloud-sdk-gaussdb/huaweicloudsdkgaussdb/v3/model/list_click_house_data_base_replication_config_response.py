# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClickHouseDataBaseReplicationConfigResponse(SdkResponse):

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
        'database_info': 'ChDatabaseConfigResponse',
        'table_infos': 'list[ChDatabaseTableConfigCheckResult]',
        'table_repl_config': 'ChDatabaseTableReplConfigInfo',
        'is_tables_change': 'bool',
        'new_table_repl_config': 'ChDatabaseTableReplConfigInfo',
        'last_error_of_alter_table': 'str'
    }

    attribute_map = {
        'source_instance_id': 'source_instance_id',
        'source_node_id': 'source_node_id',
        'database_info': 'database_info',
        'table_infos': 'table_infos',
        'table_repl_config': 'table_repl_config',
        'is_tables_change': 'is_tables_change',
        'new_table_repl_config': 'new_table_repl_config',
        'last_error_of_alter_table': 'last_error_of_alter_table'
    }

    def __init__(self, source_instance_id=None, source_node_id=None, database_info=None, table_infos=None, table_repl_config=None, is_tables_change=None, new_table_repl_config=None, last_error_of_alter_table=None):
        r"""ListClickHouseDataBaseReplicationConfigResponse

        The model defined in huaweicloud sdk

        :param source_instance_id: 源实例ID。
        :type source_instance_id: str
        :param source_node_id: 源实例节点ID。
        :type source_node_id: str
        :param database_info: 
        :type database_info: :class:`huaweicloudsdkgaussdb.v3.ChDatabaseConfigResponse`
        :param table_infos: 表配置信息。
        :type table_infos: list[:class:`huaweicloudsdkgaussdb.v3.ChDatabaseTableConfigCheckResult`]
        :param table_repl_config: 
        :type table_repl_config: :class:`huaweicloudsdkgaussdb.v3.ChDatabaseTableReplConfigInfo`
        :param is_tables_change: 同步任务表是否变化。
        :type is_tables_change: bool
        :param new_table_repl_config: 
        :type new_table_repl_config: :class:`huaweicloudsdkgaussdb.v3.ChDatabaseTableReplConfigInfo`
        :param last_error_of_alter_table: 最近一次alter table的异常信息。
        :type last_error_of_alter_table: str
        """
        
        super(ListClickHouseDataBaseReplicationConfigResponse, self).__init__()

        self._source_instance_id = None
        self._source_node_id = None
        self._database_info = None
        self._table_infos = None
        self._table_repl_config = None
        self._is_tables_change = None
        self._new_table_repl_config = None
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
        if is_tables_change is not None:
            self.is_tables_change = is_tables_change
        if new_table_repl_config is not None:
            self.new_table_repl_config = new_table_repl_config
        if last_error_of_alter_table is not None:
            self.last_error_of_alter_table = last_error_of_alter_table

    @property
    def source_instance_id(self):
        r"""Gets the source_instance_id of this ListClickHouseDataBaseReplicationConfigResponse.

        源实例ID。

        :return: The source_instance_id of this ListClickHouseDataBaseReplicationConfigResponse.
        :rtype: str
        """
        return self._source_instance_id

    @source_instance_id.setter
    def source_instance_id(self, source_instance_id):
        r"""Sets the source_instance_id of this ListClickHouseDataBaseReplicationConfigResponse.

        源实例ID。

        :param source_instance_id: The source_instance_id of this ListClickHouseDataBaseReplicationConfigResponse.
        :type source_instance_id: str
        """
        self._source_instance_id = source_instance_id

    @property
    def source_node_id(self):
        r"""Gets the source_node_id of this ListClickHouseDataBaseReplicationConfigResponse.

        源实例节点ID。

        :return: The source_node_id of this ListClickHouseDataBaseReplicationConfigResponse.
        :rtype: str
        """
        return self._source_node_id

    @source_node_id.setter
    def source_node_id(self, source_node_id):
        r"""Sets the source_node_id of this ListClickHouseDataBaseReplicationConfigResponse.

        源实例节点ID。

        :param source_node_id: The source_node_id of this ListClickHouseDataBaseReplicationConfigResponse.
        :type source_node_id: str
        """
        self._source_node_id = source_node_id

    @property
    def database_info(self):
        r"""Gets the database_info of this ListClickHouseDataBaseReplicationConfigResponse.

        :return: The database_info of this ListClickHouseDataBaseReplicationConfigResponse.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ChDatabaseConfigResponse`
        """
        return self._database_info

    @database_info.setter
    def database_info(self, database_info):
        r"""Sets the database_info of this ListClickHouseDataBaseReplicationConfigResponse.

        :param database_info: The database_info of this ListClickHouseDataBaseReplicationConfigResponse.
        :type database_info: :class:`huaweicloudsdkgaussdb.v3.ChDatabaseConfigResponse`
        """
        self._database_info = database_info

    @property
    def table_infos(self):
        r"""Gets the table_infos of this ListClickHouseDataBaseReplicationConfigResponse.

        表配置信息。

        :return: The table_infos of this ListClickHouseDataBaseReplicationConfigResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.ChDatabaseTableConfigCheckResult`]
        """
        return self._table_infos

    @table_infos.setter
    def table_infos(self, table_infos):
        r"""Sets the table_infos of this ListClickHouseDataBaseReplicationConfigResponse.

        表配置信息。

        :param table_infos: The table_infos of this ListClickHouseDataBaseReplicationConfigResponse.
        :type table_infos: list[:class:`huaweicloudsdkgaussdb.v3.ChDatabaseTableConfigCheckResult`]
        """
        self._table_infos = table_infos

    @property
    def table_repl_config(self):
        r"""Gets the table_repl_config of this ListClickHouseDataBaseReplicationConfigResponse.

        :return: The table_repl_config of this ListClickHouseDataBaseReplicationConfigResponse.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ChDatabaseTableReplConfigInfo`
        """
        return self._table_repl_config

    @table_repl_config.setter
    def table_repl_config(self, table_repl_config):
        r"""Sets the table_repl_config of this ListClickHouseDataBaseReplicationConfigResponse.

        :param table_repl_config: The table_repl_config of this ListClickHouseDataBaseReplicationConfigResponse.
        :type table_repl_config: :class:`huaweicloudsdkgaussdb.v3.ChDatabaseTableReplConfigInfo`
        """
        self._table_repl_config = table_repl_config

    @property
    def is_tables_change(self):
        r"""Gets the is_tables_change of this ListClickHouseDataBaseReplicationConfigResponse.

        同步任务表是否变化。

        :return: The is_tables_change of this ListClickHouseDataBaseReplicationConfigResponse.
        :rtype: bool
        """
        return self._is_tables_change

    @is_tables_change.setter
    def is_tables_change(self, is_tables_change):
        r"""Sets the is_tables_change of this ListClickHouseDataBaseReplicationConfigResponse.

        同步任务表是否变化。

        :param is_tables_change: The is_tables_change of this ListClickHouseDataBaseReplicationConfigResponse.
        :type is_tables_change: bool
        """
        self._is_tables_change = is_tables_change

    @property
    def new_table_repl_config(self):
        r"""Gets the new_table_repl_config of this ListClickHouseDataBaseReplicationConfigResponse.

        :return: The new_table_repl_config of this ListClickHouseDataBaseReplicationConfigResponse.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ChDatabaseTableReplConfigInfo`
        """
        return self._new_table_repl_config

    @new_table_repl_config.setter
    def new_table_repl_config(self, new_table_repl_config):
        r"""Sets the new_table_repl_config of this ListClickHouseDataBaseReplicationConfigResponse.

        :param new_table_repl_config: The new_table_repl_config of this ListClickHouseDataBaseReplicationConfigResponse.
        :type new_table_repl_config: :class:`huaweicloudsdkgaussdb.v3.ChDatabaseTableReplConfigInfo`
        """
        self._new_table_repl_config = new_table_repl_config

    @property
    def last_error_of_alter_table(self):
        r"""Gets the last_error_of_alter_table of this ListClickHouseDataBaseReplicationConfigResponse.

        最近一次alter table的异常信息。

        :return: The last_error_of_alter_table of this ListClickHouseDataBaseReplicationConfigResponse.
        :rtype: str
        """
        return self._last_error_of_alter_table

    @last_error_of_alter_table.setter
    def last_error_of_alter_table(self, last_error_of_alter_table):
        r"""Sets the last_error_of_alter_table of this ListClickHouseDataBaseReplicationConfigResponse.

        最近一次alter table的异常信息。

        :param last_error_of_alter_table: The last_error_of_alter_table of this ListClickHouseDataBaseReplicationConfigResponse.
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
        if not isinstance(other, ListClickHouseDataBaseReplicationConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
