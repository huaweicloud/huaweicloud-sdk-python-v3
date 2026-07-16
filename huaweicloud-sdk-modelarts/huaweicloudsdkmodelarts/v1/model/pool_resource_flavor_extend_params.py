# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolResourceFlavorExtendParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'docker_base_size': 'str'
    }

    attribute_map = {
        'docker_base_size': 'dockerBaseSize'
    }

    def __init__(self, docker_base_size=None):
        r"""PoolResourceFlavorExtendParams

        The model defined in huaweicloud sdk

        :param docker_base_size: **参数解释**：指定资源池节点的容器引擎空间大小。值为0时表示不限制大小。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type docker_base_size: str
        """
        
        

        self._docker_base_size = None
        self.discriminator = None

        if docker_base_size is not None:
            self.docker_base_size = docker_base_size

    @property
    def docker_base_size(self):
        r"""Gets the docker_base_size of this PoolResourceFlavorExtendParams.

        **参数解释**：指定资源池节点的容器引擎空间大小。值为0时表示不限制大小。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The docker_base_size of this PoolResourceFlavorExtendParams.
        :rtype: str
        """
        return self._docker_base_size

    @docker_base_size.setter
    def docker_base_size(self, docker_base_size):
        r"""Sets the docker_base_size of this PoolResourceFlavorExtendParams.

        **参数解释**：指定资源池节点的容器引擎空间大小。值为0时表示不限制大小。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param docker_base_size: The docker_base_size of this PoolResourceFlavorExtendParams.
        :type docker_base_size: str
        """
        self._docker_base_size = docker_base_size

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
        if not isinstance(other, PoolResourceFlavorExtendParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
