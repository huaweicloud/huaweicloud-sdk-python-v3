# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IndexAdviceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'schema_name': 'str',
        'table_name': 'str',
        'index_name': 'str',
        'columns': 'list[str]',
        'unique': 'bool',
        'track_id': 'str',
        'quality': 'object',
        'ddl_add_index': 'str'
    }

    attribute_map = {
        'schema_name': 'schema_name',
        'table_name': 'table_name',
        'index_name': 'index_name',
        'columns': 'columns',
        'unique': 'unique',
        'track_id': 'track_id',
        'quality': 'quality',
        'ddl_add_index': 'ddl_add_index'
    }

    def __init__(self, schema_name=None, table_name=None, index_name=None, columns=None, unique=None, track_id=None, quality=None, ddl_add_index=None):
        """IndexAdviceInfo

        The model defined in huaweicloud sdk

        :param schema_name: schema名
        :type schema_name: str
        :param table_name: 表名
        :type table_name: str
        :param index_name: 索引名
        :type index_name: str
        :param columns: 列
        :type columns: list[str]
        :param unique: 是否唯一
        :type unique: bool
        :param track_id: 追踪id
        :type track_id: str
        :param quality: 质量
        :type quality: object
        :param ddl_add_index: ddl需要添加的索引
        :type ddl_add_index: str
        """
        
        

        self._schema_name = None
        self._table_name = None
        self._index_name = None
        self._columns = None
        self._unique = None
        self._track_id = None
        self._quality = None
        self._ddl_add_index = None
        self.discriminator = None

        if schema_name is not None:
            self.schema_name = schema_name
        if table_name is not None:
            self.table_name = table_name
        if index_name is not None:
            self.index_name = index_name
        if columns is not None:
            self.columns = columns
        if unique is not None:
            self.unique = unique
        if track_id is not None:
            self.track_id = track_id
        if quality is not None:
            self.quality = quality
        if ddl_add_index is not None:
            self.ddl_add_index = ddl_add_index

    @property
    def schema_name(self):
        """Gets the schema_name of this IndexAdviceInfo.

        schema名

        :return: The schema_name of this IndexAdviceInfo.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """Sets the schema_name of this IndexAdviceInfo.

        schema名

        :param schema_name: The schema_name of this IndexAdviceInfo.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def table_name(self):
        """Gets the table_name of this IndexAdviceInfo.

        表名

        :return: The table_name of this IndexAdviceInfo.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this IndexAdviceInfo.

        表名

        :param table_name: The table_name of this IndexAdviceInfo.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def index_name(self):
        """Gets the index_name of this IndexAdviceInfo.

        索引名

        :return: The index_name of this IndexAdviceInfo.
        :rtype: str
        """
        return self._index_name

    @index_name.setter
    def index_name(self, index_name):
        """Sets the index_name of this IndexAdviceInfo.

        索引名

        :param index_name: The index_name of this IndexAdviceInfo.
        :type index_name: str
        """
        self._index_name = index_name

    @property
    def columns(self):
        """Gets the columns of this IndexAdviceInfo.

        列

        :return: The columns of this IndexAdviceInfo.
        :rtype: list[str]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this IndexAdviceInfo.

        列

        :param columns: The columns of this IndexAdviceInfo.
        :type columns: list[str]
        """
        self._columns = columns

    @property
    def unique(self):
        """Gets the unique of this IndexAdviceInfo.

        是否唯一

        :return: The unique of this IndexAdviceInfo.
        :rtype: bool
        """
        return self._unique

    @unique.setter
    def unique(self, unique):
        """Sets the unique of this IndexAdviceInfo.

        是否唯一

        :param unique: The unique of this IndexAdviceInfo.
        :type unique: bool
        """
        self._unique = unique

    @property
    def track_id(self):
        """Gets the track_id of this IndexAdviceInfo.

        追踪id

        :return: The track_id of this IndexAdviceInfo.
        :rtype: str
        """
        return self._track_id

    @track_id.setter
    def track_id(self, track_id):
        """Sets the track_id of this IndexAdviceInfo.

        追踪id

        :param track_id: The track_id of this IndexAdviceInfo.
        :type track_id: str
        """
        self._track_id = track_id

    @property
    def quality(self):
        """Gets the quality of this IndexAdviceInfo.

        质量

        :return: The quality of this IndexAdviceInfo.
        :rtype: object
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        """Sets the quality of this IndexAdviceInfo.

        质量

        :param quality: The quality of this IndexAdviceInfo.
        :type quality: object
        """
        self._quality = quality

    @property
    def ddl_add_index(self):
        """Gets the ddl_add_index of this IndexAdviceInfo.

        ddl需要添加的索引

        :return: The ddl_add_index of this IndexAdviceInfo.
        :rtype: str
        """
        return self._ddl_add_index

    @ddl_add_index.setter
    def ddl_add_index(self, ddl_add_index):
        """Sets the ddl_add_index of this IndexAdviceInfo.

        ddl需要添加的索引

        :param ddl_add_index: The ddl_add_index of this IndexAdviceInfo.
        :type ddl_add_index: str
        """
        self._ddl_add_index = ddl_add_index

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
        if not isinstance(other, IndexAdviceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
