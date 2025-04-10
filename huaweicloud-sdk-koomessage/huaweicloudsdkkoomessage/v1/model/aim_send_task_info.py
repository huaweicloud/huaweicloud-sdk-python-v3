# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AIMSendTaskInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_name': 'str',
        'sms_channel': 'AIMSendTaskSmsChannel',
        'resolve_task': 'AIMResolveTaskMode'
    }

    attribute_map = {
        'task_name': 'task_name',
        'sms_channel': 'sms_channel',
        'resolve_task': 'resolve_task'
    }

    def __init__(self, task_name=None, sms_channel=None, resolve_task=None):
        r"""AIMSendTaskInfo

        The model defined in huaweicloud sdk

        :param task_name: 智能信息发送任务名称。
        :type task_name: str
        :param sms_channel: 
        :type sms_channel: :class:`huaweicloudsdkkoomessage.v1.AIMSendTaskSmsChannel`
        :param resolve_task: 
        :type resolve_task: :class:`huaweicloudsdkkoomessage.v1.AIMResolveTaskMode`
        """
        
        

        self._task_name = None
        self._sms_channel = None
        self._resolve_task = None
        self.discriminator = None

        if task_name is not None:
            self.task_name = task_name
        if sms_channel is not None:
            self.sms_channel = sms_channel
        if resolve_task is not None:
            self.resolve_task = resolve_task

    @property
    def task_name(self):
        r"""Gets the task_name of this AIMSendTaskInfo.

        智能信息发送任务名称。

        :return: The task_name of this AIMSendTaskInfo.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this AIMSendTaskInfo.

        智能信息发送任务名称。

        :param task_name: The task_name of this AIMSendTaskInfo.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def sms_channel(self):
        r"""Gets the sms_channel of this AIMSendTaskInfo.

        :return: The sms_channel of this AIMSendTaskInfo.
        :rtype: :class:`huaweicloudsdkkoomessage.v1.AIMSendTaskSmsChannel`
        """
        return self._sms_channel

    @sms_channel.setter
    def sms_channel(self, sms_channel):
        r"""Sets the sms_channel of this AIMSendTaskInfo.

        :param sms_channel: The sms_channel of this AIMSendTaskInfo.
        :type sms_channel: :class:`huaweicloudsdkkoomessage.v1.AIMSendTaskSmsChannel`
        """
        self._sms_channel = sms_channel

    @property
    def resolve_task(self):
        r"""Gets the resolve_task of this AIMSendTaskInfo.

        :return: The resolve_task of this AIMSendTaskInfo.
        :rtype: :class:`huaweicloudsdkkoomessage.v1.AIMResolveTaskMode`
        """
        return self._resolve_task

    @resolve_task.setter
    def resolve_task(self, resolve_task):
        r"""Sets the resolve_task of this AIMSendTaskInfo.

        :param resolve_task: The resolve_task of this AIMSendTaskInfo.
        :type resolve_task: :class:`huaweicloudsdkkoomessage.v1.AIMResolveTaskMode`
        """
        self._resolve_task = resolve_task

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
        if not isinstance(other, AIMSendTaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
