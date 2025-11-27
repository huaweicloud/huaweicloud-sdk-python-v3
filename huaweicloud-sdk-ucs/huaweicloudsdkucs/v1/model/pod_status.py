# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PodStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'phase': 'str',
        'host_ip': 'str',
        'start_time': 'str',
        'container_statuses': 'list[ContainerStatus]'
    }

    attribute_map = {
        'phase': 'phase',
        'host_ip': 'hostIP',
        'start_time': 'startTime',
        'container_statuses': 'containerStatuses'
    }

    def __init__(self, phase=None, host_ip=None, start_time=None, container_statuses=None):
        r"""PodStatus

        The model defined in huaweicloud sdk

        :param phase: 表示Pod的生命周期状态，有 5 种取值： - Pending：Pod 已被接受但尚未完全就绪 - Running：Pod 已绑定到节点且至少有一个容器在运行 - Succeeded：Pod 中所有容器都已成功终止，且不会被重启 - Failed：Pod 中至少一个容器失败终止 - Unknown：无法获取 Pod 状态
        :type phase: str
        :param host_ip: Pod所在主机的IP地址
        :type host_ip: str
        :param start_time: 记录Pod被Kubelet认可的时间
        :type start_time: str
        :param container_statuses: 容器的状态列表
        :type container_statuses: list[:class:`huaweicloudsdkucs.v1.ContainerStatus`]
        """
        
        

        self._phase = None
        self._host_ip = None
        self._start_time = None
        self._container_statuses = None
        self.discriminator = None

        if phase is not None:
            self.phase = phase
        if host_ip is not None:
            self.host_ip = host_ip
        if start_time is not None:
            self.start_time = start_time
        if container_statuses is not None:
            self.container_statuses = container_statuses

    @property
    def phase(self):
        r"""Gets the phase of this PodStatus.

        表示Pod的生命周期状态，有 5 种取值： - Pending：Pod 已被接受但尚未完全就绪 - Running：Pod 已绑定到节点且至少有一个容器在运行 - Succeeded：Pod 中所有容器都已成功终止，且不会被重启 - Failed：Pod 中至少一个容器失败终止 - Unknown：无法获取 Pod 状态

        :return: The phase of this PodStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        r"""Sets the phase of this PodStatus.

        表示Pod的生命周期状态，有 5 种取值： - Pending：Pod 已被接受但尚未完全就绪 - Running：Pod 已绑定到节点且至少有一个容器在运行 - Succeeded：Pod 中所有容器都已成功终止，且不会被重启 - Failed：Pod 中至少一个容器失败终止 - Unknown：无法获取 Pod 状态

        :param phase: The phase of this PodStatus.
        :type phase: str
        """
        self._phase = phase

    @property
    def host_ip(self):
        r"""Gets the host_ip of this PodStatus.

        Pod所在主机的IP地址

        :return: The host_ip of this PodStatus.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this PodStatus.

        Pod所在主机的IP地址

        :param host_ip: The host_ip of this PodStatus.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def start_time(self):
        r"""Gets the start_time of this PodStatus.

        记录Pod被Kubelet认可的时间

        :return: The start_time of this PodStatus.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this PodStatus.

        记录Pod被Kubelet认可的时间

        :param start_time: The start_time of this PodStatus.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def container_statuses(self):
        r"""Gets the container_statuses of this PodStatus.

        容器的状态列表

        :return: The container_statuses of this PodStatus.
        :rtype: list[:class:`huaweicloudsdkucs.v1.ContainerStatus`]
        """
        return self._container_statuses

    @container_statuses.setter
    def container_statuses(self, container_statuses):
        r"""Sets the container_statuses of this PodStatus.

        容器的状态列表

        :param container_statuses: The container_statuses of this PodStatus.
        :type container_statuses: list[:class:`huaweicloudsdkucs.v1.ContainerStatus`]
        """
        self._container_statuses = container_statuses

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
        if not isinstance(other, PodStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
