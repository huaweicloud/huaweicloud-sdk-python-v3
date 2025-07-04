# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListQueuesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_success': 'bool',
        'message': 'str',
        'queues': 'list[Queue]'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'queues': 'queues'
    }

    def __init__(self, is_success=None, message=None, queues=None):
        r"""ListQueuesResponse

        The model defined in huaweicloud sdk

        :param is_success: 参数解释: 请求执行是否成功。“true”表示请求执行成功 示例: true 约束限制:  无 取值范围: 无 默认取值: 无
        :type is_success: bool
        :param message: 参数解释: 系统提示信息，执行成功时，信息可能为空 示例: test 约束限制:  无 取值范围: 无 默认取值: 无
        :type message: str
        :param queues: 队列信息。
        :type queues: list[:class:`huaweicloudsdkdli.v1.Queue`]
        """
        
        super(ListQueuesResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._queues = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if queues is not None:
            self.queues = queues

    @property
    def is_success(self):
        r"""Gets the is_success of this ListQueuesResponse.

        参数解释: 请求执行是否成功。“true”表示请求执行成功 示例: true 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The is_success of this ListQueuesResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        r"""Sets the is_success of this ListQueuesResponse.

        参数解释: 请求执行是否成功。“true”表示请求执行成功 示例: true 约束限制:  无 取值范围: 无 默认取值: 无

        :param is_success: The is_success of this ListQueuesResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        r"""Gets the message of this ListQueuesResponse.

        参数解释: 系统提示信息，执行成功时，信息可能为空 示例: test 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The message of this ListQueuesResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ListQueuesResponse.

        参数解释: 系统提示信息，执行成功时，信息可能为空 示例: test 约束限制:  无 取值范围: 无 默认取值: 无

        :param message: The message of this ListQueuesResponse.
        :type message: str
        """
        self._message = message

    @property
    def queues(self):
        r"""Gets the queues of this ListQueuesResponse.

        队列信息。

        :return: The queues of this ListQueuesResponse.
        :rtype: list[:class:`huaweicloudsdkdli.v1.Queue`]
        """
        return self._queues

    @queues.setter
    def queues(self, queues):
        r"""Sets the queues of this ListQueuesResponse.

        队列信息。

        :param queues: The queues of this ListQueuesResponse.
        :type queues: list[:class:`huaweicloudsdkdli.v1.Queue`]
        """
        self._queues = queues

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
        if not isinstance(other, ListQueuesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
