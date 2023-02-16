# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SessionAskQuestionReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'question': 'str',
        'domain': 'str',
        'top': 'int',
        'themes': 'list[RelationTheme]',
        'source_qa_pair_id': 'str',
        'chat_enable': 'bool',
        'product_type_id': 'str'
    }

    attribute_map = {
        'question': 'question',
        'domain': 'domain',
        'top': 'top',
        'themes': 'themes',
        'source_qa_pair_id': 'source_qa_pair_id',
        'chat_enable': 'chat_enable',
        'product_type_id': 'product_type_id'
    }

    def __init__(self, question=None, domain=None, top=None, themes=None, source_qa_pair_id=None, chat_enable=None, product_type_id=None):
        """SessionAskQuestionReq

        The model defined in huaweicloud sdk

        :param question: 用户输入问题
        :type question: str
        :param domain: 问答领域
        :type domain: str
        :param top: 最大返回数据条数
        :type top: int
        :param themes: 主题列表
        :type themes: list[:class:`huaweicloudsdkosm.v2.RelationTheme`]
        :param source_qa_pair_id: 语料ID
        :type source_qa_pair_id: str
        :param chat_enable: 是否需要兜底
        :type chat_enable: bool
        :param product_type_id: 产品类型Id
        :type product_type_id: str
        """
        
        

        self._question = None
        self._domain = None
        self._top = None
        self._themes = None
        self._source_qa_pair_id = None
        self._chat_enable = None
        self._product_type_id = None
        self.discriminator = None

        self.question = question
        if domain is not None:
            self.domain = domain
        if top is not None:
            self.top = top
        if themes is not None:
            self.themes = themes
        if source_qa_pair_id is not None:
            self.source_qa_pair_id = source_qa_pair_id
        if chat_enable is not None:
            self.chat_enable = chat_enable
        if product_type_id is not None:
            self.product_type_id = product_type_id

    @property
    def question(self):
        """Gets the question of this SessionAskQuestionReq.

        用户输入问题

        :return: The question of this SessionAskQuestionReq.
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question):
        """Sets the question of this SessionAskQuestionReq.

        用户输入问题

        :param question: The question of this SessionAskQuestionReq.
        :type question: str
        """
        self._question = question

    @property
    def domain(self):
        """Gets the domain of this SessionAskQuestionReq.

        问答领域

        :return: The domain of this SessionAskQuestionReq.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this SessionAskQuestionReq.

        问答领域

        :param domain: The domain of this SessionAskQuestionReq.
        :type domain: str
        """
        self._domain = domain

    @property
    def top(self):
        """Gets the top of this SessionAskQuestionReq.

        最大返回数据条数

        :return: The top of this SessionAskQuestionReq.
        :rtype: int
        """
        return self._top

    @top.setter
    def top(self, top):
        """Sets the top of this SessionAskQuestionReq.

        最大返回数据条数

        :param top: The top of this SessionAskQuestionReq.
        :type top: int
        """
        self._top = top

    @property
    def themes(self):
        """Gets the themes of this SessionAskQuestionReq.

        主题列表

        :return: The themes of this SessionAskQuestionReq.
        :rtype: list[:class:`huaweicloudsdkosm.v2.RelationTheme`]
        """
        return self._themes

    @themes.setter
    def themes(self, themes):
        """Sets the themes of this SessionAskQuestionReq.

        主题列表

        :param themes: The themes of this SessionAskQuestionReq.
        :type themes: list[:class:`huaweicloudsdkosm.v2.RelationTheme`]
        """
        self._themes = themes

    @property
    def source_qa_pair_id(self):
        """Gets the source_qa_pair_id of this SessionAskQuestionReq.

        语料ID

        :return: The source_qa_pair_id of this SessionAskQuestionReq.
        :rtype: str
        """
        return self._source_qa_pair_id

    @source_qa_pair_id.setter
    def source_qa_pair_id(self, source_qa_pair_id):
        """Sets the source_qa_pair_id of this SessionAskQuestionReq.

        语料ID

        :param source_qa_pair_id: The source_qa_pair_id of this SessionAskQuestionReq.
        :type source_qa_pair_id: str
        """
        self._source_qa_pair_id = source_qa_pair_id

    @property
    def chat_enable(self):
        """Gets the chat_enable of this SessionAskQuestionReq.

        是否需要兜底

        :return: The chat_enable of this SessionAskQuestionReq.
        :rtype: bool
        """
        return self._chat_enable

    @chat_enable.setter
    def chat_enable(self, chat_enable):
        """Sets the chat_enable of this SessionAskQuestionReq.

        是否需要兜底

        :param chat_enable: The chat_enable of this SessionAskQuestionReq.
        :type chat_enable: bool
        """
        self._chat_enable = chat_enable

    @property
    def product_type_id(self):
        """Gets the product_type_id of this SessionAskQuestionReq.

        产品类型Id

        :return: The product_type_id of this SessionAskQuestionReq.
        :rtype: str
        """
        return self._product_type_id

    @product_type_id.setter
    def product_type_id(self, product_type_id):
        """Sets the product_type_id of this SessionAskQuestionReq.

        产品类型Id

        :param product_type_id: The product_type_id of this SessionAskQuestionReq.
        :type product_type_id: str
        """
        self._product_type_id = product_type_id

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
        if not isinstance(other, SessionAskQuestionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
