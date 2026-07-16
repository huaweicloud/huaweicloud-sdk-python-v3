# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkflowSchedulePolicies:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'on_failure': 'str',
        'on_running': 'str'
    }

    attribute_map = {
        'on_failure': 'on_failure',
        'on_running': 'on_running'
    }

    def __init__(self, on_failure=None, on_running=None):
        r"""WorkflowSchedulePolicies

        The model defined in huaweicloud sdk

        :param on_failure: 定时调度策略中的标记，失败时触发。
        :type on_failure: str
        :param on_running: 定时调度策略中的标记，running时触发。
        :type on_running: str
        """
        
        

        self._on_failure = None
        self._on_running = None
        self.discriminator = None

        if on_failure is not None:
            self.on_failure = on_failure
        if on_running is not None:
            self.on_running = on_running

    @property
    def on_failure(self):
        r"""Gets the on_failure of this WorkflowSchedulePolicies.

        定时调度策略中的标记，失败时触发。

        :return: The on_failure of this WorkflowSchedulePolicies.
        :rtype: str
        """
        return self._on_failure

    @on_failure.setter
    def on_failure(self, on_failure):
        r"""Sets the on_failure of this WorkflowSchedulePolicies.

        定时调度策略中的标记，失败时触发。

        :param on_failure: The on_failure of this WorkflowSchedulePolicies.
        :type on_failure: str
        """
        self._on_failure = on_failure

    @property
    def on_running(self):
        r"""Gets the on_running of this WorkflowSchedulePolicies.

        定时调度策略中的标记，running时触发。

        :return: The on_running of this WorkflowSchedulePolicies.
        :rtype: str
        """
        return self._on_running

    @on_running.setter
    def on_running(self, on_running):
        r"""Sets the on_running of this WorkflowSchedulePolicies.

        定时调度策略中的标记，running时触发。

        :param on_running: The on_running of this WorkflowSchedulePolicies.
        :type on_running: str
        """
        self._on_running = on_running

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
        if not isinstance(other, WorkflowSchedulePolicies):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
