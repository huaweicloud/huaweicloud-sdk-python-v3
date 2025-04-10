# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkspaceTransformVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_model_id': 'str',
        'target_model_name': 'str',
        'description': 'str',
        'update_exist_tables': 'bool',
        'ids': 'list[str]',
        'dw_type': 'str',
        'connection_id': 'str',
        'database': 'str',
        'queue': 'str',
        'schema': 'str'
    }

    attribute_map = {
        'target_model_id': 'target_model_id',
        'target_model_name': 'target_model_name',
        'description': 'description',
        'update_exist_tables': 'update_exist_tables',
        'ids': 'ids',
        'dw_type': 'dw_type',
        'connection_id': 'connection_id',
        'database': 'database',
        'queue': 'queue',
        'schema': 'schema'
    }

    def __init__(self, target_model_id=None, target_model_name=None, description=None, update_exist_tables=None, ids=None, dw_type=None, connection_id=None, database=None, queue=None, schema=None):
        r"""WorkspaceTransformVO

        The model defined in huaweicloud sdk

        :param target_model_id: 所属关系建模的模型ID，ID字符串。
        :type target_model_id: str
        :param target_model_name: 工作区名字。
        :type target_model_name: str
        :param description: 描述。
        :type description: str
        :param update_exist_tables: 是否更新已有表。
        :type update_exist_tables: bool
        :param ids: 需要物化的逻辑实体的ID列表，ID字符串。
        :type ids: list[str]
        :param dw_type: 数据连接类型，对应表所在的数仓类型，取值可以为DLI、DWS、MRS_HIVE、POSTGRESQL、MRS_SPARK、CLICKHOUSE、MYSQL、ORACLE和DORIS等。
        :type dw_type: str
        :param connection_id: 转化后物理表所属的数据连接ID。
        :type connection_id: str
        :param database: 转化后物理表所属的数据库。
        :type database: str
        :param queue: 转化后物理表所属的队列（仅DLI）。
        :type queue: str
        :param schema: 转化后物理表所属的schema（仅DWS和PostgreSQL）。
        :type schema: str
        """
        
        

        self._target_model_id = None
        self._target_model_name = None
        self._description = None
        self._update_exist_tables = None
        self._ids = None
        self._dw_type = None
        self._connection_id = None
        self._database = None
        self._queue = None
        self._schema = None
        self.discriminator = None

        if target_model_id is not None:
            self.target_model_id = target_model_id
        self.target_model_name = target_model_name
        if description is not None:
            self.description = description
        if update_exist_tables is not None:
            self.update_exist_tables = update_exist_tables
        if ids is not None:
            self.ids = ids
        self.dw_type = dw_type
        if connection_id is not None:
            self.connection_id = connection_id
        if database is not None:
            self.database = database
        if queue is not None:
            self.queue = queue
        if schema is not None:
            self.schema = schema

    @property
    def target_model_id(self):
        r"""Gets the target_model_id of this WorkspaceTransformVO.

        所属关系建模的模型ID，ID字符串。

        :return: The target_model_id of this WorkspaceTransformVO.
        :rtype: str
        """
        return self._target_model_id

    @target_model_id.setter
    def target_model_id(self, target_model_id):
        r"""Sets the target_model_id of this WorkspaceTransformVO.

        所属关系建模的模型ID，ID字符串。

        :param target_model_id: The target_model_id of this WorkspaceTransformVO.
        :type target_model_id: str
        """
        self._target_model_id = target_model_id

    @property
    def target_model_name(self):
        r"""Gets the target_model_name of this WorkspaceTransformVO.

        工作区名字。

        :return: The target_model_name of this WorkspaceTransformVO.
        :rtype: str
        """
        return self._target_model_name

    @target_model_name.setter
    def target_model_name(self, target_model_name):
        r"""Sets the target_model_name of this WorkspaceTransformVO.

        工作区名字。

        :param target_model_name: The target_model_name of this WorkspaceTransformVO.
        :type target_model_name: str
        """
        self._target_model_name = target_model_name

    @property
    def description(self):
        r"""Gets the description of this WorkspaceTransformVO.

        描述。

        :return: The description of this WorkspaceTransformVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this WorkspaceTransformVO.

        描述。

        :param description: The description of this WorkspaceTransformVO.
        :type description: str
        """
        self._description = description

    @property
    def update_exist_tables(self):
        r"""Gets the update_exist_tables of this WorkspaceTransformVO.

        是否更新已有表。

        :return: The update_exist_tables of this WorkspaceTransformVO.
        :rtype: bool
        """
        return self._update_exist_tables

    @update_exist_tables.setter
    def update_exist_tables(self, update_exist_tables):
        r"""Sets the update_exist_tables of this WorkspaceTransformVO.

        是否更新已有表。

        :param update_exist_tables: The update_exist_tables of this WorkspaceTransformVO.
        :type update_exist_tables: bool
        """
        self._update_exist_tables = update_exist_tables

    @property
    def ids(self):
        r"""Gets the ids of this WorkspaceTransformVO.

        需要物化的逻辑实体的ID列表，ID字符串。

        :return: The ids of this WorkspaceTransformVO.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this WorkspaceTransformVO.

        需要物化的逻辑实体的ID列表，ID字符串。

        :param ids: The ids of this WorkspaceTransformVO.
        :type ids: list[str]
        """
        self._ids = ids

    @property
    def dw_type(self):
        r"""Gets the dw_type of this WorkspaceTransformVO.

        数据连接类型，对应表所在的数仓类型，取值可以为DLI、DWS、MRS_HIVE、POSTGRESQL、MRS_SPARK、CLICKHOUSE、MYSQL、ORACLE和DORIS等。

        :return: The dw_type of this WorkspaceTransformVO.
        :rtype: str
        """
        return self._dw_type

    @dw_type.setter
    def dw_type(self, dw_type):
        r"""Sets the dw_type of this WorkspaceTransformVO.

        数据连接类型，对应表所在的数仓类型，取值可以为DLI、DWS、MRS_HIVE、POSTGRESQL、MRS_SPARK、CLICKHOUSE、MYSQL、ORACLE和DORIS等。

        :param dw_type: The dw_type of this WorkspaceTransformVO.
        :type dw_type: str
        """
        self._dw_type = dw_type

    @property
    def connection_id(self):
        r"""Gets the connection_id of this WorkspaceTransformVO.

        转化后物理表所属的数据连接ID。

        :return: The connection_id of this WorkspaceTransformVO.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        r"""Sets the connection_id of this WorkspaceTransformVO.

        转化后物理表所属的数据连接ID。

        :param connection_id: The connection_id of this WorkspaceTransformVO.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def database(self):
        r"""Gets the database of this WorkspaceTransformVO.

        转化后物理表所属的数据库。

        :return: The database of this WorkspaceTransformVO.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this WorkspaceTransformVO.

        转化后物理表所属的数据库。

        :param database: The database of this WorkspaceTransformVO.
        :type database: str
        """
        self._database = database

    @property
    def queue(self):
        r"""Gets the queue of this WorkspaceTransformVO.

        转化后物理表所属的队列（仅DLI）。

        :return: The queue of this WorkspaceTransformVO.
        :rtype: str
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        r"""Sets the queue of this WorkspaceTransformVO.

        转化后物理表所属的队列（仅DLI）。

        :param queue: The queue of this WorkspaceTransformVO.
        :type queue: str
        """
        self._queue = queue

    @property
    def schema(self):
        r"""Gets the schema of this WorkspaceTransformVO.

        转化后物理表所属的schema（仅DWS和PostgreSQL）。

        :return: The schema of this WorkspaceTransformVO.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this WorkspaceTransformVO.

        转化后物理表所属的schema（仅DWS和PostgreSQL）。

        :param schema: The schema of this WorkspaceTransformVO.
        :type schema: str
        """
        self._schema = schema

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
        if not isinstance(other, WorkspaceTransformVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
