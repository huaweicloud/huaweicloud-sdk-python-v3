# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RayClusterConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable_custom': 'bool',
        'head_group_spec': 'HeadGroupSpecV2',
        'worker_group_specs': 'list[WorkerGroupSpecV2]'
    }

    attribute_map = {
        'enable_custom': 'enable_custom',
        'head_group_spec': 'head_group_spec',
        'worker_group_specs': 'worker_group_specs'
    }

    def __init__(self, enable_custom=None, head_group_spec=None, worker_group_specs=None):
        r"""RayClusterConfig

        The model defined in huaweicloud sdk

        :param enable_custom: **参数解释**：是否开启资源自定义。 **约束限制**：不涉及。 **取值范围**：开启true，关闭false。 **默认取值**：false。 
        :type enable_custom: bool
        :param head_group_spec: 
        :type head_group_spec: :class:`huaweicloudsdkdataartsfabric.v1.HeadGroupSpecV2`
        :param worker_group_specs: **参数解释**：Worker Group的配置。 **约束限制**：[1,1000]。 
        :type worker_group_specs: list[:class:`huaweicloudsdkdataartsfabric.v1.WorkerGroupSpecV2`]
        """
        
        

        self._enable_custom = None
        self._head_group_spec = None
        self._worker_group_specs = None
        self.discriminator = None

        if enable_custom is not None:
            self.enable_custom = enable_custom
        self.head_group_spec = head_group_spec
        self.worker_group_specs = worker_group_specs

    @property
    def enable_custom(self):
        r"""Gets the enable_custom of this RayClusterConfig.

        **参数解释**：是否开启资源自定义。 **约束限制**：不涉及。 **取值范围**：开启true，关闭false。 **默认取值**：false。 

        :return: The enable_custom of this RayClusterConfig.
        :rtype: bool
        """
        return self._enable_custom

    @enable_custom.setter
    def enable_custom(self, enable_custom):
        r"""Sets the enable_custom of this RayClusterConfig.

        **参数解释**：是否开启资源自定义。 **约束限制**：不涉及。 **取值范围**：开启true，关闭false。 **默认取值**：false。 

        :param enable_custom: The enable_custom of this RayClusterConfig.
        :type enable_custom: bool
        """
        self._enable_custom = enable_custom

    @property
    def head_group_spec(self):
        r"""Gets the head_group_spec of this RayClusterConfig.

        :return: The head_group_spec of this RayClusterConfig.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.HeadGroupSpecV2`
        """
        return self._head_group_spec

    @head_group_spec.setter
    def head_group_spec(self, head_group_spec):
        r"""Sets the head_group_spec of this RayClusterConfig.

        :param head_group_spec: The head_group_spec of this RayClusterConfig.
        :type head_group_spec: :class:`huaweicloudsdkdataartsfabric.v1.HeadGroupSpecV2`
        """
        self._head_group_spec = head_group_spec

    @property
    def worker_group_specs(self):
        r"""Gets the worker_group_specs of this RayClusterConfig.

        **参数解释**：Worker Group的配置。 **约束限制**：[1,1000]。 

        :return: The worker_group_specs of this RayClusterConfig.
        :rtype: list[:class:`huaweicloudsdkdataartsfabric.v1.WorkerGroupSpecV2`]
        """
        return self._worker_group_specs

    @worker_group_specs.setter
    def worker_group_specs(self, worker_group_specs):
        r"""Sets the worker_group_specs of this RayClusterConfig.

        **参数解释**：Worker Group的配置。 **约束限制**：[1,1000]。 

        :param worker_group_specs: The worker_group_specs of this RayClusterConfig.
        :type worker_group_specs: list[:class:`huaweicloudsdkdataartsfabric.v1.WorkerGroupSpecV2`]
        """
        self._worker_group_specs = worker_group_specs

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
        if not isinstance(other, RayClusterConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
