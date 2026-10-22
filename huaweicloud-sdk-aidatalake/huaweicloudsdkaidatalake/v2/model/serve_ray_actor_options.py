# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServeRayActorOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'num_cpus': 'float',
        'num_gpus': 'float',
        'resources': 'dict(str, float)'
    }

    attribute_map = {
        'num_cpus': 'num_cpus',
        'num_gpus': 'num_gpus',
        'resources': 'resources'
    }

    def __init__(self, num_cpus=None, num_gpus=None, resources=None):
        r"""ServeRayActorOptions

        The model defined in huaweicloud sdk

        :param num_cpus: **参数解释**：CPU 核数。 **约束限制**：不涉及。 **取值范围**：不小于0。 **默认取值**：不涉及。
        :type num_cpus: float
        :param num_gpus: **参数解释**：GPU 卡数。 **约束限制**：不涉及。 **取值范围**：不小于0。 **默认取值**：不涉及。
        :type num_gpus: float
        :param resources: **参数解释**：自定义资源映射。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type resources: dict(str, float)
        """
        
        

        self._num_cpus = None
        self._num_gpus = None
        self._resources = None
        self.discriminator = None

        if num_cpus is not None:
            self.num_cpus = num_cpus
        if num_gpus is not None:
            self.num_gpus = num_gpus
        if resources is not None:
            self.resources = resources

    @property
    def num_cpus(self):
        r"""Gets the num_cpus of this ServeRayActorOptions.

        **参数解释**：CPU 核数。 **约束限制**：不涉及。 **取值范围**：不小于0。 **默认取值**：不涉及。

        :return: The num_cpus of this ServeRayActorOptions.
        :rtype: float
        """
        return self._num_cpus

    @num_cpus.setter
    def num_cpus(self, num_cpus):
        r"""Sets the num_cpus of this ServeRayActorOptions.

        **参数解释**：CPU 核数。 **约束限制**：不涉及。 **取值范围**：不小于0。 **默认取值**：不涉及。

        :param num_cpus: The num_cpus of this ServeRayActorOptions.
        :type num_cpus: float
        """
        self._num_cpus = num_cpus

    @property
    def num_gpus(self):
        r"""Gets the num_gpus of this ServeRayActorOptions.

        **参数解释**：GPU 卡数。 **约束限制**：不涉及。 **取值范围**：不小于0。 **默认取值**：不涉及。

        :return: The num_gpus of this ServeRayActorOptions.
        :rtype: float
        """
        return self._num_gpus

    @num_gpus.setter
    def num_gpus(self, num_gpus):
        r"""Sets the num_gpus of this ServeRayActorOptions.

        **参数解释**：GPU 卡数。 **约束限制**：不涉及。 **取值范围**：不小于0。 **默认取值**：不涉及。

        :param num_gpus: The num_gpus of this ServeRayActorOptions.
        :type num_gpus: float
        """
        self._num_gpus = num_gpus

    @property
    def resources(self):
        r"""Gets the resources of this ServeRayActorOptions.

        **参数解释**：自定义资源映射。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The resources of this ServeRayActorOptions.
        :rtype: dict(str, float)
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this ServeRayActorOptions.

        **参数解释**：自定义资源映射。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param resources: The resources of this ServeRayActorOptions.
        :type resources: dict(str, float)
        """
        self._resources = resources

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
        if not isinstance(other, ServeRayActorOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
