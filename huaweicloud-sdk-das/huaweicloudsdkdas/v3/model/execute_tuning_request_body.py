# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteTuningRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database_name': 'str',
        'schema_name': 'str',
        'sql_script': 'str',
        'node_type': 'str',
        'node_id': 'str',
        'use_default_search_path': 'bool'
    }

    attribute_map = {
        'database_name': 'database_name',
        'schema_name': 'schema_name',
        'sql_script': 'sql_script',
        'node_type': 'node_type',
        'node_id': 'node_id',
        'use_default_search_path': 'use_default_search_path'
    }

    def __init__(self, database_name=None, schema_name=None, sql_script=None, node_type=None, node_id=None, use_default_search_path=None):
        r"""ExecuteTuningRequestBody

        The model defined in huaweicloud sdk

        :param database_name: 数据库名称
        :type database_name: str
        :param schema_name: schema名称，诊断实例类型为postgresql时可用
        :type schema_name: str
        :param sql_script: 诊断的SQL语句
        :type sql_script: str
        :param node_type: 执行节点类型，取值范围：master（主节点）、slave（副节点）、readreplica（只读节点）
        :type node_type: str
        :param node_id: 执行节点ID，实例节点的唯一标识
        :type node_id: str
        :param use_default_search_path: 是否使用search_path作为环境变量，诊断实例类型为postgresql时可用
        :type use_default_search_path: bool
        """
        
        

        self._database_name = None
        self._schema_name = None
        self._sql_script = None
        self._node_type = None
        self._node_id = None
        self._use_default_search_path = None
        self.discriminator = None

        self.database_name = database_name
        if schema_name is not None:
            self.schema_name = schema_name
        self.sql_script = sql_script
        if node_type is not None:
            self.node_type = node_type
        if node_id is not None:
            self.node_id = node_id
        if use_default_search_path is not None:
            self.use_default_search_path = use_default_search_path

    @property
    def database_name(self):
        r"""Gets the database_name of this ExecuteTuningRequestBody.

        数据库名称

        :return: The database_name of this ExecuteTuningRequestBody.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ExecuteTuningRequestBody.

        数据库名称

        :param database_name: The database_name of this ExecuteTuningRequestBody.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def schema_name(self):
        r"""Gets the schema_name of this ExecuteTuningRequestBody.

        schema名称，诊断实例类型为postgresql时可用

        :return: The schema_name of this ExecuteTuningRequestBody.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this ExecuteTuningRequestBody.

        schema名称，诊断实例类型为postgresql时可用

        :param schema_name: The schema_name of this ExecuteTuningRequestBody.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def sql_script(self):
        r"""Gets the sql_script of this ExecuteTuningRequestBody.

        诊断的SQL语句

        :return: The sql_script of this ExecuteTuningRequestBody.
        :rtype: str
        """
        return self._sql_script

    @sql_script.setter
    def sql_script(self, sql_script):
        r"""Sets the sql_script of this ExecuteTuningRequestBody.

        诊断的SQL语句

        :param sql_script: The sql_script of this ExecuteTuningRequestBody.
        :type sql_script: str
        """
        self._sql_script = sql_script

    @property
    def node_type(self):
        r"""Gets the node_type of this ExecuteTuningRequestBody.

        执行节点类型，取值范围：master（主节点）、slave（副节点）、readreplica（只读节点）

        :return: The node_type of this ExecuteTuningRequestBody.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        r"""Sets the node_type of this ExecuteTuningRequestBody.

        执行节点类型，取值范围：master（主节点）、slave（副节点）、readreplica（只读节点）

        :param node_type: The node_type of this ExecuteTuningRequestBody.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def node_id(self):
        r"""Gets the node_id of this ExecuteTuningRequestBody.

        执行节点ID，实例节点的唯一标识

        :return: The node_id of this ExecuteTuningRequestBody.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ExecuteTuningRequestBody.

        执行节点ID，实例节点的唯一标识

        :param node_id: The node_id of this ExecuteTuningRequestBody.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def use_default_search_path(self):
        r"""Gets the use_default_search_path of this ExecuteTuningRequestBody.

        是否使用search_path作为环境变量，诊断实例类型为postgresql时可用

        :return: The use_default_search_path of this ExecuteTuningRequestBody.
        :rtype: bool
        """
        return self._use_default_search_path

    @use_default_search_path.setter
    def use_default_search_path(self, use_default_search_path):
        r"""Sets the use_default_search_path of this ExecuteTuningRequestBody.

        是否使用search_path作为环境变量，诊断实例类型为postgresql时可用

        :param use_default_search_path: The use_default_search_path of this ExecuteTuningRequestBody.
        :type use_default_search_path: bool
        """
        self._use_default_search_path = use_default_search_path

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
        if not isinstance(other, ExecuteTuningRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
