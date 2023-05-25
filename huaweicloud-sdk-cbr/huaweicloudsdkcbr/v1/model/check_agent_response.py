# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckAgentResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_status': 'list[ProtectableAgentStatus]'
    }

    attribute_map = {
        'agent_status': 'agent_status'
    }

    def __init__(self, agent_status=None):
        """CheckAgentResponse

        The model defined in huaweicloud sdk

        :param agent_status: 状态列表
        :type agent_status: list[:class:`huaweicloudsdkcbr.v1.ProtectableAgentStatus`]
        """
        
        super(CheckAgentResponse, self).__init__()

        self._agent_status = None
        self.discriminator = None

        if agent_status is not None:
            self.agent_status = agent_status

    @property
    def agent_status(self):
        """Gets the agent_status of this CheckAgentResponse.

        状态列表

        :return: The agent_status of this CheckAgentResponse.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.ProtectableAgentStatus`]
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        """Sets the agent_status of this CheckAgentResponse.

        状态列表

        :param agent_status: The agent_status of this CheckAgentResponse.
        :type agent_status: list[:class:`huaweicloudsdkcbr.v1.ProtectableAgentStatus`]
        """
        self._agent_status = agent_status

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
        if not isinstance(other, CheckAgentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
