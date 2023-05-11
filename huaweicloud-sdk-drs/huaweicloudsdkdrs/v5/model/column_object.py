# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ColumnObject:

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
        'primary_key_for_data_filtering': 'str',
        'index_for_data_filtering': 'str',
        'name': 'str',
        'type': 'str',
        'primary_key_for_column_filtering': 'str',
        'filtered': 'bool',
        'additional': 'bool',
        'operation_type': 'str',
        'value': 'str'
    }

    attribute_map = {
        'sync_type': 'sync_type',
        'primary_key_for_data_filtering': 'primary_key_for_data_filtering',
        'index_for_data_filtering': 'index_for_data_filtering',
        'name': 'name',
        'type': 'type',
        'primary_key_for_column_filtering': 'primary_key_for_column_filtering',
        'filtered': 'filtered',
        'additional': 'additional',
        'operation_type': 'operation_type',
        'value': 'value'
    }

    def __init__(self, sync_type=None, primary_key_for_data_filtering=None, index_for_data_filtering=None, name=None, type=None, primary_key_for_column_filtering=None, filtered=None, additional=None, operation_type=None, value=None):
        """ColumnObject

        The model defined in huaweicloud sdk

        :param sync_type: 该列在实时同步场景下的类型。取值： - config：当该列作为数据过滤高级设置的关联列时，需要填写，同时如果该列是主建或优化查询所需的索引，则需要填写primary_key_for_data_filtering或index_for_data_filtering。（注意：是否同步该列到目标库由“filtered”属性控制，与库级、模式级、表级控制方式不同。）
        :type sync_type: str
        :param primary_key_for_data_filtering: 该列是否在数据过滤高级设置场景下为主键，如果是主建则填该列列名，否则不填。
        :type primary_key_for_data_filtering: str
        :param index_for_data_filtering: 优化查询所需的索引，将会为缓存数据增加索引，不会影响源表，当该列作为数据过滤高级设置的关联索引时，需要填写，否则不填。
        :type index_for_data_filtering: str
        :param name: 该列在目标库的名称（列名映射），当该列为“附加列”时须与数据库表级对象中列名保持一致。
        :type name: str
        :param type: 该列字段的数据类型。 列过滤：填写源列字段的数据类型。 附加列：新填充的列指定字段的数据类型，根据不同操作类型来决定取值范围与约束。取值： - 以默认值方式，支持：int,long,varchar(256),datetime,timestamp。 - 以create_time为列，支持：long,datetime,timestamp。 - 以update_time为列，支持：long,datetime,timestamp。 - 以表达式为列，支持：varchar(256)，且列值仅为：concat(__current_database, &#39;@&#39;, __current_table) - 以serverName@database@table为列，支持：varchar(256)。
        :type type: str
        :param primary_key_for_column_filtering: 该列是否在列映射场景下为主键，如果是主建则填PRI，否则填空。
        :type primary_key_for_column_filtering: str
        :param filtered: 该列是否进列过滤，不能与附加列additional同时使用。取值： - true：表示同步该列。 - false：表示过滤该列不同步。
        :type filtered: bool
        :param additional: 该列是否为附加列，当该列为附加列时：name必须与表级对象中列名一致，并且不能与列过滤filtered同时使用。
        :type additional: bool
        :param operation_type: 操作类型，以特定的操作类型填充新加的列。取值： - 以默认值方式：\&quot;operation_type\&quot;:\&quot;ADDITIONALCOLUMN,default_value\&quot; - 以create_time为列：\&quot;operation_type\&quot;:\&quot;ADDITIONALCOLUMN,create_time\&quot; - 以update_time为列：\&quot;operation_type\&quot;:\&quot;ADDITIONALCOLUMN,update_time\&quot; - 以表达式为列：\&quot;operation_type\&quot;:\&quot;ADDITIONALCOLUMN,expression\&quot; - 以serverName@database@table为列：\&quot;operation_type\&quot;:\&quot;ADDITIONALCOLUMN,server_database_table\&quot;
        :type operation_type: str
        :param value: 附加列的值。约束： - 当操作类型仅“以默认值方式”，“以serverName@database@table为列”时，才支持输入对应字段类型的值。 - 当操作类型为“以表达式为列”时，该字段为固定值\&quot;concat(__current_database, &#39;@&#39;, __current_table)\&quot;，不需要填写。
        :type value: str
        """
        
        

        self._sync_type = None
        self._primary_key_for_data_filtering = None
        self._index_for_data_filtering = None
        self._name = None
        self._type = None
        self._primary_key_for_column_filtering = None
        self._filtered = None
        self._additional = None
        self._operation_type = None
        self._value = None
        self.discriminator = None

        if sync_type is not None:
            self.sync_type = sync_type
        if primary_key_for_data_filtering is not None:
            self.primary_key_for_data_filtering = primary_key_for_data_filtering
        if index_for_data_filtering is not None:
            self.index_for_data_filtering = index_for_data_filtering
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if primary_key_for_column_filtering is not None:
            self.primary_key_for_column_filtering = primary_key_for_column_filtering
        if filtered is not None:
            self.filtered = filtered
        if additional is not None:
            self.additional = additional
        if operation_type is not None:
            self.operation_type = operation_type
        if value is not None:
            self.value = value

    @property
    def sync_type(self):
        """Gets the sync_type of this ColumnObject.

        该列在实时同步场景下的类型。取值： - config：当该列作为数据过滤高级设置的关联列时，需要填写，同时如果该列是主建或优化查询所需的索引，则需要填写primary_key_for_data_filtering或index_for_data_filtering。（注意：是否同步该列到目标库由“filtered”属性控制，与库级、模式级、表级控制方式不同。）

        :return: The sync_type of this ColumnObject.
        :rtype: str
        """
        return self._sync_type

    @sync_type.setter
    def sync_type(self, sync_type):
        """Sets the sync_type of this ColumnObject.

        该列在实时同步场景下的类型。取值： - config：当该列作为数据过滤高级设置的关联列时，需要填写，同时如果该列是主建或优化查询所需的索引，则需要填写primary_key_for_data_filtering或index_for_data_filtering。（注意：是否同步该列到目标库由“filtered”属性控制，与库级、模式级、表级控制方式不同。）

        :param sync_type: The sync_type of this ColumnObject.
        :type sync_type: str
        """
        self._sync_type = sync_type

    @property
    def primary_key_for_data_filtering(self):
        """Gets the primary_key_for_data_filtering of this ColumnObject.

        该列是否在数据过滤高级设置场景下为主键，如果是主建则填该列列名，否则不填。

        :return: The primary_key_for_data_filtering of this ColumnObject.
        :rtype: str
        """
        return self._primary_key_for_data_filtering

    @primary_key_for_data_filtering.setter
    def primary_key_for_data_filtering(self, primary_key_for_data_filtering):
        """Sets the primary_key_for_data_filtering of this ColumnObject.

        该列是否在数据过滤高级设置场景下为主键，如果是主建则填该列列名，否则不填。

        :param primary_key_for_data_filtering: The primary_key_for_data_filtering of this ColumnObject.
        :type primary_key_for_data_filtering: str
        """
        self._primary_key_for_data_filtering = primary_key_for_data_filtering

    @property
    def index_for_data_filtering(self):
        """Gets the index_for_data_filtering of this ColumnObject.

        优化查询所需的索引，将会为缓存数据增加索引，不会影响源表，当该列作为数据过滤高级设置的关联索引时，需要填写，否则不填。

        :return: The index_for_data_filtering of this ColumnObject.
        :rtype: str
        """
        return self._index_for_data_filtering

    @index_for_data_filtering.setter
    def index_for_data_filtering(self, index_for_data_filtering):
        """Sets the index_for_data_filtering of this ColumnObject.

        优化查询所需的索引，将会为缓存数据增加索引，不会影响源表，当该列作为数据过滤高级设置的关联索引时，需要填写，否则不填。

        :param index_for_data_filtering: The index_for_data_filtering of this ColumnObject.
        :type index_for_data_filtering: str
        """
        self._index_for_data_filtering = index_for_data_filtering

    @property
    def name(self):
        """Gets the name of this ColumnObject.

        该列在目标库的名称（列名映射），当该列为“附加列”时须与数据库表级对象中列名保持一致。

        :return: The name of this ColumnObject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ColumnObject.

        该列在目标库的名称（列名映射），当该列为“附加列”时须与数据库表级对象中列名保持一致。

        :param name: The name of this ColumnObject.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this ColumnObject.

        该列字段的数据类型。 列过滤：填写源列字段的数据类型。 附加列：新填充的列指定字段的数据类型，根据不同操作类型来决定取值范围与约束。取值： - 以默认值方式，支持：int,long,varchar(256),datetime,timestamp。 - 以create_time为列，支持：long,datetime,timestamp。 - 以update_time为列，支持：long,datetime,timestamp。 - 以表达式为列，支持：varchar(256)，且列值仅为：concat(__current_database, '@', __current_table) - 以serverName@database@table为列，支持：varchar(256)。

        :return: The type of this ColumnObject.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ColumnObject.

        该列字段的数据类型。 列过滤：填写源列字段的数据类型。 附加列：新填充的列指定字段的数据类型，根据不同操作类型来决定取值范围与约束。取值： - 以默认值方式，支持：int,long,varchar(256),datetime,timestamp。 - 以create_time为列，支持：long,datetime,timestamp。 - 以update_time为列，支持：long,datetime,timestamp。 - 以表达式为列，支持：varchar(256)，且列值仅为：concat(__current_database, '@', __current_table) - 以serverName@database@table为列，支持：varchar(256)。

        :param type: The type of this ColumnObject.
        :type type: str
        """
        self._type = type

    @property
    def primary_key_for_column_filtering(self):
        """Gets the primary_key_for_column_filtering of this ColumnObject.

        该列是否在列映射场景下为主键，如果是主建则填PRI，否则填空。

        :return: The primary_key_for_column_filtering of this ColumnObject.
        :rtype: str
        """
        return self._primary_key_for_column_filtering

    @primary_key_for_column_filtering.setter
    def primary_key_for_column_filtering(self, primary_key_for_column_filtering):
        """Sets the primary_key_for_column_filtering of this ColumnObject.

        该列是否在列映射场景下为主键，如果是主建则填PRI，否则填空。

        :param primary_key_for_column_filtering: The primary_key_for_column_filtering of this ColumnObject.
        :type primary_key_for_column_filtering: str
        """
        self._primary_key_for_column_filtering = primary_key_for_column_filtering

    @property
    def filtered(self):
        """Gets the filtered of this ColumnObject.

        该列是否进列过滤，不能与附加列additional同时使用。取值： - true：表示同步该列。 - false：表示过滤该列不同步。

        :return: The filtered of this ColumnObject.
        :rtype: bool
        """
        return self._filtered

    @filtered.setter
    def filtered(self, filtered):
        """Sets the filtered of this ColumnObject.

        该列是否进列过滤，不能与附加列additional同时使用。取值： - true：表示同步该列。 - false：表示过滤该列不同步。

        :param filtered: The filtered of this ColumnObject.
        :type filtered: bool
        """
        self._filtered = filtered

    @property
    def additional(self):
        """Gets the additional of this ColumnObject.

        该列是否为附加列，当该列为附加列时：name必须与表级对象中列名一致，并且不能与列过滤filtered同时使用。

        :return: The additional of this ColumnObject.
        :rtype: bool
        """
        return self._additional

    @additional.setter
    def additional(self, additional):
        """Sets the additional of this ColumnObject.

        该列是否为附加列，当该列为附加列时：name必须与表级对象中列名一致，并且不能与列过滤filtered同时使用。

        :param additional: The additional of this ColumnObject.
        :type additional: bool
        """
        self._additional = additional

    @property
    def operation_type(self):
        """Gets the operation_type of this ColumnObject.

        操作类型，以特定的操作类型填充新加的列。取值： - 以默认值方式：\"operation_type\":\"ADDITIONALCOLUMN,default_value\" - 以create_time为列：\"operation_type\":\"ADDITIONALCOLUMN,create_time\" - 以update_time为列：\"operation_type\":\"ADDITIONALCOLUMN,update_time\" - 以表达式为列：\"operation_type\":\"ADDITIONALCOLUMN,expression\" - 以serverName@database@table为列：\"operation_type\":\"ADDITIONALCOLUMN,server_database_table\"

        :return: The operation_type of this ColumnObject.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this ColumnObject.

        操作类型，以特定的操作类型填充新加的列。取值： - 以默认值方式：\"operation_type\":\"ADDITIONALCOLUMN,default_value\" - 以create_time为列：\"operation_type\":\"ADDITIONALCOLUMN,create_time\" - 以update_time为列：\"operation_type\":\"ADDITIONALCOLUMN,update_time\" - 以表达式为列：\"operation_type\":\"ADDITIONALCOLUMN,expression\" - 以serverName@database@table为列：\"operation_type\":\"ADDITIONALCOLUMN,server_database_table\"

        :param operation_type: The operation_type of this ColumnObject.
        :type operation_type: str
        """
        self._operation_type = operation_type

    @property
    def value(self):
        """Gets the value of this ColumnObject.

        附加列的值。约束： - 当操作类型仅“以默认值方式”，“以serverName@database@table为列”时，才支持输入对应字段类型的值。 - 当操作类型为“以表达式为列”时，该字段为固定值\"concat(__current_database, '@', __current_table)\"，不需要填写。

        :return: The value of this ColumnObject.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ColumnObject.

        附加列的值。约束： - 当操作类型仅“以默认值方式”，“以serverName@database@table为列”时，才支持输入对应字段类型的值。 - 当操作类型为“以表达式为列”时，该字段为固定值\"concat(__current_database, '@', __current_table)\"，不需要填写。

        :param value: The value of this ColumnObject.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, ColumnObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
