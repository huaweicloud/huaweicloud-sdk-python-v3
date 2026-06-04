# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IcebergStructField:

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
        'name': 'str',
        'type': 'str',
        'type_json': 'str',
        'required': 'bool',
        'doc': 'str',
        'write_default': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'type_json': 'type_json',
        'required': 'required',
        'doc': 'doc',
        'write_default': 'write_default'
    }

    def __init__(self, id=None, name=None, type=None, type_json=None, required=None, doc=None, write_default=None):
        r"""IcebergStructField

        The model defined in huaweicloud sdk

        :param id: 字段id。
        :type id: int
        :param name: 字段名称。
        :type name: str
        :param type: 字段类型, 包含 BOOLEAN, INTEGER, LONG, FLOAT, DOUBLE, DATE, TIME, TIMESTAMP, TIMESTAMP_NANO, STRING, UUID, FIXED, BINARY, DECIMAL, STRUCT, LIST, MAP
        :type type: str
        :param type_json: 如果type字段输入了STRUCT, LIST, MAP以外的类型，此处应该为空。如果type类型输入了STRUCT, LIST, MAP，此处应该为嵌套类型json体的字符串。
        :type type_json: str
        :param required: 表示这个字段是必须的还是可选的
        :type required: bool
        :param doc: comment
        :type doc: str
        :param write_default: 字段写入默认值, 在每次写入操作时生效，覆盖显式写入的null值。
        :type write_default: str
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._type_json = None
        self._required = None
        self._doc = None
        self._write_default = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.type = type
        if type_json is not None:
            self.type_json = type_json
        self.required = required
        if doc is not None:
            self.doc = doc
        if write_default is not None:
            self.write_default = write_default

    @property
    def id(self):
        r"""Gets the id of this IcebergStructField.

        字段id。

        :return: The id of this IcebergStructField.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this IcebergStructField.

        字段id。

        :param id: The id of this IcebergStructField.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this IcebergStructField.

        字段名称。

        :return: The name of this IcebergStructField.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this IcebergStructField.

        字段名称。

        :param name: The name of this IcebergStructField.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this IcebergStructField.

        字段类型, 包含 BOOLEAN, INTEGER, LONG, FLOAT, DOUBLE, DATE, TIME, TIMESTAMP, TIMESTAMP_NANO, STRING, UUID, FIXED, BINARY, DECIMAL, STRUCT, LIST, MAP

        :return: The type of this IcebergStructField.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this IcebergStructField.

        字段类型, 包含 BOOLEAN, INTEGER, LONG, FLOAT, DOUBLE, DATE, TIME, TIMESTAMP, TIMESTAMP_NANO, STRING, UUID, FIXED, BINARY, DECIMAL, STRUCT, LIST, MAP

        :param type: The type of this IcebergStructField.
        :type type: str
        """
        self._type = type

    @property
    def type_json(self):
        r"""Gets the type_json of this IcebergStructField.

        如果type字段输入了STRUCT, LIST, MAP以外的类型，此处应该为空。如果type类型输入了STRUCT, LIST, MAP，此处应该为嵌套类型json体的字符串。

        :return: The type_json of this IcebergStructField.
        :rtype: str
        """
        return self._type_json

    @type_json.setter
    def type_json(self, type_json):
        r"""Sets the type_json of this IcebergStructField.

        如果type字段输入了STRUCT, LIST, MAP以外的类型，此处应该为空。如果type类型输入了STRUCT, LIST, MAP，此处应该为嵌套类型json体的字符串。

        :param type_json: The type_json of this IcebergStructField.
        :type type_json: str
        """
        self._type_json = type_json

    @property
    def required(self):
        r"""Gets the required of this IcebergStructField.

        表示这个字段是必须的还是可选的

        :return: The required of this IcebergStructField.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        r"""Sets the required of this IcebergStructField.

        表示这个字段是必须的还是可选的

        :param required: The required of this IcebergStructField.
        :type required: bool
        """
        self._required = required

    @property
    def doc(self):
        r"""Gets the doc of this IcebergStructField.

        comment

        :return: The doc of this IcebergStructField.
        :rtype: str
        """
        return self._doc

    @doc.setter
    def doc(self, doc):
        r"""Sets the doc of this IcebergStructField.

        comment

        :param doc: The doc of this IcebergStructField.
        :type doc: str
        """
        self._doc = doc

    @property
    def write_default(self):
        r"""Gets the write_default of this IcebergStructField.

        字段写入默认值, 在每次写入操作时生效，覆盖显式写入的null值。

        :return: The write_default of this IcebergStructField.
        :rtype: str
        """
        return self._write_default

    @write_default.setter
    def write_default(self, write_default):
        r"""Sets the write_default of this IcebergStructField.

        字段写入默认值, 在每次写入操作时生效，覆盖显式写入的null值。

        :param write_default: The write_default of this IcebergStructField.
        :type write_default: str
        """
        self._write_default = write_default

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
        if not isinstance(other, IcebergStructField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
