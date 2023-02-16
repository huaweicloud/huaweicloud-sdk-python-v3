# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AskQuestionReq:

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
        'domains': 'list[str]',
        'top': 'int',
        'session_id': 'str',
        'source_qa_pair_id': 'str',
        'operate_type': 'int',
        'threshold_enable': 'str',
        'product_type_id': 'str'
    }

    attribute_map = {
        'question': 'question',
        'domains': 'domains',
        'top': 'top',
        'session_id': 'session_id',
        'source_qa_pair_id': 'source_qa_pair_id',
        'operate_type': 'operate_type',
        'threshold_enable': 'threshold_enable',
        'product_type_id': 'product_type_id'
    }

    def __init__(self, question=None, domains=None, top=None, session_id=None, source_qa_pair_id=None, operate_type=None, threshold_enable=None, product_type_id=None):
        """AskQuestionReq

        The model defined in huaweicloud sdk

        :param question: 用户输入问题
        :type question: str
        :param domains: 主题列表
        :type domains: list[str]
        :param top: 返回匹配度最高的数据条数
        :type top: int
        :param session_id: 会话ID
        :type session_id: str
        :param source_qa_pair_id: 语料ID
        :type source_qa_pair_id: str
        :param operate_type: 操作类型:0-手动输入，1-单击热点问题，2-单击猜你想问，3-单击推荐问题，4-单击问题提示
        :type operate_type: int
        :param threshold_enable: 是否启用内部阈值开关
        :type threshold_enable: str
        :param product_type_id: 产品类型id
        :type product_type_id: str
        """
        
        

        self._question = None
        self._domains = None
        self._top = None
        self._session_id = None
        self._source_qa_pair_id = None
        self._operate_type = None
        self._threshold_enable = None
        self._product_type_id = None
        self.discriminator = None

        self.question = question
        if domains is not None:
            self.domains = domains
        if top is not None:
            self.top = top
        self.session_id = session_id
        if source_qa_pair_id is not None:
            self.source_qa_pair_id = source_qa_pair_id
        if operate_type is not None:
            self.operate_type = operate_type
        if threshold_enable is not None:
            self.threshold_enable = threshold_enable
        if product_type_id is not None:
            self.product_type_id = product_type_id

    @property
    def question(self):
        """Gets the question of this AskQuestionReq.

        用户输入问题

        :return: The question of this AskQuestionReq.
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question):
        """Sets the question of this AskQuestionReq.

        用户输入问题

        :param question: The question of this AskQuestionReq.
        :type question: str
        """
        self._question = question

    @property
    def domains(self):
        """Gets the domains of this AskQuestionReq.

        主题列表

        :return: The domains of this AskQuestionReq.
        :rtype: list[str]
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        """Sets the domains of this AskQuestionReq.

        主题列表

        :param domains: The domains of this AskQuestionReq.
        :type domains: list[str]
        """
        self._domains = domains

    @property
    def top(self):
        """Gets the top of this AskQuestionReq.

        返回匹配度最高的数据条数

        :return: The top of this AskQuestionReq.
        :rtype: int
        """
        return self._top

    @top.setter
    def top(self, top):
        """Sets the top of this AskQuestionReq.

        返回匹配度最高的数据条数

        :param top: The top of this AskQuestionReq.
        :type top: int
        """
        self._top = top

    @property
    def session_id(self):
        """Gets the session_id of this AskQuestionReq.

        会话ID

        :return: The session_id of this AskQuestionReq.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this AskQuestionReq.

        会话ID

        :param session_id: The session_id of this AskQuestionReq.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def source_qa_pair_id(self):
        """Gets the source_qa_pair_id of this AskQuestionReq.

        语料ID

        :return: The source_qa_pair_id of this AskQuestionReq.
        :rtype: str
        """
        return self._source_qa_pair_id

    @source_qa_pair_id.setter
    def source_qa_pair_id(self, source_qa_pair_id):
        """Sets the source_qa_pair_id of this AskQuestionReq.

        语料ID

        :param source_qa_pair_id: The source_qa_pair_id of this AskQuestionReq.
        :type source_qa_pair_id: str
        """
        self._source_qa_pair_id = source_qa_pair_id

    @property
    def operate_type(self):
        """Gets the operate_type of this AskQuestionReq.

        操作类型:0-手动输入，1-单击热点问题，2-单击猜你想问，3-单击推荐问题，4-单击问题提示

        :return: The operate_type of this AskQuestionReq.
        :rtype: int
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        """Sets the operate_type of this AskQuestionReq.

        操作类型:0-手动输入，1-单击热点问题，2-单击猜你想问，3-单击推荐问题，4-单击问题提示

        :param operate_type: The operate_type of this AskQuestionReq.
        :type operate_type: int
        """
        self._operate_type = operate_type

    @property
    def threshold_enable(self):
        """Gets the threshold_enable of this AskQuestionReq.

        是否启用内部阈值开关

        :return: The threshold_enable of this AskQuestionReq.
        :rtype: str
        """
        return self._threshold_enable

    @threshold_enable.setter
    def threshold_enable(self, threshold_enable):
        """Sets the threshold_enable of this AskQuestionReq.

        是否启用内部阈值开关

        :param threshold_enable: The threshold_enable of this AskQuestionReq.
        :type threshold_enable: str
        """
        self._threshold_enable = threshold_enable

    @property
    def product_type_id(self):
        """Gets the product_type_id of this AskQuestionReq.

        产品类型id

        :return: The product_type_id of this AskQuestionReq.
        :rtype: str
        """
        return self._product_type_id

    @product_type_id.setter
    def product_type_id(self, product_type_id):
        """Sets the product_type_id of this AskQuestionReq.

        产品类型id

        :param product_type_id: The product_type_id of this AskQuestionReq.
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
        if not isinstance(other, AskQuestionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
