# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTableResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_success': 'bool',
        'message': 'str',
        'column_count': 'int',
        'columns': 'list[Column]',
        'table_type': 'str',
        'data_type': 'str',
        'data_location': 'str',
        'storage_properties': 'list[object]',
        'table_comment': 'str',
        'create_table_sql': 'str'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'column_count': 'column_count',
        'columns': 'columns',
        'table_type': 'table_type',
        'data_type': 'data_type',
        'data_location': 'data_location',
        'storage_properties': 'storage_properties',
        'table_comment': 'table_comment',
        'create_table_sql': 'create_table_sql'
    }

    def __init__(self, is_success=None, message=None, column_count=None, columns=None, table_type=None, data_type=None, data_location=None, storage_properties=None, table_comment=None, create_table_sql=None):
        r"""ShowTableResponse

        The model defined in huaweicloud sdk

        :param is_success: 执行请求是否成功。“true”表示请求执行成功。
        :type is_success: bool
        :param message: 系统提示信息，执行成功时，信息可能为空。
        :type message: str
        :param column_count: 表的总列数。
        :type column_count: int
        :param columns: 表的列信息，包含列名称、类型和描述信息。
        :type columns: list[:class:`huaweicloudsdkdli.v1.Column`]
        :param table_type: 表类型，包括“MANAGED”，“EXTERNAL”和“VIEW”。
        :type table_type: str
        :param data_type: 数据类型，包括“csv”，“parquet”，“orc”，“json”，“carbon”和“avro”。
        :type data_type: str
        :param data_location: 数据存储的路径，以“s3a”开头。
        :type data_location: str
        :param storage_properties: 存储属性，以“key/value”的格式出现，包含delimiter，escape，quote，header，dateformat，timestampformat参数。
        :type storage_properties: list[object]
        :param table_comment: 表的注释。
        :type table_comment: str
        :param create_table_sql: 建表的语句
        :type create_table_sql: str
        """
        
        super(ShowTableResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._column_count = None
        self._columns = None
        self._table_type = None
        self._data_type = None
        self._data_location = None
        self._storage_properties = None
        self._table_comment = None
        self._create_table_sql = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if column_count is not None:
            self.column_count = column_count
        if columns is not None:
            self.columns = columns
        if table_type is not None:
            self.table_type = table_type
        if data_type is not None:
            self.data_type = data_type
        if data_location is not None:
            self.data_location = data_location
        if storage_properties is not None:
            self.storage_properties = storage_properties
        if table_comment is not None:
            self.table_comment = table_comment
        if create_table_sql is not None:
            self.create_table_sql = create_table_sql

    @property
    def is_success(self):
        r"""Gets the is_success of this ShowTableResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :return: The is_success of this ShowTableResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        r"""Sets the is_success of this ShowTableResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :param is_success: The is_success of this ShowTableResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        r"""Gets the message of this ShowTableResponse.

        系统提示信息，执行成功时，信息可能为空。

        :return: The message of this ShowTableResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ShowTableResponse.

        系统提示信息，执行成功时，信息可能为空。

        :param message: The message of this ShowTableResponse.
        :type message: str
        """
        self._message = message

    @property
    def column_count(self):
        r"""Gets the column_count of this ShowTableResponse.

        表的总列数。

        :return: The column_count of this ShowTableResponse.
        :rtype: int
        """
        return self._column_count

    @column_count.setter
    def column_count(self, column_count):
        r"""Sets the column_count of this ShowTableResponse.

        表的总列数。

        :param column_count: The column_count of this ShowTableResponse.
        :type column_count: int
        """
        self._column_count = column_count

    @property
    def columns(self):
        r"""Gets the columns of this ShowTableResponse.

        表的列信息，包含列名称、类型和描述信息。

        :return: The columns of this ShowTableResponse.
        :rtype: list[:class:`huaweicloudsdkdli.v1.Column`]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        r"""Sets the columns of this ShowTableResponse.

        表的列信息，包含列名称、类型和描述信息。

        :param columns: The columns of this ShowTableResponse.
        :type columns: list[:class:`huaweicloudsdkdli.v1.Column`]
        """
        self._columns = columns

    @property
    def table_type(self):
        r"""Gets the table_type of this ShowTableResponse.

        表类型，包括“MANAGED”，“EXTERNAL”和“VIEW”。

        :return: The table_type of this ShowTableResponse.
        :rtype: str
        """
        return self._table_type

    @table_type.setter
    def table_type(self, table_type):
        r"""Sets the table_type of this ShowTableResponse.

        表类型，包括“MANAGED”，“EXTERNAL”和“VIEW”。

        :param table_type: The table_type of this ShowTableResponse.
        :type table_type: str
        """
        self._table_type = table_type

    @property
    def data_type(self):
        r"""Gets the data_type of this ShowTableResponse.

        数据类型，包括“csv”，“parquet”，“orc”，“json”，“carbon”和“avro”。

        :return: The data_type of this ShowTableResponse.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        r"""Sets the data_type of this ShowTableResponse.

        数据类型，包括“csv”，“parquet”，“orc”，“json”，“carbon”和“avro”。

        :param data_type: The data_type of this ShowTableResponse.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def data_location(self):
        r"""Gets the data_location of this ShowTableResponse.

        数据存储的路径，以“s3a”开头。

        :return: The data_location of this ShowTableResponse.
        :rtype: str
        """
        return self._data_location

    @data_location.setter
    def data_location(self, data_location):
        r"""Sets the data_location of this ShowTableResponse.

        数据存储的路径，以“s3a”开头。

        :param data_location: The data_location of this ShowTableResponse.
        :type data_location: str
        """
        self._data_location = data_location

    @property
    def storage_properties(self):
        r"""Gets the storage_properties of this ShowTableResponse.

        存储属性，以“key/value”的格式出现，包含delimiter，escape，quote，header，dateformat，timestampformat参数。

        :return: The storage_properties of this ShowTableResponse.
        :rtype: list[object]
        """
        return self._storage_properties

    @storage_properties.setter
    def storage_properties(self, storage_properties):
        r"""Sets the storage_properties of this ShowTableResponse.

        存储属性，以“key/value”的格式出现，包含delimiter，escape，quote，header，dateformat，timestampformat参数。

        :param storage_properties: The storage_properties of this ShowTableResponse.
        :type storage_properties: list[object]
        """
        self._storage_properties = storage_properties

    @property
    def table_comment(self):
        r"""Gets the table_comment of this ShowTableResponse.

        表的注释。

        :return: The table_comment of this ShowTableResponse.
        :rtype: str
        """
        return self._table_comment

    @table_comment.setter
    def table_comment(self, table_comment):
        r"""Sets the table_comment of this ShowTableResponse.

        表的注释。

        :param table_comment: The table_comment of this ShowTableResponse.
        :type table_comment: str
        """
        self._table_comment = table_comment

    @property
    def create_table_sql(self):
        r"""Gets the create_table_sql of this ShowTableResponse.

        建表的语句

        :return: The create_table_sql of this ShowTableResponse.
        :rtype: str
        """
        return self._create_table_sql

    @create_table_sql.setter
    def create_table_sql(self, create_table_sql):
        r"""Sets the create_table_sql of this ShowTableResponse.

        建表的语句

        :param create_table_sql: The create_table_sql of this ShowTableResponse.
        :type create_table_sql: str
        """
        self._create_table_sql = create_table_sql

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
        if not isinstance(other, ShowTableResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
