# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostSentenceEmbeddingReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'sentences': 'list[str]',
        'domain': 'str'
    }

    attribute_map = {
        'sentences': 'sentences',
        'domain': 'domain'
    }

    def __init__(self, sentences=None, domain=None):
        """PostSentenceEmbeddingReq

        The model defined in huaweicloud sdk

        :param sentences: 文本列表，文本长度为1~512，列表大小为1~1000，文本编码为UTF-8。
        :type sentences: list[str]
        :param domain: 支持的领域类型，目前只支持通用领域，默认为general。
        :type domain: str
        """
        
        

        self._sentences = None
        self._domain = None
        self.discriminator = None

        self.sentences = sentences
        if domain is not None:
            self.domain = domain

    @property
    def sentences(self):
        """Gets the sentences of this PostSentenceEmbeddingReq.

        文本列表，文本长度为1~512，列表大小为1~1000，文本编码为UTF-8。

        :return: The sentences of this PostSentenceEmbeddingReq.
        :rtype: list[str]
        """
        return self._sentences

    @sentences.setter
    def sentences(self, sentences):
        """Sets the sentences of this PostSentenceEmbeddingReq.

        文本列表，文本长度为1~512，列表大小为1~1000，文本编码为UTF-8。

        :param sentences: The sentences of this PostSentenceEmbeddingReq.
        :type sentences: list[str]
        """
        self._sentences = sentences

    @property
    def domain(self):
        """Gets the domain of this PostSentenceEmbeddingReq.

        支持的领域类型，目前只支持通用领域，默认为general。

        :return: The domain of this PostSentenceEmbeddingReq.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this PostSentenceEmbeddingReq.

        支持的领域类型，目前只支持通用领域，默认为general。

        :param domain: The domain of this PostSentenceEmbeddingReq.
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
        if not isinstance(other, PostSentenceEmbeddingReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
