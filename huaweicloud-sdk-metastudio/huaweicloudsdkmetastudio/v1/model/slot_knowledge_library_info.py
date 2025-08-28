# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SlotKnowledgeLibraryInfo:

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
        'knowledge_library_id': 'str'
    }

    attribute_map = {
        'language': 'language',
        'knowledge_library_id': 'knowledge_library_id'
    }

    def __init__(self, language=None, knowledge_library_id=None):
        r"""SlotKnowledgeLibraryInfo

        The model defined in huaweicloud sdk

        :param language: 
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        :param knowledge_library_id: 知识库ID。
        :type knowledge_library_id: str
        """
        
        

        self._language = None
        self._knowledge_library_id = None
        self.discriminator = None

        self.language = language
        self.knowledge_library_id = knowledge_library_id

    @property
    def language(self):
        r"""Gets the language of this SlotKnowledgeLibraryInfo.

        :return: The language of this SlotKnowledgeLibraryInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this SlotKnowledgeLibraryInfo.

        :param language: The language of this SlotKnowledgeLibraryInfo.
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        self._language = language

    @property
    def knowledge_library_id(self):
        r"""Gets the knowledge_library_id of this SlotKnowledgeLibraryInfo.

        知识库ID。

        :return: The knowledge_library_id of this SlotKnowledgeLibraryInfo.
        :rtype: str
        """
        return self._knowledge_library_id

    @knowledge_library_id.setter
    def knowledge_library_id(self, knowledge_library_id):
        r"""Sets the knowledge_library_id of this SlotKnowledgeLibraryInfo.

        知识库ID。

        :param knowledge_library_id: The knowledge_library_id of this SlotKnowledgeLibraryInfo.
        :type knowledge_library_id: str
        """
        self._knowledge_library_id = knowledge_library_id

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
        if not isinstance(other, SlotKnowledgeLibraryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
