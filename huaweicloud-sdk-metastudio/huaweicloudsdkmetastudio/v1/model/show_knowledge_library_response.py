# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowKnowledgeLibraryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'knowledge_library_id': 'str',
        'name': 'str',
        'language': 'LanguageEnum',
        'knowledge_type': 'KnowledgeTypeEnum',
        'knowledge_size': 'int',
        'topk': 'int',
        'score': 'float',
        'create_time': 'str',
        'update_time': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'knowledge_library_id': 'knowledge_library_id',
        'name': 'name',
        'language': 'language',
        'knowledge_type': 'knowledge_type',
        'knowledge_size': 'knowledge_size',
        'topk': 'topk',
        'score': 'score',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, knowledge_library_id=None, name=None, language=None, knowledge_type=None, knowledge_size=None, topk=None, score=None, create_time=None, update_time=None, x_request_id=None):
        r"""ShowKnowledgeLibraryResponse

        The model defined in huaweicloud sdk

        :param knowledge_library_id: 知识库ID。
        :type knowledge_library_id: str
        :param name: 知识库名称。
        :type name: str
        :param language: 
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        :param knowledge_type: 
        :type knowledge_type: :class:`huaweicloudsdkmetastudio.v1.KnowledgeTypeEnum`
        :param knowledge_size: 知识库大小(文档库为文档数量)
        :type knowledge_size: int
        :param topk: 文档库召回topk
        :type topk: int
        :param score: 知识库召回得分
        :type score: float
        :param create_time: 创建时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type create_time: str
        :param update_time: 更新时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type update_time: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowKnowledgeLibraryResponse, self).__init__()

        self._knowledge_library_id = None
        self._name = None
        self._language = None
        self._knowledge_type = None
        self._knowledge_size = None
        self._topk = None
        self._score = None
        self._create_time = None
        self._update_time = None
        self._x_request_id = None
        self.discriminator = None

        if knowledge_library_id is not None:
            self.knowledge_library_id = knowledge_library_id
        if name is not None:
            self.name = name
        if language is not None:
            self.language = language
        if knowledge_type is not None:
            self.knowledge_type = knowledge_type
        if knowledge_size is not None:
            self.knowledge_size = knowledge_size
        if topk is not None:
            self.topk = topk
        if score is not None:
            self.score = score
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def knowledge_library_id(self):
        r"""Gets the knowledge_library_id of this ShowKnowledgeLibraryResponse.

        知识库ID。

        :return: The knowledge_library_id of this ShowKnowledgeLibraryResponse.
        :rtype: str
        """
        return self._knowledge_library_id

    @knowledge_library_id.setter
    def knowledge_library_id(self, knowledge_library_id):
        r"""Sets the knowledge_library_id of this ShowKnowledgeLibraryResponse.

        知识库ID。

        :param knowledge_library_id: The knowledge_library_id of this ShowKnowledgeLibraryResponse.
        :type knowledge_library_id: str
        """
        self._knowledge_library_id = knowledge_library_id

    @property
    def name(self):
        r"""Gets the name of this ShowKnowledgeLibraryResponse.

        知识库名称。

        :return: The name of this ShowKnowledgeLibraryResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowKnowledgeLibraryResponse.

        知识库名称。

        :param name: The name of this ShowKnowledgeLibraryResponse.
        :type name: str
        """
        self._name = name

    @property
    def language(self):
        r"""Gets the language of this ShowKnowledgeLibraryResponse.

        :return: The language of this ShowKnowledgeLibraryResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ShowKnowledgeLibraryResponse.

        :param language: The language of this ShowKnowledgeLibraryResponse.
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        self._language = language

    @property
    def knowledge_type(self):
        r"""Gets the knowledge_type of this ShowKnowledgeLibraryResponse.

        :return: The knowledge_type of this ShowKnowledgeLibraryResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.KnowledgeTypeEnum`
        """
        return self._knowledge_type

    @knowledge_type.setter
    def knowledge_type(self, knowledge_type):
        r"""Sets the knowledge_type of this ShowKnowledgeLibraryResponse.

        :param knowledge_type: The knowledge_type of this ShowKnowledgeLibraryResponse.
        :type knowledge_type: :class:`huaweicloudsdkmetastudio.v1.KnowledgeTypeEnum`
        """
        self._knowledge_type = knowledge_type

    @property
    def knowledge_size(self):
        r"""Gets the knowledge_size of this ShowKnowledgeLibraryResponse.

        知识库大小(文档库为文档数量)

        :return: The knowledge_size of this ShowKnowledgeLibraryResponse.
        :rtype: int
        """
        return self._knowledge_size

    @knowledge_size.setter
    def knowledge_size(self, knowledge_size):
        r"""Sets the knowledge_size of this ShowKnowledgeLibraryResponse.

        知识库大小(文档库为文档数量)

        :param knowledge_size: The knowledge_size of this ShowKnowledgeLibraryResponse.
        :type knowledge_size: int
        """
        self._knowledge_size = knowledge_size

    @property
    def topk(self):
        r"""Gets the topk of this ShowKnowledgeLibraryResponse.

        文档库召回topk

        :return: The topk of this ShowKnowledgeLibraryResponse.
        :rtype: int
        """
        return self._topk

    @topk.setter
    def topk(self, topk):
        r"""Sets the topk of this ShowKnowledgeLibraryResponse.

        文档库召回topk

        :param topk: The topk of this ShowKnowledgeLibraryResponse.
        :type topk: int
        """
        self._topk = topk

    @property
    def score(self):
        r"""Gets the score of this ShowKnowledgeLibraryResponse.

        知识库召回得分

        :return: The score of this ShowKnowledgeLibraryResponse.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this ShowKnowledgeLibraryResponse.

        知识库召回得分

        :param score: The score of this ShowKnowledgeLibraryResponse.
        :type score: float
        """
        self._score = score

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowKnowledgeLibraryResponse.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The create_time of this ShowKnowledgeLibraryResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowKnowledgeLibraryResponse.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param create_time: The create_time of this ShowKnowledgeLibraryResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowKnowledgeLibraryResponse.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The update_time of this ShowKnowledgeLibraryResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowKnowledgeLibraryResponse.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param update_time: The update_time of this ShowKnowledgeLibraryResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowKnowledgeLibraryResponse.

        :return: The x_request_id of this ShowKnowledgeLibraryResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowKnowledgeLibraryResponse.

        :param x_request_id: The x_request_id of this ShowKnowledgeLibraryResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowKnowledgeLibraryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
