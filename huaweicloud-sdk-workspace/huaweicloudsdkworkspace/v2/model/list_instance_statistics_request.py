# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceStatisticsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ai_agent_type': 'str'
    }

    attribute_map = {
        'ai_agent_type': 'ai_agent_type'
    }

    def __init__(self, ai_agent_type=None):
        r"""ListInstanceStatisticsRequest

        The model defined in huaweicloud sdk

        :param ai_agent_type: Agent 类型
        :type ai_agent_type: str
        """
        
        

        self._ai_agent_type = None
        self.discriminator = None

        if ai_agent_type is not None:
            self.ai_agent_type = ai_agent_type

    @property
    def ai_agent_type(self):
        r"""Gets the ai_agent_type of this ListInstanceStatisticsRequest.

        Agent 类型

        :return: The ai_agent_type of this ListInstanceStatisticsRequest.
        :rtype: str
        """
        return self._ai_agent_type

    @ai_agent_type.setter
    def ai_agent_type(self, ai_agent_type):
        r"""Sets the ai_agent_type of this ListInstanceStatisticsRequest.

        Agent 类型

        :param ai_agent_type: The ai_agent_type of this ListInstanceStatisticsRequest.
        :type ai_agent_type: str
        """
        self._ai_agent_type = ai_agent_type

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
        if not isinstance(other, ListInstanceStatisticsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
