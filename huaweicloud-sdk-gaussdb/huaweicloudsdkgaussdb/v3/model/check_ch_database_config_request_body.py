# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckChDatabaseConfigRequestBody:

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
        'db_configs': 'list[ChDatabaseConfigsInfo]',
        'table_repl_config': 'ChDatabaseTableReplConfigInfo'
    }

    attribute_map = {
        'source_instance_id': 'source_instance_id',
        'source_node_id': 'source_node_id',
        'source_database_name': 'source_database_name',
        'db_configs': 'db_configs',
        'table_repl_config': 'table_repl_config'
    }

    def __init__(self, source_instance_id=None, source_node_id=None, source_database_name=None, db_configs=None, table_repl_config=None):
        r"""CheckChDatabaseConfigRequestBody

        The model defined in huaweicloud sdk

        :param source_instance_id: 源实例ID，严格匹配UUID规则。
        :type source_instance_id: str
        :param source_node_id: 源节点ID。TaurusDB只读节点ID。如为空，则取TaurusDB主节点ID。
        :type source_node_id: str
        :param source_database_name: 源数据库名。
        :type source_database_name: str
        :param db_configs: 库配置列表。
        :type db_configs: list[:class:`huaweicloudsdkgaussdb.v3.ChDatabaseConfigsInfo`]
        :param table_repl_config: 
        :type table_repl_config: :class:`huaweicloudsdkgaussdb.v3.ChDatabaseTableReplConfigInfo`
        """
        
        

        self._source_instance_id = None
        self._source_node_id = None
        self._source_database_name = None
        self._db_configs = None
        self._table_repl_config = None
        self.discriminator = None

        self.source_instance_id = source_instance_id
        if source_node_id is not None:
            self.source_node_id = source_node_id
        self.source_database_name = source_database_name
        self.db_configs = db_configs
        self.table_repl_config = table_repl_config

    @property
    def source_instance_id(self):
        r"""Gets the source_instance_id of this CheckChDatabaseConfigRequestBody.

        源实例ID，严格匹配UUID规则。

        :return: The source_instance_id of this CheckChDatabaseConfigRequestBody.
        :rtype: str
        """
        return self._source_instance_id

    @source_instance_id.setter
    def source_instance_id(self, source_instance_id):
        r"""Sets the source_instance_id of this CheckChDatabaseConfigRequestBody.

        源实例ID，严格匹配UUID规则。

        :param source_instance_id: The source_instance_id of this CheckChDatabaseConfigRequestBody.
        :type source_instance_id: str
        """
        self._source_instance_id = source_instance_id

    @property
    def source_node_id(self):
        r"""Gets the source_node_id of this CheckChDatabaseConfigRequestBody.

        源节点ID。TaurusDB只读节点ID。如为空，则取TaurusDB主节点ID。

        :return: The source_node_id of this CheckChDatabaseConfigRequestBody.
        :rtype: str
        """
        return self._source_node_id

    @source_node_id.setter
    def source_node_id(self, source_node_id):
        r"""Sets the source_node_id of this CheckChDatabaseConfigRequestBody.

        源节点ID。TaurusDB只读节点ID。如为空，则取TaurusDB主节点ID。

        :param source_node_id: The source_node_id of this CheckChDatabaseConfigRequestBody.
        :type source_node_id: str
        """
        self._source_node_id = source_node_id

    @property
    def source_database_name(self):
        r"""Gets the source_database_name of this CheckChDatabaseConfigRequestBody.

        源数据库名。

        :return: The source_database_name of this CheckChDatabaseConfigRequestBody.
        :rtype: str
        """
        return self._source_database_name

    @source_database_name.setter
    def source_database_name(self, source_database_name):
        r"""Sets the source_database_name of this CheckChDatabaseConfigRequestBody.

        源数据库名。

        :param source_database_name: The source_database_name of this CheckChDatabaseConfigRequestBody.
        :type source_database_name: str
        """
        self._source_database_name = source_database_name

    @property
    def db_configs(self):
        r"""Gets the db_configs of this CheckChDatabaseConfigRequestBody.

        库配置列表。

        :return: The db_configs of this CheckChDatabaseConfigRequestBody.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.ChDatabaseConfigsInfo`]
        """
        return self._db_configs

    @db_configs.setter
    def db_configs(self, db_configs):
        r"""Sets the db_configs of this CheckChDatabaseConfigRequestBody.

        库配置列表。

        :param db_configs: The db_configs of this CheckChDatabaseConfigRequestBody.
        :type db_configs: list[:class:`huaweicloudsdkgaussdb.v3.ChDatabaseConfigsInfo`]
        """
        self._db_configs = db_configs

    @property
    def table_repl_config(self):
        r"""Gets the table_repl_config of this CheckChDatabaseConfigRequestBody.

        :return: The table_repl_config of this CheckChDatabaseConfigRequestBody.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ChDatabaseTableReplConfigInfo`
        """
        return self._table_repl_config

    @table_repl_config.setter
    def table_repl_config(self, table_repl_config):
        r"""Sets the table_repl_config of this CheckChDatabaseConfigRequestBody.

        :param table_repl_config: The table_repl_config of this CheckChDatabaseConfigRequestBody.
        :type table_repl_config: :class:`huaweicloudsdkgaussdb.v3.ChDatabaseTableReplConfigInfo`
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
        if not isinstance(other, CheckChDatabaseConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
