# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskAlgorithmRemote:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'obs': 'TaskAlgorithmRemoteObs'
    }

    attribute_map = {
        'obs': 'obs'
    }

    def __init__(self, obs=None):
        r"""TaskAlgorithmRemote

        The model defined in huaweicloud sdk

        :param obs: 
        :type obs: :class:`huaweicloudsdkmodelarts.v1.TaskAlgorithmRemoteObs`
        """
        
        

        self._obs = None
        self.discriminator = None

        self.obs = obs

    @property
    def obs(self):
        r"""Gets the obs of this TaskAlgorithmRemote.

        :return: The obs of this TaskAlgorithmRemote.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.TaskAlgorithmRemoteObs`
        """
        return self._obs

    @obs.setter
    def obs(self, obs):
        r"""Sets the obs of this TaskAlgorithmRemote.

        :param obs: The obs of this TaskAlgorithmRemote.
        :type obs: :class:`huaweicloudsdkmodelarts.v1.TaskAlgorithmRemoteObs`
        """
        self._obs = obs

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
        if not isinstance(other, TaskAlgorithmRemote):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
