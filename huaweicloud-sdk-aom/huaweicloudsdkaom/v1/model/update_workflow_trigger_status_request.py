# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateWorkflowTriggerStatusRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workflow_id': 'str',
        'action': 'str'
    }

    attribute_map = {
        'workflow_id': 'workflow_id',
        'action': 'action'
    }

    def __init__(self, workflow_id=None, action=None):
        r"""UpdateWorkflowTriggerStatusRequest

        The model defined in huaweicloud sdk

        :param workflow_id: 任务id，待修改任务的id。
        :type workflow_id: str
        :param action: 启动或暂停任务的定时执行。enable为开启定时任务，disable为关闭定时任务
        :type action: str
        """
        
        

        self._workflow_id = None
        self._action = None
        self.discriminator = None

        self.workflow_id = workflow_id
        self.action = action

    @property
    def workflow_id(self):
        r"""Gets the workflow_id of this UpdateWorkflowTriggerStatusRequest.

        任务id，待修改任务的id。

        :return: The workflow_id of this UpdateWorkflowTriggerStatusRequest.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        r"""Sets the workflow_id of this UpdateWorkflowTriggerStatusRequest.

        任务id，待修改任务的id。

        :param workflow_id: The workflow_id of this UpdateWorkflowTriggerStatusRequest.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def action(self):
        r"""Gets the action of this UpdateWorkflowTriggerStatusRequest.

        启动或暂停任务的定时执行。enable为开启定时任务，disable为关闭定时任务

        :return: The action of this UpdateWorkflowTriggerStatusRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this UpdateWorkflowTriggerStatusRequest.

        启动或暂停任务的定时执行。enable为开启定时任务，disable为关闭定时任务

        :param action: The action of this UpdateWorkflowTriggerStatusRequest.
        :type action: str
        """
        self._action = action

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
        if not isinstance(other, UpdateWorkflowTriggerStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
