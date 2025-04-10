# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SendAimBatchDifferentMessagesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'status': 'str',
        'result': 'list[SmsDetailResponse]'
    }

    attribute_map = {
        'task_id': 'task_id',
        'status': 'status',
        'result': 'result'
    }

    def __init__(self, task_id=None, status=None, result=None):
        r"""SendAimBatchDifferentMessagesResponse

        The model defined in huaweicloud sdk

        :param task_id: 任务ID。
        :type task_id: str
        :param status: 任务状态。  - Success：发送成功 - Failed：发送失败  &gt; 此状态仅代表任务提交状态，不代表智能信息发送结果。用户手机接收智能信息结果请以收到的回执结果为准，也可通过查询智能信息发送明细API获取或登录KooMessage控制台查看。
        :type status: str
        :param result: 短信ID列表，当目标号码存在多个时，每个号码都会返回一个SmsID。  当返回异常响应时不携带此字段。
        :type result: list[:class:`huaweicloudsdkkoomessage.v1.SmsDetailResponse`]
        """
        
        super(SendAimBatchDifferentMessagesResponse, self).__init__()

        self._task_id = None
        self._status = None
        self._result = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if status is not None:
            self.status = status
        if result is not None:
            self.result = result

    @property
    def task_id(self):
        r"""Gets the task_id of this SendAimBatchDifferentMessagesResponse.

        任务ID。

        :return: The task_id of this SendAimBatchDifferentMessagesResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this SendAimBatchDifferentMessagesResponse.

        任务ID。

        :param task_id: The task_id of this SendAimBatchDifferentMessagesResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def status(self):
        r"""Gets the status of this SendAimBatchDifferentMessagesResponse.

        任务状态。  - Success：发送成功 - Failed：发送失败  > 此状态仅代表任务提交状态，不代表智能信息发送结果。用户手机接收智能信息结果请以收到的回执结果为准，也可通过查询智能信息发送明细API获取或登录KooMessage控制台查看。

        :return: The status of this SendAimBatchDifferentMessagesResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SendAimBatchDifferentMessagesResponse.

        任务状态。  - Success：发送成功 - Failed：发送失败  > 此状态仅代表任务提交状态，不代表智能信息发送结果。用户手机接收智能信息结果请以收到的回执结果为准，也可通过查询智能信息发送明细API获取或登录KooMessage控制台查看。

        :param status: The status of this SendAimBatchDifferentMessagesResponse.
        :type status: str
        """
        self._status = status

    @property
    def result(self):
        r"""Gets the result of this SendAimBatchDifferentMessagesResponse.

        短信ID列表，当目标号码存在多个时，每个号码都会返回一个SmsID。  当返回异常响应时不携带此字段。

        :return: The result of this SendAimBatchDifferentMessagesResponse.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.SmsDetailResponse`]
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this SendAimBatchDifferentMessagesResponse.

        短信ID列表，当目标号码存在多个时，每个号码都会返回一个SmsID。  当返回异常响应时不携带此字段。

        :param result: The result of this SendAimBatchDifferentMessagesResponse.
        :type result: list[:class:`huaweicloudsdkkoomessage.v1.SmsDetailResponse`]
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
        if not isinstance(other, SendAimBatchDifferentMessagesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
