# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RetrievalResultInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_id': 'str',
        'title': 'str',
        'chunk_id': 'str',
        'content': 'str',
        'similarity': 'float',
        'knowledge_base_id': 'str',
        'image_ids': 'list[str]'
    }

    attribute_map = {
        'file_id': 'file_id',
        'title': 'title',
        'chunk_id': 'chunk_id',
        'content': 'content',
        'similarity': 'similarity',
        'knowledge_base_id': 'knowledge_base_id',
        'image_ids': 'image_ids'
    }

    def __init__(self, file_id=None, title=None, chunk_id=None, content=None, similarity=None, knowledge_base_id=None, image_ids=None):
        r"""RetrievalResultInfo

        The model defined in huaweicloud sdk

        :param file_id: **参数解释**： 文件ID（或FAQ ID）。  **取值范围**： 不涉及。
        :type file_id: str
        :param title: **参数解释**： 文档标题（如果是FAQ，返回QUESTION）。  **取值范围**： 不涉及。
        :type title: str
        :param chunk_id: **参数解释**： 分片ID。  **取值范围**： 不涉及。
        :type chunk_id: str
        :param content: **参数解释**： 文本内容（如果是FAQ，返回ANSWER）。  **取值范围**： 不涉及。
        :type content: str
        :param similarity: **参数解释**： 相似度。  **取值范围**： [0.0, 1.0]，包含两端。
        :type similarity: float
        :param knowledge_base_id: **参数解释**： 知识库ID。  **取值范围**： 不涉及。
        :type knowledge_base_id: str
        :param image_ids: **参数解释**： 检索到的图片列表（需知识库支持），与content中的图片占位符{KI|N}保持一一对应关系，N为图片索引值，从0开始。  **取值范围**： 不涉及。
        :type image_ids: list[str]
        """
        
        

        self._file_id = None
        self._title = None
        self._chunk_id = None
        self._content = None
        self._similarity = None
        self._knowledge_base_id = None
        self._image_ids = None
        self.discriminator = None

        if file_id is not None:
            self.file_id = file_id
        if title is not None:
            self.title = title
        if chunk_id is not None:
            self.chunk_id = chunk_id
        if content is not None:
            self.content = content
        if similarity is not None:
            self.similarity = similarity
        if knowledge_base_id is not None:
            self.knowledge_base_id = knowledge_base_id
        if image_ids is not None:
            self.image_ids = image_ids

    @property
    def file_id(self):
        r"""Gets the file_id of this RetrievalResultInfo.

        **参数解释**： 文件ID（或FAQ ID）。  **取值范围**： 不涉及。

        :return: The file_id of this RetrievalResultInfo.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        r"""Sets the file_id of this RetrievalResultInfo.

        **参数解释**： 文件ID（或FAQ ID）。  **取值范围**： 不涉及。

        :param file_id: The file_id of this RetrievalResultInfo.
        :type file_id: str
        """
        self._file_id = file_id

    @property
    def title(self):
        r"""Gets the title of this RetrievalResultInfo.

        **参数解释**： 文档标题（如果是FAQ，返回QUESTION）。  **取值范围**： 不涉及。

        :return: The title of this RetrievalResultInfo.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this RetrievalResultInfo.

        **参数解释**： 文档标题（如果是FAQ，返回QUESTION）。  **取值范围**： 不涉及。

        :param title: The title of this RetrievalResultInfo.
        :type title: str
        """
        self._title = title

    @property
    def chunk_id(self):
        r"""Gets the chunk_id of this RetrievalResultInfo.

        **参数解释**： 分片ID。  **取值范围**： 不涉及。

        :return: The chunk_id of this RetrievalResultInfo.
        :rtype: str
        """
        return self._chunk_id

    @chunk_id.setter
    def chunk_id(self, chunk_id):
        r"""Sets the chunk_id of this RetrievalResultInfo.

        **参数解释**： 分片ID。  **取值范围**： 不涉及。

        :param chunk_id: The chunk_id of this RetrievalResultInfo.
        :type chunk_id: str
        """
        self._chunk_id = chunk_id

    @property
    def content(self):
        r"""Gets the content of this RetrievalResultInfo.

        **参数解释**： 文本内容（如果是FAQ，返回ANSWER）。  **取值范围**： 不涉及。

        :return: The content of this RetrievalResultInfo.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this RetrievalResultInfo.

        **参数解释**： 文本内容（如果是FAQ，返回ANSWER）。  **取值范围**： 不涉及。

        :param content: The content of this RetrievalResultInfo.
        :type content: str
        """
        self._content = content

    @property
    def similarity(self):
        r"""Gets the similarity of this RetrievalResultInfo.

        **参数解释**： 相似度。  **取值范围**： [0.0, 1.0]，包含两端。

        :return: The similarity of this RetrievalResultInfo.
        :rtype: float
        """
        return self._similarity

    @similarity.setter
    def similarity(self, similarity):
        r"""Sets the similarity of this RetrievalResultInfo.

        **参数解释**： 相似度。  **取值范围**： [0.0, 1.0]，包含两端。

        :param similarity: The similarity of this RetrievalResultInfo.
        :type similarity: float
        """
        self._similarity = similarity

    @property
    def knowledge_base_id(self):
        r"""Gets the knowledge_base_id of this RetrievalResultInfo.

        **参数解释**： 知识库ID。  **取值范围**： 不涉及。

        :return: The knowledge_base_id of this RetrievalResultInfo.
        :rtype: str
        """
        return self._knowledge_base_id

    @knowledge_base_id.setter
    def knowledge_base_id(self, knowledge_base_id):
        r"""Sets the knowledge_base_id of this RetrievalResultInfo.

        **参数解释**： 知识库ID。  **取值范围**： 不涉及。

        :param knowledge_base_id: The knowledge_base_id of this RetrievalResultInfo.
        :type knowledge_base_id: str
        """
        self._knowledge_base_id = knowledge_base_id

    @property
    def image_ids(self):
        r"""Gets the image_ids of this RetrievalResultInfo.

        **参数解释**： 检索到的图片列表（需知识库支持），与content中的图片占位符{KI|N}保持一一对应关系，N为图片索引值，从0开始。  **取值范围**： 不涉及。

        :return: The image_ids of this RetrievalResultInfo.
        :rtype: list[str]
        """
        return self._image_ids

    @image_ids.setter
    def image_ids(self, image_ids):
        r"""Sets the image_ids of this RetrievalResultInfo.

        **参数解释**： 检索到的图片列表（需知识库支持），与content中的图片占位符{KI|N}保持一一对应关系，N为图片索引值，从0开始。  **取值范围**： 不涉及。

        :param image_ids: The image_ids of this RetrievalResultInfo.
        :type image_ids: list[str]
        """
        self._image_ids = image_ids

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
        if not isinstance(other, RetrievalResultInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
