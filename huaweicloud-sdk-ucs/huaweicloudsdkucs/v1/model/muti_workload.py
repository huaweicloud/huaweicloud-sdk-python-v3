# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MutiWorkload:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kind': 'str',
        'api_version': 'str',
        'metadata': 'ObjectMeta',
        'template': 'object',
        'propagation_policy': 'PropagationPolicy',
        'override_policy': 'OverridePolicy',
        'resource_binding': 'ResourceBinding'
    }

    attribute_map = {
        'kind': 'kind',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'template': 'template',
        'propagation_policy': 'propagationPolicy',
        'override_policy': 'overridePolicy',
        'resource_binding': 'resourceBinding'
    }

    def __init__(self, kind=None, api_version=None, metadata=None, template=None, propagation_policy=None, override_policy=None, resource_binding=None):
        r"""MutiWorkload

        The model defined in huaweicloud sdk

        :param kind: 资源类型，有以下取值： - Deployment：用于管理无状态应用 - Service：实现服务发现和负载均衡 - Ingress：管理对集群内服务的外部 HTTP/HTTPS 访问 - ConfigMap：用于存储非敏感的配置数据 - Secret：用于存储敏感信息 - Job：用于运行一次性任务的资源 - StatefulSet：用于管理有状态应用 - DaemonSet：用于在每个节点上运行一个 Pod 的资源 - PersistentVolumeClaim：用于向集群申请并使用持久化存储资源的声明
        :type kind: str
        :param api_version: API版本
        :type api_version: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkucs.v1.ObjectMeta`
        :param template: 要部署的应用模板
        :type template: object
        :param propagation_policy: 
        :type propagation_policy: :class:`huaweicloudsdkucs.v1.PropagationPolicy`
        :param override_policy: 
        :type override_policy: :class:`huaweicloudsdkucs.v1.OverridePolicy`
        :param resource_binding: 
        :type resource_binding: :class:`huaweicloudsdkucs.v1.ResourceBinding`
        """
        
        

        self._kind = None
        self._api_version = None
        self._metadata = None
        self._template = None
        self._propagation_policy = None
        self._override_policy = None
        self._resource_binding = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if api_version is not None:
            self.api_version = api_version
        if metadata is not None:
            self.metadata = metadata
        if template is not None:
            self.template = template
        if propagation_policy is not None:
            self.propagation_policy = propagation_policy
        if override_policy is not None:
            self.override_policy = override_policy
        if resource_binding is not None:
            self.resource_binding = resource_binding

    @property
    def kind(self):
        r"""Gets the kind of this MutiWorkload.

        资源类型，有以下取值： - Deployment：用于管理无状态应用 - Service：实现服务发现和负载均衡 - Ingress：管理对集群内服务的外部 HTTP/HTTPS 访问 - ConfigMap：用于存储非敏感的配置数据 - Secret：用于存储敏感信息 - Job：用于运行一次性任务的资源 - StatefulSet：用于管理有状态应用 - DaemonSet：用于在每个节点上运行一个 Pod 的资源 - PersistentVolumeClaim：用于向集群申请并使用持久化存储资源的声明

        :return: The kind of this MutiWorkload.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this MutiWorkload.

        资源类型，有以下取值： - Deployment：用于管理无状态应用 - Service：实现服务发现和负载均衡 - Ingress：管理对集群内服务的外部 HTTP/HTTPS 访问 - ConfigMap：用于存储非敏感的配置数据 - Secret：用于存储敏感信息 - Job：用于运行一次性任务的资源 - StatefulSet：用于管理有状态应用 - DaemonSet：用于在每个节点上运行一个 Pod 的资源 - PersistentVolumeClaim：用于向集群申请并使用持久化存储资源的声明

        :param kind: The kind of this MutiWorkload.
        :type kind: str
        """
        self._kind = kind

    @property
    def api_version(self):
        r"""Gets the api_version of this MutiWorkload.

        API版本

        :return: The api_version of this MutiWorkload.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this MutiWorkload.

        API版本

        :param api_version: The api_version of this MutiWorkload.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def metadata(self):
        r"""Gets the metadata of this MutiWorkload.

        :return: The metadata of this MutiWorkload.
        :rtype: :class:`huaweicloudsdkucs.v1.ObjectMeta`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this MutiWorkload.

        :param metadata: The metadata of this MutiWorkload.
        :type metadata: :class:`huaweicloudsdkucs.v1.ObjectMeta`
        """
        self._metadata = metadata

    @property
    def template(self):
        r"""Gets the template of this MutiWorkload.

        要部署的应用模板

        :return: The template of this MutiWorkload.
        :rtype: object
        """
        return self._template

    @template.setter
    def template(self, template):
        r"""Sets the template of this MutiWorkload.

        要部署的应用模板

        :param template: The template of this MutiWorkload.
        :type template: object
        """
        self._template = template

    @property
    def propagation_policy(self):
        r"""Gets the propagation_policy of this MutiWorkload.

        :return: The propagation_policy of this MutiWorkload.
        :rtype: :class:`huaweicloudsdkucs.v1.PropagationPolicy`
        """
        return self._propagation_policy

    @propagation_policy.setter
    def propagation_policy(self, propagation_policy):
        r"""Sets the propagation_policy of this MutiWorkload.

        :param propagation_policy: The propagation_policy of this MutiWorkload.
        :type propagation_policy: :class:`huaweicloudsdkucs.v1.PropagationPolicy`
        """
        self._propagation_policy = propagation_policy

    @property
    def override_policy(self):
        r"""Gets the override_policy of this MutiWorkload.

        :return: The override_policy of this MutiWorkload.
        :rtype: :class:`huaweicloudsdkucs.v1.OverridePolicy`
        """
        return self._override_policy

    @override_policy.setter
    def override_policy(self, override_policy):
        r"""Sets the override_policy of this MutiWorkload.

        :param override_policy: The override_policy of this MutiWorkload.
        :type override_policy: :class:`huaweicloudsdkucs.v1.OverridePolicy`
        """
        self._override_policy = override_policy

    @property
    def resource_binding(self):
        r"""Gets the resource_binding of this MutiWorkload.

        :return: The resource_binding of this MutiWorkload.
        :rtype: :class:`huaweicloudsdkucs.v1.ResourceBinding`
        """
        return self._resource_binding

    @resource_binding.setter
    def resource_binding(self, resource_binding):
        r"""Sets the resource_binding of this MutiWorkload.

        :param resource_binding: The resource_binding of this MutiWorkload.
        :type resource_binding: :class:`huaweicloudsdkucs.v1.ResourceBinding`
        """
        self._resource_binding = resource_binding

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
        if not isinstance(other, MutiWorkload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
