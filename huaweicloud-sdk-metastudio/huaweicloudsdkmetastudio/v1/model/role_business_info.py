# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RoleBusinessInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'role_business_id': 'str',
        'role_id': 'str',
        'language': 'LanguageEnum',
        'prompt': 'str',
        'knowledge_library_list': 'list[RoleKnowledgeLibraryInfo]',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'role_business_id': 'role_business_id',
        'role_id': 'role_id',
        'language': 'language',
        'prompt': 'prompt',
        'knowledge_library_list': 'knowledge_library_list',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, role_business_id=None, role_id=None, language=None, prompt=None, knowledge_library_list=None, create_time=None, update_time=None):
        r"""RoleBusinessInfo

        The model defined in huaweicloud sdk

        :param role_business_id: 角色业务配置ID。
        :type role_business_id: str
        :param role_id: 角色ID。
        :type role_id: str
        :param language: 
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        :param prompt: 提示词。
        :type prompt: str
        :param knowledge_library_list: 知识库列表
        :type knowledge_library_list: list[:class:`huaweicloudsdkmetastudio.v1.RoleKnowledgeLibraryInfo`]
        :param create_time: 创建时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type create_time: str
        :param update_time: 更新时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type update_time: str
        """
        
        

        self._role_business_id = None
        self._role_id = None
        self._language = None
        self._prompt = None
        self._knowledge_library_list = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if role_business_id is not None:
            self.role_business_id = role_business_id
        if role_id is not None:
            self.role_id = role_id
        if language is not None:
            self.language = language
        if prompt is not None:
            self.prompt = prompt
        if knowledge_library_list is not None:
            self.knowledge_library_list = knowledge_library_list
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def role_business_id(self):
        r"""Gets the role_business_id of this RoleBusinessInfo.

        角色业务配置ID。

        :return: The role_business_id of this RoleBusinessInfo.
        :rtype: str
        """
        return self._role_business_id

    @role_business_id.setter
    def role_business_id(self, role_business_id):
        r"""Sets the role_business_id of this RoleBusinessInfo.

        角色业务配置ID。

        :param role_business_id: The role_business_id of this RoleBusinessInfo.
        :type role_business_id: str
        """
        self._role_business_id = role_business_id

    @property
    def role_id(self):
        r"""Gets the role_id of this RoleBusinessInfo.

        角色ID。

        :return: The role_id of this RoleBusinessInfo.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        r"""Sets the role_id of this RoleBusinessInfo.

        角色ID。

        :param role_id: The role_id of this RoleBusinessInfo.
        :type role_id: str
        """
        self._role_id = role_id

    @property
    def language(self):
        r"""Gets the language of this RoleBusinessInfo.

        :return: The language of this RoleBusinessInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this RoleBusinessInfo.

        :param language: The language of this RoleBusinessInfo.
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        self._language = language

    @property
    def prompt(self):
        r"""Gets the prompt of this RoleBusinessInfo.

        提示词。

        :return: The prompt of this RoleBusinessInfo.
        :rtype: str
        """
        return self._prompt

    @prompt.setter
    def prompt(self, prompt):
        r"""Sets the prompt of this RoleBusinessInfo.

        提示词。

        :param prompt: The prompt of this RoleBusinessInfo.
        :type prompt: str
        """
        self._prompt = prompt

    @property
    def knowledge_library_list(self):
        r"""Gets the knowledge_library_list of this RoleBusinessInfo.

        知识库列表

        :return: The knowledge_library_list of this RoleBusinessInfo.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.RoleKnowledgeLibraryInfo`]
        """
        return self._knowledge_library_list

    @knowledge_library_list.setter
    def knowledge_library_list(self, knowledge_library_list):
        r"""Sets the knowledge_library_list of this RoleBusinessInfo.

        知识库列表

        :param knowledge_library_list: The knowledge_library_list of this RoleBusinessInfo.
        :type knowledge_library_list: list[:class:`huaweicloudsdkmetastudio.v1.RoleKnowledgeLibraryInfo`]
        """
        self._knowledge_library_list = knowledge_library_list

    @property
    def create_time(self):
        r"""Gets the create_time of this RoleBusinessInfo.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The create_time of this RoleBusinessInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this RoleBusinessInfo.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param create_time: The create_time of this RoleBusinessInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this RoleBusinessInfo.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The update_time of this RoleBusinessInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this RoleBusinessInfo.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param update_time: The update_time of this RoleBusinessInfo.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, RoleBusinessInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
