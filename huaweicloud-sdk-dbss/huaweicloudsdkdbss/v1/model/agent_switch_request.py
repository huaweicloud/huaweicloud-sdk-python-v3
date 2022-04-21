# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgentSwitchRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'agent_id': 'str',
        'status': 'int'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'status': 'status'
    }

    def __init__(self, agent_id=None, status=None):
        """AgentSwitchRequest

        The model defined in huaweicloud sdk

        :param agent_id: 审计agent的ID
        :type agent_id: str
        :param status: Agent开关状态 1：开启 0：关闭
        :type status: int
        """
        
        

        self._agent_id = None
        self._status = None
        self.discriminator = None

        self.agent_id = agent_id
        self.status = status

    @property
    def agent_id(self):
        """Gets the agent_id of this AgentSwitchRequest.

        审计agent的ID

        :return: The agent_id of this AgentSwitchRequest.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this AgentSwitchRequest.

        审计agent的ID

        :param agent_id: The agent_id of this AgentSwitchRequest.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def status(self):
        """Gets the status of this AgentSwitchRequest.

        Agent开关状态 1：开启 0：关闭

        :return: The status of this AgentSwitchRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AgentSwitchRequest.

        Agent开关状态 1：开启 0：关闭

        :param status: The status of this AgentSwitchRequest.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, AgentSwitchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
