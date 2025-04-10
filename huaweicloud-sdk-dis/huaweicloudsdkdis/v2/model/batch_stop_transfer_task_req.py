# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchStopTransferTaskReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'tasks': 'list[BatchTransferTask]'
    }

    attribute_map = {
        'action': 'action',
        'tasks': 'tasks'
    }

    def __init__(self, action=None, tasks=None):
        r"""BatchStopTransferTaskReq

        The model defined in huaweicloud sdk

        :param action: 转储任务操作，目前支持：  - stop：停止转储任务
        :type action: str
        :param tasks: 待暂停的转储任务列表。
        :type tasks: list[:class:`huaweicloudsdkdis.v2.BatchTransferTask`]
        """
        
        

        self._action = None
        self._tasks = None
        self.discriminator = None

        self.action = action
        self.tasks = tasks

    @property
    def action(self):
        r"""Gets the action of this BatchStopTransferTaskReq.

        转储任务操作，目前支持：  - stop：停止转储任务

        :return: The action of this BatchStopTransferTaskReq.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this BatchStopTransferTaskReq.

        转储任务操作，目前支持：  - stop：停止转储任务

        :param action: The action of this BatchStopTransferTaskReq.
        :type action: str
        """
        self._action = action

    @property
    def tasks(self):
        r"""Gets the tasks of this BatchStopTransferTaskReq.

        待暂停的转储任务列表。

        :return: The tasks of this BatchStopTransferTaskReq.
        :rtype: list[:class:`huaweicloudsdkdis.v2.BatchTransferTask`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        r"""Sets the tasks of this BatchStopTransferTaskReq.

        待暂停的转储任务列表。

        :param tasks: The tasks of this BatchStopTransferTaskReq.
        :type tasks: list[:class:`huaweicloudsdkdis.v2.BatchTransferTask`]
        """
        self._tasks = tasks

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
        if not isinstance(other, BatchStopTransferTaskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
