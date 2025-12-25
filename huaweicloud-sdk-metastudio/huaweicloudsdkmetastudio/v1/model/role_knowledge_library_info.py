# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RoleKnowledgeLibraryInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'knowledge_type': 'str',
        'knowledge_library_info_list': 'list[KnowledgeLibraryBaseInfo]'
    }

    attribute_map = {
        'knowledge_type': 'knowledge_type',
        'knowledge_library_info_list': 'knowledge_library_info_list'
    }

    def __init__(self, knowledge_type=None, knowledge_library_info_list=None):
        r"""RoleKnowledgeLibraryInfo

        The model defined in huaweicloud sdk

        :param knowledge_type: 知识库类型 * QUESTION_ANSWER：问答 * DOCUMENT：文档
        :type knowledge_type: str
        :param knowledge_library_info_list: 知识库列表
        :type knowledge_library_info_list: list[:class:`huaweicloudsdkmetastudio.v1.KnowledgeLibraryBaseInfo`]
        """
        
        

        self._knowledge_type = None
        self._knowledge_library_info_list = None
        self.discriminator = None

        self.knowledge_type = knowledge_type
        self.knowledge_library_info_list = knowledge_library_info_list

    @property
    def knowledge_type(self):
        r"""Gets the knowledge_type of this RoleKnowledgeLibraryInfo.

        知识库类型 * QUESTION_ANSWER：问答 * DOCUMENT：文档

        :return: The knowledge_type of this RoleKnowledgeLibraryInfo.
        :rtype: str
        """
        return self._knowledge_type

    @knowledge_type.setter
    def knowledge_type(self, knowledge_type):
        r"""Sets the knowledge_type of this RoleKnowledgeLibraryInfo.

        知识库类型 * QUESTION_ANSWER：问答 * DOCUMENT：文档

        :param knowledge_type: The knowledge_type of this RoleKnowledgeLibraryInfo.
        :type knowledge_type: str
        """
        self._knowledge_type = knowledge_type

    @property
    def knowledge_library_info_list(self):
        r"""Gets the knowledge_library_info_list of this RoleKnowledgeLibraryInfo.

        知识库列表

        :return: The knowledge_library_info_list of this RoleKnowledgeLibraryInfo.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.KnowledgeLibraryBaseInfo`]
        """
        return self._knowledge_library_info_list

    @knowledge_library_info_list.setter
    def knowledge_library_info_list(self, knowledge_library_info_list):
        r"""Sets the knowledge_library_info_list of this RoleKnowledgeLibraryInfo.

        知识库列表

        :param knowledge_library_info_list: The knowledge_library_info_list of this RoleKnowledgeLibraryInfo.
        :type knowledge_library_info_list: list[:class:`huaweicloudsdkmetastudio.v1.KnowledgeLibraryBaseInfo`]
        """
        self._knowledge_library_info_list = knowledge_library_info_list

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
        if not isinstance(other, RoleKnowledgeLibraryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
