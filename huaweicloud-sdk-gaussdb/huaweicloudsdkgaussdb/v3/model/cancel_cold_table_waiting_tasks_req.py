# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CancelColdTableWaitingTasksReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cancel_tasks': 'list[CancelColdTableWaitingTask]'
    }

    attribute_map = {
        'cancel_tasks': 'cancel_tasks'
    }

    def __init__(self, cancel_tasks=None):
        r"""CancelColdTableWaitingTasksReq

        The model defined in huaweicloud sdk

        :param cancel_tasks: **参数解释**：  取消目标列表。  **约束限制**：  列表长度不超过50。
        :type cancel_tasks: list[:class:`huaweicloudsdkgaussdb.v3.CancelColdTableWaitingTask`]
        """
        
        

        self._cancel_tasks = None
        self.discriminator = None

        self.cancel_tasks = cancel_tasks

    @property
    def cancel_tasks(self):
        r"""Gets the cancel_tasks of this CancelColdTableWaitingTasksReq.

        **参数解释**：  取消目标列表。  **约束限制**：  列表长度不超过50。

        :return: The cancel_tasks of this CancelColdTableWaitingTasksReq.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.CancelColdTableWaitingTask`]
        """
        return self._cancel_tasks

    @cancel_tasks.setter
    def cancel_tasks(self, cancel_tasks):
        r"""Sets the cancel_tasks of this CancelColdTableWaitingTasksReq.

        **参数解释**：  取消目标列表。  **约束限制**：  列表长度不超过50。

        :param cancel_tasks: The cancel_tasks of this CancelColdTableWaitingTasksReq.
        :type cancel_tasks: list[:class:`huaweicloudsdkgaussdb.v3.CancelColdTableWaitingTask`]
        """
        self._cancel_tasks = cancel_tasks

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CancelColdTableWaitingTasksReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
