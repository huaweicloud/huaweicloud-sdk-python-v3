# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryAssociatedQuestionReq:

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
        'domains': 'list[str]'
    }

    attribute_map = {
        'question': 'question',
        'top': 'top',
        'domains': 'domains'
    }

    def __init__(self, question=None, top=None, domains=None):
        """QueryAssociatedQuestionReq

        The model defined in huaweicloud sdk

        :param question: 用户输入问题
        :type question: str
        :param top: 返回匹配度最高的数据条数
        :type top: int
        :param domains: 问答领域
        :type domains: list[str]
        """
        
        

        self._question = None
        self._top = None
        self._domains = None
        self.discriminator = None

        self.question = question
        if top is not None:
            self.top = top
        if domains is not None:
            self.domains = domains

    @property
    def question(self):
        """Gets the question of this QueryAssociatedQuestionReq.

        用户输入问题

        :return: The question of this QueryAssociatedQuestionReq.
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question):
        """Sets the question of this QueryAssociatedQuestionReq.

        用户输入问题

        :param question: The question of this QueryAssociatedQuestionReq.
        :type question: str
        """
        self._question = question

    @property
    def top(self):
        """Gets the top of this QueryAssociatedQuestionReq.

        返回匹配度最高的数据条数

        :return: The top of this QueryAssociatedQuestionReq.
        :rtype: int
        """
        return self._top

    @top.setter
    def top(self, top):
        """Sets the top of this QueryAssociatedQuestionReq.

        返回匹配度最高的数据条数

        :param top: The top of this QueryAssociatedQuestionReq.
        :type top: int
        """
        self._top = top

    @property
    def domains(self):
        """Gets the domains of this QueryAssociatedQuestionReq.

        问答领域

        :return: The domains of this QueryAssociatedQuestionReq.
        :rtype: list[str]
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        """Sets the domains of this QueryAssociatedQuestionReq.

        问答领域

        :param domains: The domains of this QueryAssociatedQuestionReq.
        :type domains: list[str]
        """
        self._domains = domains

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
        if not isinstance(other, QueryAssociatedQuestionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
