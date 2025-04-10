# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EntitySentimentReq:

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
        'entity': 'str',
        'type': 'int'
    }

    attribute_map = {
        'content': 'content',
        'entity': 'entity',
        'type': 'type'
    }

    def __init__(self, content=None, entity=None, type=None):
        r"""EntitySentimentReq

        The model defined in huaweicloud sdk

        :param content: 请求文本。文本编码要求为utf-8，仅支持中文实体情感分析。 限定content+entity长度为512以内，长度超过512时，只检测前512个字符。 
        :type content: str
        :param entity: 请求实体。文本编码要求为utf-8.仅支持中文实体情感分析。 限定content+entity长度为512以内，长度超过512时，只检测前512个字符。
        :type entity: str
        :param type: 取值如下： 3 金融领域
        :type type: int
        """
        
        

        self._content = None
        self._entity = None
        self._type = None
        self.discriminator = None

        self.content = content
        self.entity = entity
        self.type = type

    @property
    def content(self):
        r"""Gets the content of this EntitySentimentReq.

        请求文本。文本编码要求为utf-8，仅支持中文实体情感分析。 限定content+entity长度为512以内，长度超过512时，只检测前512个字符。 

        :return: The content of this EntitySentimentReq.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this EntitySentimentReq.

        请求文本。文本编码要求为utf-8，仅支持中文实体情感分析。 限定content+entity长度为512以内，长度超过512时，只检测前512个字符。 

        :param content: The content of this EntitySentimentReq.
        :type content: str
        """
        self._content = content

    @property
    def entity(self):
        r"""Gets the entity of this EntitySentimentReq.

        请求实体。文本编码要求为utf-8.仅支持中文实体情感分析。 限定content+entity长度为512以内，长度超过512时，只检测前512个字符。

        :return: The entity of this EntitySentimentReq.
        :rtype: str
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        r"""Sets the entity of this EntitySentimentReq.

        请求实体。文本编码要求为utf-8.仅支持中文实体情感分析。 限定content+entity长度为512以内，长度超过512时，只检测前512个字符。

        :param entity: The entity of this EntitySentimentReq.
        :type entity: str
        """
        self._entity = entity

    @property
    def type(self):
        r"""Gets the type of this EntitySentimentReq.

        取值如下： 3 金融领域

        :return: The type of this EntitySentimentReq.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this EntitySentimentReq.

        取值如下： 3 金融领域

        :param type: The type of this EntitySentimentReq.
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
        if not isinstance(other, EntitySentimentReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
