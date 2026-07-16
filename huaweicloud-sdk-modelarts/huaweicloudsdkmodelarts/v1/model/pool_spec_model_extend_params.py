# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolSpecModelExtendParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'docker_base_size': 'str',
        'volume_group': 'str',
        'runtime': 'str'
    }

    attribute_map = {
        'docker_base_size': 'dockerBaseSize',
        'volume_group': 'volumeGroup',
        'runtime': 'runtime'
    }

    def __init__(self, docker_base_size=None, volume_group=None, runtime=None):
        r"""PoolSpecModelExtendParams

        The model defined in huaweicloud sdk

        :param docker_base_size: **参数解释**：资源池创建的节点的容器引擎空间大小。值为0时表示不限制大小。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type docker_base_size: str
        :param volume_group: **参数描述**：磁盘分组名称。 **取值范围**：不涉及。
        :type volume_group: str
        :param runtime: **参数描述**：模型运行时环境。 **取值范围**：不涉及。
        :type runtime: str
        """
        
        

        self._docker_base_size = None
        self._volume_group = None
        self._runtime = None
        self.discriminator = None

        if docker_base_size is not None:
            self.docker_base_size = docker_base_size
        if volume_group is not None:
            self.volume_group = volume_group
        if runtime is not None:
            self.runtime = runtime

    @property
    def docker_base_size(self):
        r"""Gets the docker_base_size of this PoolSpecModelExtendParams.

        **参数解释**：资源池创建的节点的容器引擎空间大小。值为0时表示不限制大小。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The docker_base_size of this PoolSpecModelExtendParams.
        :rtype: str
        """
        return self._docker_base_size

    @docker_base_size.setter
    def docker_base_size(self, docker_base_size):
        r"""Sets the docker_base_size of this PoolSpecModelExtendParams.

        **参数解释**：资源池创建的节点的容器引擎空间大小。值为0时表示不限制大小。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param docker_base_size: The docker_base_size of this PoolSpecModelExtendParams.
        :type docker_base_size: str
        """
        self._docker_base_size = docker_base_size

    @property
    def volume_group(self):
        r"""Gets the volume_group of this PoolSpecModelExtendParams.

        **参数描述**：磁盘分组名称。 **取值范围**：不涉及。

        :return: The volume_group of this PoolSpecModelExtendParams.
        :rtype: str
        """
        return self._volume_group

    @volume_group.setter
    def volume_group(self, volume_group):
        r"""Sets the volume_group of this PoolSpecModelExtendParams.

        **参数描述**：磁盘分组名称。 **取值范围**：不涉及。

        :param volume_group: The volume_group of this PoolSpecModelExtendParams.
        :type volume_group: str
        """
        self._volume_group = volume_group

    @property
    def runtime(self):
        r"""Gets the runtime of this PoolSpecModelExtendParams.

        **参数描述**：模型运行时环境。 **取值范围**：不涉及。

        :return: The runtime of this PoolSpecModelExtendParams.
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        r"""Sets the runtime of this PoolSpecModelExtendParams.

        **参数描述**：模型运行时环境。 **取值范围**：不涉及。

        :param runtime: The runtime of this PoolSpecModelExtendParams.
        :type runtime: str
        """
        self._runtime = runtime

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
        if not isinstance(other, PoolSpecModelExtendParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
