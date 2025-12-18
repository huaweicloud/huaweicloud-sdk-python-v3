# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SchemaVolumeResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'schema_size': 'str',
        'table_count': 'str',
        'user_name': 'str',
        'nsp_name': 'str'
    }

    attribute_map = {
        'schema_size': 'schema_size',
        'table_count': 'table_count',
        'user_name': 'user_name',
        'nsp_name': 'nsp_name'
    }

    def __init__(self, schema_size=None, table_count=None, user_name=None, nsp_name=None):
        r"""SchemaVolumeResult

        The model defined in huaweicloud sdk

        :param schema_size: **参数解释**: schema的大小。 **取值范围**: 不涉及。 
        :type schema_size: str
        :param table_count: **参数解释**: schema拥有的表数量。 **取值范围**: 不涉及。 
        :type table_count: str
        :param user_name: **参数解释**: schema所属用户名称。 **取值范围**: 不涉及。 
        :type user_name: str
        :param nsp_name: **参数解释**: schema名称空间的名称。 **取值范围**: 不涉及。 
        :type nsp_name: str
        """
        
        

        self._schema_size = None
        self._table_count = None
        self._user_name = None
        self._nsp_name = None
        self.discriminator = None

        if schema_size is not None:
            self.schema_size = schema_size
        if table_count is not None:
            self.table_count = table_count
        if user_name is not None:
            self.user_name = user_name
        if nsp_name is not None:
            self.nsp_name = nsp_name

    @property
    def schema_size(self):
        r"""Gets the schema_size of this SchemaVolumeResult.

        **参数解释**: schema的大小。 **取值范围**: 不涉及。 

        :return: The schema_size of this SchemaVolumeResult.
        :rtype: str
        """
        return self._schema_size

    @schema_size.setter
    def schema_size(self, schema_size):
        r"""Sets the schema_size of this SchemaVolumeResult.

        **参数解释**: schema的大小。 **取值范围**: 不涉及。 

        :param schema_size: The schema_size of this SchemaVolumeResult.
        :type schema_size: str
        """
        self._schema_size = schema_size

    @property
    def table_count(self):
        r"""Gets the table_count of this SchemaVolumeResult.

        **参数解释**: schema拥有的表数量。 **取值范围**: 不涉及。 

        :return: The table_count of this SchemaVolumeResult.
        :rtype: str
        """
        return self._table_count

    @table_count.setter
    def table_count(self, table_count):
        r"""Sets the table_count of this SchemaVolumeResult.

        **参数解释**: schema拥有的表数量。 **取值范围**: 不涉及。 

        :param table_count: The table_count of this SchemaVolumeResult.
        :type table_count: str
        """
        self._table_count = table_count

    @property
    def user_name(self):
        r"""Gets the user_name of this SchemaVolumeResult.

        **参数解释**: schema所属用户名称。 **取值范围**: 不涉及。 

        :return: The user_name of this SchemaVolumeResult.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this SchemaVolumeResult.

        **参数解释**: schema所属用户名称。 **取值范围**: 不涉及。 

        :param user_name: The user_name of this SchemaVolumeResult.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def nsp_name(self):
        r"""Gets the nsp_name of this SchemaVolumeResult.

        **参数解释**: schema名称空间的名称。 **取值范围**: 不涉及。 

        :return: The nsp_name of this SchemaVolumeResult.
        :rtype: str
        """
        return self._nsp_name

    @nsp_name.setter
    def nsp_name(self, nsp_name):
        r"""Sets the nsp_name of this SchemaVolumeResult.

        **参数解释**: schema名称空间的名称。 **取值范围**: 不涉及。 

        :param nsp_name: The nsp_name of this SchemaVolumeResult.
        :type nsp_name: str
        """
        self._nsp_name = nsp_name

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
        if not isinstance(other, SchemaVolumeResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
