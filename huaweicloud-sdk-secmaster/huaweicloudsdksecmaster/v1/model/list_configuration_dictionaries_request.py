# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConfigurationDictionariesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'x_language': 'str',
        'scene': 'str',
        'level': 'str',
        'scope': 'str',
        'dict_key': 'str',
        'is_built_in': 'bool',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'x_language': 'X-Language',
        'scene': 'scene',
        'level': 'level',
        'scope': 'scope',
        'dict_key': 'dict_key',
        'is_built_in': 'is_built_in',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, project_id=None, x_language=None, scene=None, level=None, scope=None, dict_key=None, is_built_in=None, offset=None, limit=None):
        r"""ListConfigurationDictionariesRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type project_id: str
        :param x_language: 用户当前语言环境
        :type x_language: str
        :param scene: 字典使用场景, 告警为ALERT, 等级云为QUAD_CLOUD
        :type scene: str
        :param level: 仅QUAD_CLOUD场景使用[S1, S2, S3, S4]
        :type level: str
        :param scope: 该字典作用域
        :type scope: str
        :param dict_key: 字典key
        :type dict_key: str
        :param is_built_in: 是否为系统内置字典数据,true：系统内置，false：自定义
        :type is_built_in: bool
        :param offset: 分页参数：返回起始偏移量
        :type offset: int
        :param limit: 分页参数：返回数据量大小
        :type limit: int
        """
        
        

        self._project_id = None
        self._x_language = None
        self._scene = None
        self._level = None
        self._scope = None
        self._dict_key = None
        self._is_built_in = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.project_id = project_id
        self.x_language = x_language
        if scene is not None:
            self.scene = scene
        if level is not None:
            self.level = level
        if scope is not None:
            self.scope = scope
        if dict_key is not None:
            self.dict_key = dict_key
        if is_built_in is not None:
            self.is_built_in = is_built_in
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def project_id(self):
        r"""Gets the project_id of this ListConfigurationDictionariesRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The project_id of this ListConfigurationDictionariesRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListConfigurationDictionariesRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param project_id: The project_id of this ListConfigurationDictionariesRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def x_language(self):
        r"""Gets the x_language of this ListConfigurationDictionariesRequest.

        用户当前语言环境

        :return: The x_language of this ListConfigurationDictionariesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListConfigurationDictionariesRequest.

        用户当前语言环境

        :param x_language: The x_language of this ListConfigurationDictionariesRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def scene(self):
        r"""Gets the scene of this ListConfigurationDictionariesRequest.

        字典使用场景, 告警为ALERT, 等级云为QUAD_CLOUD

        :return: The scene of this ListConfigurationDictionariesRequest.
        :rtype: str
        """
        return self._scene

    @scene.setter
    def scene(self, scene):
        r"""Sets the scene of this ListConfigurationDictionariesRequest.

        字典使用场景, 告警为ALERT, 等级云为QUAD_CLOUD

        :param scene: The scene of this ListConfigurationDictionariesRequest.
        :type scene: str
        """
        self._scene = scene

    @property
    def level(self):
        r"""Gets the level of this ListConfigurationDictionariesRequest.

        仅QUAD_CLOUD场景使用[S1, S2, S3, S4]

        :return: The level of this ListConfigurationDictionariesRequest.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this ListConfigurationDictionariesRequest.

        仅QUAD_CLOUD场景使用[S1, S2, S3, S4]

        :param level: The level of this ListConfigurationDictionariesRequest.
        :type level: str
        """
        self._level = level

    @property
    def scope(self):
        r"""Gets the scope of this ListConfigurationDictionariesRequest.

        该字典作用域

        :return: The scope of this ListConfigurationDictionariesRequest.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this ListConfigurationDictionariesRequest.

        该字典作用域

        :param scope: The scope of this ListConfigurationDictionariesRequest.
        :type scope: str
        """
        self._scope = scope

    @property
    def dict_key(self):
        r"""Gets the dict_key of this ListConfigurationDictionariesRequest.

        字典key

        :return: The dict_key of this ListConfigurationDictionariesRequest.
        :rtype: str
        """
        return self._dict_key

    @dict_key.setter
    def dict_key(self, dict_key):
        r"""Sets the dict_key of this ListConfigurationDictionariesRequest.

        字典key

        :param dict_key: The dict_key of this ListConfigurationDictionariesRequest.
        :type dict_key: str
        """
        self._dict_key = dict_key

    @property
    def is_built_in(self):
        r"""Gets the is_built_in of this ListConfigurationDictionariesRequest.

        是否为系统内置字典数据,true：系统内置，false：自定义

        :return: The is_built_in of this ListConfigurationDictionariesRequest.
        :rtype: bool
        """
        return self._is_built_in

    @is_built_in.setter
    def is_built_in(self, is_built_in):
        r"""Sets the is_built_in of this ListConfigurationDictionariesRequest.

        是否为系统内置字典数据,true：系统内置，false：自定义

        :param is_built_in: The is_built_in of this ListConfigurationDictionariesRequest.
        :type is_built_in: bool
        """
        self._is_built_in = is_built_in

    @property
    def offset(self):
        r"""Gets the offset of this ListConfigurationDictionariesRequest.

        分页参数：返回起始偏移量

        :return: The offset of this ListConfigurationDictionariesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListConfigurationDictionariesRequest.

        分页参数：返回起始偏移量

        :param offset: The offset of this ListConfigurationDictionariesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListConfigurationDictionariesRequest.

        分页参数：返回数据量大小

        :return: The limit of this ListConfigurationDictionariesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListConfigurationDictionariesRequest.

        分页参数：返回数据量大小

        :param limit: The limit of this ListConfigurationDictionariesRequest.
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
        if not isinstance(other, ListConfigurationDictionariesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
