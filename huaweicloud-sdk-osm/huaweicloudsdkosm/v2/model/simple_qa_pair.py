# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SimpleQaPair:

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
        'qa_pair_id': 'str'
    }

    attribute_map = {
        'question': 'question',
        'domain': 'domain',
        'qa_pair_id': 'qa_pair_id'
    }

    def __init__(self, question=None, domain=None, qa_pair_id=None):
        """SimpleQaPair

        The model defined in huaweicloud sdk

        :param question: 问题
        :type question: str
        :param domain: 主题
        :type domain: str
        :param qa_pair_id: 语料Id
        :type qa_pair_id: str
        """
        
        

        self._question = None
        self._domain = None
        self._qa_pair_id = None
        self.discriminator = None

        if question is not None:
            self.question = question
        if domain is not None:
            self.domain = domain
        if qa_pair_id is not None:
            self.qa_pair_id = qa_pair_id

    @property
    def question(self):
        """Gets the question of this SimpleQaPair.

        问题

        :return: The question of this SimpleQaPair.
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question):
        """Sets the question of this SimpleQaPair.

        问题

        :param question: The question of this SimpleQaPair.
        :type question: str
        """
        self._question = question

    @property
    def domain(self):
        """Gets the domain of this SimpleQaPair.

        主题

        :return: The domain of this SimpleQaPair.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this SimpleQaPair.

        主题

        :param domain: The domain of this SimpleQaPair.
        :type domain: str
        """
        self._domain = domain

    @property
    def qa_pair_id(self):
        """Gets the qa_pair_id of this SimpleQaPair.

        语料Id

        :return: The qa_pair_id of this SimpleQaPair.
        :rtype: str
        """
        return self._qa_pair_id

    @qa_pair_id.setter
    def qa_pair_id(self, qa_pair_id):
        """Sets the qa_pair_id of this SimpleQaPair.

        语料Id

        :param qa_pair_id: The qa_pair_id of this SimpleQaPair.
        :type qa_pair_id: str
        """
        self._qa_pair_id = qa_pair_id

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
        if not isinstance(other, SimpleQaPair):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
