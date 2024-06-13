# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RemediationExecution:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'automatic': 'bool',
        'resource_id': 'str',
        'resource_name': 'str',
        'resource_provider': 'str',
        'resource_type': 'str',
        'invocation_time': 'str',
        'state': 'str',
        'message': 'str'
    }

    attribute_map = {
        'automatic': 'automatic',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'resource_provider': 'resource_provider',
        'resource_type': 'resource_type',
        'invocation_time': 'invocation_time',
        'state': 'state',
        'message': 'message'
    }

    def __init__(self, automatic=None, resource_id=None, resource_name=None, resource_provider=None, resource_type=None, invocation_time=None, state=None, message=None):
        """RemediationExecution

        The model defined in huaweicloud sdk

        :param automatic: 是否为自动修正。
        :type automatic: bool
        :param resource_id: 资源ID。
        :type resource_id: str
        :param resource_name: 资源名称。
        :type resource_name: str
        :param resource_provider: 云服务名称。
        :type resource_provider: str
        :param resource_type: 资源类型。
        :type resource_type: str
        :param invocation_time: 补救执行的开始时间。
        :type invocation_time: str
        :param state: 合规规则修正执行的状态。
        :type state: str
        :param message: 合规规则修正执行的信息。
        :type message: str
        """
        
        

        self._automatic = None
        self._resource_id = None
        self._resource_name = None
        self._resource_provider = None
        self._resource_type = None
        self._invocation_time = None
        self._state = None
        self._message = None
        self.discriminator = None

        if automatic is not None:
            self.automatic = automatic
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_provider is not None:
            self.resource_provider = resource_provider
        if resource_type is not None:
            self.resource_type = resource_type
        if invocation_time is not None:
            self.invocation_time = invocation_time
        if state is not None:
            self.state = state
        if message is not None:
            self.message = message

    @property
    def automatic(self):
        """Gets the automatic of this RemediationExecution.

        是否为自动修正。

        :return: The automatic of this RemediationExecution.
        :rtype: bool
        """
        return self._automatic

    @automatic.setter
    def automatic(self, automatic):
        """Sets the automatic of this RemediationExecution.

        是否为自动修正。

        :param automatic: The automatic of this RemediationExecution.
        :type automatic: bool
        """
        self._automatic = automatic

    @property
    def resource_id(self):
        """Gets the resource_id of this RemediationExecution.

        资源ID。

        :return: The resource_id of this RemediationExecution.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this RemediationExecution.

        资源ID。

        :param resource_id: The resource_id of this RemediationExecution.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this RemediationExecution.

        资源名称。

        :return: The resource_name of this RemediationExecution.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this RemediationExecution.

        资源名称。

        :param resource_name: The resource_name of this RemediationExecution.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_provider(self):
        """Gets the resource_provider of this RemediationExecution.

        云服务名称。

        :return: The resource_provider of this RemediationExecution.
        :rtype: str
        """
        return self._resource_provider

    @resource_provider.setter
    def resource_provider(self, resource_provider):
        """Sets the resource_provider of this RemediationExecution.

        云服务名称。

        :param resource_provider: The resource_provider of this RemediationExecution.
        :type resource_provider: str
        """
        self._resource_provider = resource_provider

    @property
    def resource_type(self):
        """Gets the resource_type of this RemediationExecution.

        资源类型。

        :return: The resource_type of this RemediationExecution.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this RemediationExecution.

        资源类型。

        :param resource_type: The resource_type of this RemediationExecution.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def invocation_time(self):
        """Gets the invocation_time of this RemediationExecution.

        补救执行的开始时间。

        :return: The invocation_time of this RemediationExecution.
        :rtype: str
        """
        return self._invocation_time

    @invocation_time.setter
    def invocation_time(self, invocation_time):
        """Sets the invocation_time of this RemediationExecution.

        补救执行的开始时间。

        :param invocation_time: The invocation_time of this RemediationExecution.
        :type invocation_time: str
        """
        self._invocation_time = invocation_time

    @property
    def state(self):
        """Gets the state of this RemediationExecution.

        合规规则修正执行的状态。

        :return: The state of this RemediationExecution.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this RemediationExecution.

        合规规则修正执行的状态。

        :param state: The state of this RemediationExecution.
        :type state: str
        """
        self._state = state

    @property
    def message(self):
        """Gets the message of this RemediationExecution.

        合规规则修正执行的信息。

        :return: The message of this RemediationExecution.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this RemediationExecution.

        合规规则修正执行的信息。

        :param message: The message of this RemediationExecution.
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
        if not isinstance(other, RemediationExecution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
