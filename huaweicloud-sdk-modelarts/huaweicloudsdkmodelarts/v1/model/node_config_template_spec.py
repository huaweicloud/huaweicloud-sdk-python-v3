# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeConfigTemplateSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'docker_base_size': 'int',
        'docker_lvm_config': 'DockerLvmConfig'
    }

    attribute_map = {
        'docker_base_size': 'dockerBaseSize',
        'docker_lvm_config': 'dockerLvmConfig'
    }

    def __init__(self, docker_base_size=None, docker_lvm_config=None):
        r"""NodeConfigTemplateSpec

        The model defined in huaweicloud sdk

        :param docker_base_size: **参数解释**： 资源池节点上单容器的可用磁盘空间大小，单位G。 **取值范围**： 不涉及。
        :type docker_base_size: int
        :param docker_lvm_config: 
        :type docker_lvm_config: :class:`huaweicloudsdkmodelarts.v1.DockerLvmConfig`
        """
        
        

        self._docker_base_size = None
        self._docker_lvm_config = None
        self.discriminator = None

        self.docker_base_size = docker_base_size
        if docker_lvm_config is not None:
            self.docker_lvm_config = docker_lvm_config

    @property
    def docker_base_size(self):
        r"""Gets the docker_base_size of this NodeConfigTemplateSpec.

        **参数解释**： 资源池节点上单容器的可用磁盘空间大小，单位G。 **取值范围**： 不涉及。

        :return: The docker_base_size of this NodeConfigTemplateSpec.
        :rtype: int
        """
        return self._docker_base_size

    @docker_base_size.setter
    def docker_base_size(self, docker_base_size):
        r"""Sets the docker_base_size of this NodeConfigTemplateSpec.

        **参数解释**： 资源池节点上单容器的可用磁盘空间大小，单位G。 **取值范围**： 不涉及。

        :param docker_base_size: The docker_base_size of this NodeConfigTemplateSpec.
        :type docker_base_size: int
        """
        self._docker_base_size = docker_base_size

    @property
    def docker_lvm_config(self):
        r"""Gets the docker_lvm_config of this NodeConfigTemplateSpec.

        :return: The docker_lvm_config of this NodeConfigTemplateSpec.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DockerLvmConfig`
        """
        return self._docker_lvm_config

    @docker_lvm_config.setter
    def docker_lvm_config(self, docker_lvm_config):
        r"""Sets the docker_lvm_config of this NodeConfigTemplateSpec.

        :param docker_lvm_config: The docker_lvm_config of this NodeConfigTemplateSpec.
        :type docker_lvm_config: :class:`huaweicloudsdkmodelarts.v1.DockerLvmConfig`
        """
        self._docker_lvm_config = docker_lvm_config

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
        if not isinstance(other, NodeConfigTemplateSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
