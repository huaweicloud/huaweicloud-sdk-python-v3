# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RayActorOptions:

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
        'memory': 'float',
        'resources': 'str'
    }

    attribute_map = {
        'num_cpus': 'num_cpus',
        'memory': 'memory',
        'resources': 'resources'
    }

    def __init__(self, num_cpus=None, memory=None, resources=None):
        r"""RayActorOptions

        The model defined in huaweicloud sdk

        :param num_cpus: **参数解释**：CPU数量。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 
        :type num_cpus: float
        :param memory: **参数解释**：内存数量。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 
        :type memory: float
        :param resources: **参数解释**：资源配置。 **约束限制**：不涉及。 **取值范围**：长度[0,1024]。 **默认取值**：不涉及。 
        :type resources: str
        """
        
        

        self._num_cpus = None
        self._memory = None
        self._resources = None
        self.discriminator = None

        if num_cpus is not None:
            self.num_cpus = num_cpus
        if memory is not None:
            self.memory = memory
        if resources is not None:
            self.resources = resources

    @property
    def num_cpus(self):
        r"""Gets the num_cpus of this RayActorOptions.

        **参数解释**：CPU数量。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :return: The num_cpus of this RayActorOptions.
        :rtype: float
        """
        return self._num_cpus

    @num_cpus.setter
    def num_cpus(self, num_cpus):
        r"""Sets the num_cpus of this RayActorOptions.

        **参数解释**：CPU数量。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :param num_cpus: The num_cpus of this RayActorOptions.
        :type num_cpus: float
        """
        self._num_cpus = num_cpus

    @property
    def memory(self):
        r"""Gets the memory of this RayActorOptions.

        **参数解释**：内存数量。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :return: The memory of this RayActorOptions.
        :rtype: float
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this RayActorOptions.

        **参数解释**：内存数量。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :param memory: The memory of this RayActorOptions.
        :type memory: float
        """
        self._memory = memory

    @property
    def resources(self):
        r"""Gets the resources of this RayActorOptions.

        **参数解释**：资源配置。 **约束限制**：不涉及。 **取值范围**：长度[0,1024]。 **默认取值**：不涉及。 

        :return: The resources of this RayActorOptions.
        :rtype: str
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this RayActorOptions.

        **参数解释**：资源配置。 **约束限制**：不涉及。 **取值范围**：长度[0,1024]。 **默认取值**：不涉及。 

        :param resources: The resources of this RayActorOptions.
        :type resources: str
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
        if not isinstance(other, RayActorOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
