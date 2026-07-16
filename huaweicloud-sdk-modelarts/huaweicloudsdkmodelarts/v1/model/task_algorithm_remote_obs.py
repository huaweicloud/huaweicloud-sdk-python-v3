# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskAlgorithmRemoteObs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'obs_url': 'str'
    }

    attribute_map = {
        'obs_url': 'obs_url'
    }

    def __init__(self, obs_url=None):
        r"""TaskAlgorithmRemoteObs

        The model defined in huaweicloud sdk

        :param obs_url: **参数解释**：数据实际输出到OBS的路径。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type obs_url: str
        """
        
        

        self._obs_url = None
        self.discriminator = None

        self.obs_url = obs_url

    @property
    def obs_url(self):
        r"""Gets the obs_url of this TaskAlgorithmRemoteObs.

        **参数解释**：数据实际输出到OBS的路径。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The obs_url of this TaskAlgorithmRemoteObs.
        :rtype: str
        """
        return self._obs_url

    @obs_url.setter
    def obs_url(self, obs_url):
        r"""Sets the obs_url of this TaskAlgorithmRemoteObs.

        **参数解释**：数据实际输出到OBS的路径。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param obs_url: The obs_url of this TaskAlgorithmRemoteObs.
        :type obs_url: str
        """
        self._obs_url = obs_url

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
        if not isinstance(other, TaskAlgorithmRemoteObs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
