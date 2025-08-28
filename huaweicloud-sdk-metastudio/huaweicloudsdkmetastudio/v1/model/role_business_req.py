# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RoleBusinessReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'language': 'LanguageEnum',
        'prompt': 'str',
        'knowledge_library_list': 'list[RoleKnowledgeLibraryReq]'
    }

    attribute_map = {
        'language': 'language',
        'prompt': 'prompt',
        'knowledge_library_list': 'knowledge_library_list'
    }

    def __init__(self, language=None, prompt=None, knowledge_library_list=None):
        r"""RoleBusinessReq

        The model defined in huaweicloud sdk

        :param language: 
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        :param prompt: 提示词。
        :type prompt: str
        :param knowledge_library_list: 知识库列表
        :type knowledge_library_list: list[:class:`huaweicloudsdkmetastudio.v1.RoleKnowledgeLibraryReq`]
        """
        
        

        self._language = None
        self._prompt = None
        self._knowledge_library_list = None
        self.discriminator = None

        self.language = language
        if prompt is not None:
            self.prompt = prompt
        if knowledge_library_list is not None:
            self.knowledge_library_list = knowledge_library_list

    @property
    def language(self):
        r"""Gets the language of this RoleBusinessReq.

        :return: The language of this RoleBusinessReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this RoleBusinessReq.

        :param language: The language of this RoleBusinessReq.
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        self._language = language

    @property
    def prompt(self):
        r"""Gets the prompt of this RoleBusinessReq.

        提示词。

        :return: The prompt of this RoleBusinessReq.
        :rtype: str
        """
        return self._prompt

    @prompt.setter
    def prompt(self, prompt):
        r"""Sets the prompt of this RoleBusinessReq.

        提示词。

        :param prompt: The prompt of this RoleBusinessReq.
        :type prompt: str
        """
        self._prompt = prompt

    @property
    def knowledge_library_list(self):
        r"""Gets the knowledge_library_list of this RoleBusinessReq.

        知识库列表

        :return: The knowledge_library_list of this RoleBusinessReq.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.RoleKnowledgeLibraryReq`]
        """
        return self._knowledge_library_list

    @knowledge_library_list.setter
    def knowledge_library_list(self, knowledge_library_list):
        r"""Sets the knowledge_library_list of this RoleBusinessReq.

        知识库列表

        :param knowledge_library_list: The knowledge_library_list of this RoleBusinessReq.
        :type knowledge_library_list: list[:class:`huaweicloudsdkmetastudio.v1.RoleKnowledgeLibraryReq`]
        """
        self._knowledge_library_list = knowledge_library_list

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
        if not isinstance(other, RoleBusinessReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
