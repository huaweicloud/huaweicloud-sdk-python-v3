# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlgorithmResponseMetadata:

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
        'name': 'str',
        'description': 'str',
        'workspace_id': 'str',
        'ai_project': 'str',
        'user_name': 'str',
        'domain_id': 'str',
        'source': 'str',
        'api_version': 'str',
        'is_valid': 'bool',
        'state': 'str',
        'tags': 'list[dict(str, str)]',
        'attr_list': 'list[str]',
        'version_num': 'int',
        'size': 'int',
        'create_time': 'int',
        'update_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'workspace_id': 'workspace_id',
        'ai_project': 'ai_project',
        'user_name': 'user_name',
        'domain_id': 'domain_id',
        'source': 'source',
        'api_version': 'api_version',
        'is_valid': 'is_valid',
        'state': 'state',
        'tags': 'tags',
        'attr_list': 'attr_list',
        'version_num': 'version_num',
        'size': 'size',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, description=None, workspace_id=None, ai_project=None, user_name=None, domain_id=None, source=None, api_version=None, is_valid=None, state=None, tags=None, attr_list=None, version_num=None, size=None, create_time=None, update_time=None):
        r"""AlgorithmResponseMetadata

        The model defined in huaweicloud sdk

        :param id: **参数解释**：算法id，创建算法时无需填写。 **取值范围**：不涉及。
        :type id: str
        :param name: 算法名称。限制为1-64位只含数字、字母、下划线和中划线的名称。
        :type name: str
        :param description: 对算法的描述，默认为“NULL”，字符串的长度限制为[0, 256]。
        :type description: str
        :param workspace_id: 指定算法所处的工作空间，默认值为“0”。“0” 为默认的工作空间。
        :type workspace_id: str
        :param ai_project: 指定算法所属的ai项目，默认值为\&quot;default-ai-project\&quot;。ai项目已下线，无需关注。
        :type ai_project: str
        :param user_name: 用户名称。
        :type user_name: str
        :param domain_id: 用户的domainID。
        :type domain_id: str
        :param source: 算法来源类型。
        :type source: str
        :param api_version: 算法api版本，标识新旧版。
        :type api_version: str
        :param is_valid: **参数解释**：算法可用性。 **取值范围**： - true：可用 - false：不可用
        :type is_valid: bool
        :param state: 算法状态。
        :type state: str
        :param tags: 算法标签。
        :type tags: list[dict(str, str)]
        :param attr_list: 算法属性列表。
        :type attr_list: list[str]
        :param version_num: 算法版本数量，默认为0。
        :type version_num: int
        :param size: 算法大小。
        :type size: int
        :param create_time: 算法创建时间戳。
        :type create_time: int
        :param update_time: 算法更新时间戳。
        :type update_time: int
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._workspace_id = None
        self._ai_project = None
        self._user_name = None
        self._domain_id = None
        self._source = None
        self._api_version = None
        self._is_valid = None
        self._state = None
        self._tags = None
        self._attr_list = None
        self._version_num = None
        self._size = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if description is not None:
            self.description = description
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if ai_project is not None:
            self.ai_project = ai_project
        if user_name is not None:
            self.user_name = user_name
        if domain_id is not None:
            self.domain_id = domain_id
        if source is not None:
            self.source = source
        if api_version is not None:
            self.api_version = api_version
        if is_valid is not None:
            self.is_valid = is_valid
        if state is not None:
            self.state = state
        if tags is not None:
            self.tags = tags
        if attr_list is not None:
            self.attr_list = attr_list
        if version_num is not None:
            self.version_num = version_num
        if size is not None:
            self.size = size
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this AlgorithmResponseMetadata.

        **参数解释**：算法id，创建算法时无需填写。 **取值范围**：不涉及。

        :return: The id of this AlgorithmResponseMetadata.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AlgorithmResponseMetadata.

        **参数解释**：算法id，创建算法时无需填写。 **取值范围**：不涉及。

        :param id: The id of this AlgorithmResponseMetadata.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this AlgorithmResponseMetadata.

        算法名称。限制为1-64位只含数字、字母、下划线和中划线的名称。

        :return: The name of this AlgorithmResponseMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AlgorithmResponseMetadata.

        算法名称。限制为1-64位只含数字、字母、下划线和中划线的名称。

        :param name: The name of this AlgorithmResponseMetadata.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this AlgorithmResponseMetadata.

        对算法的描述，默认为“NULL”，字符串的长度限制为[0, 256]。

        :return: The description of this AlgorithmResponseMetadata.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AlgorithmResponseMetadata.

        对算法的描述，默认为“NULL”，字符串的长度限制为[0, 256]。

        :param description: The description of this AlgorithmResponseMetadata.
        :type description: str
        """
        self._description = description

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this AlgorithmResponseMetadata.

        指定算法所处的工作空间，默认值为“0”。“0” 为默认的工作空间。

        :return: The workspace_id of this AlgorithmResponseMetadata.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this AlgorithmResponseMetadata.

        指定算法所处的工作空间，默认值为“0”。“0” 为默认的工作空间。

        :param workspace_id: The workspace_id of this AlgorithmResponseMetadata.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def ai_project(self):
        r"""Gets the ai_project of this AlgorithmResponseMetadata.

        指定算法所属的ai项目，默认值为\"default-ai-project\"。ai项目已下线，无需关注。

        :return: The ai_project of this AlgorithmResponseMetadata.
        :rtype: str
        """
        return self._ai_project

    @ai_project.setter
    def ai_project(self, ai_project):
        r"""Sets the ai_project of this AlgorithmResponseMetadata.

        指定算法所属的ai项目，默认值为\"default-ai-project\"。ai项目已下线，无需关注。

        :param ai_project: The ai_project of this AlgorithmResponseMetadata.
        :type ai_project: str
        """
        self._ai_project = ai_project

    @property
    def user_name(self):
        r"""Gets the user_name of this AlgorithmResponseMetadata.

        用户名称。

        :return: The user_name of this AlgorithmResponseMetadata.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this AlgorithmResponseMetadata.

        用户名称。

        :param user_name: The user_name of this AlgorithmResponseMetadata.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def domain_id(self):
        r"""Gets the domain_id of this AlgorithmResponseMetadata.

        用户的domainID。

        :return: The domain_id of this AlgorithmResponseMetadata.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this AlgorithmResponseMetadata.

        用户的domainID。

        :param domain_id: The domain_id of this AlgorithmResponseMetadata.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def source(self):
        r"""Gets the source of this AlgorithmResponseMetadata.

        算法来源类型。

        :return: The source of this AlgorithmResponseMetadata.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this AlgorithmResponseMetadata.

        算法来源类型。

        :param source: The source of this AlgorithmResponseMetadata.
        :type source: str
        """
        self._source = source

    @property
    def api_version(self):
        r"""Gets the api_version of this AlgorithmResponseMetadata.

        算法api版本，标识新旧版。

        :return: The api_version of this AlgorithmResponseMetadata.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this AlgorithmResponseMetadata.

        算法api版本，标识新旧版。

        :param api_version: The api_version of this AlgorithmResponseMetadata.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def is_valid(self):
        r"""Gets the is_valid of this AlgorithmResponseMetadata.

        **参数解释**：算法可用性。 **取值范围**： - true：可用 - false：不可用

        :return: The is_valid of this AlgorithmResponseMetadata.
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        r"""Sets the is_valid of this AlgorithmResponseMetadata.

        **参数解释**：算法可用性。 **取值范围**： - true：可用 - false：不可用

        :param is_valid: The is_valid of this AlgorithmResponseMetadata.
        :type is_valid: bool
        """
        self._is_valid = is_valid

    @property
    def state(self):
        r"""Gets the state of this AlgorithmResponseMetadata.

        算法状态。

        :return: The state of this AlgorithmResponseMetadata.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this AlgorithmResponseMetadata.

        算法状态。

        :param state: The state of this AlgorithmResponseMetadata.
        :type state: str
        """
        self._state = state

    @property
    def tags(self):
        r"""Gets the tags of this AlgorithmResponseMetadata.

        算法标签。

        :return: The tags of this AlgorithmResponseMetadata.
        :rtype: list[dict(str, str)]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this AlgorithmResponseMetadata.

        算法标签。

        :param tags: The tags of this AlgorithmResponseMetadata.
        :type tags: list[dict(str, str)]
        """
        self._tags = tags

    @property
    def attr_list(self):
        r"""Gets the attr_list of this AlgorithmResponseMetadata.

        算法属性列表。

        :return: The attr_list of this AlgorithmResponseMetadata.
        :rtype: list[str]
        """
        return self._attr_list

    @attr_list.setter
    def attr_list(self, attr_list):
        r"""Sets the attr_list of this AlgorithmResponseMetadata.

        算法属性列表。

        :param attr_list: The attr_list of this AlgorithmResponseMetadata.
        :type attr_list: list[str]
        """
        self._attr_list = attr_list

    @property
    def version_num(self):
        r"""Gets the version_num of this AlgorithmResponseMetadata.

        算法版本数量，默认为0。

        :return: The version_num of this AlgorithmResponseMetadata.
        :rtype: int
        """
        return self._version_num

    @version_num.setter
    def version_num(self, version_num):
        r"""Sets the version_num of this AlgorithmResponseMetadata.

        算法版本数量，默认为0。

        :param version_num: The version_num of this AlgorithmResponseMetadata.
        :type version_num: int
        """
        self._version_num = version_num

    @property
    def size(self):
        r"""Gets the size of this AlgorithmResponseMetadata.

        算法大小。

        :return: The size of this AlgorithmResponseMetadata.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this AlgorithmResponseMetadata.

        算法大小。

        :param size: The size of this AlgorithmResponseMetadata.
        :type size: int
        """
        self._size = size

    @property
    def create_time(self):
        r"""Gets the create_time of this AlgorithmResponseMetadata.

        算法创建时间戳。

        :return: The create_time of this AlgorithmResponseMetadata.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AlgorithmResponseMetadata.

        算法创建时间戳。

        :param create_time: The create_time of this AlgorithmResponseMetadata.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this AlgorithmResponseMetadata.

        算法更新时间戳。

        :return: The update_time of this AlgorithmResponseMetadata.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AlgorithmResponseMetadata.

        算法更新时间戳。

        :param update_time: The update_time of this AlgorithmResponseMetadata.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, AlgorithmResponseMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
