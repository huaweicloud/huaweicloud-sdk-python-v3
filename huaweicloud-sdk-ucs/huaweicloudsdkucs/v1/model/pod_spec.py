# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PodSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'volumes': 'list[object]',
        'containers': 'list[object]',
        'restart_policy': 'str',
        'termination_grace_period_seconds': 'int',
        'active_deadline_seconds': 'int',
        'dns_policy': 'str',
        'node_selector': 'dict(str, str)',
        'service_account_name': 'str',
        'service_account': 'str',
        'automount_service_account_token': 'bool',
        'node_name': 'str',
        'security_context': 'object',
        'scheduler_name': 'str',
        'tolerations': 'list[Toleration]',
        'priority': 'int',
        'enable_service_links': 'bool',
        'preemption_policy': 'str'
    }

    attribute_map = {
        'volumes': 'volumes',
        'containers': 'containers',
        'restart_policy': 'restartPolicy',
        'termination_grace_period_seconds': 'terminationGracePeriodSeconds',
        'active_deadline_seconds': 'activeDeadlineSeconds',
        'dns_policy': 'dnsPolicy',
        'node_selector': 'nodeSelector',
        'service_account_name': 'serviceAccountName',
        'service_account': 'serviceAccount',
        'automount_service_account_token': 'automountServiceAccountToken',
        'node_name': 'nodeName',
        'security_context': 'securityContext',
        'scheduler_name': 'schedulerName',
        'tolerations': 'tolerations',
        'priority': 'priority',
        'enable_service_links': 'enableServiceLinks',
        'preemption_policy': 'preemptionPolicy'
    }

    def __init__(self, volumes=None, containers=None, restart_policy=None, termination_grace_period_seconds=None, active_deadline_seconds=None, dns_policy=None, node_selector=None, service_account_name=None, service_account=None, automount_service_account_token=None, node_name=None, security_context=None, scheduler_name=None, tolerations=None, priority=None, enable_service_links=None, preemption_policy=None):
        r"""PodSpec

        The model defined in huaweicloud sdk

        :param volumes: 定义 Pod 可以挂载的存储卷列表
        :type volumes: list[object]
        :param containers: Pod中的主要容器列表
        :type containers: list[object]
        :param restart_policy: 容器失败后的重启策略
        :type restart_policy: str
        :param termination_grace_period_seconds: 容器终止前的优雅退出时间
        :type termination_grace_period_seconds: int
        :param active_deadline_seconds: Pod在节点上的最大存活时间
        :type active_deadline_seconds: int
        :param dns_policy: DNS策略
        :type dns_policy: str
        :param node_selector: 节点选择器，用于指定Pod可以调度到哪些节点
        :type node_selector: dict(str, str)
        :param service_account_name: 运行此Pod所使用的ServiceAccount名称
        :type service_account_name: str
        :param service_account: 提供向后兼容的旧版ServiceAccount字段
        :type service_account: str
        :param automount_service_account_token: 是否自动挂载ServiceAccount的令牌
        :type automount_service_account_token: bool
        :param node_name: 指定Pod应该调度到的节点
        :type node_name: str
        :param security_context: Pod级别的安全上下文
        :type security_context: object
        :param scheduler_name: 指定使用的调度器
        :type scheduler_name: str
        :param tolerations: 容器容忍的污点列表
        :type tolerations: list[:class:`huaweicloudsdkucs.v1.Toleration`]
        :param priority: Pod 的优先级
        :type priority: int
        :param enable_service_links: 服务信息是否注入到Pod的环境变量中
        :type enable_service_links: bool
        :param preemption_policy: 抢占优先级策略
        :type preemption_policy: str
        """
        
        

        self._volumes = None
        self._containers = None
        self._restart_policy = None
        self._termination_grace_period_seconds = None
        self._active_deadline_seconds = None
        self._dns_policy = None
        self._node_selector = None
        self._service_account_name = None
        self._service_account = None
        self._automount_service_account_token = None
        self._node_name = None
        self._security_context = None
        self._scheduler_name = None
        self._tolerations = None
        self._priority = None
        self._enable_service_links = None
        self._preemption_policy = None
        self.discriminator = None

        if volumes is not None:
            self.volumes = volumes
        if containers is not None:
            self.containers = containers
        if restart_policy is not None:
            self.restart_policy = restart_policy
        if termination_grace_period_seconds is not None:
            self.termination_grace_period_seconds = termination_grace_period_seconds
        if active_deadline_seconds is not None:
            self.active_deadline_seconds = active_deadline_seconds
        if dns_policy is not None:
            self.dns_policy = dns_policy
        if node_selector is not None:
            self.node_selector = node_selector
        if service_account_name is not None:
            self.service_account_name = service_account_name
        if service_account is not None:
            self.service_account = service_account
        if automount_service_account_token is not None:
            self.automount_service_account_token = automount_service_account_token
        if node_name is not None:
            self.node_name = node_name
        if security_context is not None:
            self.security_context = security_context
        if scheduler_name is not None:
            self.scheduler_name = scheduler_name
        if tolerations is not None:
            self.tolerations = tolerations
        if priority is not None:
            self.priority = priority
        if enable_service_links is not None:
            self.enable_service_links = enable_service_links
        if preemption_policy is not None:
            self.preemption_policy = preemption_policy

    @property
    def volumes(self):
        r"""Gets the volumes of this PodSpec.

        定义 Pod 可以挂载的存储卷列表

        :return: The volumes of this PodSpec.
        :rtype: list[object]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        r"""Sets the volumes of this PodSpec.

        定义 Pod 可以挂载的存储卷列表

        :param volumes: The volumes of this PodSpec.
        :type volumes: list[object]
        """
        self._volumes = volumes

    @property
    def containers(self):
        r"""Gets the containers of this PodSpec.

        Pod中的主要容器列表

        :return: The containers of this PodSpec.
        :rtype: list[object]
        """
        return self._containers

    @containers.setter
    def containers(self, containers):
        r"""Sets the containers of this PodSpec.

        Pod中的主要容器列表

        :param containers: The containers of this PodSpec.
        :type containers: list[object]
        """
        self._containers = containers

    @property
    def restart_policy(self):
        r"""Gets the restart_policy of this PodSpec.

        容器失败后的重启策略

        :return: The restart_policy of this PodSpec.
        :rtype: str
        """
        return self._restart_policy

    @restart_policy.setter
    def restart_policy(self, restart_policy):
        r"""Sets the restart_policy of this PodSpec.

        容器失败后的重启策略

        :param restart_policy: The restart_policy of this PodSpec.
        :type restart_policy: str
        """
        self._restart_policy = restart_policy

    @property
    def termination_grace_period_seconds(self):
        r"""Gets the termination_grace_period_seconds of this PodSpec.

        容器终止前的优雅退出时间

        :return: The termination_grace_period_seconds of this PodSpec.
        :rtype: int
        """
        return self._termination_grace_period_seconds

    @termination_grace_period_seconds.setter
    def termination_grace_period_seconds(self, termination_grace_period_seconds):
        r"""Sets the termination_grace_period_seconds of this PodSpec.

        容器终止前的优雅退出时间

        :param termination_grace_period_seconds: The termination_grace_period_seconds of this PodSpec.
        :type termination_grace_period_seconds: int
        """
        self._termination_grace_period_seconds = termination_grace_period_seconds

    @property
    def active_deadline_seconds(self):
        r"""Gets the active_deadline_seconds of this PodSpec.

        Pod在节点上的最大存活时间

        :return: The active_deadline_seconds of this PodSpec.
        :rtype: int
        """
        return self._active_deadline_seconds

    @active_deadline_seconds.setter
    def active_deadline_seconds(self, active_deadline_seconds):
        r"""Sets the active_deadline_seconds of this PodSpec.

        Pod在节点上的最大存活时间

        :param active_deadline_seconds: The active_deadline_seconds of this PodSpec.
        :type active_deadline_seconds: int
        """
        self._active_deadline_seconds = active_deadline_seconds

    @property
    def dns_policy(self):
        r"""Gets the dns_policy of this PodSpec.

        DNS策略

        :return: The dns_policy of this PodSpec.
        :rtype: str
        """
        return self._dns_policy

    @dns_policy.setter
    def dns_policy(self, dns_policy):
        r"""Sets the dns_policy of this PodSpec.

        DNS策略

        :param dns_policy: The dns_policy of this PodSpec.
        :type dns_policy: str
        """
        self._dns_policy = dns_policy

    @property
    def node_selector(self):
        r"""Gets the node_selector of this PodSpec.

        节点选择器，用于指定Pod可以调度到哪些节点

        :return: The node_selector of this PodSpec.
        :rtype: dict(str, str)
        """
        return self._node_selector

    @node_selector.setter
    def node_selector(self, node_selector):
        r"""Sets the node_selector of this PodSpec.

        节点选择器，用于指定Pod可以调度到哪些节点

        :param node_selector: The node_selector of this PodSpec.
        :type node_selector: dict(str, str)
        """
        self._node_selector = node_selector

    @property
    def service_account_name(self):
        r"""Gets the service_account_name of this PodSpec.

        运行此Pod所使用的ServiceAccount名称

        :return: The service_account_name of this PodSpec.
        :rtype: str
        """
        return self._service_account_name

    @service_account_name.setter
    def service_account_name(self, service_account_name):
        r"""Sets the service_account_name of this PodSpec.

        运行此Pod所使用的ServiceAccount名称

        :param service_account_name: The service_account_name of this PodSpec.
        :type service_account_name: str
        """
        self._service_account_name = service_account_name

    @property
    def service_account(self):
        r"""Gets the service_account of this PodSpec.

        提供向后兼容的旧版ServiceAccount字段

        :return: The service_account of this PodSpec.
        :rtype: str
        """
        return self._service_account

    @service_account.setter
    def service_account(self, service_account):
        r"""Sets the service_account of this PodSpec.

        提供向后兼容的旧版ServiceAccount字段

        :param service_account: The service_account of this PodSpec.
        :type service_account: str
        """
        self._service_account = service_account

    @property
    def automount_service_account_token(self):
        r"""Gets the automount_service_account_token of this PodSpec.

        是否自动挂载ServiceAccount的令牌

        :return: The automount_service_account_token of this PodSpec.
        :rtype: bool
        """
        return self._automount_service_account_token

    @automount_service_account_token.setter
    def automount_service_account_token(self, automount_service_account_token):
        r"""Sets the automount_service_account_token of this PodSpec.

        是否自动挂载ServiceAccount的令牌

        :param automount_service_account_token: The automount_service_account_token of this PodSpec.
        :type automount_service_account_token: bool
        """
        self._automount_service_account_token = automount_service_account_token

    @property
    def node_name(self):
        r"""Gets the node_name of this PodSpec.

        指定Pod应该调度到的节点

        :return: The node_name of this PodSpec.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this PodSpec.

        指定Pod应该调度到的节点

        :param node_name: The node_name of this PodSpec.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def security_context(self):
        r"""Gets the security_context of this PodSpec.

        Pod级别的安全上下文

        :return: The security_context of this PodSpec.
        :rtype: object
        """
        return self._security_context

    @security_context.setter
    def security_context(self, security_context):
        r"""Sets the security_context of this PodSpec.

        Pod级别的安全上下文

        :param security_context: The security_context of this PodSpec.
        :type security_context: object
        """
        self._security_context = security_context

    @property
    def scheduler_name(self):
        r"""Gets the scheduler_name of this PodSpec.

        指定使用的调度器

        :return: The scheduler_name of this PodSpec.
        :rtype: str
        """
        return self._scheduler_name

    @scheduler_name.setter
    def scheduler_name(self, scheduler_name):
        r"""Sets the scheduler_name of this PodSpec.

        指定使用的调度器

        :param scheduler_name: The scheduler_name of this PodSpec.
        :type scheduler_name: str
        """
        self._scheduler_name = scheduler_name

    @property
    def tolerations(self):
        r"""Gets the tolerations of this PodSpec.

        容器容忍的污点列表

        :return: The tolerations of this PodSpec.
        :rtype: list[:class:`huaweicloudsdkucs.v1.Toleration`]
        """
        return self._tolerations

    @tolerations.setter
    def tolerations(self, tolerations):
        r"""Sets the tolerations of this PodSpec.

        容器容忍的污点列表

        :param tolerations: The tolerations of this PodSpec.
        :type tolerations: list[:class:`huaweicloudsdkucs.v1.Toleration`]
        """
        self._tolerations = tolerations

    @property
    def priority(self):
        r"""Gets the priority of this PodSpec.

        Pod 的优先级

        :return: The priority of this PodSpec.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this PodSpec.

        Pod 的优先级

        :param priority: The priority of this PodSpec.
        :type priority: int
        """
        self._priority = priority

    @property
    def enable_service_links(self):
        r"""Gets the enable_service_links of this PodSpec.

        服务信息是否注入到Pod的环境变量中

        :return: The enable_service_links of this PodSpec.
        :rtype: bool
        """
        return self._enable_service_links

    @enable_service_links.setter
    def enable_service_links(self, enable_service_links):
        r"""Sets the enable_service_links of this PodSpec.

        服务信息是否注入到Pod的环境变量中

        :param enable_service_links: The enable_service_links of this PodSpec.
        :type enable_service_links: bool
        """
        self._enable_service_links = enable_service_links

    @property
    def preemption_policy(self):
        r"""Gets the preemption_policy of this PodSpec.

        抢占优先级策略

        :return: The preemption_policy of this PodSpec.
        :rtype: str
        """
        return self._preemption_policy

    @preemption_policy.setter
    def preemption_policy(self, preemption_policy):
        r"""Sets the preemption_policy of this PodSpec.

        抢占优先级策略

        :param preemption_policy: The preemption_policy of this PodSpec.
        :type preemption_policy: str
        """
        self._preemption_policy = preemption_policy

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
        if not isinstance(other, PodSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
