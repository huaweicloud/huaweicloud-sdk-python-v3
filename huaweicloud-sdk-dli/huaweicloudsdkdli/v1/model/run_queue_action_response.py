# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunQueueActionResponse(SdkResponse):

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
        'job_id': 'str',
        'queue_name': 'str',
        'result': 'bool'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'job_id': 'job_id',
        'queue_name': 'queue_name',
        'result': 'result'
    }

    def __init__(self, is_success=None, message=None, job_id=None, queue_name=None, result=None):
        """RunQueueActionResponse

        The model defined in huaweicloud sdk

        :param is_success: 请求执行是否成功。“true”表示请求执行成功。
        :type is_success: bool
        :param message: 系统提示信息，执行成功时，信息可能为空。
        :type message: str
        :param job_id: 当force为true的时候返回的jobId，可以根据job_id的状态来看最终结果
        :type job_id: str
        :param queue_name: 扩缩容的队列名称。
        :type queue_name: str
        :param result: 扩缩容结果
        :type result: bool
        """
        
        super(RunQueueActionResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._job_id = None
        self._queue_name = None
        self._result = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if job_id is not None:
            self.job_id = job_id
        if queue_name is not None:
            self.queue_name = queue_name
        if result is not None:
            self.result = result

    @property
    def is_success(self):
        """Gets the is_success of this RunQueueActionResponse.

        请求执行是否成功。“true”表示请求执行成功。

        :return: The is_success of this RunQueueActionResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this RunQueueActionResponse.

        请求执行是否成功。“true”表示请求执行成功。

        :param is_success: The is_success of this RunQueueActionResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        """Gets the message of this RunQueueActionResponse.

        系统提示信息，执行成功时，信息可能为空。

        :return: The message of this RunQueueActionResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this RunQueueActionResponse.

        系统提示信息，执行成功时，信息可能为空。

        :param message: The message of this RunQueueActionResponse.
        :type message: str
        """
        self._message = message

    @property
    def job_id(self):
        """Gets the job_id of this RunQueueActionResponse.

        当force为true的时候返回的jobId，可以根据job_id的状态来看最终结果

        :return: The job_id of this RunQueueActionResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this RunQueueActionResponse.

        当force为true的时候返回的jobId，可以根据job_id的状态来看最终结果

        :param job_id: The job_id of this RunQueueActionResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def queue_name(self):
        """Gets the queue_name of this RunQueueActionResponse.

        扩缩容的队列名称。

        :return: The queue_name of this RunQueueActionResponse.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this RunQueueActionResponse.

        扩缩容的队列名称。

        :param queue_name: The queue_name of this RunQueueActionResponse.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def result(self):
        """Gets the result of this RunQueueActionResponse.

        扩缩容结果

        :return: The result of this RunQueueActionResponse.
        :rtype: bool
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this RunQueueActionResponse.

        扩缩容结果

        :param result: The result of this RunQueueActionResponse.
        :type result: bool
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
        if not isinstance(other, RunQueueActionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
