# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PropagationSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_selectors': 'list[ResourceSelector]',
        'propagate_deps': 'bool',
        'placement': 'Placement',
        'priority': 'int',
        'scheduler_name': 'str'
    }

    attribute_map = {
        'resource_selectors': 'resourceSelectors',
        'propagate_deps': 'propagateDeps',
        'placement': 'placement',
        'priority': 'priority',
        'scheduler_name': 'schedulerName'
    }

    def __init__(self, resource_selectors=None, propagate_deps=None, placement=None, priority=None, scheduler_name=None):
        r"""PropagationSpec

        The model defined in huaweicloud sdk

        :param resource_selectors: 资源选择器，用于选择要传播的资源
        :type resource_selectors: list[:class:`huaweicloudsdkucs.v1.ResourceSelector`]
        :param propagate_deps: 是否自动传播引用的资源
        :type propagate_deps: bool
        :param placement: 
        :type placement: :class:`huaweicloudsdkucs.v1.Placement`
        :param priority: 策略的优先级，默认值为0
        :type priority: int
        :param scheduler_name: 调度器名称，默认值为“default-scheduler”
        :type scheduler_name: str
        """
        
        

        self._resource_selectors = None
        self._propagate_deps = None
        self._placement = None
        self._priority = None
        self._scheduler_name = None
        self.discriminator = None

        if resource_selectors is not None:
            self.resource_selectors = resource_selectors
        if propagate_deps is not None:
            self.propagate_deps = propagate_deps
        if placement is not None:
            self.placement = placement
        if priority is not None:
            self.priority = priority
        if scheduler_name is not None:
            self.scheduler_name = scheduler_name

    @property
    def resource_selectors(self):
        r"""Gets the resource_selectors of this PropagationSpec.

        资源选择器，用于选择要传播的资源

        :return: The resource_selectors of this PropagationSpec.
        :rtype: list[:class:`huaweicloudsdkucs.v1.ResourceSelector`]
        """
        return self._resource_selectors

    @resource_selectors.setter
    def resource_selectors(self, resource_selectors):
        r"""Sets the resource_selectors of this PropagationSpec.

        资源选择器，用于选择要传播的资源

        :param resource_selectors: The resource_selectors of this PropagationSpec.
        :type resource_selectors: list[:class:`huaweicloudsdkucs.v1.ResourceSelector`]
        """
        self._resource_selectors = resource_selectors

    @property
    def propagate_deps(self):
        r"""Gets the propagate_deps of this PropagationSpec.

        是否自动传播引用的资源

        :return: The propagate_deps of this PropagationSpec.
        :rtype: bool
        """
        return self._propagate_deps

    @propagate_deps.setter
    def propagate_deps(self, propagate_deps):
        r"""Sets the propagate_deps of this PropagationSpec.

        是否自动传播引用的资源

        :param propagate_deps: The propagate_deps of this PropagationSpec.
        :type propagate_deps: bool
        """
        self._propagate_deps = propagate_deps

    @property
    def placement(self):
        r"""Gets the placement of this PropagationSpec.

        :return: The placement of this PropagationSpec.
        :rtype: :class:`huaweicloudsdkucs.v1.Placement`
        """
        return self._placement

    @placement.setter
    def placement(self, placement):
        r"""Sets the placement of this PropagationSpec.

        :param placement: The placement of this PropagationSpec.
        :type placement: :class:`huaweicloudsdkucs.v1.Placement`
        """
        self._placement = placement

    @property
    def priority(self):
        r"""Gets the priority of this PropagationSpec.

        策略的优先级，默认值为0

        :return: The priority of this PropagationSpec.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this PropagationSpec.

        策略的优先级，默认值为0

        :param priority: The priority of this PropagationSpec.
        :type priority: int
        """
        self._priority = priority

    @property
    def scheduler_name(self):
        r"""Gets the scheduler_name of this PropagationSpec.

        调度器名称，默认值为“default-scheduler”

        :return: The scheduler_name of this PropagationSpec.
        :rtype: str
        """
        return self._scheduler_name

    @scheduler_name.setter
    def scheduler_name(self, scheduler_name):
        r"""Sets the scheduler_name of this PropagationSpec.

        调度器名称，默认值为“default-scheduler”

        :param scheduler_name: The scheduler_name of this PropagationSpec.
        :type scheduler_name: str
        """
        self._scheduler_name = scheduler_name

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
        if not isinstance(other, PropagationSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
