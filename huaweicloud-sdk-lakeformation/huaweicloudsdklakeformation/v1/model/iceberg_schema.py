# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IcebergSchema:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'schema_id': 'int',
        'identifier_field_ids': 'list[int]',
        'type': 'str',
        'fields': 'list[IcebergStructField]',
        'primary_keys': 'list[int]',
        'last_column_id': 'int'
    }

    attribute_map = {
        'schema_id': 'schema_id',
        'identifier_field_ids': 'identifier_field_ids',
        'type': 'type',
        'fields': 'fields',
        'primary_keys': 'primary_keys',
        'last_column_id': 'last_column_id'
    }

    def __init__(self, schema_id=None, identifier_field_ids=None, type=None, fields=None, primary_keys=None, last_column_id=None):
        r"""IcebergSchema

        The model defined in huaweicloud sdk

        :param schema_id: 用来记录Iceberg表模式演化历史中模式版本的id。
        :type schema_id: int
        :param identifier_field_ids: 字段identifier的列表，可以识别表中的记录，用作行级操作以及去重。
        :type identifier_field_ids: list[int]
        :param type: 固定为struct。
        :type type: str
        :param fields: IcebergStructField的列表。
        :type fields: list[:class:`huaweicloudsdklakeformation.v1.IcebergStructField`]
        :param primary_keys: 用来指定哪些field是主键，列表内填写field_id。
        :type primary_keys: list[int]
        :param last_column_id: 为该表分配的最高列ID。
        :type last_column_id: int
        """
        
        

        self._schema_id = None
        self._identifier_field_ids = None
        self._type = None
        self._fields = None
        self._primary_keys = None
        self._last_column_id = None
        self.discriminator = None

        self.schema_id = schema_id
        self.identifier_field_ids = identifier_field_ids
        self.type = type
        self.fields = fields
        if primary_keys is not None:
            self.primary_keys = primary_keys
        if last_column_id is not None:
            self.last_column_id = last_column_id

    @property
    def schema_id(self):
        r"""Gets the schema_id of this IcebergSchema.

        用来记录Iceberg表模式演化历史中模式版本的id。

        :return: The schema_id of this IcebergSchema.
        :rtype: int
        """
        return self._schema_id

    @schema_id.setter
    def schema_id(self, schema_id):
        r"""Sets the schema_id of this IcebergSchema.

        用来记录Iceberg表模式演化历史中模式版本的id。

        :param schema_id: The schema_id of this IcebergSchema.
        :type schema_id: int
        """
        self._schema_id = schema_id

    @property
    def identifier_field_ids(self):
        r"""Gets the identifier_field_ids of this IcebergSchema.

        字段identifier的列表，可以识别表中的记录，用作行级操作以及去重。

        :return: The identifier_field_ids of this IcebergSchema.
        :rtype: list[int]
        """
        return self._identifier_field_ids

    @identifier_field_ids.setter
    def identifier_field_ids(self, identifier_field_ids):
        r"""Sets the identifier_field_ids of this IcebergSchema.

        字段identifier的列表，可以识别表中的记录，用作行级操作以及去重。

        :param identifier_field_ids: The identifier_field_ids of this IcebergSchema.
        :type identifier_field_ids: list[int]
        """
        self._identifier_field_ids = identifier_field_ids

    @property
    def type(self):
        r"""Gets the type of this IcebergSchema.

        固定为struct。

        :return: The type of this IcebergSchema.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this IcebergSchema.

        固定为struct。

        :param type: The type of this IcebergSchema.
        :type type: str
        """
        self._type = type

    @property
    def fields(self):
        r"""Gets the fields of this IcebergSchema.

        IcebergStructField的列表。

        :return: The fields of this IcebergSchema.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.IcebergStructField`]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this IcebergSchema.

        IcebergStructField的列表。

        :param fields: The fields of this IcebergSchema.
        :type fields: list[:class:`huaweicloudsdklakeformation.v1.IcebergStructField`]
        """
        self._fields = fields

    @property
    def primary_keys(self):
        r"""Gets the primary_keys of this IcebergSchema.

        用来指定哪些field是主键，列表内填写field_id。

        :return: The primary_keys of this IcebergSchema.
        :rtype: list[int]
        """
        return self._primary_keys

    @primary_keys.setter
    def primary_keys(self, primary_keys):
        r"""Sets the primary_keys of this IcebergSchema.

        用来指定哪些field是主键，列表内填写field_id。

        :param primary_keys: The primary_keys of this IcebergSchema.
        :type primary_keys: list[int]
        """
        self._primary_keys = primary_keys

    @property
    def last_column_id(self):
        r"""Gets the last_column_id of this IcebergSchema.

        为该表分配的最高列ID。

        :return: The last_column_id of this IcebergSchema.
        :rtype: int
        """
        return self._last_column_id

    @last_column_id.setter
    def last_column_id(self, last_column_id):
        r"""Sets the last_column_id of this IcebergSchema.

        为该表分配的最高列ID。

        :param last_column_id: The last_column_id of this IcebergSchema.
        :type last_column_id: int
        """
        self._last_column_id = last_column_id

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
        if not isinstance(other, IcebergSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
