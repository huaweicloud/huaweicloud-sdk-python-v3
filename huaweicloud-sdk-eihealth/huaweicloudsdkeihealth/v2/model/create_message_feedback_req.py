# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMessageFeedbackReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'labels': 'list[str]',
        'content': 'str'
    }

    attribute_map = {
        'type': 'type',
        'labels': 'labels',
        'content': 'content'
    }

    def __init__(self, type=None, labels=None, content=None):
        r"""CreateMessageFeedbackReq

        The model defined in huaweicloud sdk

        :param type: **参数解释**： 反馈类型。 **约束限制**： 不涉及 **取值范围**： * upvote：点赞 * downvote：点踩 * none：取消反馈 **默认取值**： 不涉及
        :type type: str
        :param labels: **参数解释**： 反馈标签。 **约束限制**： 最多支持设置10个标签。 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type labels: list[str]
        :param content: **参数解释**： 反馈内容。 **约束限制**： 不涉及 **取值范围**： 长度为[0-1000]个字符。 **默认取值**： 不涉及 
        :type content: str
        """
        
        

        self._type = None
        self._labels = None
        self._content = None
        self.discriminator = None

        self.type = type
        if labels is not None:
            self.labels = labels
        if content is not None:
            self.content = content

    @property
    def type(self):
        r"""Gets the type of this CreateMessageFeedbackReq.

        **参数解释**： 反馈类型。 **约束限制**： 不涉及 **取值范围**： * upvote：点赞 * downvote：点踩 * none：取消反馈 **默认取值**： 不涉及

        :return: The type of this CreateMessageFeedbackReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateMessageFeedbackReq.

        **参数解释**： 反馈类型。 **约束限制**： 不涉及 **取值范围**： * upvote：点赞 * downvote：点踩 * none：取消反馈 **默认取值**： 不涉及

        :param type: The type of this CreateMessageFeedbackReq.
        :type type: str
        """
        self._type = type

    @property
    def labels(self):
        r"""Gets the labels of this CreateMessageFeedbackReq.

        **参数解释**： 反馈标签。 **约束限制**： 最多支持设置10个标签。 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The labels of this CreateMessageFeedbackReq.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this CreateMessageFeedbackReq.

        **参数解释**： 反馈标签。 **约束限制**： 最多支持设置10个标签。 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param labels: The labels of this CreateMessageFeedbackReq.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def content(self):
        r"""Gets the content of this CreateMessageFeedbackReq.

        **参数解释**： 反馈内容。 **约束限制**： 不涉及 **取值范围**： 长度为[0-1000]个字符。 **默认取值**： 不涉及 

        :return: The content of this CreateMessageFeedbackReq.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this CreateMessageFeedbackReq.

        **参数解释**： 反馈内容。 **约束限制**： 不涉及 **取值范围**： 长度为[0-1000]个字符。 **默认取值**： 不涉及 

        :param content: The content of this CreateMessageFeedbackReq.
        :type content: str
        """
        self._content = content

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateMessageFeedbackReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
