# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeconfigSpecConfigs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_warm_up': 'list[NodeconfigSpecConfigsImageWarmUp]',
        'cpu_manager': 'NodeconfigSpecConfigsCpuManager',
        'drop_cache': 'NodeconfigSpecConfigsDropCache',
        'transparent_hugepage': 'NodeconfigSpecConfigsTransparentHugepage'
    }

    attribute_map = {
        'image_warm_up': 'image_warm_up',
        'cpu_manager': 'cpu_manager',
        'drop_cache': 'drop_cache',
        'transparent_hugepage': 'transparent_hugepage'
    }

    def __init__(self, image_warm_up=None, cpu_manager=None, drop_cache=None, transparent_hugepage=None):
        r"""NodeconfigSpecConfigs

        The model defined in huaweicloud sdk

        :param image_warm_up: **参数解释**：镜像预热任务配置列表。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type image_warm_up: list[:class:`huaweicloudsdkmodelarts.v1.NodeconfigSpecConfigsImageWarmUp`]
        :param cpu_manager: 
        :type cpu_manager: :class:`huaweicloudsdkmodelarts.v1.NodeconfigSpecConfigsCpuManager`
        :param drop_cache: 
        :type drop_cache: :class:`huaweicloudsdkmodelarts.v1.NodeconfigSpecConfigsDropCache`
        :param transparent_hugepage: 
        :type transparent_hugepage: :class:`huaweicloudsdkmodelarts.v1.NodeconfigSpecConfigsTransparentHugepage`
        """
        
        

        self._image_warm_up = None
        self._cpu_manager = None
        self._drop_cache = None
        self._transparent_hugepage = None
        self.discriminator = None

        if image_warm_up is not None:
            self.image_warm_up = image_warm_up
        if cpu_manager is not None:
            self.cpu_manager = cpu_manager
        if drop_cache is not None:
            self.drop_cache = drop_cache
        if transparent_hugepage is not None:
            self.transparent_hugepage = transparent_hugepage

    @property
    def image_warm_up(self):
        r"""Gets the image_warm_up of this NodeconfigSpecConfigs.

        **参数解释**：镜像预热任务配置列表。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The image_warm_up of this NodeconfigSpecConfigs.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.NodeconfigSpecConfigsImageWarmUp`]
        """
        return self._image_warm_up

    @image_warm_up.setter
    def image_warm_up(self, image_warm_up):
        r"""Sets the image_warm_up of this NodeconfigSpecConfigs.

        **参数解释**：镜像预热任务配置列表。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param image_warm_up: The image_warm_up of this NodeconfigSpecConfigs.
        :type image_warm_up: list[:class:`huaweicloudsdkmodelarts.v1.NodeconfigSpecConfigsImageWarmUp`]
        """
        self._image_warm_up = image_warm_up

    @property
    def cpu_manager(self):
        r"""Gets the cpu_manager of this NodeconfigSpecConfigs.

        :return: The cpu_manager of this NodeconfigSpecConfigs.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.NodeconfigSpecConfigsCpuManager`
        """
        return self._cpu_manager

    @cpu_manager.setter
    def cpu_manager(self, cpu_manager):
        r"""Sets the cpu_manager of this NodeconfigSpecConfigs.

        :param cpu_manager: The cpu_manager of this NodeconfigSpecConfigs.
        :type cpu_manager: :class:`huaweicloudsdkmodelarts.v1.NodeconfigSpecConfigsCpuManager`
        """
        self._cpu_manager = cpu_manager

    @property
    def drop_cache(self):
        r"""Gets the drop_cache of this NodeconfigSpecConfigs.

        :return: The drop_cache of this NodeconfigSpecConfigs.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.NodeconfigSpecConfigsDropCache`
        """
        return self._drop_cache

    @drop_cache.setter
    def drop_cache(self, drop_cache):
        r"""Sets the drop_cache of this NodeconfigSpecConfigs.

        :param drop_cache: The drop_cache of this NodeconfigSpecConfigs.
        :type drop_cache: :class:`huaweicloudsdkmodelarts.v1.NodeconfigSpecConfigsDropCache`
        """
        self._drop_cache = drop_cache

    @property
    def transparent_hugepage(self):
        r"""Gets the transparent_hugepage of this NodeconfigSpecConfigs.

        :return: The transparent_hugepage of this NodeconfigSpecConfigs.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.NodeconfigSpecConfigsTransparentHugepage`
        """
        return self._transparent_hugepage

    @transparent_hugepage.setter
    def transparent_hugepage(self, transparent_hugepage):
        r"""Sets the transparent_hugepage of this NodeconfigSpecConfigs.

        :param transparent_hugepage: The transparent_hugepage of this NodeconfigSpecConfigs.
        :type transparent_hugepage: :class:`huaweicloudsdkmodelarts.v1.NodeconfigSpecConfigsTransparentHugepage`
        """
        self._transparent_hugepage = transparent_hugepage

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
        if not isinstance(other, NodeconfigSpecConfigs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
