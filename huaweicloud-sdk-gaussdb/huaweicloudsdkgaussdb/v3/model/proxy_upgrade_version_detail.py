# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProxyUpgradeVersionDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'workflow_id': 'str',
        'state': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'workflow_id': 'workflow_id',
        'state': 'state',
        'error_message': 'error_message'
    }

    def __init__(self, instance_id=None, workflow_id=None, state=None, error_message=None):
        """ProxyUpgradeVersionDetail

        The model defined in huaweicloud sdk

        :param instance_id: 实例id.
        :type instance_id: str
        :param workflow_id: 工作流Id。
        :type workflow_id: str
        :param state: agent返回的升级下发状态码，默认返回。
        :type state: str
        :param error_message: 错误消息。
        :type error_message: str
        """
        
        

        self._instance_id = None
        self._workflow_id = None
        self._state = None
        self._error_message = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if workflow_id is not None:
            self.workflow_id = workflow_id
        if state is not None:
            self.state = state
        if error_message is not None:
            self.error_message = error_message

    @property
    def instance_id(self):
        """Gets the instance_id of this ProxyUpgradeVersionDetail.

        实例id.

        :return: The instance_id of this ProxyUpgradeVersionDetail.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ProxyUpgradeVersionDetail.

        实例id.

        :param instance_id: The instance_id of this ProxyUpgradeVersionDetail.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def workflow_id(self):
        """Gets the workflow_id of this ProxyUpgradeVersionDetail.

        工作流Id。

        :return: The workflow_id of this ProxyUpgradeVersionDetail.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this ProxyUpgradeVersionDetail.

        工作流Id。

        :param workflow_id: The workflow_id of this ProxyUpgradeVersionDetail.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def state(self):
        """Gets the state of this ProxyUpgradeVersionDetail.

        agent返回的升级下发状态码，默认返回。

        :return: The state of this ProxyUpgradeVersionDetail.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ProxyUpgradeVersionDetail.

        agent返回的升级下发状态码，默认返回。

        :param state: The state of this ProxyUpgradeVersionDetail.
        :type state: str
        """
        self._state = state

    @property
    def error_message(self):
        """Gets the error_message of this ProxyUpgradeVersionDetail.

        错误消息。

        :return: The error_message of this ProxyUpgradeVersionDetail.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this ProxyUpgradeVersionDetail.

        错误消息。

        :param error_message: The error_message of this ProxyUpgradeVersionDetail.
        :type error_message: str
        """
        self._error_message = error_message

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
        if not isinstance(other, ProxyUpgradeVersionDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
