# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFullSqlRequest:

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
        'sql_exec_id': 'str',
        'id': 'int',
        'sql_id': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'sql_exec_id': 'sql_exec_id',
        'id': 'id',
        'sql_id': 'sql_id'
    }

    def __init__(self, x_language=None, instance_id=None, sql_exec_id=None, id=None, sql_id=None):
        r"""ShowFullSqlRequest

        The model defined in huaweicloud sdk

        :param x_language: **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us
        :type x_language: str
        :param instance_id: **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。
        :type instance_id: str
        :param sql_exec_id: **参数解释**: 唯一SQL ID，对应内核字段：debug_query_id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type sql_exec_id: str
        :param id: **参数解释**: 采集到的全量SQL记录的唯一键ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type id: int
        :param sql_id: **参数解释**: 归一化SQL ID，对应内核字段：unique_sql_id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type sql_id: str
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._sql_exec_id = None
        self._id = None
        self._sql_id = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        self.sql_exec_id = sql_exec_id
        if id is not None:
            self.id = id
        if sql_id is not None:
            self.sql_id = sql_id

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowFullSqlRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us

        :return: The x_language of this ShowFullSqlRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowFullSqlRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us

        :param x_language: The x_language of this ShowFullSqlRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowFullSqlRequest.

        **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。

        :return: The instance_id of this ShowFullSqlRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowFullSqlRequest.

        **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。

        :param instance_id: The instance_id of this ShowFullSqlRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def sql_exec_id(self):
        r"""Gets the sql_exec_id of this ShowFullSqlRequest.

        **参数解释**: 唯一SQL ID，对应内核字段：debug_query_id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The sql_exec_id of this ShowFullSqlRequest.
        :rtype: str
        """
        return self._sql_exec_id

    @sql_exec_id.setter
    def sql_exec_id(self, sql_exec_id):
        r"""Sets the sql_exec_id of this ShowFullSqlRequest.

        **参数解释**: 唯一SQL ID，对应内核字段：debug_query_id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param sql_exec_id: The sql_exec_id of this ShowFullSqlRequest.
        :type sql_exec_id: str
        """
        self._sql_exec_id = sql_exec_id

    @property
    def id(self):
        r"""Gets the id of this ShowFullSqlRequest.

        **参数解释**: 采集到的全量SQL记录的唯一键ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The id of this ShowFullSqlRequest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowFullSqlRequest.

        **参数解释**: 采集到的全量SQL记录的唯一键ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param id: The id of this ShowFullSqlRequest.
        :type id: int
        """
        self._id = id

    @property
    def sql_id(self):
        r"""Gets the sql_id of this ShowFullSqlRequest.

        **参数解释**: 归一化SQL ID，对应内核字段：unique_sql_id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The sql_id of this ShowFullSqlRequest.
        :rtype: str
        """
        return self._sql_id

    @sql_id.setter
    def sql_id(self, sql_id):
        r"""Sets the sql_id of this ShowFullSqlRequest.

        **参数解释**: 归一化SQL ID，对应内核字段：unique_sql_id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param sql_id: The sql_id of this ShowFullSqlRequest.
        :type sql_id: str
        """
        self._sql_id = sql_id

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
        if not isinstance(other, ShowFullSqlRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
