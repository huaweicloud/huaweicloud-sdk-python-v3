# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Dictionary:

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
        'version': 'str',
        'dict_id': 'str',
        'dict_key': 'str',
        'dict_code': 'str',
        'dict_val': 'str',
        'dict_pkey': 'str',
        'dict_pcode': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'publish_time': 'str',
        'scope': 'str',
        'description': 'str',
        'extension_field': 'object',
        'project_id': 'str',
        'language': 'str'
    }

    attribute_map = {
        'id': 'id',
        'version': 'version',
        'dict_id': 'dict_id',
        'dict_key': 'dict_key',
        'dict_code': 'dict_code',
        'dict_val': 'dict_val',
        'dict_pkey': 'dict_pkey',
        'dict_pcode': 'dict_pcode',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'publish_time': 'publish_time',
        'scope': 'scope',
        'description': 'description',
        'extension_field': 'extension_field',
        'project_id': 'project_id',
        'language': 'language'
    }

    def __init__(self, id=None, version=None, dict_id=None, dict_key=None, dict_code=None, dict_val=None, dict_pkey=None, dict_pcode=None, create_time=None, update_time=None, publish_time=None, scope=None, description=None, extension_field=None, project_id=None, language=None):
        r"""Dictionary

        The model defined in huaweicloud sdk

        :param id: uuid
        :type id: str
        :param version: 版本号
        :type version: str
        :param dict_id: 字典id
        :type dict_id: str
        :param dict_key: 字典key
        :type dict_key: str
        :param dict_code: 字典code
        :type dict_code: str
        :param dict_val: 字典值
        :type dict_val: str
        :param dict_pkey: 字典关联的父key
        :type dict_pkey: str
        :param dict_pcode: 字典关联的父code
        :type dict_pcode: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        :param publish_time: 发布时间
        :type publish_time: str
        :param scope: 字典所属领域
        :type scope: str
        :param description: 字典描述信息
        :type description: str
        :param extension_field: 额外字段
        :type extension_field: object
        :param project_id: **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type project_id: str
        :param language: 用户当前语言环境
        :type language: str
        """
        
        

        self._id = None
        self._version = None
        self._dict_id = None
        self._dict_key = None
        self._dict_code = None
        self._dict_val = None
        self._dict_pkey = None
        self._dict_pcode = None
        self._create_time = None
        self._update_time = None
        self._publish_time = None
        self._scope = None
        self._description = None
        self._extension_field = None
        self._project_id = None
        self._language = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if version is not None:
            self.version = version
        if dict_id is not None:
            self.dict_id = dict_id
        if dict_key is not None:
            self.dict_key = dict_key
        if dict_code is not None:
            self.dict_code = dict_code
        if dict_val is not None:
            self.dict_val = dict_val
        if dict_pkey is not None:
            self.dict_pkey = dict_pkey
        if dict_pcode is not None:
            self.dict_pcode = dict_pcode
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if publish_time is not None:
            self.publish_time = publish_time
        if scope is not None:
            self.scope = scope
        if description is not None:
            self.description = description
        if extension_field is not None:
            self.extension_field = extension_field
        if project_id is not None:
            self.project_id = project_id
        if language is not None:
            self.language = language

    @property
    def id(self):
        r"""Gets the id of this Dictionary.

        uuid

        :return: The id of this Dictionary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Dictionary.

        uuid

        :param id: The id of this Dictionary.
        :type id: str
        """
        self._id = id

    @property
    def version(self):
        r"""Gets the version of this Dictionary.

        版本号

        :return: The version of this Dictionary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this Dictionary.

        版本号

        :param version: The version of this Dictionary.
        :type version: str
        """
        self._version = version

    @property
    def dict_id(self):
        r"""Gets the dict_id of this Dictionary.

        字典id

        :return: The dict_id of this Dictionary.
        :rtype: str
        """
        return self._dict_id

    @dict_id.setter
    def dict_id(self, dict_id):
        r"""Sets the dict_id of this Dictionary.

        字典id

        :param dict_id: The dict_id of this Dictionary.
        :type dict_id: str
        """
        self._dict_id = dict_id

    @property
    def dict_key(self):
        r"""Gets the dict_key of this Dictionary.

        字典key

        :return: The dict_key of this Dictionary.
        :rtype: str
        """
        return self._dict_key

    @dict_key.setter
    def dict_key(self, dict_key):
        r"""Sets the dict_key of this Dictionary.

        字典key

        :param dict_key: The dict_key of this Dictionary.
        :type dict_key: str
        """
        self._dict_key = dict_key

    @property
    def dict_code(self):
        r"""Gets the dict_code of this Dictionary.

        字典code

        :return: The dict_code of this Dictionary.
        :rtype: str
        """
        return self._dict_code

    @dict_code.setter
    def dict_code(self, dict_code):
        r"""Sets the dict_code of this Dictionary.

        字典code

        :param dict_code: The dict_code of this Dictionary.
        :type dict_code: str
        """
        self._dict_code = dict_code

    @property
    def dict_val(self):
        r"""Gets the dict_val of this Dictionary.

        字典值

        :return: The dict_val of this Dictionary.
        :rtype: str
        """
        return self._dict_val

    @dict_val.setter
    def dict_val(self, dict_val):
        r"""Sets the dict_val of this Dictionary.

        字典值

        :param dict_val: The dict_val of this Dictionary.
        :type dict_val: str
        """
        self._dict_val = dict_val

    @property
    def dict_pkey(self):
        r"""Gets the dict_pkey of this Dictionary.

        字典关联的父key

        :return: The dict_pkey of this Dictionary.
        :rtype: str
        """
        return self._dict_pkey

    @dict_pkey.setter
    def dict_pkey(self, dict_pkey):
        r"""Sets the dict_pkey of this Dictionary.

        字典关联的父key

        :param dict_pkey: The dict_pkey of this Dictionary.
        :type dict_pkey: str
        """
        self._dict_pkey = dict_pkey

    @property
    def dict_pcode(self):
        r"""Gets the dict_pcode of this Dictionary.

        字典关联的父code

        :return: The dict_pcode of this Dictionary.
        :rtype: str
        """
        return self._dict_pcode

    @dict_pcode.setter
    def dict_pcode(self, dict_pcode):
        r"""Sets the dict_pcode of this Dictionary.

        字典关联的父code

        :param dict_pcode: The dict_pcode of this Dictionary.
        :type dict_pcode: str
        """
        self._dict_pcode = dict_pcode

    @property
    def create_time(self):
        r"""Gets the create_time of this Dictionary.

        创建时间

        :return: The create_time of this Dictionary.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this Dictionary.

        创建时间

        :param create_time: The create_time of this Dictionary.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this Dictionary.

        更新时间

        :return: The update_time of this Dictionary.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this Dictionary.

        更新时间

        :param update_time: The update_time of this Dictionary.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def publish_time(self):
        r"""Gets the publish_time of this Dictionary.

        发布时间

        :return: The publish_time of this Dictionary.
        :rtype: str
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        r"""Sets the publish_time of this Dictionary.

        发布时间

        :param publish_time: The publish_time of this Dictionary.
        :type publish_time: str
        """
        self._publish_time = publish_time

    @property
    def scope(self):
        r"""Gets the scope of this Dictionary.

        字典所属领域

        :return: The scope of this Dictionary.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this Dictionary.

        字典所属领域

        :param scope: The scope of this Dictionary.
        :type scope: str
        """
        self._scope = scope

    @property
    def description(self):
        r"""Gets the description of this Dictionary.

        字典描述信息

        :return: The description of this Dictionary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Dictionary.

        字典描述信息

        :param description: The description of this Dictionary.
        :type description: str
        """
        self._description = description

    @property
    def extension_field(self):
        r"""Gets the extension_field of this Dictionary.

        额外字段

        :return: The extension_field of this Dictionary.
        :rtype: object
        """
        return self._extension_field

    @extension_field.setter
    def extension_field(self, extension_field):
        r"""Sets the extension_field of this Dictionary.

        额外字段

        :param extension_field: The extension_field of this Dictionary.
        :type extension_field: object
        """
        self._extension_field = extension_field

    @property
    def project_id(self):
        r"""Gets the project_id of this Dictionary.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The project_id of this Dictionary.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this Dictionary.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param project_id: The project_id of this Dictionary.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def language(self):
        r"""Gets the language of this Dictionary.

        用户当前语言环境

        :return: The language of this Dictionary.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this Dictionary.

        用户当前语言环境

        :param language: The language of this Dictionary.
        :type language: str
        """
        self._language = language

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
        if not isinstance(other, Dictionary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
