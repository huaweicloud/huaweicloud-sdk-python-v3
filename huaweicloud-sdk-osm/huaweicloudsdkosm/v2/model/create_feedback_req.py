# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFeedbackReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'int',
        'content': 'str',
        'is_helpful': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'content': 'content',
        'is_helpful': 'is_helpful'
    }

    def __init__(self, type=None, content=None, is_helpful=None):
        r"""CreateFeedbackReq

        The model defined in huaweicloud sdk

        :param type: 任务类型，例如 ecs诊断任务 1，rds诊断任务 2
        :type type: int
        :param content: 反馈内容
        :type content: str
        :param is_helpful: 是否有帮助
        :type is_helpful: bool
        """
        
        

        self._type = None
        self._content = None
        self._is_helpful = None
        self.discriminator = None

        self.type = type
        if content is not None:
            self.content = content
        self.is_helpful = is_helpful

    @property
    def type(self):
        r"""Gets the type of this CreateFeedbackReq.

        任务类型，例如 ecs诊断任务 1，rds诊断任务 2

        :return: The type of this CreateFeedbackReq.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateFeedbackReq.

        任务类型，例如 ecs诊断任务 1，rds诊断任务 2

        :param type: The type of this CreateFeedbackReq.
        :type type: int
        """
        self._type = type

    @property
    def content(self):
        r"""Gets the content of this CreateFeedbackReq.

        反馈内容

        :return: The content of this CreateFeedbackReq.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this CreateFeedbackReq.

        反馈内容

        :param content: The content of this CreateFeedbackReq.
        :type content: str
        """
        self._content = content

    @property
    def is_helpful(self):
        r"""Gets the is_helpful of this CreateFeedbackReq.

        是否有帮助

        :return: The is_helpful of this CreateFeedbackReq.
        :rtype: bool
        """
        return self._is_helpful

    @is_helpful.setter
    def is_helpful(self, is_helpful):
        r"""Sets the is_helpful of this CreateFeedbackReq.

        是否有帮助

        :param is_helpful: The is_helpful of this CreateFeedbackReq.
        :type is_helpful: bool
        """
        self._is_helpful = is_helpful

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
        if not isinstance(other, CreateFeedbackReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
