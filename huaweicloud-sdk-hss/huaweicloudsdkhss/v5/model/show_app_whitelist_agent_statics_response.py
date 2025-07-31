# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAppWhitelistAgentStaticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_num': 'int'
    }

    attribute_map = {
        'agent_num': 'agent_num'
    }

    def __init__(self, agent_num=None):
        r"""ShowAppWhitelistAgentStaticsResponse

        The model defined in huaweicloud sdk

        :param agent_num: **参数解释**: 总数 **取值范围**: 最小值0，最大值2147483647 
        :type agent_num: int
        """
        
        super(ShowAppWhitelistAgentStaticsResponse, self).__init__()

        self._agent_num = None
        self.discriminator = None

        if agent_num is not None:
            self.agent_num = agent_num

    @property
    def agent_num(self):
        r"""Gets the agent_num of this ShowAppWhitelistAgentStaticsResponse.

        **参数解释**: 总数 **取值范围**: 最小值0，最大值2147483647 

        :return: The agent_num of this ShowAppWhitelistAgentStaticsResponse.
        :rtype: int
        """
        return self._agent_num

    @agent_num.setter
    def agent_num(self, agent_num):
        r"""Sets the agent_num of this ShowAppWhitelistAgentStaticsResponse.

        **参数解释**: 总数 **取值范围**: 最小值0，最大值2147483647 

        :param agent_num: The agent_num of this ShowAppWhitelistAgentStaticsResponse.
        :type agent_num: int
        """
        self._agent_num = agent_num

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
        if not isinstance(other, ShowAppWhitelistAgentStaticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
