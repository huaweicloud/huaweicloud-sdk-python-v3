# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateTaskStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'message': 'str',
        'extend': 'object',
        'result': 'list[BatchUpdateTaskStatusResponseBodyResult]'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'extend': 'extend',
        'result': 'result'
    }

    def __init__(self, code=None, message=None, extend=None, result=None):
        """BatchUpdateTaskStatusResponse

        The model defined in huaweicloud sdk

        :param code: 响应码
        :type code: str
        :param message: 响应消息
        :type message: str
        :param extend: 扩展字段
        :type extend: object
        :param result: 批量启停任务响应结果
        :type result: list[:class:`huaweicloudsdkcpts.v1.BatchUpdateTaskStatusResponseBodyResult`]
        """
        
        super(BatchUpdateTaskStatusResponse, self).__init__()

        self._code = None
        self._message = None
        self._extend = None
        self._result = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if extend is not None:
            self.extend = extend
        if result is not None:
            self.result = result

    @property
    def code(self):
        """Gets the code of this BatchUpdateTaskStatusResponse.

        响应码

        :return: The code of this BatchUpdateTaskStatusResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this BatchUpdateTaskStatusResponse.

        响应码

        :param code: The code of this BatchUpdateTaskStatusResponse.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        """Gets the message of this BatchUpdateTaskStatusResponse.

        响应消息

        :return: The message of this BatchUpdateTaskStatusResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this BatchUpdateTaskStatusResponse.

        响应消息

        :param message: The message of this BatchUpdateTaskStatusResponse.
        :type message: str
        """
        self._message = message

    @property
    def extend(self):
        """Gets the extend of this BatchUpdateTaskStatusResponse.

        扩展字段

        :return: The extend of this BatchUpdateTaskStatusResponse.
        :rtype: object
        """
        return self._extend

    @extend.setter
    def extend(self, extend):
        """Sets the extend of this BatchUpdateTaskStatusResponse.

        扩展字段

        :param extend: The extend of this BatchUpdateTaskStatusResponse.
        :type extend: object
        """
        self._extend = extend

    @property
    def result(self):
        """Gets the result of this BatchUpdateTaskStatusResponse.

        批量启停任务响应结果

        :return: The result of this BatchUpdateTaskStatusResponse.
        :rtype: list[:class:`huaweicloudsdkcpts.v1.BatchUpdateTaskStatusResponseBodyResult`]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this BatchUpdateTaskStatusResponse.

        批量启停任务响应结果

        :param result: The result of this BatchUpdateTaskStatusResponse.
        :type result: list[:class:`huaweicloudsdkcpts.v1.BatchUpdateTaskStatusResponseBodyResult`]
        """
        self._result = result

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
        if not isinstance(other, BatchUpdateTaskStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
