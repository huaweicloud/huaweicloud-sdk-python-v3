# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventForensicInfoContainerForensic:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'container_id': 'str',
        'container_status': 'str',
        'pod_uid': 'str',
        'pod_name': 'str',
        'namespace': 'str',
        'cluster_id': 'str',
        'cluster_name': 'str',
        'image_id': 'str',
        'image_name': 'str',
        'priviledged': 'bool',
        'pid_mode': 'str',
        'ipc_mode': 'str',
        'network_mode': 'str',
        'publish_allports': 'bool',
        'capabilities': 'str',
        'security_opts': 'str',
        'ports': 'str',
        'mounts': 'str',
        'sys_call': 'str',
        'container_name': 'str'
    }

    attribute_map = {
        'container_id': 'container_id',
        'container_status': 'container_status',
        'pod_uid': 'pod_uid',
        'pod_name': 'pod_name',
        'namespace': 'namespace',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'image_id': 'image_id',
        'image_name': 'image_name',
        'priviledged': 'priviledged',
        'pid_mode': 'pid_mode',
        'ipc_mode': 'ipc_mode',
        'network_mode': 'network_mode',
        'publish_allports': 'publish_allports',
        'capabilities': 'capabilities',
        'security_opts': 'security_opts',
        'ports': 'ports',
        'mounts': 'mounts',
        'sys_call': 'sys_call',
        'container_name': 'container_name'
    }

    def __init__(self, container_id=None, container_status=None, pod_uid=None, pod_name=None, namespace=None, cluster_id=None, cluster_name=None, image_id=None, image_name=None, priviledged=None, pid_mode=None, ipc_mode=None, network_mode=None, publish_allports=None, capabilities=None, security_opts=None, ports=None, mounts=None, sys_call=None, container_name=None):
        r"""EventForensicInfoContainerForensic

        The model defined in huaweicloud sdk

        :param container_id: **参数解释**： 容器ID **取值范围**： 不涉及
        :type container_id: str
        :param container_status: **参数解释**： 容器状态 **取值范围**： 不涉及
        :type container_status: str
        :param pod_uid: **参数解释**： pod uid **取值范围**： 不涉及
        :type pod_uid: str
        :param pod_name: **参数解释**： pod name **取值范围**： 不涉及
        :type pod_name: str
        :param namespace: **参数解释**： 命名空间 **取值范围**： 不涉及
        :type namespace: str
        :param cluster_id: **参数解释**： 集群id **取值范围**： 不涉及
        :type cluster_id: str
        :param cluster_name: **参数解释**： 集群名称 **取值范围**： 不涉及
        :type cluster_name: str
        :param image_id: **参数解释**： 镜像ID **取值范围**： 不涉及
        :type image_id: str
        :param image_name: **参数解释**： 镜像名称 **取值范围**： 不涉及
        :type image_name: str
        :param priviledged: **参数解释**： 容器特权开放 **取值范围**： 不涉及
        :type priviledged: bool
        :param pid_mode: **参数解释**： 容器pid命名空间模式 **取值范围**： 不涉及
        :type pid_mode: str
        :param ipc_mode: **参数解释**： 容器ipc命名空间模式 **取值范围**： 不涉及
        :type ipc_mode: str
        :param network_mode: **参数解释**： 容器网络命名空间模式 **取值范围**： 不涉及
        :type network_mode: str
        :param publish_allports: **参数解释**： 容器开放所有端口 **取值范围**： 不涉及
        :type publish_allports: bool
        :param capabilities: **参数解释**： 容器权限 **取值范围**： 不涉及
        :type capabilities: str
        :param security_opts: **参数解释**： 容器安全选项 **取值范围**： 不涉及
        :type security_opts: str
        :param ports: **参数解释**： 容器开放端口 **取值范围**： 不涉及
        :type ports: str
        :param mounts: **参数解释**： 容器挂载目录 **取值范围**： 不涉及
        :type mounts: str
        :param sys_call: **参数解释**： 系统调用 **取值范围**： 不涉及
        :type sys_call: str
        :param container_name: **参数解释**： 容器名称 **取值范围**： 不涉及
        :type container_name: str
        """
        
        

        self._container_id = None
        self._container_status = None
        self._pod_uid = None
        self._pod_name = None
        self._namespace = None
        self._cluster_id = None
        self._cluster_name = None
        self._image_id = None
        self._image_name = None
        self._priviledged = None
        self._pid_mode = None
        self._ipc_mode = None
        self._network_mode = None
        self._publish_allports = None
        self._capabilities = None
        self._security_opts = None
        self._ports = None
        self._mounts = None
        self._sys_call = None
        self._container_name = None
        self.discriminator = None

        if container_id is not None:
            self.container_id = container_id
        if container_status is not None:
            self.container_status = container_status
        if pod_uid is not None:
            self.pod_uid = pod_uid
        if pod_name is not None:
            self.pod_name = pod_name
        if namespace is not None:
            self.namespace = namespace
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if image_id is not None:
            self.image_id = image_id
        if image_name is not None:
            self.image_name = image_name
        if priviledged is not None:
            self.priviledged = priviledged
        if pid_mode is not None:
            self.pid_mode = pid_mode
        if ipc_mode is not None:
            self.ipc_mode = ipc_mode
        if network_mode is not None:
            self.network_mode = network_mode
        if publish_allports is not None:
            self.publish_allports = publish_allports
        if capabilities is not None:
            self.capabilities = capabilities
        if security_opts is not None:
            self.security_opts = security_opts
        if ports is not None:
            self.ports = ports
        if mounts is not None:
            self.mounts = mounts
        if sys_call is not None:
            self.sys_call = sys_call
        if container_name is not None:
            self.container_name = container_name

    @property
    def container_id(self):
        r"""Gets the container_id of this EventForensicInfoContainerForensic.

        **参数解释**： 容器ID **取值范围**： 不涉及

        :return: The container_id of this EventForensicInfoContainerForensic.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this EventForensicInfoContainerForensic.

        **参数解释**： 容器ID **取值范围**： 不涉及

        :param container_id: The container_id of this EventForensicInfoContainerForensic.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def container_status(self):
        r"""Gets the container_status of this EventForensicInfoContainerForensic.

        **参数解释**： 容器状态 **取值范围**： 不涉及

        :return: The container_status of this EventForensicInfoContainerForensic.
        :rtype: str
        """
        return self._container_status

    @container_status.setter
    def container_status(self, container_status):
        r"""Sets the container_status of this EventForensicInfoContainerForensic.

        **参数解释**： 容器状态 **取值范围**： 不涉及

        :param container_status: The container_status of this EventForensicInfoContainerForensic.
        :type container_status: str
        """
        self._container_status = container_status

    @property
    def pod_uid(self):
        r"""Gets the pod_uid of this EventForensicInfoContainerForensic.

        **参数解释**： pod uid **取值范围**： 不涉及

        :return: The pod_uid of this EventForensicInfoContainerForensic.
        :rtype: str
        """
        return self._pod_uid

    @pod_uid.setter
    def pod_uid(self, pod_uid):
        r"""Sets the pod_uid of this EventForensicInfoContainerForensic.

        **参数解释**： pod uid **取值范围**： 不涉及

        :param pod_uid: The pod_uid of this EventForensicInfoContainerForensic.
        :type pod_uid: str
        """
        self._pod_uid = pod_uid

    @property
    def pod_name(self):
        r"""Gets the pod_name of this EventForensicInfoContainerForensic.

        **参数解释**： pod name **取值范围**： 不涉及

        :return: The pod_name of this EventForensicInfoContainerForensic.
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        r"""Sets the pod_name of this EventForensicInfoContainerForensic.

        **参数解释**： pod name **取值范围**： 不涉及

        :param pod_name: The pod_name of this EventForensicInfoContainerForensic.
        :type pod_name: str
        """
        self._pod_name = pod_name

    @property
    def namespace(self):
        r"""Gets the namespace of this EventForensicInfoContainerForensic.

        **参数解释**： 命名空间 **取值范围**： 不涉及

        :return: The namespace of this EventForensicInfoContainerForensic.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this EventForensicInfoContainerForensic.

        **参数解释**： 命名空间 **取值范围**： 不涉及

        :param namespace: The namespace of this EventForensicInfoContainerForensic.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this EventForensicInfoContainerForensic.

        **参数解释**： 集群id **取值范围**： 不涉及

        :return: The cluster_id of this EventForensicInfoContainerForensic.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this EventForensicInfoContainerForensic.

        **参数解释**： 集群id **取值范围**： 不涉及

        :param cluster_id: The cluster_id of this EventForensicInfoContainerForensic.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this EventForensicInfoContainerForensic.

        **参数解释**： 集群名称 **取值范围**： 不涉及

        :return: The cluster_name of this EventForensicInfoContainerForensic.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this EventForensicInfoContainerForensic.

        **参数解释**： 集群名称 **取值范围**： 不涉及

        :param cluster_name: The cluster_name of this EventForensicInfoContainerForensic.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def image_id(self):
        r"""Gets the image_id of this EventForensicInfoContainerForensic.

        **参数解释**： 镜像ID **取值范围**： 不涉及

        :return: The image_id of this EventForensicInfoContainerForensic.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this EventForensicInfoContainerForensic.

        **参数解释**： 镜像ID **取值范围**： 不涉及

        :param image_id: The image_id of this EventForensicInfoContainerForensic.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_name(self):
        r"""Gets the image_name of this EventForensicInfoContainerForensic.

        **参数解释**： 镜像名称 **取值范围**： 不涉及

        :return: The image_name of this EventForensicInfoContainerForensic.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this EventForensicInfoContainerForensic.

        **参数解释**： 镜像名称 **取值范围**： 不涉及

        :param image_name: The image_name of this EventForensicInfoContainerForensic.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def priviledged(self):
        r"""Gets the priviledged of this EventForensicInfoContainerForensic.

        **参数解释**： 容器特权开放 **取值范围**： 不涉及

        :return: The priviledged of this EventForensicInfoContainerForensic.
        :rtype: bool
        """
        return self._priviledged

    @priviledged.setter
    def priviledged(self, priviledged):
        r"""Sets the priviledged of this EventForensicInfoContainerForensic.

        **参数解释**： 容器特权开放 **取值范围**： 不涉及

        :param priviledged: The priviledged of this EventForensicInfoContainerForensic.
        :type priviledged: bool
        """
        self._priviledged = priviledged

    @property
    def pid_mode(self):
        r"""Gets the pid_mode of this EventForensicInfoContainerForensic.

        **参数解释**： 容器pid命名空间模式 **取值范围**： 不涉及

        :return: The pid_mode of this EventForensicInfoContainerForensic.
        :rtype: str
        """
        return self._pid_mode

    @pid_mode.setter
    def pid_mode(self, pid_mode):
        r"""Sets the pid_mode of this EventForensicInfoContainerForensic.

        **参数解释**： 容器pid命名空间模式 **取值范围**： 不涉及

        :param pid_mode: The pid_mode of this EventForensicInfoContainerForensic.
        :type pid_mode: str
        """
        self._pid_mode = pid_mode

    @property
    def ipc_mode(self):
        r"""Gets the ipc_mode of this EventForensicInfoContainerForensic.

        **参数解释**： 容器ipc命名空间模式 **取值范围**： 不涉及

        :return: The ipc_mode of this EventForensicInfoContainerForensic.
        :rtype: str
        """
        return self._ipc_mode

    @ipc_mode.setter
    def ipc_mode(self, ipc_mode):
        r"""Sets the ipc_mode of this EventForensicInfoContainerForensic.

        **参数解释**： 容器ipc命名空间模式 **取值范围**： 不涉及

        :param ipc_mode: The ipc_mode of this EventForensicInfoContainerForensic.
        :type ipc_mode: str
        """
        self._ipc_mode = ipc_mode

    @property
    def network_mode(self):
        r"""Gets the network_mode of this EventForensicInfoContainerForensic.

        **参数解释**： 容器网络命名空间模式 **取值范围**： 不涉及

        :return: The network_mode of this EventForensicInfoContainerForensic.
        :rtype: str
        """
        return self._network_mode

    @network_mode.setter
    def network_mode(self, network_mode):
        r"""Sets the network_mode of this EventForensicInfoContainerForensic.

        **参数解释**： 容器网络命名空间模式 **取值范围**： 不涉及

        :param network_mode: The network_mode of this EventForensicInfoContainerForensic.
        :type network_mode: str
        """
        self._network_mode = network_mode

    @property
    def publish_allports(self):
        r"""Gets the publish_allports of this EventForensicInfoContainerForensic.

        **参数解释**： 容器开放所有端口 **取值范围**： 不涉及

        :return: The publish_allports of this EventForensicInfoContainerForensic.
        :rtype: bool
        """
        return self._publish_allports

    @publish_allports.setter
    def publish_allports(self, publish_allports):
        r"""Sets the publish_allports of this EventForensicInfoContainerForensic.

        **参数解释**： 容器开放所有端口 **取值范围**： 不涉及

        :param publish_allports: The publish_allports of this EventForensicInfoContainerForensic.
        :type publish_allports: bool
        """
        self._publish_allports = publish_allports

    @property
    def capabilities(self):
        r"""Gets the capabilities of this EventForensicInfoContainerForensic.

        **参数解释**： 容器权限 **取值范围**： 不涉及

        :return: The capabilities of this EventForensicInfoContainerForensic.
        :rtype: str
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        r"""Sets the capabilities of this EventForensicInfoContainerForensic.

        **参数解释**： 容器权限 **取值范围**： 不涉及

        :param capabilities: The capabilities of this EventForensicInfoContainerForensic.
        :type capabilities: str
        """
        self._capabilities = capabilities

    @property
    def security_opts(self):
        r"""Gets the security_opts of this EventForensicInfoContainerForensic.

        **参数解释**： 容器安全选项 **取值范围**： 不涉及

        :return: The security_opts of this EventForensicInfoContainerForensic.
        :rtype: str
        """
        return self._security_opts

    @security_opts.setter
    def security_opts(self, security_opts):
        r"""Sets the security_opts of this EventForensicInfoContainerForensic.

        **参数解释**： 容器安全选项 **取值范围**： 不涉及

        :param security_opts: The security_opts of this EventForensicInfoContainerForensic.
        :type security_opts: str
        """
        self._security_opts = security_opts

    @property
    def ports(self):
        r"""Gets the ports of this EventForensicInfoContainerForensic.

        **参数解释**： 容器开放端口 **取值范围**： 不涉及

        :return: The ports of this EventForensicInfoContainerForensic.
        :rtype: str
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        r"""Sets the ports of this EventForensicInfoContainerForensic.

        **参数解释**： 容器开放端口 **取值范围**： 不涉及

        :param ports: The ports of this EventForensicInfoContainerForensic.
        :type ports: str
        """
        self._ports = ports

    @property
    def mounts(self):
        r"""Gets the mounts of this EventForensicInfoContainerForensic.

        **参数解释**： 容器挂载目录 **取值范围**： 不涉及

        :return: The mounts of this EventForensicInfoContainerForensic.
        :rtype: str
        """
        return self._mounts

    @mounts.setter
    def mounts(self, mounts):
        r"""Sets the mounts of this EventForensicInfoContainerForensic.

        **参数解释**： 容器挂载目录 **取值范围**： 不涉及

        :param mounts: The mounts of this EventForensicInfoContainerForensic.
        :type mounts: str
        """
        self._mounts = mounts

    @property
    def sys_call(self):
        r"""Gets the sys_call of this EventForensicInfoContainerForensic.

        **参数解释**： 系统调用 **取值范围**： 不涉及

        :return: The sys_call of this EventForensicInfoContainerForensic.
        :rtype: str
        """
        return self._sys_call

    @sys_call.setter
    def sys_call(self, sys_call):
        r"""Sets the sys_call of this EventForensicInfoContainerForensic.

        **参数解释**： 系统调用 **取值范围**： 不涉及

        :param sys_call: The sys_call of this EventForensicInfoContainerForensic.
        :type sys_call: str
        """
        self._sys_call = sys_call

    @property
    def container_name(self):
        r"""Gets the container_name of this EventForensicInfoContainerForensic.

        **参数解释**： 容器名称 **取值范围**： 不涉及

        :return: The container_name of this EventForensicInfoContainerForensic.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this EventForensicInfoContainerForensic.

        **参数解释**： 容器名称 **取值范围**： 不涉及

        :param container_name: The container_name of this EventForensicInfoContainerForensic.
        :type container_name: str
        """
        self._container_name = container_name

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
        if not isinstance(other, EventForensicInfoContainerForensic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
