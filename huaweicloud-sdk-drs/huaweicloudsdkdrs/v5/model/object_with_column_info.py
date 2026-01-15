# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObjectWithColumnInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'parent_id': 'str',
        'type': 'str',
        'name': 'str',
        'alias_name': 'str',
        'notices': 'list[str]',
        'extend_info': 'str',
        'is_support_expand': 'bool',
        'has_column_info': 'bool',
        'is_preset': 'bool',
        'token_count': 'str',
        'is_sent': 'bool',
        'sent_alias_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'parent_id': 'parent_id',
        'type': 'type',
        'name': 'name',
        'alias_name': 'alias_name',
        'notices': 'notices',
        'extend_info': 'extend_info',
        'is_support_expand': 'is_support_expand',
        'has_column_info': 'has_column_info',
        'is_preset': 'is_preset',
        'token_count': 'token_count',
        'is_sent': 'is_sent',
        'sent_alias_name': 'sent_alias_name'
    }

    def __init__(self, id=None, parent_id=None, type=None, name=None, alias_name=None, notices=None, extend_info=None, is_support_expand=None, has_column_info=None, is_preset=None, token_count=None, is_sent=None, sent_alias_name=None):
        r"""ObjectWithColumnInfo

        The model defined in huaweicloud sdk

        :param id: 本节点id
        :type id: str
        :param parent_id: 父节点id
        :type parent_id: str
        :param type: 节点类型
        :type type: str
        :param name: 节点名称
        :type name: str
        :param alias_name: 节点别名
        :type alias_name: str
        :param notices: 提示信息，例如提示库下表过多
        :type notices: list[str]
        :param extend_info: 扩展信息，例如提示有无数据,结构是否在目标库中存在
        :type extend_info: str
        :param is_support_expand: 是否支持展开查询
        :type is_support_expand: bool
        :param has_column_info: 是否有列信息
        :type has_column_info: bool
        :param is_preset: 是否预置
        :type is_preset: bool
        :param token_count: token个数
        :type token_count: str
        :param is_sent: 是否已经下发给node
        :type is_sent: bool
        :param sent_alias_name: 下发给node的别名
        :type sent_alias_name: str
        """
        
        

        self._id = None
        self._parent_id = None
        self._type = None
        self._name = None
        self._alias_name = None
        self._notices = None
        self._extend_info = None
        self._is_support_expand = None
        self._has_column_info = None
        self._is_preset = None
        self._token_count = None
        self._is_sent = None
        self._sent_alias_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if parent_id is not None:
            self.parent_id = parent_id
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if alias_name is not None:
            self.alias_name = alias_name
        if notices is not None:
            self.notices = notices
        if extend_info is not None:
            self.extend_info = extend_info
        if is_support_expand is not None:
            self.is_support_expand = is_support_expand
        if has_column_info is not None:
            self.has_column_info = has_column_info
        if is_preset is not None:
            self.is_preset = is_preset
        if token_count is not None:
            self.token_count = token_count
        if is_sent is not None:
            self.is_sent = is_sent
        if sent_alias_name is not None:
            self.sent_alias_name = sent_alias_name

    @property
    def id(self):
        r"""Gets the id of this ObjectWithColumnInfo.

        本节点id

        :return: The id of this ObjectWithColumnInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ObjectWithColumnInfo.

        本节点id

        :param id: The id of this ObjectWithColumnInfo.
        :type id: str
        """
        self._id = id

    @property
    def parent_id(self):
        r"""Gets the parent_id of this ObjectWithColumnInfo.

        父节点id

        :return: The parent_id of this ObjectWithColumnInfo.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this ObjectWithColumnInfo.

        父节点id

        :param parent_id: The parent_id of this ObjectWithColumnInfo.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def type(self):
        r"""Gets the type of this ObjectWithColumnInfo.

        节点类型

        :return: The type of this ObjectWithColumnInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ObjectWithColumnInfo.

        节点类型

        :param type: The type of this ObjectWithColumnInfo.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        r"""Gets the name of this ObjectWithColumnInfo.

        节点名称

        :return: The name of this ObjectWithColumnInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ObjectWithColumnInfo.

        节点名称

        :param name: The name of this ObjectWithColumnInfo.
        :type name: str
        """
        self._name = name

    @property
    def alias_name(self):
        r"""Gets the alias_name of this ObjectWithColumnInfo.

        节点别名

        :return: The alias_name of this ObjectWithColumnInfo.
        :rtype: str
        """
        return self._alias_name

    @alias_name.setter
    def alias_name(self, alias_name):
        r"""Sets the alias_name of this ObjectWithColumnInfo.

        节点别名

        :param alias_name: The alias_name of this ObjectWithColumnInfo.
        :type alias_name: str
        """
        self._alias_name = alias_name

    @property
    def notices(self):
        r"""Gets the notices of this ObjectWithColumnInfo.

        提示信息，例如提示库下表过多

        :return: The notices of this ObjectWithColumnInfo.
        :rtype: list[str]
        """
        return self._notices

    @notices.setter
    def notices(self, notices):
        r"""Sets the notices of this ObjectWithColumnInfo.

        提示信息，例如提示库下表过多

        :param notices: The notices of this ObjectWithColumnInfo.
        :type notices: list[str]
        """
        self._notices = notices

    @property
    def extend_info(self):
        r"""Gets the extend_info of this ObjectWithColumnInfo.

        扩展信息，例如提示有无数据,结构是否在目标库中存在

        :return: The extend_info of this ObjectWithColumnInfo.
        :rtype: str
        """
        return self._extend_info

    @extend_info.setter
    def extend_info(self, extend_info):
        r"""Sets the extend_info of this ObjectWithColumnInfo.

        扩展信息，例如提示有无数据,结构是否在目标库中存在

        :param extend_info: The extend_info of this ObjectWithColumnInfo.
        :type extend_info: str
        """
        self._extend_info = extend_info

    @property
    def is_support_expand(self):
        r"""Gets the is_support_expand of this ObjectWithColumnInfo.

        是否支持展开查询

        :return: The is_support_expand of this ObjectWithColumnInfo.
        :rtype: bool
        """
        return self._is_support_expand

    @is_support_expand.setter
    def is_support_expand(self, is_support_expand):
        r"""Sets the is_support_expand of this ObjectWithColumnInfo.

        是否支持展开查询

        :param is_support_expand: The is_support_expand of this ObjectWithColumnInfo.
        :type is_support_expand: bool
        """
        self._is_support_expand = is_support_expand

    @property
    def has_column_info(self):
        r"""Gets the has_column_info of this ObjectWithColumnInfo.

        是否有列信息

        :return: The has_column_info of this ObjectWithColumnInfo.
        :rtype: bool
        """
        return self._has_column_info

    @has_column_info.setter
    def has_column_info(self, has_column_info):
        r"""Sets the has_column_info of this ObjectWithColumnInfo.

        是否有列信息

        :param has_column_info: The has_column_info of this ObjectWithColumnInfo.
        :type has_column_info: bool
        """
        self._has_column_info = has_column_info

    @property
    def is_preset(self):
        r"""Gets the is_preset of this ObjectWithColumnInfo.

        是否预置

        :return: The is_preset of this ObjectWithColumnInfo.
        :rtype: bool
        """
        return self._is_preset

    @is_preset.setter
    def is_preset(self, is_preset):
        r"""Sets the is_preset of this ObjectWithColumnInfo.

        是否预置

        :param is_preset: The is_preset of this ObjectWithColumnInfo.
        :type is_preset: bool
        """
        self._is_preset = is_preset

    @property
    def token_count(self):
        r"""Gets the token_count of this ObjectWithColumnInfo.

        token个数

        :return: The token_count of this ObjectWithColumnInfo.
        :rtype: str
        """
        return self._token_count

    @token_count.setter
    def token_count(self, token_count):
        r"""Sets the token_count of this ObjectWithColumnInfo.

        token个数

        :param token_count: The token_count of this ObjectWithColumnInfo.
        :type token_count: str
        """
        self._token_count = token_count

    @property
    def is_sent(self):
        r"""Gets the is_sent of this ObjectWithColumnInfo.

        是否已经下发给node

        :return: The is_sent of this ObjectWithColumnInfo.
        :rtype: bool
        """
        return self._is_sent

    @is_sent.setter
    def is_sent(self, is_sent):
        r"""Sets the is_sent of this ObjectWithColumnInfo.

        是否已经下发给node

        :param is_sent: The is_sent of this ObjectWithColumnInfo.
        :type is_sent: bool
        """
        self._is_sent = is_sent

    @property
    def sent_alias_name(self):
        r"""Gets the sent_alias_name of this ObjectWithColumnInfo.

        下发给node的别名

        :return: The sent_alias_name of this ObjectWithColumnInfo.
        :rtype: str
        """
        return self._sent_alias_name

    @sent_alias_name.setter
    def sent_alias_name(self, sent_alias_name):
        r"""Sets the sent_alias_name of this ObjectWithColumnInfo.

        下发给node的别名

        :param sent_alias_name: The sent_alias_name of this ObjectWithColumnInfo.
        :type sent_alias_name: str
        """
        self._sent_alias_name = sent_alias_name

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
        if not isinstance(other, ObjectWithColumnInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
