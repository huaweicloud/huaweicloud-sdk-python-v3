# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDatabaseVolumesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'instance_id': 'str',
        'database_name': 'str',
        'table_space_name': 'str',
        'user_name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'database_name': 'database_name',
        'table_space_name': 'table_space_name',
        'user_name': 'user_name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, x_language=None, instance_id=None, database_name=None, table_space_name=None, user_name=None, offset=None, limit=None):
        r"""ListDatabaseVolumesRequest

        The model defined in huaweicloud sdk

        :param x_language: **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us
        :type x_language: str
        :param instance_id: **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。
        :type instance_id: str
        :param database_name: **参数解释**: 数据库名称。 **约束限制**: 不涉及 **取值范围**: 不涉及 **默认取值**: 不涉及。 
        :type database_name: str
        :param table_space_name: **参数解释**: 数据库的缺省表空间名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 
        :type table_space_name: str
        :param user_name: **参数解释**: 表所属用户名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 
        :type user_name: str
        :param offset: **参数解释**: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。 **约束限制**: 不涉及。 **取值范围**: 0 - 10000 **默认取值**: 0 
        :type offset: int
        :param limit: **参数解释**: 查询记录数。 **约束限制**: 不能为负数。 **取值范围**: 最小值为1，最大值为200。 **默认取值**: 100 
        :type limit: int
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._database_name = None
        self._table_space_name = None
        self._user_name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        if database_name is not None:
            self.database_name = database_name
        if table_space_name is not None:
            self.table_space_name = table_space_name
        if user_name is not None:
            self.user_name = user_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def x_language(self):
        r"""Gets the x_language of this ListDatabaseVolumesRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us

        :return: The x_language of this ListDatabaseVolumesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListDatabaseVolumesRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us

        :param x_language: The x_language of this ListDatabaseVolumesRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListDatabaseVolumesRequest.

        **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。

        :return: The instance_id of this ListDatabaseVolumesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListDatabaseVolumesRequest.

        **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。

        :param instance_id: The instance_id of this ListDatabaseVolumesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def database_name(self):
        r"""Gets the database_name of this ListDatabaseVolumesRequest.

        **参数解释**: 数据库名称。 **约束限制**: 不涉及 **取值范围**: 不涉及 **默认取值**: 不涉及。 

        :return: The database_name of this ListDatabaseVolumesRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ListDatabaseVolumesRequest.

        **参数解释**: 数据库名称。 **约束限制**: 不涉及 **取值范围**: 不涉及 **默认取值**: 不涉及。 

        :param database_name: The database_name of this ListDatabaseVolumesRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_space_name(self):
        r"""Gets the table_space_name of this ListDatabaseVolumesRequest.

        **参数解释**: 数据库的缺省表空间名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 

        :return: The table_space_name of this ListDatabaseVolumesRequest.
        :rtype: str
        """
        return self._table_space_name

    @table_space_name.setter
    def table_space_name(self, table_space_name):
        r"""Sets the table_space_name of this ListDatabaseVolumesRequest.

        **参数解释**: 数据库的缺省表空间名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 

        :param table_space_name: The table_space_name of this ListDatabaseVolumesRequest.
        :type table_space_name: str
        """
        self._table_space_name = table_space_name

    @property
    def user_name(self):
        r"""Gets the user_name of this ListDatabaseVolumesRequest.

        **参数解释**: 表所属用户名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 

        :return: The user_name of this ListDatabaseVolumesRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ListDatabaseVolumesRequest.

        **参数解释**: 表所属用户名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 

        :param user_name: The user_name of this ListDatabaseVolumesRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def offset(self):
        r"""Gets the offset of this ListDatabaseVolumesRequest.

        **参数解释**: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。 **约束限制**: 不涉及。 **取值范围**: 0 - 10000 **默认取值**: 0 

        :return: The offset of this ListDatabaseVolumesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListDatabaseVolumesRequest.

        **参数解释**: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。 **约束限制**: 不涉及。 **取值范围**: 0 - 10000 **默认取值**: 0 

        :param offset: The offset of this ListDatabaseVolumesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListDatabaseVolumesRequest.

        **参数解释**: 查询记录数。 **约束限制**: 不能为负数。 **取值范围**: 最小值为1，最大值为200。 **默认取值**: 100 

        :return: The limit of this ListDatabaseVolumesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDatabaseVolumesRequest.

        **参数解释**: 查询记录数。 **约束限制**: 不能为负数。 **取值范围**: 最小值为1，最大值为200。 **默认取值**: 100 

        :param limit: The limit of this ListDatabaseVolumesRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListDatabaseVolumesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
