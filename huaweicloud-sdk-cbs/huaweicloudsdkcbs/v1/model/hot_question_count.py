# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HotQuestionCount:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'qa_pair_id': 'str',
        'st_question': 'str',
        'domain': 'str'
    }

    attribute_map = {
        'qa_pair_id': 'qa_pair_id',
        'st_question': 'st_question',
        'domain': 'domain'
    }

    def __init__(self, qa_pair_id=None, st_question=None, domain=None):
        """HotQuestionCount

        The model defined in huaweicloud sdk

        :param qa_pair_id: 问答对ID。
        :type qa_pair_id: str
        :param st_question: 标准问题。
        :type st_question: str
        :param domain: 标准问题所属领域。
        :type domain: str
        """
        
        

        self._qa_pair_id = None
        self._st_question = None
        self._domain = None
        self.discriminator = None

        if qa_pair_id is not None:
            self.qa_pair_id = qa_pair_id
        if st_question is not None:
            self.st_question = st_question
        if domain is not None:
            self.domain = domain

    @property
    def qa_pair_id(self):
        """Gets the qa_pair_id of this HotQuestionCount.

        问答对ID。

        :return: The qa_pair_id of this HotQuestionCount.
        :rtype: str
        """
        return self._qa_pair_id

    @qa_pair_id.setter
    def qa_pair_id(self, qa_pair_id):
        """Sets the qa_pair_id of this HotQuestionCount.

        问答对ID。

        :param qa_pair_id: The qa_pair_id of this HotQuestionCount.
        :type qa_pair_id: str
        """
        self._qa_pair_id = qa_pair_id

    @property
    def st_question(self):
        """Gets the st_question of this HotQuestionCount.

        标准问题。

        :return: The st_question of this HotQuestionCount.
        :rtype: str
        """
        return self._st_question

    @st_question.setter
    def st_question(self, st_question):
        """Sets the st_question of this HotQuestionCount.

        标准问题。

        :param st_question: The st_question of this HotQuestionCount.
        :type st_question: str
        """
        self._st_question = st_question

    @property
    def domain(self):
        """Gets the domain of this HotQuestionCount.

        标准问题所属领域。

        :return: The domain of this HotQuestionCount.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this HotQuestionCount.

        标准问题所属领域。

        :param domain: The domain of this HotQuestionCount.
        :type domain: str
        """
        self._domain = domain

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
        if not isinstance(other, HotQuestionCount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
