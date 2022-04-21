# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunEntitySentimentResponse(SdkResponse):

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
        'label': 'int',
        'confidence': 'float',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'content': 'content',
        'entity': 'entity',
        'label': 'label',
        'confidence': 'confidence',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, content=None, entity=None, label=None, confidence=None, error_code=None, error_msg=None):
        """RunEntitySentimentResponse

        The model defined in huaweicloud sdk

        :param content: 响应的文本
        :type content: str
        :param entity: 响应的实体
        :type entity: str
        :param label: 响应的情感标签，0表示负面，1表示非负面，2表示不相关
        :type label: int
        :param confidence: 该实体在文本中的情感label的置信度
        :type confidence: float
        :param error_code: 调用失败时的错误码，具体请参见错误码。调用成功时无此字段。
        :type error_code: str
        :param error_msg: 调用失败时的错误信息。调用成功时无此字段。
        :type error_msg: str
        """
        
        super(RunEntitySentimentResponse, self).__init__()

        self._content = None
        self._entity = None
        self._label = None
        self._confidence = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if entity is not None:
            self.entity = entity
        if label is not None:
            self.label = label
        if confidence is not None:
            self.confidence = confidence
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def content(self):
        """Gets the content of this RunEntitySentimentResponse.

        响应的文本

        :return: The content of this RunEntitySentimentResponse.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this RunEntitySentimentResponse.

        响应的文本

        :param content: The content of this RunEntitySentimentResponse.
        :type content: str
        """
        self._content = content

    @property
    def entity(self):
        """Gets the entity of this RunEntitySentimentResponse.

        响应的实体

        :return: The entity of this RunEntitySentimentResponse.
        :rtype: str
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this RunEntitySentimentResponse.

        响应的实体

        :param entity: The entity of this RunEntitySentimentResponse.
        :type entity: str
        """
        self._entity = entity

    @property
    def label(self):
        """Gets the label of this RunEntitySentimentResponse.

        响应的情感标签，0表示负面，1表示非负面，2表示不相关

        :return: The label of this RunEntitySentimentResponse.
        :rtype: int
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this RunEntitySentimentResponse.

        响应的情感标签，0表示负面，1表示非负面，2表示不相关

        :param label: The label of this RunEntitySentimentResponse.
        :type label: int
        """
        self._label = label

    @property
    def confidence(self):
        """Gets the confidence of this RunEntitySentimentResponse.

        该实体在文本中的情感label的置信度

        :return: The confidence of this RunEntitySentimentResponse.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this RunEntitySentimentResponse.

        该实体在文本中的情感label的置信度

        :param confidence: The confidence of this RunEntitySentimentResponse.
        :type confidence: float
        """
        self._confidence = confidence

    @property
    def error_code(self):
        """Gets the error_code of this RunEntitySentimentResponse.

        调用失败时的错误码，具体请参见错误码。调用成功时无此字段。

        :return: The error_code of this RunEntitySentimentResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this RunEntitySentimentResponse.

        调用失败时的错误码，具体请参见错误码。调用成功时无此字段。

        :param error_code: The error_code of this RunEntitySentimentResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this RunEntitySentimentResponse.

        调用失败时的错误信息。调用成功时无此字段。

        :return: The error_msg of this RunEntitySentimentResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this RunEntitySentimentResponse.

        调用失败时的错误信息。调用成功时无此字段。

        :param error_msg: The error_msg of this RunEntitySentimentResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, RunEntitySentimentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
