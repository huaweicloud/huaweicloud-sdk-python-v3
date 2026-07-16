# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskEnv:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'envs': 'list[EnvVar]'
    }

    attribute_map = {
        'envs': 'envs'
    }

    def __init__(self, envs=None):
        r"""TaskEnv

        The model defined in huaweicloud sdk

        :param envs: 精调训练环境变量信息
        :type envs: list[:class:`huaweicloudsdkmodelarts.v1.EnvVar`]
        """
        
        

        self._envs = None
        self.discriminator = None

        if envs is not None:
            self.envs = envs

    @property
    def envs(self):
        r"""Gets the envs of this TaskEnv.

        精调训练环境变量信息

        :return: The envs of this TaskEnv.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.EnvVar`]
        """
        return self._envs

    @envs.setter
    def envs(self, envs):
        r"""Sets the envs of this TaskEnv.

        精调训练环境变量信息

        :param envs: The envs of this TaskEnv.
        :type envs: list[:class:`huaweicloudsdkmodelarts.v1.EnvVar`]
        """
        self._envs = envs

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
        if not isinstance(other, TaskEnv):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
