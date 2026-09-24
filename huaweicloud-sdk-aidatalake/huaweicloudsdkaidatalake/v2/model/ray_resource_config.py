# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RayResourceConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'head_resource_spec': 'RayHeadResourceSpec',
        'worker_resource_spec': 'list[RayWorkerResourceSpec]'
    }

    attribute_map = {
        'head_resource_spec': 'head_resource_spec',
        'worker_resource_spec': 'worker_resource_spec'
    }

    def __init__(self, head_resource_spec=None, worker_resource_spec=None):
        r"""RayResourceConfig

        The model defined in huaweicloud sdk

        :param head_resource_spec: 
        :type head_resource_spec: :class:`huaweicloudsdkaidatalake.v2.RayHeadResourceSpec`
        :param worker_resource_spec: **参数解释**：worker资源配置。 **约束限制**：仅提交作业到RayJob端点时配置。
        :type worker_resource_spec: list[:class:`huaweicloudsdkaidatalake.v2.RayWorkerResourceSpec`]
        """
        
        

        self._head_resource_spec = None
        self._worker_resource_spec = None
        self.discriminator = None

        self.head_resource_spec = head_resource_spec
        self.worker_resource_spec = worker_resource_spec

    @property
    def head_resource_spec(self):
        r"""Gets the head_resource_spec of this RayResourceConfig.

        :return: The head_resource_spec of this RayResourceConfig.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.RayHeadResourceSpec`
        """
        return self._head_resource_spec

    @head_resource_spec.setter
    def head_resource_spec(self, head_resource_spec):
        r"""Sets the head_resource_spec of this RayResourceConfig.

        :param head_resource_spec: The head_resource_spec of this RayResourceConfig.
        :type head_resource_spec: :class:`huaweicloudsdkaidatalake.v2.RayHeadResourceSpec`
        """
        self._head_resource_spec = head_resource_spec

    @property
    def worker_resource_spec(self):
        r"""Gets the worker_resource_spec of this RayResourceConfig.

        **参数解释**：worker资源配置。 **约束限制**：仅提交作业到RayJob端点时配置。

        :return: The worker_resource_spec of this RayResourceConfig.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.RayWorkerResourceSpec`]
        """
        return self._worker_resource_spec

    @worker_resource_spec.setter
    def worker_resource_spec(self, worker_resource_spec):
        r"""Sets the worker_resource_spec of this RayResourceConfig.

        **参数解释**：worker资源配置。 **约束限制**：仅提交作业到RayJob端点时配置。

        :param worker_resource_spec: The worker_resource_spec of this RayResourceConfig.
        :type worker_resource_spec: list[:class:`huaweicloudsdkaidatalake.v2.RayWorkerResourceSpec`]
        """
        self._worker_resource_spec = worker_resource_spec

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
        if not isinstance(other, RayResourceConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
