# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RemediationExecutionStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_key': 'RemediationResourceKey',
        'invocation_time': 'str',
        'state': 'str',
        'message': 'str'
    }

    attribute_map = {
        'resource_key': 'resource_key',
        'invocation_time': 'invocation_time',
        'state': 'state',
        'message': 'message'
    }

    def __init__(self, resource_key=None, invocation_time=None, state=None, message=None):
        r"""RemediationExecutionStatus

        The model defined in huaweicloud sdk

        :param resource_key: 
        :type resource_key: :class:`huaweicloudsdkconfig.v1.RemediationResourceKey`
        :param invocation_time: 补救执行的开始时间。
        :type invocation_time: str
        :param state: 合规规则修正执行的状态。
        :type state: str
        :param message: 合规规则修正执行的信息。
        :type message: str
        """
        
        

        self._resource_key = None
        self._invocation_time = None
        self._state = None
        self._message = None
        self.discriminator = None

        if resource_key is not None:
            self.resource_key = resource_key
        if invocation_time is not None:
            self.invocation_time = invocation_time
        if state is not None:
            self.state = state
        if message is not None:
            self.message = message

    @property
    def resource_key(self):
        r"""Gets the resource_key of this RemediationExecutionStatus.

        :return: The resource_key of this RemediationExecutionStatus.
        :rtype: :class:`huaweicloudsdkconfig.v1.RemediationResourceKey`
        """
        return self._resource_key

    @resource_key.setter
    def resource_key(self, resource_key):
        r"""Sets the resource_key of this RemediationExecutionStatus.

        :param resource_key: The resource_key of this RemediationExecutionStatus.
        :type resource_key: :class:`huaweicloudsdkconfig.v1.RemediationResourceKey`
        """
        self._resource_key = resource_key

    @property
    def invocation_time(self):
        r"""Gets the invocation_time of this RemediationExecutionStatus.

        补救执行的开始时间。

        :return: The invocation_time of this RemediationExecutionStatus.
        :rtype: str
        """
        return self._invocation_time

    @invocation_time.setter
    def invocation_time(self, invocation_time):
        r"""Sets the invocation_time of this RemediationExecutionStatus.

        补救执行的开始时间。

        :param invocation_time: The invocation_time of this RemediationExecutionStatus.
        :type invocation_time: str
        """
        self._invocation_time = invocation_time

    @property
    def state(self):
        r"""Gets the state of this RemediationExecutionStatus.

        合规规则修正执行的状态。

        :return: The state of this RemediationExecutionStatus.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this RemediationExecutionStatus.

        合规规则修正执行的状态。

        :param state: The state of this RemediationExecutionStatus.
        :type state: str
        """
        self._state = state

    @property
    def message(self):
        r"""Gets the message of this RemediationExecutionStatus.

        合规规则修正执行的信息。

        :return: The message of this RemediationExecutionStatus.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this RemediationExecutionStatus.

        合规规则修正执行的信息。

        :param message: The message of this RemediationExecutionStatus.
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
        if not isinstance(other, RemediationExecutionStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
