# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SensitiveDataDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'cluster_name': 'str',
        'database_name': 'str',
        'schema_name': 'str',
        'table_name': 'str',
        'column_name': 'str',
        'rule_id': 'str',
        'active_flag': 'int',
        'classification_id': 'str',
        'category_id': 'str',
        'sync_time': 'int',
        'find_time': 'int',
        'task_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'cluster_name': 'cluster_name',
        'database_name': 'database_name',
        'schema_name': 'schema_name',
        'table_name': 'table_name',
        'column_name': 'column_name',
        'rule_id': 'rule_id',
        'active_flag': 'active_flag',
        'classification_id': 'classification_id',
        'category_id': 'category_id',
        'sync_time': 'sync_time',
        'find_time': 'find_time',
        'task_id': 'task_id'
    }

    def __init__(self, id=None, cluster_name=None, database_name=None, schema_name=None, table_name=None, column_name=None, rule_id=None, active_flag=None, classification_id=None, category_id=None, sync_time=None, find_time=None, task_id=None):
        r"""SensitiveDataDTO

        The model defined in huaweicloud sdk

        :param id: 唯一标识，自动生成的ID。
        :type id: int
        :param cluster_name: 集群名称。
        :type cluster_name: str
        :param database_name: 数据库名。
        :type database_name: str
        :param schema_name: 模式名。
        :type schema_name: str
        :param table_name: 表名称。
        :type table_name: str
        :param column_name: 字段名称。
        :type column_name: str
        :param rule_id: 规则id。
        :type rule_id: str
        :param active_flag: 是否有效。1:有效 2:无效 3:待确认。
        :type active_flag: int
        :param classification_id: 数据密级id。
        :type classification_id: str
        :param category_id: 分类ID。
        :type category_id: str
        :param sync_time: 同步时间。
        :type sync_time: int
        :param find_time: 最后发现时间。
        :type find_time: int
        :param task_id: 任务id。
        :type task_id: str
        """
        
        

        self._id = None
        self._cluster_name = None
        self._database_name = None
        self._schema_name = None
        self._table_name = None
        self._column_name = None
        self._rule_id = None
        self._active_flag = None
        self._classification_id = None
        self._category_id = None
        self._sync_time = None
        self._find_time = None
        self._task_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if database_name is not None:
            self.database_name = database_name
        if schema_name is not None:
            self.schema_name = schema_name
        if table_name is not None:
            self.table_name = table_name
        if column_name is not None:
            self.column_name = column_name
        if rule_id is not None:
            self.rule_id = rule_id
        if active_flag is not None:
            self.active_flag = active_flag
        if classification_id is not None:
            self.classification_id = classification_id
        if category_id is not None:
            self.category_id = category_id
        if sync_time is not None:
            self.sync_time = sync_time
        if find_time is not None:
            self.find_time = find_time
        if task_id is not None:
            self.task_id = task_id

    @property
    def id(self):
        r"""Gets the id of this SensitiveDataDTO.

        唯一标识，自动生成的ID。

        :return: The id of this SensitiveDataDTO.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SensitiveDataDTO.

        唯一标识，自动生成的ID。

        :param id: The id of this SensitiveDataDTO.
        :type id: int
        """
        self._id = id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this SensitiveDataDTO.

        集群名称。

        :return: The cluster_name of this SensitiveDataDTO.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this SensitiveDataDTO.

        集群名称。

        :param cluster_name: The cluster_name of this SensitiveDataDTO.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def database_name(self):
        r"""Gets the database_name of this SensitiveDataDTO.

        数据库名。

        :return: The database_name of this SensitiveDataDTO.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this SensitiveDataDTO.

        数据库名。

        :param database_name: The database_name of this SensitiveDataDTO.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def schema_name(self):
        r"""Gets the schema_name of this SensitiveDataDTO.

        模式名。

        :return: The schema_name of this SensitiveDataDTO.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this SensitiveDataDTO.

        模式名。

        :param schema_name: The schema_name of this SensitiveDataDTO.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def table_name(self):
        r"""Gets the table_name of this SensitiveDataDTO.

        表名称。

        :return: The table_name of this SensitiveDataDTO.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this SensitiveDataDTO.

        表名称。

        :param table_name: The table_name of this SensitiveDataDTO.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def column_name(self):
        r"""Gets the column_name of this SensitiveDataDTO.

        字段名称。

        :return: The column_name of this SensitiveDataDTO.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        r"""Sets the column_name of this SensitiveDataDTO.

        字段名称。

        :param column_name: The column_name of this SensitiveDataDTO.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def rule_id(self):
        r"""Gets the rule_id of this SensitiveDataDTO.

        规则id。

        :return: The rule_id of this SensitiveDataDTO.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this SensitiveDataDTO.

        规则id。

        :param rule_id: The rule_id of this SensitiveDataDTO.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def active_flag(self):
        r"""Gets the active_flag of this SensitiveDataDTO.

        是否有效。1:有效 2:无效 3:待确认。

        :return: The active_flag of this SensitiveDataDTO.
        :rtype: int
        """
        return self._active_flag

    @active_flag.setter
    def active_flag(self, active_flag):
        r"""Sets the active_flag of this SensitiveDataDTO.

        是否有效。1:有效 2:无效 3:待确认。

        :param active_flag: The active_flag of this SensitiveDataDTO.
        :type active_flag: int
        """
        self._active_flag = active_flag

    @property
    def classification_id(self):
        r"""Gets the classification_id of this SensitiveDataDTO.

        数据密级id。

        :return: The classification_id of this SensitiveDataDTO.
        :rtype: str
        """
        return self._classification_id

    @classification_id.setter
    def classification_id(self, classification_id):
        r"""Sets the classification_id of this SensitiveDataDTO.

        数据密级id。

        :param classification_id: The classification_id of this SensitiveDataDTO.
        :type classification_id: str
        """
        self._classification_id = classification_id

    @property
    def category_id(self):
        r"""Gets the category_id of this SensitiveDataDTO.

        分类ID。

        :return: The category_id of this SensitiveDataDTO.
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        r"""Sets the category_id of this SensitiveDataDTO.

        分类ID。

        :param category_id: The category_id of this SensitiveDataDTO.
        :type category_id: str
        """
        self._category_id = category_id

    @property
    def sync_time(self):
        r"""Gets the sync_time of this SensitiveDataDTO.

        同步时间。

        :return: The sync_time of this SensitiveDataDTO.
        :rtype: int
        """
        return self._sync_time

    @sync_time.setter
    def sync_time(self, sync_time):
        r"""Sets the sync_time of this SensitiveDataDTO.

        同步时间。

        :param sync_time: The sync_time of this SensitiveDataDTO.
        :type sync_time: int
        """
        self._sync_time = sync_time

    @property
    def find_time(self):
        r"""Gets the find_time of this SensitiveDataDTO.

        最后发现时间。

        :return: The find_time of this SensitiveDataDTO.
        :rtype: int
        """
        return self._find_time

    @find_time.setter
    def find_time(self, find_time):
        r"""Sets the find_time of this SensitiveDataDTO.

        最后发现时间。

        :param find_time: The find_time of this SensitiveDataDTO.
        :type find_time: int
        """
        self._find_time = find_time

    @property
    def task_id(self):
        r"""Gets the task_id of this SensitiveDataDTO.

        任务id。

        :return: The task_id of this SensitiveDataDTO.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this SensitiveDataDTO.

        任务id。

        :param task_id: The task_id of this SensitiveDataDTO.
        :type task_id: str
        """
        self._task_id = task_id

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
        if not isinstance(other, SensitiveDataDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
