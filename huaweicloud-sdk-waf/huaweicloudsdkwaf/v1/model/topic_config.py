# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopicConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topic_name': 'str',
        'topic_description': 'str',
        'sensitive_words': 'list[str]',
        'black_samples': 'list[str]',
        'white_samples': 'list[str]',
        'scope': 'str',
        'block_response': 'str',
        'custom_llm_id': 'str'
    }

    attribute_map = {
        'topic_name': 'topic_name',
        'topic_description': 'topic_description',
        'sensitive_words': 'sensitive_words',
        'black_samples': 'black_samples',
        'white_samples': 'white_samples',
        'scope': 'scope',
        'block_response': 'block_response',
        'custom_llm_id': 'custom_llm_id'
    }

    def __init__(self, topic_name=None, topic_description=None, sensitive_words=None, black_samples=None, white_samples=None, scope=None, block_response=None, custom_llm_id=None):
        r"""TopicConfig

        The model defined in huaweicloud sdk

        :param topic_name: 话题名称
        :type topic_name: str
        :param topic_description: 话题描述
        :type topic_description: str
        :param sensitive_words: 敏感词列表
        :type sensitive_words: list[str]
        :param black_samples: 黑样本列表
        :type black_samples: list[str]
        :param white_samples: 白样本列表
        :type white_samples: list[str]
        :param scope: 检测作用域，取值 request/response/request_response（值合法性由后端validateTopicConfig校验，契约层不声明enum）
        :type scope: str
        :param block_response: 拦截回包内容（仅外层action.category&#x3D;block时有意义，非block落库归一化为null）
        :type block_response: str
        :param custom_llm_id: 关联的自定义大模型ID（可选）
        :type custom_llm_id: str
        """
        
        

        self._topic_name = None
        self._topic_description = None
        self._sensitive_words = None
        self._black_samples = None
        self._white_samples = None
        self._scope = None
        self._block_response = None
        self._custom_llm_id = None
        self.discriminator = None

        self.topic_name = topic_name
        self.topic_description = topic_description
        if sensitive_words is not None:
            self.sensitive_words = sensitive_words
        if black_samples is not None:
            self.black_samples = black_samples
        if white_samples is not None:
            self.white_samples = white_samples
        self.scope = scope
        if block_response is not None:
            self.block_response = block_response
        if custom_llm_id is not None:
            self.custom_llm_id = custom_llm_id

    @property
    def topic_name(self):
        r"""Gets the topic_name of this TopicConfig.

        话题名称

        :return: The topic_name of this TopicConfig.
        :rtype: str
        """
        return self._topic_name

    @topic_name.setter
    def topic_name(self, topic_name):
        r"""Sets the topic_name of this TopicConfig.

        话题名称

        :param topic_name: The topic_name of this TopicConfig.
        :type topic_name: str
        """
        self._topic_name = topic_name

    @property
    def topic_description(self):
        r"""Gets the topic_description of this TopicConfig.

        话题描述

        :return: The topic_description of this TopicConfig.
        :rtype: str
        """
        return self._topic_description

    @topic_description.setter
    def topic_description(self, topic_description):
        r"""Sets the topic_description of this TopicConfig.

        话题描述

        :param topic_description: The topic_description of this TopicConfig.
        :type topic_description: str
        """
        self._topic_description = topic_description

    @property
    def sensitive_words(self):
        r"""Gets the sensitive_words of this TopicConfig.

        敏感词列表

        :return: The sensitive_words of this TopicConfig.
        :rtype: list[str]
        """
        return self._sensitive_words

    @sensitive_words.setter
    def sensitive_words(self, sensitive_words):
        r"""Sets the sensitive_words of this TopicConfig.

        敏感词列表

        :param sensitive_words: The sensitive_words of this TopicConfig.
        :type sensitive_words: list[str]
        """
        self._sensitive_words = sensitive_words

    @property
    def black_samples(self):
        r"""Gets the black_samples of this TopicConfig.

        黑样本列表

        :return: The black_samples of this TopicConfig.
        :rtype: list[str]
        """
        return self._black_samples

    @black_samples.setter
    def black_samples(self, black_samples):
        r"""Sets the black_samples of this TopicConfig.

        黑样本列表

        :param black_samples: The black_samples of this TopicConfig.
        :type black_samples: list[str]
        """
        self._black_samples = black_samples

    @property
    def white_samples(self):
        r"""Gets the white_samples of this TopicConfig.

        白样本列表

        :return: The white_samples of this TopicConfig.
        :rtype: list[str]
        """
        return self._white_samples

    @white_samples.setter
    def white_samples(self, white_samples):
        r"""Sets the white_samples of this TopicConfig.

        白样本列表

        :param white_samples: The white_samples of this TopicConfig.
        :type white_samples: list[str]
        """
        self._white_samples = white_samples

    @property
    def scope(self):
        r"""Gets the scope of this TopicConfig.

        检测作用域，取值 request/response/request_response（值合法性由后端validateTopicConfig校验，契约层不声明enum）

        :return: The scope of this TopicConfig.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this TopicConfig.

        检测作用域，取值 request/response/request_response（值合法性由后端validateTopicConfig校验，契约层不声明enum）

        :param scope: The scope of this TopicConfig.
        :type scope: str
        """
        self._scope = scope

    @property
    def block_response(self):
        r"""Gets the block_response of this TopicConfig.

        拦截回包内容（仅外层action.category=block时有意义，非block落库归一化为null）

        :return: The block_response of this TopicConfig.
        :rtype: str
        """
        return self._block_response

    @block_response.setter
    def block_response(self, block_response):
        r"""Sets the block_response of this TopicConfig.

        拦截回包内容（仅外层action.category=block时有意义，非block落库归一化为null）

        :param block_response: The block_response of this TopicConfig.
        :type block_response: str
        """
        self._block_response = block_response

    @property
    def custom_llm_id(self):
        r"""Gets the custom_llm_id of this TopicConfig.

        关联的自定义大模型ID（可选）

        :return: The custom_llm_id of this TopicConfig.
        :rtype: str
        """
        return self._custom_llm_id

    @custom_llm_id.setter
    def custom_llm_id(self, custom_llm_id):
        r"""Sets the custom_llm_id of this TopicConfig.

        关联的自定义大模型ID（可选）

        :param custom_llm_id: The custom_llm_id of this TopicConfig.
        :type custom_llm_id: str
        """
        self._custom_llm_id = custom_llm_id

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
        if not isinstance(other, TopicConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
