# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AspectSentimentAdvanceRequest:

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
        'type': 'int'
    }

    attribute_map = {
        'content': 'content',
        'type': 'type'
    }

    def __init__(self, content=None, type=None):
        r"""AspectSentimentAdvanceRequest

        The model defined in huaweicloud sdk

        :param content: 待分析文本。文本编码要求为utf-8，仅支持中文。 限定4096个字符以内，建议文本长度300个字符以内。
        :type content: str
        :param type: 取值如下： 1 手机领域 2 汽车领域
        :type type: int
        """
        
        

        self._content = None
        self._type = None
        self.discriminator = None

        self.content = content
        self.type = type

    @property
    def content(self):
        r"""Gets the content of this AspectSentimentAdvanceRequest.

        待分析文本。文本编码要求为utf-8，仅支持中文。 限定4096个字符以内，建议文本长度300个字符以内。

        :return: The content of this AspectSentimentAdvanceRequest.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this AspectSentimentAdvanceRequest.

        待分析文本。文本编码要求为utf-8，仅支持中文。 限定4096个字符以内，建议文本长度300个字符以内。

        :param content: The content of this AspectSentimentAdvanceRequest.
        :type content: str
        """
        self._content = content

    @property
    def type(self):
        r"""Gets the type of this AspectSentimentAdvanceRequest.

        取值如下： 1 手机领域 2 汽车领域

        :return: The type of this AspectSentimentAdvanceRequest.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AspectSentimentAdvanceRequest.

        取值如下： 1 手机领域 2 汽车领域

        :param type: The type of this AspectSentimentAdvanceRequest.
        :type type: int
        """
        self._type = type

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
        if not isinstance(other, AspectSentimentAdvanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
