# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ColdTableMetaInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'space_id': 'str',
        'dd_id': 'str',
        'database_name': 'str',
        'table_name': 'str',
        'partition_name': 'str',
        'expiration_time': 'int',
        'retained_time': 'int',
        'data_size': 'float'
    }

    attribute_map = {
        'space_id': 'space_id',
        'dd_id': 'dd_id',
        'database_name': 'database_name',
        'table_name': 'table_name',
        'partition_name': 'partition_name',
        'expiration_time': 'expiration_time',
        'retained_time': 'retained_time',
        'data_size': 'data_size'
    }

    def __init__(self, space_id=None, dd_id=None, database_name=None, table_name=None, partition_name=None, expiration_time=None, retained_time=None, data_size=None):
        r"""ColdTableMetaInfo

        The model defined in huaweicloud sdk

        :param space_id: **参数解释**：  表空间ID。  **取值范围**：  不涉及。
        :type space_id: str
        :param dd_id: **参数解释**：  表ID。  **取值范围**：  不涉及。
        :type dd_id: str
        :param database_name: **参数解释**：  冷表库名。  **取值范围**：  不涉及。
        :type database_name: str
        :param table_name: **参数解释**：  冷表表名。  **取值范围**：  不涉及。
        :type table_name: str
        :param partition_name: **参数解释**：  冷表分区名。  **取值范围**：  不涉及。
        :type partition_name: str
        :param expiration_time: **参数解释**：  冷表有效周期（秒）。  **取值范围**：  ≥0。
        :type expiration_time: int
        :param retained_time: **参数解释**：  冷表已保留时间（秒）。  **取值范围**：  ≥0。
        :type retained_time: int
        :param data_size: **参数解释**：  冷表数据量大小（MB）。  **取值范围**：  ≥0。
        :type data_size: float
        """
        
        

        self._space_id = None
        self._dd_id = None
        self._database_name = None
        self._table_name = None
        self._partition_name = None
        self._expiration_time = None
        self._retained_time = None
        self._data_size = None
        self.discriminator = None

        if space_id is not None:
            self.space_id = space_id
        if dd_id is not None:
            self.dd_id = dd_id
        if database_name is not None:
            self.database_name = database_name
        if table_name is not None:
            self.table_name = table_name
        if partition_name is not None:
            self.partition_name = partition_name
        if expiration_time is not None:
            self.expiration_time = expiration_time
        if retained_time is not None:
            self.retained_time = retained_time
        if data_size is not None:
            self.data_size = data_size

    @property
    def space_id(self):
        r"""Gets the space_id of this ColdTableMetaInfo.

        **参数解释**：  表空间ID。  **取值范围**：  不涉及。

        :return: The space_id of this ColdTableMetaInfo.
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        r"""Sets the space_id of this ColdTableMetaInfo.

        **参数解释**：  表空间ID。  **取值范围**：  不涉及。

        :param space_id: The space_id of this ColdTableMetaInfo.
        :type space_id: str
        """
        self._space_id = space_id

    @property
    def dd_id(self):
        r"""Gets the dd_id of this ColdTableMetaInfo.

        **参数解释**：  表ID。  **取值范围**：  不涉及。

        :return: The dd_id of this ColdTableMetaInfo.
        :rtype: str
        """
        return self._dd_id

    @dd_id.setter
    def dd_id(self, dd_id):
        r"""Sets the dd_id of this ColdTableMetaInfo.

        **参数解释**：  表ID。  **取值范围**：  不涉及。

        :param dd_id: The dd_id of this ColdTableMetaInfo.
        :type dd_id: str
        """
        self._dd_id = dd_id

    @property
    def database_name(self):
        r"""Gets the database_name of this ColdTableMetaInfo.

        **参数解释**：  冷表库名。  **取值范围**：  不涉及。

        :return: The database_name of this ColdTableMetaInfo.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ColdTableMetaInfo.

        **参数解释**：  冷表库名。  **取值范围**：  不涉及。

        :param database_name: The database_name of this ColdTableMetaInfo.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_name(self):
        r"""Gets the table_name of this ColdTableMetaInfo.

        **参数解释**：  冷表表名。  **取值范围**：  不涉及。

        :return: The table_name of this ColdTableMetaInfo.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this ColdTableMetaInfo.

        **参数解释**：  冷表表名。  **取值范围**：  不涉及。

        :param table_name: The table_name of this ColdTableMetaInfo.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def partition_name(self):
        r"""Gets the partition_name of this ColdTableMetaInfo.

        **参数解释**：  冷表分区名。  **取值范围**：  不涉及。

        :return: The partition_name of this ColdTableMetaInfo.
        :rtype: str
        """
        return self._partition_name

    @partition_name.setter
    def partition_name(self, partition_name):
        r"""Sets the partition_name of this ColdTableMetaInfo.

        **参数解释**：  冷表分区名。  **取值范围**：  不涉及。

        :param partition_name: The partition_name of this ColdTableMetaInfo.
        :type partition_name: str
        """
        self._partition_name = partition_name

    @property
    def expiration_time(self):
        r"""Gets the expiration_time of this ColdTableMetaInfo.

        **参数解释**：  冷表有效周期（秒）。  **取值范围**：  ≥0。

        :return: The expiration_time of this ColdTableMetaInfo.
        :rtype: int
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        r"""Sets the expiration_time of this ColdTableMetaInfo.

        **参数解释**：  冷表有效周期（秒）。  **取值范围**：  ≥0。

        :param expiration_time: The expiration_time of this ColdTableMetaInfo.
        :type expiration_time: int
        """
        self._expiration_time = expiration_time

    @property
    def retained_time(self):
        r"""Gets the retained_time of this ColdTableMetaInfo.

        **参数解释**：  冷表已保留时间（秒）。  **取值范围**：  ≥0。

        :return: The retained_time of this ColdTableMetaInfo.
        :rtype: int
        """
        return self._retained_time

    @retained_time.setter
    def retained_time(self, retained_time):
        r"""Sets the retained_time of this ColdTableMetaInfo.

        **参数解释**：  冷表已保留时间（秒）。  **取值范围**：  ≥0。

        :param retained_time: The retained_time of this ColdTableMetaInfo.
        :type retained_time: int
        """
        self._retained_time = retained_time

    @property
    def data_size(self):
        r"""Gets the data_size of this ColdTableMetaInfo.

        **参数解释**：  冷表数据量大小（MB）。  **取值范围**：  ≥0。

        :return: The data_size of this ColdTableMetaInfo.
        :rtype: float
        """
        return self._data_size

    @data_size.setter
    def data_size(self, data_size):
        r"""Sets the data_size of this ColdTableMetaInfo.

        **参数解释**：  冷表数据量大小（MB）。  **取值范围**：  ≥0。

        :param data_size: The data_size of this ColdTableMetaInfo.
        :type data_size: float
        """
        self._data_size = data_size

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
        if not isinstance(other, ColdTableMetaInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
