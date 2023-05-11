# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RelevanceQapair:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'link': 'str',
        'question': 'str',
        'qa_pair_id': 'str'
    }

    attribute_map = {
        'link': 'link',
        'question': 'question',
        'qa_pair_id': 'qa_pair_id'
    }

    def __init__(self, link=None, question=None, qa_pair_id=None):
        """RelevanceQapair

        The model defined in huaweicloud sdk

        :param link: 链接
        :type link: str
        :param question: 标准问题
        :type question: str
        :param qa_pair_id: 标准问题Id
        :type qa_pair_id: str
        """
        
        

        self._link = None
        self._question = None
        self._qa_pair_id = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if question is not None:
            self.question = question
        if qa_pair_id is not None:
            self.qa_pair_id = qa_pair_id

    @property
    def link(self):
        """Gets the link of this RelevanceQapair.

        链接

        :return: The link of this RelevanceQapair.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this RelevanceQapair.

        链接

        :param link: The link of this RelevanceQapair.
        :type link: str
        """
        self._link = link

    @property
    def question(self):
        """Gets the question of this RelevanceQapair.

        标准问题

        :return: The question of this RelevanceQapair.
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question):
        """Sets the question of this RelevanceQapair.

        标准问题

        :param question: The question of this RelevanceQapair.
        :type question: str
        """
        self._question = question

    @property
    def qa_pair_id(self):
        """Gets the qa_pair_id of this RelevanceQapair.

        标准问题Id

        :return: The qa_pair_id of this RelevanceQapair.
        :rtype: str
        """
        return self._qa_pair_id

    @qa_pair_id.setter
    def qa_pair_id(self, qa_pair_id):
        """Sets the qa_pair_id of this RelevanceQapair.

        标准问题Id

        :param qa_pair_id: The qa_pair_id of this RelevanceQapair.
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
        if not isinstance(other, RelevanceQapair):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
