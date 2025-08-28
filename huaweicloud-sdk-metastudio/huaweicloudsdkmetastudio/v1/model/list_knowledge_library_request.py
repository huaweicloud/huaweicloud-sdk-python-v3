# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListKnowledgeLibraryRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_app_user_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'language': 'str',
        'knowledge_type': 'str',
        'name': 'str'
    }

    attribute_map = {
        'x_app_user_id': 'X-App-UserId',
        'offset': 'offset',
        'limit': 'limit',
        'language': 'language',
        'knowledge_type': 'knowledge_type',
        'name': 'name'
    }

    def __init__(self, x_app_user_id=None, offset=None, limit=None, language=None, knowledge_type=None, name=None):
        r"""ListKnowledgeLibraryRequest

        The model defined in huaweicloud sdk

        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        :param offset: 偏移量，表示从此偏移量开始查询。
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param language: 角色语言  * CN：中文  * EN：英文
        :type language: str
        :param knowledge_type: 知识库类型  * QUESTION_ANSWER：问答  * DOCUMENT：文档
        :type knowledge_type: str
        :param name: 知识库名称
        :type name: str
        """
        
        

        self._x_app_user_id = None
        self._offset = None
        self._limit = None
        self._language = None
        self._knowledge_type = None
        self._name = None
        self.discriminator = None

        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if language is not None:
            self.language = language
        if knowledge_type is not None:
            self.knowledge_type = knowledge_type
        if name is not None:
            self.name = name

    @property
    def x_app_user_id(self):
        r"""Gets the x_app_user_id of this ListKnowledgeLibraryRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this ListKnowledgeLibraryRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        r"""Sets the x_app_user_id of this ListKnowledgeLibraryRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this ListKnowledgeLibraryRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def offset(self):
        r"""Gets the offset of this ListKnowledgeLibraryRequest.

        偏移量，表示从此偏移量开始查询。

        :return: The offset of this ListKnowledgeLibraryRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListKnowledgeLibraryRequest.

        偏移量，表示从此偏移量开始查询。

        :param offset: The offset of this ListKnowledgeLibraryRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListKnowledgeLibraryRequest.

        每页显示的条目数量。

        :return: The limit of this ListKnowledgeLibraryRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListKnowledgeLibraryRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListKnowledgeLibraryRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def language(self):
        r"""Gets the language of this ListKnowledgeLibraryRequest.

        角色语言  * CN：中文  * EN：英文

        :return: The language of this ListKnowledgeLibraryRequest.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ListKnowledgeLibraryRequest.

        角色语言  * CN：中文  * EN：英文

        :param language: The language of this ListKnowledgeLibraryRequest.
        :type language: str
        """
        self._language = language

    @property
    def knowledge_type(self):
        r"""Gets the knowledge_type of this ListKnowledgeLibraryRequest.

        知识库类型  * QUESTION_ANSWER：问答  * DOCUMENT：文档

        :return: The knowledge_type of this ListKnowledgeLibraryRequest.
        :rtype: str
        """
        return self._knowledge_type

    @knowledge_type.setter
    def knowledge_type(self, knowledge_type):
        r"""Sets the knowledge_type of this ListKnowledgeLibraryRequest.

        知识库类型  * QUESTION_ANSWER：问答  * DOCUMENT：文档

        :param knowledge_type: The knowledge_type of this ListKnowledgeLibraryRequest.
        :type knowledge_type: str
        """
        self._knowledge_type = knowledge_type

    @property
    def name(self):
        r"""Gets the name of this ListKnowledgeLibraryRequest.

        知识库名称

        :return: The name of this ListKnowledgeLibraryRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListKnowledgeLibraryRequest.

        知识库名称

        :param name: The name of this ListKnowledgeLibraryRequest.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ListKnowledgeLibraryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
