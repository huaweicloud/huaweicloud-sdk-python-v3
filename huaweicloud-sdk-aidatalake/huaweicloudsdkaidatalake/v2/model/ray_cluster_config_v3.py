# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RayClusterConfigV3:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'head_group_spec': 'HeadGroupSpecV3',
        'worker_group_specs': 'list[WorkerGroupSpecV3]'
    }

    attribute_map = {
        'head_group_spec': 'head_group_spec',
        'worker_group_specs': 'worker_group_specs'
    }

    def __init__(self, head_group_spec=None, worker_group_specs=None):
        r"""RayClusterConfigV3

        The model defined in huaweicloud sdk

        :param head_group_spec: 
        :type head_group_spec: :class:`huaweicloudsdkaidatalake.v2.HeadGroupSpecV3`
        :param worker_group_specs: **参数解释**：Worker Group的配置。 **约束限制**：不涉及。
        :type worker_group_specs: list[:class:`huaweicloudsdkaidatalake.v2.WorkerGroupSpecV3`]
        """
        
        

        self._head_group_spec = None
        self._worker_group_specs = None
        self.discriminator = None

        self.head_group_spec = head_group_spec
        self.worker_group_specs = worker_group_specs

    @property
    def head_group_spec(self):
        r"""Gets the head_group_spec of this RayClusterConfigV3.

        :return: The head_group_spec of this RayClusterConfigV3.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.HeadGroupSpecV3`
        """
        return self._head_group_spec

    @head_group_spec.setter
    def head_group_spec(self, head_group_spec):
        r"""Sets the head_group_spec of this RayClusterConfigV3.

        :param head_group_spec: The head_group_spec of this RayClusterConfigV3.
        :type head_group_spec: :class:`huaweicloudsdkaidatalake.v2.HeadGroupSpecV3`
        """
        self._head_group_spec = head_group_spec

    @property
    def worker_group_specs(self):
        r"""Gets the worker_group_specs of this RayClusterConfigV3.

        **参数解释**：Worker Group的配置。 **约束限制**：不涉及。

        :return: The worker_group_specs of this RayClusterConfigV3.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.WorkerGroupSpecV3`]
        """
        return self._worker_group_specs

    @worker_group_specs.setter
    def worker_group_specs(self, worker_group_specs):
        r"""Sets the worker_group_specs of this RayClusterConfigV3.

        **参数解释**：Worker Group的配置。 **约束限制**：不涉及。

        :param worker_group_specs: The worker_group_specs of this RayClusterConfigV3.
        :type worker_group_specs: list[:class:`huaweicloudsdkaidatalake.v2.WorkerGroupSpecV3`]
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
        if not isinstance(other, RayClusterConfigV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
