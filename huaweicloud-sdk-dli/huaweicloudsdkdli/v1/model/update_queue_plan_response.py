# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateQueuePlanResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'queue_name': 'str',
        'plan_id': 'int',
        'is_success': 'bool',
        'message': 'str'
    }

    attribute_map = {
        'queue_name': 'queue_name',
        'plan_id': 'plan_id',
        'is_success': 'is_success',
        'message': 'message'
    }

    def __init__(self, queue_name=None, plan_id=None, is_success=None, message=None):
        r"""UpdateQueuePlanResponse

        The model defined in huaweicloud sdk

        :param queue_name: 定时扩缩容计划对应的队列名称
        :type queue_name: str
        :param plan_id: 扩缩容计划的ID编号
        :type plan_id: int
        :param is_success: 请求执行是否成功。“true”表示请求执行成功。
        :type is_success: bool
        :param message: 系统提示信息，执行成功时，信息可能为空。
        :type message: str
        """
        
        super(UpdateQueuePlanResponse, self).__init__()

        self._queue_name = None
        self._plan_id = None
        self._is_success = None
        self._message = None
        self.discriminator = None

        if queue_name is not None:
            self.queue_name = queue_name
        if plan_id is not None:
            self.plan_id = plan_id
        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message

    @property
    def queue_name(self):
        r"""Gets the queue_name of this UpdateQueuePlanResponse.

        定时扩缩容计划对应的队列名称

        :return: The queue_name of this UpdateQueuePlanResponse.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        r"""Sets the queue_name of this UpdateQueuePlanResponse.

        定时扩缩容计划对应的队列名称

        :param queue_name: The queue_name of this UpdateQueuePlanResponse.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def plan_id(self):
        r"""Gets the plan_id of this UpdateQueuePlanResponse.

        扩缩容计划的ID编号

        :return: The plan_id of this UpdateQueuePlanResponse.
        :rtype: int
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        r"""Sets the plan_id of this UpdateQueuePlanResponse.

        扩缩容计划的ID编号

        :param plan_id: The plan_id of this UpdateQueuePlanResponse.
        :type plan_id: int
        """
        self._plan_id = plan_id

    @property
    def is_success(self):
        r"""Gets the is_success of this UpdateQueuePlanResponse.

        请求执行是否成功。“true”表示请求执行成功。

        :return: The is_success of this UpdateQueuePlanResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        r"""Sets the is_success of this UpdateQueuePlanResponse.

        请求执行是否成功。“true”表示请求执行成功。

        :param is_success: The is_success of this UpdateQueuePlanResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        r"""Gets the message of this UpdateQueuePlanResponse.

        系统提示信息，执行成功时，信息可能为空。

        :return: The message of this UpdateQueuePlanResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this UpdateQueuePlanResponse.

        系统提示信息，执行成功时，信息可能为空。

        :param message: The message of this UpdateQueuePlanResponse.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, UpdateQueuePlanResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
