# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QaAskReq:

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
        'top': 'int',
        'themes': 'list[RelationTheme]',
        'source': 'str',
        'session_id': 'str',
        'source_qa_pair_id': 'str',
        'alternative_answer_enable': 'bool',
        'product_type_id': 'str',
        'specify_node_id': 'str'
    }

    attribute_map = {
        'question': 'question',
        'top': 'top',
        'themes': 'themes',
        'source': 'source',
        'session_id': 'session_id',
        'source_qa_pair_id': 'source_qa_pair_id',
        'alternative_answer_enable': 'alternative_answer_enable',
        'product_type_id': 'product_type_id',
        'specify_node_id': 'specify_node_id'
    }

    def __init__(self, question=None, top=None, themes=None, source=None, session_id=None, source_qa_pair_id=None, alternative_answer_enable=None, product_type_id=None, specify_node_id=None):
        """QaAskReq

        The model defined in huaweicloud sdk

        :param question: 用户输入问题
        :type question: str
        :param top: 最大返回数据条数
        :type top: int
        :param themes: 主题列表
        :type themes: list[:class:`huaweicloudsdkosm.v2.RelationTheme`]
        :param source: - PORTAL:  - INCIDENT:  
        :type source: str
        :param session_id: 会话ID
        :type session_id: str
        :param source_qa_pair_id: 语料ID
        :type source_qa_pair_id: str
        :param alternative_answer_enable: 是否需要备选答案
        :type alternative_answer_enable: bool
        :param product_type_id: 产品类型Id
        :type product_type_id: str
        :param specify_node_id: 指定的节点ID
        :type specify_node_id: str
        """
        
        

        self._question = None
        self._top = None
        self._themes = None
        self._source = None
        self._session_id = None
        self._source_qa_pair_id = None
        self._alternative_answer_enable = None
        self._product_type_id = None
        self._specify_node_id = None
        self.discriminator = None

        self.question = question
        if top is not None:
            self.top = top
        if themes is not None:
            self.themes = themes
        if source is not None:
            self.source = source
        if session_id is not None:
            self.session_id = session_id
        if source_qa_pair_id is not None:
            self.source_qa_pair_id = source_qa_pair_id
        if alternative_answer_enable is not None:
            self.alternative_answer_enable = alternative_answer_enable
        if product_type_id is not None:
            self.product_type_id = product_type_id
        if specify_node_id is not None:
            self.specify_node_id = specify_node_id

    @property
    def question(self):
        """Gets the question of this QaAskReq.

        用户输入问题

        :return: The question of this QaAskReq.
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question):
        """Sets the question of this QaAskReq.

        用户输入问题

        :param question: The question of this QaAskReq.
        :type question: str
        """
        self._question = question

    @property
    def top(self):
        """Gets the top of this QaAskReq.

        最大返回数据条数

        :return: The top of this QaAskReq.
        :rtype: int
        """
        return self._top

    @top.setter
    def top(self, top):
        """Sets the top of this QaAskReq.

        最大返回数据条数

        :param top: The top of this QaAskReq.
        :type top: int
        """
        self._top = top

    @property
    def themes(self):
        """Gets the themes of this QaAskReq.

        主题列表

        :return: The themes of this QaAskReq.
        :rtype: list[:class:`huaweicloudsdkosm.v2.RelationTheme`]
        """
        return self._themes

    @themes.setter
    def themes(self, themes):
        """Sets the themes of this QaAskReq.

        主题列表

        :param themes: The themes of this QaAskReq.
        :type themes: list[:class:`huaweicloudsdkosm.v2.RelationTheme`]
        """
        self._themes = themes

    @property
    def source(self):
        """Gets the source of this QaAskReq.

        - PORTAL:  - INCIDENT:  

        :return: The source of this QaAskReq.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this QaAskReq.

        - PORTAL:  - INCIDENT:  

        :param source: The source of this QaAskReq.
        :type source: str
        """
        self._source = source

    @property
    def session_id(self):
        """Gets the session_id of this QaAskReq.

        会话ID

        :return: The session_id of this QaAskReq.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this QaAskReq.

        会话ID

        :param session_id: The session_id of this QaAskReq.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def source_qa_pair_id(self):
        """Gets the source_qa_pair_id of this QaAskReq.

        语料ID

        :return: The source_qa_pair_id of this QaAskReq.
        :rtype: str
        """
        return self._source_qa_pair_id

    @source_qa_pair_id.setter
    def source_qa_pair_id(self, source_qa_pair_id):
        """Sets the source_qa_pair_id of this QaAskReq.

        语料ID

        :param source_qa_pair_id: The source_qa_pair_id of this QaAskReq.
        :type source_qa_pair_id: str
        """
        self._source_qa_pair_id = source_qa_pair_id

    @property
    def alternative_answer_enable(self):
        """Gets the alternative_answer_enable of this QaAskReq.

        是否需要备选答案

        :return: The alternative_answer_enable of this QaAskReq.
        :rtype: bool
        """
        return self._alternative_answer_enable

    @alternative_answer_enable.setter
    def alternative_answer_enable(self, alternative_answer_enable):
        """Sets the alternative_answer_enable of this QaAskReq.

        是否需要备选答案

        :param alternative_answer_enable: The alternative_answer_enable of this QaAskReq.
        :type alternative_answer_enable: bool
        """
        self._alternative_answer_enable = alternative_answer_enable

    @property
    def product_type_id(self):
        """Gets the product_type_id of this QaAskReq.

        产品类型Id

        :return: The product_type_id of this QaAskReq.
        :rtype: str
        """
        return self._product_type_id

    @product_type_id.setter
    def product_type_id(self, product_type_id):
        """Sets the product_type_id of this QaAskReq.

        产品类型Id

        :param product_type_id: The product_type_id of this QaAskReq.
        :type product_type_id: str
        """
        self._product_type_id = product_type_id

    @property
    def specify_node_id(self):
        """Gets the specify_node_id of this QaAskReq.

        指定的节点ID

        :return: The specify_node_id of this QaAskReq.
        :rtype: str
        """
        return self._specify_node_id

    @specify_node_id.setter
    def specify_node_id(self, specify_node_id):
        """Sets the specify_node_id of this QaAskReq.

        指定的节点ID

        :param specify_node_id: The specify_node_id of this QaAskReq.
        :type specify_node_id: str
        """
        self._specify_node_id = specify_node_id

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
        if not isinstance(other, QaAskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
