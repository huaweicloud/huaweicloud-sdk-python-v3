# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatabaseVolumeResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database_name': 'str',
        'table_space_name': 'str',
        'user_name': 'str',
        'database_size': 'str'
    }

    attribute_map = {
        'database_name': 'database_name',
        'table_space_name': 'table_space_name',
        'user_name': 'user_name',
        'database_size': 'database_size'
    }

    def __init__(self, database_name=None, table_space_name=None, user_name=None, database_size=None):
        r"""DatabaseVolumeResult

        The model defined in huaweicloud sdk

        :param database_name: **参数解释**: 数据库名称。 **取值范围**: 不涉及。 
        :type database_name: str
        :param table_space_name: **参数解释**: 数据库的缺省表空间名。 **取值范围**: 不涉及。 
        :type table_space_name: str
        :param user_name: **参数解释**: 表所属用户名称。 **取值范围**: 不涉及。 
        :type user_name: str
        :param database_size: **参数解释**: 数据库占用空间大小。 **取值范围**: 不涉及。 
        :type database_size: str
        """
        
        

        self._database_name = None
        self._table_space_name = None
        self._user_name = None
        self._database_size = None
        self.discriminator = None

        if database_name is not None:
            self.database_name = database_name
        if table_space_name is not None:
            self.table_space_name = table_space_name
        if user_name is not None:
            self.user_name = user_name
        if database_size is not None:
            self.database_size = database_size

    @property
    def database_name(self):
        r"""Gets the database_name of this DatabaseVolumeResult.

        **参数解释**: 数据库名称。 **取值范围**: 不涉及。 

        :return: The database_name of this DatabaseVolumeResult.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this DatabaseVolumeResult.

        **参数解释**: 数据库名称。 **取值范围**: 不涉及。 

        :param database_name: The database_name of this DatabaseVolumeResult.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_space_name(self):
        r"""Gets the table_space_name of this DatabaseVolumeResult.

        **参数解释**: 数据库的缺省表空间名。 **取值范围**: 不涉及。 

        :return: The table_space_name of this DatabaseVolumeResult.
        :rtype: str
        """
        return self._table_space_name

    @table_space_name.setter
    def table_space_name(self, table_space_name):
        r"""Sets the table_space_name of this DatabaseVolumeResult.

        **参数解释**: 数据库的缺省表空间名。 **取值范围**: 不涉及。 

        :param table_space_name: The table_space_name of this DatabaseVolumeResult.
        :type table_space_name: str
        """
        self._table_space_name = table_space_name

    @property
    def user_name(self):
        r"""Gets the user_name of this DatabaseVolumeResult.

        **参数解释**: 表所属用户名称。 **取值范围**: 不涉及。 

        :return: The user_name of this DatabaseVolumeResult.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this DatabaseVolumeResult.

        **参数解释**: 表所属用户名称。 **取值范围**: 不涉及。 

        :param user_name: The user_name of this DatabaseVolumeResult.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def database_size(self):
        r"""Gets the database_size of this DatabaseVolumeResult.

        **参数解释**: 数据库占用空间大小。 **取值范围**: 不涉及。 

        :return: The database_size of this DatabaseVolumeResult.
        :rtype: str
        """
        return self._database_size

    @database_size.setter
    def database_size(self, database_size):
        r"""Sets the database_size of this DatabaseVolumeResult.

        **参数解释**: 数据库占用空间大小。 **取值范围**: 不涉及。 

        :param database_size: The database_size of this DatabaseVolumeResult.
        :type database_size: str
        """
        self._database_size = database_size

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
        if not isinstance(other, DatabaseVolumeResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
