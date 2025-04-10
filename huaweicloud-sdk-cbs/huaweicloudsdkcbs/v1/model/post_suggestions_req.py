# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostSuggestionsReq:

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
        'top': 'int'
    }

    attribute_map = {
        'question': 'question',
        'top': 'top'
    }

    def __init__(self, question=None, top=None):
        r"""PostSuggestionsReq

        The model defined in huaweicloud sdk

        :param question: 用户输入的问题，长度为1~512。
        :type question: str
        :param top: 最多提示条数，默认为5，取值范围[1,10]。
        :type top: int
        """
        
        

        self._question = None
        self._top = None
        self.discriminator = None

        self.question = question
        if top is not None:
            self.top = top

    @property
    def question(self):
        r"""Gets the question of this PostSuggestionsReq.

        用户输入的问题，长度为1~512。

        :return: The question of this PostSuggestionsReq.
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question):
        r"""Sets the question of this PostSuggestionsReq.

        用户输入的问题，长度为1~512。

        :param question: The question of this PostSuggestionsReq.
        :type question: str
        """
        self._question = question

    @property
    def top(self):
        r"""Gets the top of this PostSuggestionsReq.

        最多提示条数，默认为5，取值范围[1,10]。

        :return: The top of this PostSuggestionsReq.
        :rtype: int
        """
        return self._top

    @top.setter
    def top(self, top):
        r"""Sets the top of this PostSuggestionsReq.

        最多提示条数，默认为5，取值范围[1,10]。

        :param top: The top of this PostSuggestionsReq.
        :type top: int
        """
        self._top = top

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
        if not isinstance(other, PostSuggestionsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
