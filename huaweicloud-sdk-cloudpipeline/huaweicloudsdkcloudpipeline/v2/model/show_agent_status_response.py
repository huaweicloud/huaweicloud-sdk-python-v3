# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowAgentStatusResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'agent_id': 'str'
    }

    attribute_map = {
        'status': 'status',
        'agent_id': 'agent_id'
    }

    def __init__(self, status=None, agent_id=None):
        """ShowAgentStatusResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._status = None
        self._agent_id = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if agent_id is not None:
            self.agent_id = agent_id

    @property
    def status(self):
        """Gets the status of this ShowAgentStatusResponse.

        Agent状态

        :return: The status of this ShowAgentStatusResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowAgentStatusResponse.

        Agent状态

        :param status: The status of this ShowAgentStatusResponse.
        :type: str
        """
        self._status = status

    @property
    def agent_id(self):
        """Gets the agent_id of this ShowAgentStatusResponse.

        AgentID

        :return: The agent_id of this ShowAgentStatusResponse.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this ShowAgentStatusResponse.

        AgentID

        :param agent_id: The agent_id of this ShowAgentStatusResponse.
        :type: str
        """
        self._agent_id = agent_id

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowAgentStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
