# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtendQuestion:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content': 'str',
        'score': 'float'
    }

    attribute_map = {
        'content': 'content',
        'score': 'score'
    }

    def __init__(self, content=None, score=None):
        """ExtendQuestion

        The model defined in huaweicloud sdk

        :param content: 扩展问内容
        :type content: str
        :param score: 分值
        :type score: float
        """
        
        

        self._content = None
        self._score = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if score is not None:
            self.score = score

    @property
    def content(self):
        """Gets the content of this ExtendQuestion.

        扩展问内容

        :return: The content of this ExtendQuestion.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ExtendQuestion.

        扩展问内容

        :param content: The content of this ExtendQuestion.
        :type content: str
        """
        self._content = content

    @property
    def score(self):
        """Gets the score of this ExtendQuestion.

        分值

        :return: The score of this ExtendQuestion.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this ExtendQuestion.

        分值

        :param score: The score of this ExtendQuestion.
        :type score: float
        """
        self._score = score

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
        if not isinstance(other, ExtendQuestion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
