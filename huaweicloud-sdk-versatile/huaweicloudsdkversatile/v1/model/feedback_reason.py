# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FeedbackReason:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[str]',
        'content': 'str'
    }

    attribute_map = {
        'tags': 'tags',
        'content': 'content'
    }

    def __init__(self, tags=None, content=None):
        r"""FeedbackReason

        The model defined in huaweicloud sdk

        :param tags: 原因标签列表
        :type tags: list[str]
        :param content: 具体原因内容
        :type content: str
        """
        
        

        self._tags = None
        self._content = None
        self.discriminator = None

        self.tags = tags
        if content is not None:
            self.content = content

    @property
    def tags(self):
        r"""Gets the tags of this FeedbackReason.

        原因标签列表

        :return: The tags of this FeedbackReason.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this FeedbackReason.

        原因标签列表

        :param tags: The tags of this FeedbackReason.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def content(self):
        r"""Gets the content of this FeedbackReason.

        具体原因内容

        :return: The content of this FeedbackReason.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this FeedbackReason.

        具体原因内容

        :param content: The content of this FeedbackReason.
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
        if not isinstance(other, FeedbackReason):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
