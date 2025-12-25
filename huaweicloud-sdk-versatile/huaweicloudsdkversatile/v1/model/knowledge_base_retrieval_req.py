# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KnowledgeBaseRetrievalReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'knowledge_base_ids': 'list[str]',
        'query': 'str',
        'search_mode': 'str',
        'top_k': 'int',
        'similarity_threshold': 'float',
        'image_mask_policy': 'str'
    }

    attribute_map = {
        'knowledge_base_ids': 'knowledge_base_ids',
        'query': 'query',
        'search_mode': 'search_mode',
        'top_k': 'top_k',
        'similarity_threshold': 'similarity_threshold',
        'image_mask_policy': 'image_mask_policy'
    }

    def __init__(self, knowledge_base_ids=None, query=None, search_mode=None, top_k=None, similarity_threshold=None, image_mask_policy=None):
        r"""KnowledgeBaseRetrievalReq

        The model defined in huaweicloud sdk

        :param knowledge_base_ids: **参数解释**： 知识库ID列表。  **约束限制**： 最多可同时检索3个知识库。  **取值范围**： 不涉及。  **默认取值**： 不涉及。
        :type knowledge_base_ids: list[str]
        :param query: **参数解释**： 用户输入的问题或关键词。  **约束限制**： 不涉及。  **取值范围**： 长度 1 至 4096 字符。  **默认取值**： 不涉及。
        :type query: str
        :param search_mode: **参数解释**： 检索策略模式。  **约束限制**： 不涉及。  **取值范围**： - doc：语义检索。 - keyword：关键词检索。 - mix：混合检索。 - faq：FAQ检索。  **默认取值**： doc。
        :type search_mode: str
        :param top_k: **参数解释**： 每个知识库最多返回的检索结果数量。  **约束限制**： 若传入小数，系统会默认截断小数部分。  **取值范围**： 1 至 100（含）。  **默认取值**： 10。
        :type top_k: int
        :param similarity_threshold: **参数解释**： 检索结果的最低相关度得分，低于此值的片段将被过滤。  **约束限制**： 不涉及。  **取值范围**： [0.0, 1.0]，包含两端。  **默认取值**： 0.5。
        :type similarity_threshold: float
        :param image_mask_policy: **参数解释**： 知识检索结果切片中，对图片标签进行处理和保留的具体方式。  **约束限制**： 该功能要求被检索的知识库本身支持返回图片信息。  **取值范围**： - RETAIN_IMAGE_ID：保留图片ID，格式：{KI|imageId}。 - RETAIN_PLACEHOLDER：保留占位符，格式：{KI|N}，N为序号。 - REMOVE_IMAGE：移除图片（即替换为空字符串）。  **默认取值**： REMOVE_IMAGE。
        :type image_mask_policy: str
        """
        
        

        self._knowledge_base_ids = None
        self._query = None
        self._search_mode = None
        self._top_k = None
        self._similarity_threshold = None
        self._image_mask_policy = None
        self.discriminator = None

        self.knowledge_base_ids = knowledge_base_ids
        self.query = query
        if search_mode is not None:
            self.search_mode = search_mode
        if top_k is not None:
            self.top_k = top_k
        if similarity_threshold is not None:
            self.similarity_threshold = similarity_threshold
        if image_mask_policy is not None:
            self.image_mask_policy = image_mask_policy

    @property
    def knowledge_base_ids(self):
        r"""Gets the knowledge_base_ids of this KnowledgeBaseRetrievalReq.

        **参数解释**： 知识库ID列表。  **约束限制**： 最多可同时检索3个知识库。  **取值范围**： 不涉及。  **默认取值**： 不涉及。

        :return: The knowledge_base_ids of this KnowledgeBaseRetrievalReq.
        :rtype: list[str]
        """
        return self._knowledge_base_ids

    @knowledge_base_ids.setter
    def knowledge_base_ids(self, knowledge_base_ids):
        r"""Sets the knowledge_base_ids of this KnowledgeBaseRetrievalReq.

        **参数解释**： 知识库ID列表。  **约束限制**： 最多可同时检索3个知识库。  **取值范围**： 不涉及。  **默认取值**： 不涉及。

        :param knowledge_base_ids: The knowledge_base_ids of this KnowledgeBaseRetrievalReq.
        :type knowledge_base_ids: list[str]
        """
        self._knowledge_base_ids = knowledge_base_ids

    @property
    def query(self):
        r"""Gets the query of this KnowledgeBaseRetrievalReq.

        **参数解释**： 用户输入的问题或关键词。  **约束限制**： 不涉及。  **取值范围**： 长度 1 至 4096 字符。  **默认取值**： 不涉及。

        :return: The query of this KnowledgeBaseRetrievalReq.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this KnowledgeBaseRetrievalReq.

        **参数解释**： 用户输入的问题或关键词。  **约束限制**： 不涉及。  **取值范围**： 长度 1 至 4096 字符。  **默认取值**： 不涉及。

        :param query: The query of this KnowledgeBaseRetrievalReq.
        :type query: str
        """
        self._query = query

    @property
    def search_mode(self):
        r"""Gets the search_mode of this KnowledgeBaseRetrievalReq.

        **参数解释**： 检索策略模式。  **约束限制**： 不涉及。  **取值范围**： - doc：语义检索。 - keyword：关键词检索。 - mix：混合检索。 - faq：FAQ检索。  **默认取值**： doc。

        :return: The search_mode of this KnowledgeBaseRetrievalReq.
        :rtype: str
        """
        return self._search_mode

    @search_mode.setter
    def search_mode(self, search_mode):
        r"""Sets the search_mode of this KnowledgeBaseRetrievalReq.

        **参数解释**： 检索策略模式。  **约束限制**： 不涉及。  **取值范围**： - doc：语义检索。 - keyword：关键词检索。 - mix：混合检索。 - faq：FAQ检索。  **默认取值**： doc。

        :param search_mode: The search_mode of this KnowledgeBaseRetrievalReq.
        :type search_mode: str
        """
        self._search_mode = search_mode

    @property
    def top_k(self):
        r"""Gets the top_k of this KnowledgeBaseRetrievalReq.

        **参数解释**： 每个知识库最多返回的检索结果数量。  **约束限制**： 若传入小数，系统会默认截断小数部分。  **取值范围**： 1 至 100（含）。  **默认取值**： 10。

        :return: The top_k of this KnowledgeBaseRetrievalReq.
        :rtype: int
        """
        return self._top_k

    @top_k.setter
    def top_k(self, top_k):
        r"""Sets the top_k of this KnowledgeBaseRetrievalReq.

        **参数解释**： 每个知识库最多返回的检索结果数量。  **约束限制**： 若传入小数，系统会默认截断小数部分。  **取值范围**： 1 至 100（含）。  **默认取值**： 10。

        :param top_k: The top_k of this KnowledgeBaseRetrievalReq.
        :type top_k: int
        """
        self._top_k = top_k

    @property
    def similarity_threshold(self):
        r"""Gets the similarity_threshold of this KnowledgeBaseRetrievalReq.

        **参数解释**： 检索结果的最低相关度得分，低于此值的片段将被过滤。  **约束限制**： 不涉及。  **取值范围**： [0.0, 1.0]，包含两端。  **默认取值**： 0.5。

        :return: The similarity_threshold of this KnowledgeBaseRetrievalReq.
        :rtype: float
        """
        return self._similarity_threshold

    @similarity_threshold.setter
    def similarity_threshold(self, similarity_threshold):
        r"""Sets the similarity_threshold of this KnowledgeBaseRetrievalReq.

        **参数解释**： 检索结果的最低相关度得分，低于此值的片段将被过滤。  **约束限制**： 不涉及。  **取值范围**： [0.0, 1.0]，包含两端。  **默认取值**： 0.5。

        :param similarity_threshold: The similarity_threshold of this KnowledgeBaseRetrievalReq.
        :type similarity_threshold: float
        """
        self._similarity_threshold = similarity_threshold

    @property
    def image_mask_policy(self):
        r"""Gets the image_mask_policy of this KnowledgeBaseRetrievalReq.

        **参数解释**： 知识检索结果切片中，对图片标签进行处理和保留的具体方式。  **约束限制**： 该功能要求被检索的知识库本身支持返回图片信息。  **取值范围**： - RETAIN_IMAGE_ID：保留图片ID，格式：{KI|imageId}。 - RETAIN_PLACEHOLDER：保留占位符，格式：{KI|N}，N为序号。 - REMOVE_IMAGE：移除图片（即替换为空字符串）。  **默认取值**： REMOVE_IMAGE。

        :return: The image_mask_policy of this KnowledgeBaseRetrievalReq.
        :rtype: str
        """
        return self._image_mask_policy

    @image_mask_policy.setter
    def image_mask_policy(self, image_mask_policy):
        r"""Sets the image_mask_policy of this KnowledgeBaseRetrievalReq.

        **参数解释**： 知识检索结果切片中，对图片标签进行处理和保留的具体方式。  **约束限制**： 该功能要求被检索的知识库本身支持返回图片信息。  **取值范围**： - RETAIN_IMAGE_ID：保留图片ID，格式：{KI|imageId}。 - RETAIN_PLACEHOLDER：保留占位符，格式：{KI|N}，N为序号。 - REMOVE_IMAGE：移除图片（即替换为空字符串）。  **默认取值**： REMOVE_IMAGE。

        :param image_mask_policy: The image_mask_policy of this KnowledgeBaseRetrievalReq.
        :type image_mask_policy: str
        """
        self._image_mask_policy = image_mask_policy

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
        if not isinstance(other, KnowledgeBaseRetrievalReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
