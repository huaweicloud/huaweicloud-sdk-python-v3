# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InnerRayJobConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'raycluster_endpoint_name': 'list[str]',
        'task_resources': 'list[str]'
    }

    attribute_map = {
        'raycluster_endpoint_name': 'raycluster_endpoint_name',
        'task_resources': 'task_resources'
    }

    def __init__(self, raycluster_endpoint_name=None, task_resources=None):
        r"""InnerRayJobConfig

        The model defined in huaweicloud sdk

        :param raycluster_endpoint_name: **参数解释**：作业将运行的Ray集群端点列表，可设置多个。 **约束限制**：不涉及。 **取值范围**：每个元素最小长度1，最大长度63。 **默认取值**：不涉及。
        :type raycluster_endpoint_name: list[str]
        :param task_resources: **参数解释**：集群中所需的资源规格。 **约束限制**：最小值为1，最大值为4。
        :type task_resources: list[str]
        """
        
        

        self._raycluster_endpoint_name = None
        self._task_resources = None
        self.discriminator = None

        if raycluster_endpoint_name is not None:
            self.raycluster_endpoint_name = raycluster_endpoint_name
        if task_resources is not None:
            self.task_resources = task_resources

    @property
    def raycluster_endpoint_name(self):
        r"""Gets the raycluster_endpoint_name of this InnerRayJobConfig.

        **参数解释**：作业将运行的Ray集群端点列表，可设置多个。 **约束限制**：不涉及。 **取值范围**：每个元素最小长度1，最大长度63。 **默认取值**：不涉及。

        :return: The raycluster_endpoint_name of this InnerRayJobConfig.
        :rtype: list[str]
        """
        return self._raycluster_endpoint_name

    @raycluster_endpoint_name.setter
    def raycluster_endpoint_name(self, raycluster_endpoint_name):
        r"""Sets the raycluster_endpoint_name of this InnerRayJobConfig.

        **参数解释**：作业将运行的Ray集群端点列表，可设置多个。 **约束限制**：不涉及。 **取值范围**：每个元素最小长度1，最大长度63。 **默认取值**：不涉及。

        :param raycluster_endpoint_name: The raycluster_endpoint_name of this InnerRayJobConfig.
        :type raycluster_endpoint_name: list[str]
        """
        self._raycluster_endpoint_name = raycluster_endpoint_name

    @property
    def task_resources(self):
        r"""Gets the task_resources of this InnerRayJobConfig.

        **参数解释**：集群中所需的资源规格。 **约束限制**：最小值为1，最大值为4。

        :return: The task_resources of this InnerRayJobConfig.
        :rtype: list[str]
        """
        return self._task_resources

    @task_resources.setter
    def task_resources(self, task_resources):
        r"""Sets the task_resources of this InnerRayJobConfig.

        **参数解释**：集群中所需的资源规格。 **约束限制**：最小值为1，最大值为4。

        :param task_resources: The task_resources of this InnerRayJobConfig.
        :type task_resources: list[str]
        """
        self._task_resources = task_resources

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
        if not isinstance(other, InnerRayJobConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
