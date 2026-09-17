# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsThirdPartyAgentsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'agent_type': 'str',
        'agent_name': 'str'
    }

    attribute_map = {
        'type': 'type',
        'agent_type': 'agent_type',
        'agent_name': 'agent_name'
    }

    def __init__(self, type=None, agent_type=None, agent_name=None):
        r"""ListOpsThirdPartyAgentsRequest

        The model defined in huaweicloud sdk

        :param type: 
        :type type: str
        :param agent_type: 
        :type agent_type: str
        :param agent_name: 
        :type agent_name: str
        """
        
        

        self._type = None
        self._agent_type = None
        self._agent_name = None
        self.discriminator = None

        self.type = type
        if agent_type is not None:
            self.agent_type = agent_type
        if agent_name is not None:
            self.agent_name = agent_name

    @property
    def type(self):
        r"""Gets the type of this ListOpsThirdPartyAgentsRequest.

        :return: The type of this ListOpsThirdPartyAgentsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListOpsThirdPartyAgentsRequest.

        :param type: The type of this ListOpsThirdPartyAgentsRequest.
        :type type: str
        """
        self._type = type

    @property
    def agent_type(self):
        r"""Gets the agent_type of this ListOpsThirdPartyAgentsRequest.

        :return: The agent_type of this ListOpsThirdPartyAgentsRequest.
        :rtype: str
        """
        return self._agent_type

    @agent_type.setter
    def agent_type(self, agent_type):
        r"""Sets the agent_type of this ListOpsThirdPartyAgentsRequest.

        :param agent_type: The agent_type of this ListOpsThirdPartyAgentsRequest.
        :type agent_type: str
        """
        self._agent_type = agent_type

    @property
    def agent_name(self):
        r"""Gets the agent_name of this ListOpsThirdPartyAgentsRequest.

        :return: The agent_name of this ListOpsThirdPartyAgentsRequest.
        :rtype: str
        """
        return self._agent_name

    @agent_name.setter
    def agent_name(self, agent_name):
        r"""Sets the agent_name of this ListOpsThirdPartyAgentsRequest.

        :param agent_name: The agent_name of this ListOpsThirdPartyAgentsRequest.
        :type agent_name: str
        """
        self._agent_name = agent_name

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
        if not isinstance(other, ListOpsThirdPartyAgentsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
