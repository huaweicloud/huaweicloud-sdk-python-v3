# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepositoryTemplateDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repository_id': 'int',
        'name': 'str',
        'system': 'bool',
        'tags': 'list[str]',
        'description': 'str',
        'language': 'str',
        'repository_name': 'str',
        'brief_introduction': 'str',
        'created_at': 'str',
        'used_times': 'int',
        'liked_times': 'int',
        'creator_name': 'str',
        'https_url': 'str'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'name': 'name',
        'system': 'system',
        'tags': 'tags',
        'description': 'description',
        'language': 'language',
        'repository_name': 'repository_name',
        'brief_introduction': 'brief_introduction',
        'created_at': 'created_at',
        'used_times': 'used_times',
        'liked_times': 'liked_times',
        'creator_name': 'creator_name',
        'https_url': 'https_url'
    }

    def __init__(self, repository_id=None, name=None, system=None, tags=None, description=None, language=None, repository_name=None, brief_introduction=None, created_at=None, used_times=None, liked_times=None, creator_name=None, https_url=None):
        r"""RepositoryTemplateDto

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库Id。
        :type repository_id: int
        :param name: **参数解释：** 模板仓标题。 **取值范围：** 字符串长度1-50。
        :type name: str
        :param system: **参数解释：** 是否是系统模版。 **取值范围：** - true，系统模版。 - false，个人模版。
        :type system: bool
        :param tags: **参数解释：** 标签列表。 **取值范围：** 不涉及。
        :type tags: list[str]
        :param description: **参数解释：** 仓库描述信息。 **取值范围：** 字符串长度0-2000。
        :type description: str
        :param language: **参数解释：** 编程语言。 **取值范围：** 字符串长度0-32。
        :type language: str
        :param repository_name: **参数解释：** 模板仓的仓库名称。 **取值范围：** 字符串长度0-255。
        :type repository_name: str
        :param brief_introduction: **参数解释：** 模板仓的简介。 **取值范围：** 字符串长度0-32。
        :type brief_introduction: str
        :param created_at: **参数解释：** 创建时间。
        :type created_at: str
        :param used_times: **参数解释：** 模板仓被使用的次数。
        :type used_times: int
        :param liked_times: **参数解释：** 模板仓被点赞的次数。
        :type liked_times: int
        :param creator_name: **参数解释：** 作者。 **取值范围：** 字符串长度0-128。
        :type creator_name: str
        :param https_url: **参数解释：** 代码仓https协议的git地址。 **取值范围：** 字符串最大长度512。
        :type https_url: str
        """
        
        

        self._repository_id = None
        self._name = None
        self._system = None
        self._tags = None
        self._description = None
        self._language = None
        self._repository_name = None
        self._brief_introduction = None
        self._created_at = None
        self._used_times = None
        self._liked_times = None
        self._creator_name = None
        self._https_url = None
        self.discriminator = None

        if repository_id is not None:
            self.repository_id = repository_id
        if name is not None:
            self.name = name
        if system is not None:
            self.system = system
        if tags is not None:
            self.tags = tags
        if description is not None:
            self.description = description
        if language is not None:
            self.language = language
        if repository_name is not None:
            self.repository_name = repository_name
        if brief_introduction is not None:
            self.brief_introduction = brief_introduction
        if created_at is not None:
            self.created_at = created_at
        if used_times is not None:
            self.used_times = used_times
        if liked_times is not None:
            self.liked_times = liked_times
        if creator_name is not None:
            self.creator_name = creator_name
        if https_url is not None:
            self.https_url = https_url

    @property
    def repository_id(self):
        r"""Gets the repository_id of this RepositoryTemplateDto.

        **参数解释：** 仓库Id。

        :return: The repository_id of this RepositoryTemplateDto.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this RepositoryTemplateDto.

        **参数解释：** 仓库Id。

        :param repository_id: The repository_id of this RepositoryTemplateDto.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def name(self):
        r"""Gets the name of this RepositoryTemplateDto.

        **参数解释：** 模板仓标题。 **取值范围：** 字符串长度1-50。

        :return: The name of this RepositoryTemplateDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RepositoryTemplateDto.

        **参数解释：** 模板仓标题。 **取值范围：** 字符串长度1-50。

        :param name: The name of this RepositoryTemplateDto.
        :type name: str
        """
        self._name = name

    @property
    def system(self):
        r"""Gets the system of this RepositoryTemplateDto.

        **参数解释：** 是否是系统模版。 **取值范围：** - true，系统模版。 - false，个人模版。

        :return: The system of this RepositoryTemplateDto.
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        r"""Sets the system of this RepositoryTemplateDto.

        **参数解释：** 是否是系统模版。 **取值范围：** - true，系统模版。 - false，个人模版。

        :param system: The system of this RepositoryTemplateDto.
        :type system: bool
        """
        self._system = system

    @property
    def tags(self):
        r"""Gets the tags of this RepositoryTemplateDto.

        **参数解释：** 标签列表。 **取值范围：** 不涉及。

        :return: The tags of this RepositoryTemplateDto.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this RepositoryTemplateDto.

        **参数解释：** 标签列表。 **取值范围：** 不涉及。

        :param tags: The tags of this RepositoryTemplateDto.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def description(self):
        r"""Gets the description of this RepositoryTemplateDto.

        **参数解释：** 仓库描述信息。 **取值范围：** 字符串长度0-2000。

        :return: The description of this RepositoryTemplateDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RepositoryTemplateDto.

        **参数解释：** 仓库描述信息。 **取值范围：** 字符串长度0-2000。

        :param description: The description of this RepositoryTemplateDto.
        :type description: str
        """
        self._description = description

    @property
    def language(self):
        r"""Gets the language of this RepositoryTemplateDto.

        **参数解释：** 编程语言。 **取值范围：** 字符串长度0-32。

        :return: The language of this RepositoryTemplateDto.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this RepositoryTemplateDto.

        **参数解释：** 编程语言。 **取值范围：** 字符串长度0-32。

        :param language: The language of this RepositoryTemplateDto.
        :type language: str
        """
        self._language = language

    @property
    def repository_name(self):
        r"""Gets the repository_name of this RepositoryTemplateDto.

        **参数解释：** 模板仓的仓库名称。 **取值范围：** 字符串长度0-255。

        :return: The repository_name of this RepositoryTemplateDto.
        :rtype: str
        """
        return self._repository_name

    @repository_name.setter
    def repository_name(self, repository_name):
        r"""Sets the repository_name of this RepositoryTemplateDto.

        **参数解释：** 模板仓的仓库名称。 **取值范围：** 字符串长度0-255。

        :param repository_name: The repository_name of this RepositoryTemplateDto.
        :type repository_name: str
        """
        self._repository_name = repository_name

    @property
    def brief_introduction(self):
        r"""Gets the brief_introduction of this RepositoryTemplateDto.

        **参数解释：** 模板仓的简介。 **取值范围：** 字符串长度0-32。

        :return: The brief_introduction of this RepositoryTemplateDto.
        :rtype: str
        """
        return self._brief_introduction

    @brief_introduction.setter
    def brief_introduction(self, brief_introduction):
        r"""Sets the brief_introduction of this RepositoryTemplateDto.

        **参数解释：** 模板仓的简介。 **取值范围：** 字符串长度0-32。

        :param brief_introduction: The brief_introduction of this RepositoryTemplateDto.
        :type brief_introduction: str
        """
        self._brief_introduction = brief_introduction

    @property
    def created_at(self):
        r"""Gets the created_at of this RepositoryTemplateDto.

        **参数解释：** 创建时间。

        :return: The created_at of this RepositoryTemplateDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this RepositoryTemplateDto.

        **参数解释：** 创建时间。

        :param created_at: The created_at of this RepositoryTemplateDto.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def used_times(self):
        r"""Gets the used_times of this RepositoryTemplateDto.

        **参数解释：** 模板仓被使用的次数。

        :return: The used_times of this RepositoryTemplateDto.
        :rtype: int
        """
        return self._used_times

    @used_times.setter
    def used_times(self, used_times):
        r"""Sets the used_times of this RepositoryTemplateDto.

        **参数解释：** 模板仓被使用的次数。

        :param used_times: The used_times of this RepositoryTemplateDto.
        :type used_times: int
        """
        self._used_times = used_times

    @property
    def liked_times(self):
        r"""Gets the liked_times of this RepositoryTemplateDto.

        **参数解释：** 模板仓被点赞的次数。

        :return: The liked_times of this RepositoryTemplateDto.
        :rtype: int
        """
        return self._liked_times

    @liked_times.setter
    def liked_times(self, liked_times):
        r"""Sets the liked_times of this RepositoryTemplateDto.

        **参数解释：** 模板仓被点赞的次数。

        :param liked_times: The liked_times of this RepositoryTemplateDto.
        :type liked_times: int
        """
        self._liked_times = liked_times

    @property
    def creator_name(self):
        r"""Gets the creator_name of this RepositoryTemplateDto.

        **参数解释：** 作者。 **取值范围：** 字符串长度0-128。

        :return: The creator_name of this RepositoryTemplateDto.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this RepositoryTemplateDto.

        **参数解释：** 作者。 **取值范围：** 字符串长度0-128。

        :param creator_name: The creator_name of this RepositoryTemplateDto.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def https_url(self):
        r"""Gets the https_url of this RepositoryTemplateDto.

        **参数解释：** 代码仓https协议的git地址。 **取值范围：** 字符串最大长度512。

        :return: The https_url of this RepositoryTemplateDto.
        :rtype: str
        """
        return self._https_url

    @https_url.setter
    def https_url(self, https_url):
        r"""Sets the https_url of this RepositoryTemplateDto.

        **参数解释：** 代码仓https协议的git地址。 **取值范围：** 字符串最大长度512。

        :param https_url: The https_url of this RepositoryTemplateDto.
        :type https_url: str
        """
        self._https_url = https_url

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
        if not isinstance(other, RepositoryTemplateDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
