# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RemoveAgentPathRequest:

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
        'body': 'AgentRemovePathReq'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'body': 'body'
    }

    def __init__(self, agent_id=None, body=None):
        r"""RemoveAgentPathRequest

        The model defined in huaweicloud sdk

        :param agent_id: 客户端ID
        :type agent_id: str
        :param body: Body of the RemoveAgentPathRequest
        :type body: :class:`huaweicloudsdkcbr.v1.AgentRemovePathReq`
        """
        
        

        self._agent_id = None
        self._body = None
        self.discriminator = None

        self.agent_id = agent_id
        if body is not None:
            self.body = body

    @property
    def agent_id(self):
        r"""Gets the agent_id of this RemoveAgentPathRequest.

        客户端ID

        :return: The agent_id of this RemoveAgentPathRequest.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this RemoveAgentPathRequest.

        客户端ID

        :param agent_id: The agent_id of this RemoveAgentPathRequest.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def body(self):
        r"""Gets the body of this RemoveAgentPathRequest.

        :return: The body of this RemoveAgentPathRequest.
        :rtype: :class:`huaweicloudsdkcbr.v1.AgentRemovePathReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this RemoveAgentPathRequest.

        :param body: The body of this RemoveAgentPathRequest.
        :type body: :class:`huaweicloudsdkcbr.v1.AgentRemovePathReq`
        """
        self._body = body

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
        if not isinstance(other, RemoveAgentPathRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
