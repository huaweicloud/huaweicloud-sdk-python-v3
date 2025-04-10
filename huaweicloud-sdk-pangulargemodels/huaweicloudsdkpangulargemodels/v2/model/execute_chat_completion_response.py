# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteChatCompletionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'created': 'int',
        'choices': 'list[ChatChoice]',
        'usage': 'CompletionUsage'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'choices': 'choices',
        'usage': 'usage'
    }

    def __init__(self, id=None, created=None, choices=None, usage=None):
        r"""ExecuteChatCompletionResponse

        The model defined in huaweicloud sdk

        :param id: 响应ID
        :type id: str
        :param created: 响应时间
        :type created: int
        :param choices: 模型回复
        :type choices: list[:class:`huaweicloudsdkpangulargemodels.v2.ChatChoice`]
        :param usage: 
        :type usage: :class:`huaweicloudsdkpangulargemodels.v2.CompletionUsage`
        """
        
        super(ExecuteChatCompletionResponse, self).__init__()

        self._id = None
        self._created = None
        self._choices = None
        self._usage = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created is not None:
            self.created = created
        if choices is not None:
            self.choices = choices
        if usage is not None:
            self.usage = usage

    @property
    def id(self):
        r"""Gets the id of this ExecuteChatCompletionResponse.

        响应ID

        :return: The id of this ExecuteChatCompletionResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ExecuteChatCompletionResponse.

        响应ID

        :param id: The id of this ExecuteChatCompletionResponse.
        :type id: str
        """
        self._id = id

    @property
    def created(self):
        r"""Gets the created of this ExecuteChatCompletionResponse.

        响应时间

        :return: The created of this ExecuteChatCompletionResponse.
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this ExecuteChatCompletionResponse.

        响应时间

        :param created: The created of this ExecuteChatCompletionResponse.
        :type created: int
        """
        self._created = created

    @property
    def choices(self):
        r"""Gets the choices of this ExecuteChatCompletionResponse.

        模型回复

        :return: The choices of this ExecuteChatCompletionResponse.
        :rtype: list[:class:`huaweicloudsdkpangulargemodels.v2.ChatChoice`]
        """
        return self._choices

    @choices.setter
    def choices(self, choices):
        r"""Sets the choices of this ExecuteChatCompletionResponse.

        模型回复

        :param choices: The choices of this ExecuteChatCompletionResponse.
        :type choices: list[:class:`huaweicloudsdkpangulargemodels.v2.ChatChoice`]
        """
        self._choices = choices

    @property
    def usage(self):
        r"""Gets the usage of this ExecuteChatCompletionResponse.

        :return: The usage of this ExecuteChatCompletionResponse.
        :rtype: :class:`huaweicloudsdkpangulargemodels.v2.CompletionUsage`
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        r"""Sets the usage of this ExecuteChatCompletionResponse.

        :param usage: The usage of this ExecuteChatCompletionResponse.
        :type usage: :class:`huaweicloudsdkpangulargemodels.v2.CompletionUsage`
        """
        self._usage = usage

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
        if not isinstance(other, ExecuteChatCompletionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
