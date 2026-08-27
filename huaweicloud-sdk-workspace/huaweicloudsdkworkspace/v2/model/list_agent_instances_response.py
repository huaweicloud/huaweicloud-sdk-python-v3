# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAgentInstancesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_instances': 'list[AgentInstanceInfo]',
        'total_count': 'int'
    }

    attribute_map = {
        'agent_instances': 'agent_instances',
        'total_count': 'total_count'
    }

    def __init__(self, agent_instances=None, total_count=None):
        r"""ListAgentInstancesResponse

        The model defined in huaweicloud sdk

        :param agent_instances: Agent 示例信息
        :type agent_instances: list[:class:`huaweicloudsdkworkspace.v2.AgentInstanceInfo`]
        :param total_count: 总记录数
        :type total_count: int
        """
        
        super().__init__()

        self._agent_instances = None
        self._total_count = None
        self.discriminator = None

        if agent_instances is not None:
            self.agent_instances = agent_instances
        if total_count is not None:
            self.total_count = total_count

    @property
    def agent_instances(self):
        r"""Gets the agent_instances of this ListAgentInstancesResponse.

        Agent 示例信息

        :return: The agent_instances of this ListAgentInstancesResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.AgentInstanceInfo`]
        """
        return self._agent_instances

    @agent_instances.setter
    def agent_instances(self, agent_instances):
        r"""Sets the agent_instances of this ListAgentInstancesResponse.

        Agent 示例信息

        :param agent_instances: The agent_instances of this ListAgentInstancesResponse.
        :type agent_instances: list[:class:`huaweicloudsdkworkspace.v2.AgentInstanceInfo`]
        """
        self._agent_instances = agent_instances

    @property
    def total_count(self):
        r"""Gets the total_count of this ListAgentInstancesResponse.

        总记录数

        :return: The total_count of this ListAgentInstancesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListAgentInstancesResponse.

        总记录数

        :param total_count: The total_count of this ListAgentInstancesResponse.
        :type total_count: int
        """
        self._total_count = total_count

    def to_dict(self):
        import warnings
        warnings.warn("ListAgentInstancesResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListAgentInstancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
