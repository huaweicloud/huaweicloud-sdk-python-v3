# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkflowStepPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'poll_interval_seconds': 'str',
        'max_execution_minutes': 'str'
    }

    attribute_map = {
        'poll_interval_seconds': 'poll_interval_seconds',
        'max_execution_minutes': 'max_execution_minutes'
    }

    def __init__(self, poll_interval_seconds=None, max_execution_minutes=None):
        r"""WorkflowStepPolicy

        The model defined in huaweicloud sdk

        :param poll_interval_seconds: 节点执行间隔。
        :type poll_interval_seconds: str
        :param max_execution_minutes: 最大执行时间。
        :type max_execution_minutes: str
        """
        
        

        self._poll_interval_seconds = None
        self._max_execution_minutes = None
        self.discriminator = None

        if poll_interval_seconds is not None:
            self.poll_interval_seconds = poll_interval_seconds
        if max_execution_minutes is not None:
            self.max_execution_minutes = max_execution_minutes

    @property
    def poll_interval_seconds(self):
        r"""Gets the poll_interval_seconds of this WorkflowStepPolicy.

        节点执行间隔。

        :return: The poll_interval_seconds of this WorkflowStepPolicy.
        :rtype: str
        """
        return self._poll_interval_seconds

    @poll_interval_seconds.setter
    def poll_interval_seconds(self, poll_interval_seconds):
        r"""Sets the poll_interval_seconds of this WorkflowStepPolicy.

        节点执行间隔。

        :param poll_interval_seconds: The poll_interval_seconds of this WorkflowStepPolicy.
        :type poll_interval_seconds: str
        """
        self._poll_interval_seconds = poll_interval_seconds

    @property
    def max_execution_minutes(self):
        r"""Gets the max_execution_minutes of this WorkflowStepPolicy.

        最大执行时间。

        :return: The max_execution_minutes of this WorkflowStepPolicy.
        :rtype: str
        """
        return self._max_execution_minutes

    @max_execution_minutes.setter
    def max_execution_minutes(self, max_execution_minutes):
        r"""Sets the max_execution_minutes of this WorkflowStepPolicy.

        最大执行时间。

        :param max_execution_minutes: The max_execution_minutes of this WorkflowStepPolicy.
        :type max_execution_minutes: str
        """
        self._max_execution_minutes = max_execution_minutes

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
        if not isinstance(other, WorkflowStepPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
