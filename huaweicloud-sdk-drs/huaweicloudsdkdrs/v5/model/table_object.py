# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TableObject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sync_type': 'str',
        'type': 'str',
        'name': 'str',
        'all': 'bool',
        'db_alias_name': 'str',
        'schema_alias_name': 'str',
        'filtered': 'bool',
        'filter_conditions': 'list[str]',
        'config_conditions': 'list[str]',
        'has_been_sent': 'bool',
        'columns': 'dict(str, ColumnObject)'
    }

    attribute_map = {
        'sync_type': 'sync_type',
        'type': 'type',
        'name': 'name',
        'all': 'all',
        'db_alias_name': 'db_alias_name',
        'schema_alias_name': 'schema_alias_name',
        'filtered': 'filtered',
        'filter_conditions': 'filter_conditions',
        'config_conditions': 'config_conditions',
        'has_been_sent': 'has_been_sent',
        'columns': 'columns'
    }

    def __init__(self, sync_type=None, type=None, name=None, all=None, db_alias_name=None, schema_alias_name=None, filtered=None, filter_conditions=None, config_conditions=None, has_been_sent=None, columns=None):
        """TableObject

        The model defined in huaweicloud sdk

        :param sync_type: 该表在实时同步场景下的类型。取值： - config：仅当该表作为数据过滤高级设置的关联表时，需要填写，此时该表以及该表下的columns“不会”被同步到目标库，name、all、filtered、filter_conditions属性不生效，columns需要填写被关联的相关对象，config_conditions需要填写数据过滤高级设置的配置条件。（注意：如果需要同步该表级对象，则在下级对象中填写sync_type值为config。）
        :type sync_type: str
        :param type: 对象类型。取值： - table：表。 - view：视图。 - procedure：存储过程。
        :type type: str
        :param name: 该表在目标库的名称（表名映射）。
        :type name: str
        :param all: 是否整表迁移或同步。注意： 1.当该表不需要做列过滤、列映射时，填true，如果需要做列过滤、列映射则填false； 2.当该表需要做附加列时，需要填true，并且在columns里填写附加列信息； 3.当该表所包含的列作为数据过滤高级设置的关联列时，需要填true，并且在columns里填写关联列信息、config_conditions填写数据过滤高级设置的配置条件；
        :type all: bool
        :param db_alias_name: 一对多情况下，表级上对库名的映射。
        :type db_alias_name: str
        :param schema_alias_name: 一对多情况下，表级上对schema名的映射。
        :type schema_alias_name: str
        :param filtered: 该表是否进行数据过滤。
        :type filtered: bool
        :param filter_conditions: 该表数据的过滤条件，生成加工规则值为SQL条件语句，长度限制512。
        :type filter_conditions: list[str]
        :param config_conditions: 该表数据过滤高级设置的配置条件，当该表作为联表查询时填写，生成加工规则值为SQL条件语句，长度限制512。
        :type config_conditions: list[str]
        :param has_been_sent: 是否已经进行同步。
        :type has_been_sent: bool
        :param columns: 需要同步/映射/过滤/新增的列，当需要列过滤、列映射、附加列功能时填写，仅在实时同步任务中生效，当整表同步为false时需要填写。
        :type columns: dict(str, ColumnObject)
        """
        
        

        self._sync_type = None
        self._type = None
        self._name = None
        self._all = None
        self._db_alias_name = None
        self._schema_alias_name = None
        self._filtered = None
        self._filter_conditions = None
        self._config_conditions = None
        self._has_been_sent = None
        self._columns = None
        self.discriminator = None

        if sync_type is not None:
            self.sync_type = sync_type
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if all is not None:
            self.all = all
        if db_alias_name is not None:
            self.db_alias_name = db_alias_name
        if schema_alias_name is not None:
            self.schema_alias_name = schema_alias_name
        if filtered is not None:
            self.filtered = filtered
        if filter_conditions is not None:
            self.filter_conditions = filter_conditions
        if config_conditions is not None:
            self.config_conditions = config_conditions
        if has_been_sent is not None:
            self.has_been_sent = has_been_sent
        if columns is not None:
            self.columns = columns

    @property
    def sync_type(self):
        """Gets the sync_type of this TableObject.

        该表在实时同步场景下的类型。取值： - config：仅当该表作为数据过滤高级设置的关联表时，需要填写，此时该表以及该表下的columns“不会”被同步到目标库，name、all、filtered、filter_conditions属性不生效，columns需要填写被关联的相关对象，config_conditions需要填写数据过滤高级设置的配置条件。（注意：如果需要同步该表级对象，则在下级对象中填写sync_type值为config。）

        :return: The sync_type of this TableObject.
        :rtype: str
        """
        return self._sync_type

    @sync_type.setter
    def sync_type(self, sync_type):
        """Sets the sync_type of this TableObject.

        该表在实时同步场景下的类型。取值： - config：仅当该表作为数据过滤高级设置的关联表时，需要填写，此时该表以及该表下的columns“不会”被同步到目标库，name、all、filtered、filter_conditions属性不生效，columns需要填写被关联的相关对象，config_conditions需要填写数据过滤高级设置的配置条件。（注意：如果需要同步该表级对象，则在下级对象中填写sync_type值为config。）

        :param sync_type: The sync_type of this TableObject.
        :type sync_type: str
        """
        self._sync_type = sync_type

    @property
    def type(self):
        """Gets the type of this TableObject.

        对象类型。取值： - table：表。 - view：视图。 - procedure：存储过程。

        :return: The type of this TableObject.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TableObject.

        对象类型。取值： - table：表。 - view：视图。 - procedure：存储过程。

        :param type: The type of this TableObject.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        """Gets the name of this TableObject.

        该表在目标库的名称（表名映射）。

        :return: The name of this TableObject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TableObject.

        该表在目标库的名称（表名映射）。

        :param name: The name of this TableObject.
        :type name: str
        """
        self._name = name

    @property
    def all(self):
        """Gets the all of this TableObject.

        是否整表迁移或同步。注意： 1.当该表不需要做列过滤、列映射时，填true，如果需要做列过滤、列映射则填false； 2.当该表需要做附加列时，需要填true，并且在columns里填写附加列信息； 3.当该表所包含的列作为数据过滤高级设置的关联列时，需要填true，并且在columns里填写关联列信息、config_conditions填写数据过滤高级设置的配置条件；

        :return: The all of this TableObject.
        :rtype: bool
        """
        return self._all

    @all.setter
    def all(self, all):
        """Sets the all of this TableObject.

        是否整表迁移或同步。注意： 1.当该表不需要做列过滤、列映射时，填true，如果需要做列过滤、列映射则填false； 2.当该表需要做附加列时，需要填true，并且在columns里填写附加列信息； 3.当该表所包含的列作为数据过滤高级设置的关联列时，需要填true，并且在columns里填写关联列信息、config_conditions填写数据过滤高级设置的配置条件；

        :param all: The all of this TableObject.
        :type all: bool
        """
        self._all = all

    @property
    def db_alias_name(self):
        """Gets the db_alias_name of this TableObject.

        一对多情况下，表级上对库名的映射。

        :return: The db_alias_name of this TableObject.
        :rtype: str
        """
        return self._db_alias_name

    @db_alias_name.setter
    def db_alias_name(self, db_alias_name):
        """Sets the db_alias_name of this TableObject.

        一对多情况下，表级上对库名的映射。

        :param db_alias_name: The db_alias_name of this TableObject.
        :type db_alias_name: str
        """
        self._db_alias_name = db_alias_name

    @property
    def schema_alias_name(self):
        """Gets the schema_alias_name of this TableObject.

        一对多情况下，表级上对schema名的映射。

        :return: The schema_alias_name of this TableObject.
        :rtype: str
        """
        return self._schema_alias_name

    @schema_alias_name.setter
    def schema_alias_name(self, schema_alias_name):
        """Sets the schema_alias_name of this TableObject.

        一对多情况下，表级上对schema名的映射。

        :param schema_alias_name: The schema_alias_name of this TableObject.
        :type schema_alias_name: str
        """
        self._schema_alias_name = schema_alias_name

    @property
    def filtered(self):
        """Gets the filtered of this TableObject.

        该表是否进行数据过滤。

        :return: The filtered of this TableObject.
        :rtype: bool
        """
        return self._filtered

    @filtered.setter
    def filtered(self, filtered):
        """Sets the filtered of this TableObject.

        该表是否进行数据过滤。

        :param filtered: The filtered of this TableObject.
        :type filtered: bool
        """
        self._filtered = filtered

    @property
    def filter_conditions(self):
        """Gets the filter_conditions of this TableObject.

        该表数据的过滤条件，生成加工规则值为SQL条件语句，长度限制512。

        :return: The filter_conditions of this TableObject.
        :rtype: list[str]
        """
        return self._filter_conditions

    @filter_conditions.setter
    def filter_conditions(self, filter_conditions):
        """Sets the filter_conditions of this TableObject.

        该表数据的过滤条件，生成加工规则值为SQL条件语句，长度限制512。

        :param filter_conditions: The filter_conditions of this TableObject.
        :type filter_conditions: list[str]
        """
        self._filter_conditions = filter_conditions

    @property
    def config_conditions(self):
        """Gets the config_conditions of this TableObject.

        该表数据过滤高级设置的配置条件，当该表作为联表查询时填写，生成加工规则值为SQL条件语句，长度限制512。

        :return: The config_conditions of this TableObject.
        :rtype: list[str]
        """
        return self._config_conditions

    @config_conditions.setter
    def config_conditions(self, config_conditions):
        """Sets the config_conditions of this TableObject.

        该表数据过滤高级设置的配置条件，当该表作为联表查询时填写，生成加工规则值为SQL条件语句，长度限制512。

        :param config_conditions: The config_conditions of this TableObject.
        :type config_conditions: list[str]
        """
        self._config_conditions = config_conditions

    @property
    def has_been_sent(self):
        """Gets the has_been_sent of this TableObject.

        是否已经进行同步。

        :return: The has_been_sent of this TableObject.
        :rtype: bool
        """
        return self._has_been_sent

    @has_been_sent.setter
    def has_been_sent(self, has_been_sent):
        """Sets the has_been_sent of this TableObject.

        是否已经进行同步。

        :param has_been_sent: The has_been_sent of this TableObject.
        :type has_been_sent: bool
        """
        self._has_been_sent = has_been_sent

    @property
    def columns(self):
        """Gets the columns of this TableObject.

        需要同步/映射/过滤/新增的列，当需要列过滤、列映射、附加列功能时填写，仅在实时同步任务中生效，当整表同步为false时需要填写。

        :return: The columns of this TableObject.
        :rtype: dict(str, ColumnObject)
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this TableObject.

        需要同步/映射/过滤/新增的列，当需要列过滤、列映射、附加列功能时填写，仅在实时同步任务中生效，当整表同步为false时需要填写。

        :param columns: The columns of this TableObject.
        :type columns: dict(str, ColumnObject)
        """
        self._columns = columns

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
        if not isinstance(other, TableObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
