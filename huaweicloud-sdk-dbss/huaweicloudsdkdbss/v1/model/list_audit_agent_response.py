# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAuditAgentResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agents': 'list[AuditAgentRespoonseAgents]'
    }

    attribute_map = {
        'agents': 'agents'
    }

    def __init__(self, agents=None):
        r"""ListAuditAgentResponse

        The model defined in huaweicloud sdk

        :param agents: agent列表
        :type agents: list[:class:`huaweicloudsdkdbss.v1.AuditAgentRespoonseAgents`]
        """
        
        super(ListAuditAgentResponse, self).__init__()

        self._agents = None
        self.discriminator = None

        if agents is not None:
            self.agents = agents

    @property
    def agents(self):
        r"""Gets the agents of this ListAuditAgentResponse.

        agent列表

        :return: The agents of this ListAuditAgentResponse.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.AuditAgentRespoonseAgents`]
        """
        return self._agents

    @agents.setter
    def agents(self, agents):
        r"""Sets the agents of this ListAuditAgentResponse.

        agent列表

        :param agents: The agents of this ListAuditAgentResponse.
        :type agents: list[:class:`huaweicloudsdkdbss.v1.AuditAgentRespoonseAgents`]
        """
        self._agents = agents

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
        if not isinstance(other, ListAuditAgentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
