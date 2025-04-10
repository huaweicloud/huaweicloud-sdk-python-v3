# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SingleAgentParam:

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
        'inner_ip': 'str'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'inner_ip': 'inner_ip'
    }

    def __init__(self, agent_id=None, inner_ip=None):
        r"""SingleAgentParam

        The model defined in huaweicloud sdk

        :param agent_id: agent ID唯一值。
        :type agent_id: str
        :param inner_ip: 主机ip。
        :type inner_ip: str
        """
        
        

        self._agent_id = None
        self._inner_ip = None
        self.discriminator = None

        self.agent_id = agent_id
        self.inner_ip = inner_ip

    @property
    def agent_id(self):
        r"""Gets the agent_id of this SingleAgentParam.

        agent ID唯一值。

        :return: The agent_id of this SingleAgentParam.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this SingleAgentParam.

        agent ID唯一值。

        :param agent_id: The agent_id of this SingleAgentParam.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def inner_ip(self):
        r"""Gets the inner_ip of this SingleAgentParam.

        主机ip。

        :return: The inner_ip of this SingleAgentParam.
        :rtype: str
        """
        return self._inner_ip

    @inner_ip.setter
    def inner_ip(self, inner_ip):
        r"""Sets the inner_ip of this SingleAgentParam.

        主机ip。

        :param inner_ip: The inner_ip of this SingleAgentParam.
        :type inner_ip: str
        """
        self._inner_ip = inner_ip

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
        if not isinstance(other, SingleAgentParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
