# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClassificationReq:

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
        'domain': 'int'
    }

    attribute_map = {
        'content': 'content',
        'domain': 'domain'
    }

    def __init__(self, content=None, domain=None):
        """ClassificationReq

        The model defined in huaweicloud sdk

        :param content: 待分析文本。文本编码要求为utf-8。 限定400个字符以内，文本长度超过400个字符时，只检测前400个字符。
        :type content: str
        :param domain: 1 广告检测
        :type domain: int
        """
        
        

        self._content = None
        self._domain = None
        self.discriminator = None

        self.content = content
        if domain is not None:
            self.domain = domain

    @property
    def content(self):
        """Gets the content of this ClassificationReq.

        待分析文本。文本编码要求为utf-8。 限定400个字符以内，文本长度超过400个字符时，只检测前400个字符。

        :return: The content of this ClassificationReq.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ClassificationReq.

        待分析文本。文本编码要求为utf-8。 限定400个字符以内，文本长度超过400个字符时，只检测前400个字符。

        :param content: The content of this ClassificationReq.
        :type content: str
        """
        self._content = content

    @property
    def domain(self):
        """Gets the domain of this ClassificationReq.

        1 广告检测

        :return: The domain of this ClassificationReq.
        :rtype: int
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ClassificationReq.

        1 广告检测

        :param domain: The domain of this ClassificationReq.
        :type domain: int
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
        if not isinstance(other, ClassificationReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
