# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSqlPatchRequest:

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
        'node_id': 'str',
        'sql_id': 'str',
        'database_name': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'node_id': 'node_id',
        'sql_id': 'sql_id',
        'database_name': 'database_name'
    }

    def __init__(self, x_language=None, instance_id=None, node_id=None, sql_id=None, database_name=None):
        r"""ShowSqlPatchRequest

        The model defined in huaweicloud sdk

        :param x_language: **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us **默认取值**: en-us
        :type x_language: str
        :param instance_id: **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。
        :type instance_id: str
        :param node_id: **参数解释** : 节点ID。 **约束限制** : 不涉及。 **取值范围** : 由 32 个字符（英文字母、数字、-或\\），后跟 \&quot;no\&quot;，再跟 \&quot;14\&quot; 或 \&quot;20\&quot; 组成的字符串。 **默认取值** : 不涉及。
        :type node_id: str
        :param sql_id: **参数解释** : 慢SQL的ID。 **约束限制** : 不涉及。 **取值范围** : 由数字组成，且长度为1~256个字符。 **默认取值** : 不涉及。
        :type sql_id: str
        :param database_name: **参数解释** : 数据库名称。慢SQL场景可以不填，其他场景必填。 **约束限制** : 不能使用模板库，且是已存在的数据库名称。 模板库包括 template0 ，template1。 **取值范围** : 只能由字母、数字、_及$组成，且长度为0~63个字符，不能以数字开头。 **默认取值** : 不涉及。
        :type database_name: str
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._node_id = None
        self._sql_id = None
        self._database_name = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        self.node_id = node_id
        self.sql_id = sql_id
        if database_name is not None:
            self.database_name = database_name

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowSqlPatchRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us **默认取值**: en-us

        :return: The x_language of this ShowSqlPatchRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowSqlPatchRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us **默认取值**: en-us

        :param x_language: The x_language of this ShowSqlPatchRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowSqlPatchRequest.

        **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。

        :return: The instance_id of this ShowSqlPatchRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowSqlPatchRequest.

        **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。

        :param instance_id: The instance_id of this ShowSqlPatchRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def node_id(self):
        r"""Gets the node_id of this ShowSqlPatchRequest.

        **参数解释** : 节点ID。 **约束限制** : 不涉及。 **取值范围** : 由 32 个字符（英文字母、数字、-或\\），后跟 \"no\"，再跟 \"14\" 或 \"20\" 组成的字符串。 **默认取值** : 不涉及。

        :return: The node_id of this ShowSqlPatchRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ShowSqlPatchRequest.

        **参数解释** : 节点ID。 **约束限制** : 不涉及。 **取值范围** : 由 32 个字符（英文字母、数字、-或\\），后跟 \"no\"，再跟 \"14\" 或 \"20\" 组成的字符串。 **默认取值** : 不涉及。

        :param node_id: The node_id of this ShowSqlPatchRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def sql_id(self):
        r"""Gets the sql_id of this ShowSqlPatchRequest.

        **参数解释** : 慢SQL的ID。 **约束限制** : 不涉及。 **取值范围** : 由数字组成，且长度为1~256个字符。 **默认取值** : 不涉及。

        :return: The sql_id of this ShowSqlPatchRequest.
        :rtype: str
        """
        return self._sql_id

    @sql_id.setter
    def sql_id(self, sql_id):
        r"""Sets the sql_id of this ShowSqlPatchRequest.

        **参数解释** : 慢SQL的ID。 **约束限制** : 不涉及。 **取值范围** : 由数字组成，且长度为1~256个字符。 **默认取值** : 不涉及。

        :param sql_id: The sql_id of this ShowSqlPatchRequest.
        :type sql_id: str
        """
        self._sql_id = sql_id

    @property
    def database_name(self):
        r"""Gets the database_name of this ShowSqlPatchRequest.

        **参数解释** : 数据库名称。慢SQL场景可以不填，其他场景必填。 **约束限制** : 不能使用模板库，且是已存在的数据库名称。 模板库包括 template0 ，template1。 **取值范围** : 只能由字母、数字、_及$组成，且长度为0~63个字符，不能以数字开头。 **默认取值** : 不涉及。

        :return: The database_name of this ShowSqlPatchRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ShowSqlPatchRequest.

        **参数解释** : 数据库名称。慢SQL场景可以不填，其他场景必填。 **约束限制** : 不能使用模板库，且是已存在的数据库名称。 模板库包括 template0 ，template1。 **取值范围** : 只能由字母、数字、_及$组成，且长度为0~63个字符，不能以数字开头。 **默认取值** : 不涉及。

        :param database_name: The database_name of this ShowSqlPatchRequest.
        :type database_name: str
        """
        self._database_name = database_name

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
        if not isinstance(other, ShowSqlPatchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
