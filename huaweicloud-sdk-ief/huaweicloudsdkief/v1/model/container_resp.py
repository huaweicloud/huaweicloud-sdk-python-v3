# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContainerResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'args': 'list[str]',
        'command': 'list[str]',
        'name': 'str',
        'envs': 'list[EnvPods]',
        'image_url': 'str',
        'version': 'str',
        'liveness_probe': 'Probe',
        'readiness_probe': 'Probe',
        'ports': 'list[HostContainerPort]',
        'resources': 'DeploymentResources',
        'volumes': 'list[Volumes]',
        'restarts': 'int',
        'message': 'str',
        'reason': 'str',
        'is_ready': 'str',
        'privileged': 'bool',
        'container_id': 'str',
        'state': 'str',
        'npu_type': 'str'
    }

    attribute_map = {
        'args': 'args',
        'command': 'command',
        'name': 'name',
        'envs': 'envs',
        'image_url': 'image_url',
        'version': 'version',
        'liveness_probe': 'liveness_probe',
        'readiness_probe': 'readiness_probe',
        'ports': 'ports',
        'resources': 'resources',
        'volumes': 'volumes',
        'restarts': 'restarts',
        'message': 'message',
        'reason': 'reason',
        'is_ready': 'is_ready',
        'privileged': 'privileged',
        'container_id': 'container_id',
        'state': 'state',
        'npu_type': 'npu_type'
    }

    def __init__(self, args=None, command=None, name=None, envs=None, image_url=None, version=None, liveness_probe=None, readiness_probe=None, ports=None, resources=None, volumes=None, restarts=None, message=None, reason=None, is_ready=None, privileged=None, container_id=None, state=None, npu_type=None):
        """ContainerResp

        The model defined in huaweicloud sdk

        :param args: 容器启动参数，字符总长度最大为65536
        :type args: list[str]
        :param command: 容器启动命令，字符总长度最大为65536。 command支持使用数组定义多条命令，但在IEF控制台界面只会显示第一条命令。
        :type command: list[str]
        :param name: 容器名称，只允许英文小写字母、数字、中划线，最大长度32， 英文小写字母或数字开头和结尾
        :type name: str
        :param envs: 环境变量
        :type envs: list[:class:`huaweicloudsdkief.v1.EnvPods`]
        :param image_url: 容器镜像URL
        :type image_url: str
        :param version: 容器镜像版本
        :type version: str
        :param liveness_probe: 
        :type liveness_probe: :class:`huaweicloudsdkief.v1.Probe`
        :param readiness_probe: 
        :type readiness_probe: :class:`huaweicloudsdkief.v1.Probe`
        :param ports: 容器端口映射值
        :type ports: list[:class:`huaweicloudsdkief.v1.HostContainerPort`]
        :param resources: 
        :type resources: :class:`huaweicloudsdkief.v1.DeploymentResources`
        :param volumes: 卷配置
        :type volumes: list[:class:`huaweicloudsdkief.v1.Volumes`]
        :param restarts: 容器重启次数
        :type restarts: int
        :param message: 容器故障详情
        :type message: str
        :param reason: 容器故障原因
        :type reason: str
        :param is_ready: 健康检查结果
        :type is_ready: str
        :param privileged: 是否启用特权容器，默认值false
        :type privileged: bool
        :param container_id: 容器ID
        :type container_id: str
        :param state: 容器状态
        :type state: str
        :param npu_type: NPU类型，支持D310类型和D910类型。 - D310表示D310类型。 - D910表示D910类型。 - 不填表示为D310类型。
        :type npu_type: str
        """
        
        

        self._args = None
        self._command = None
        self._name = None
        self._envs = None
        self._image_url = None
        self._version = None
        self._liveness_probe = None
        self._readiness_probe = None
        self._ports = None
        self._resources = None
        self._volumes = None
        self._restarts = None
        self._message = None
        self._reason = None
        self._is_ready = None
        self._privileged = None
        self._container_id = None
        self._state = None
        self._npu_type = None
        self.discriminator = None

        if args is not None:
            self.args = args
        if command is not None:
            self.command = command
        self.name = name
        if envs is not None:
            self.envs = envs
        self.image_url = image_url
        if version is not None:
            self.version = version
        if liveness_probe is not None:
            self.liveness_probe = liveness_probe
        if readiness_probe is not None:
            self.readiness_probe = readiness_probe
        if ports is not None:
            self.ports = ports
        if resources is not None:
            self.resources = resources
        if volumes is not None:
            self.volumes = volumes
        if restarts is not None:
            self.restarts = restarts
        if message is not None:
            self.message = message
        if reason is not None:
            self.reason = reason
        if is_ready is not None:
            self.is_ready = is_ready
        if privileged is not None:
            self.privileged = privileged
        if container_id is not None:
            self.container_id = container_id
        if state is not None:
            self.state = state
        if npu_type is not None:
            self.npu_type = npu_type

    @property
    def args(self):
        """Gets the args of this ContainerResp.

        容器启动参数，字符总长度最大为65536

        :return: The args of this ContainerResp.
        :rtype: list[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this ContainerResp.

        容器启动参数，字符总长度最大为65536

        :param args: The args of this ContainerResp.
        :type args: list[str]
        """
        self._args = args

    @property
    def command(self):
        """Gets the command of this ContainerResp.

        容器启动命令，字符总长度最大为65536。 command支持使用数组定义多条命令，但在IEF控制台界面只会显示第一条命令。

        :return: The command of this ContainerResp.
        :rtype: list[str]
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this ContainerResp.

        容器启动命令，字符总长度最大为65536。 command支持使用数组定义多条命令，但在IEF控制台界面只会显示第一条命令。

        :param command: The command of this ContainerResp.
        :type command: list[str]
        """
        self._command = command

    @property
    def name(self):
        """Gets the name of this ContainerResp.

        容器名称，只允许英文小写字母、数字、中划线，最大长度32， 英文小写字母或数字开头和结尾

        :return: The name of this ContainerResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ContainerResp.

        容器名称，只允许英文小写字母、数字、中划线，最大长度32， 英文小写字母或数字开头和结尾

        :param name: The name of this ContainerResp.
        :type name: str
        """
        self._name = name

    @property
    def envs(self):
        """Gets the envs of this ContainerResp.

        环境变量

        :return: The envs of this ContainerResp.
        :rtype: list[:class:`huaweicloudsdkief.v1.EnvPods`]
        """
        return self._envs

    @envs.setter
    def envs(self, envs):
        """Sets the envs of this ContainerResp.

        环境变量

        :param envs: The envs of this ContainerResp.
        :type envs: list[:class:`huaweicloudsdkief.v1.EnvPods`]
        """
        self._envs = envs

    @property
    def image_url(self):
        """Gets the image_url of this ContainerResp.

        容器镜像URL

        :return: The image_url of this ContainerResp.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this ContainerResp.

        容器镜像URL

        :param image_url: The image_url of this ContainerResp.
        :type image_url: str
        """
        self._image_url = image_url

    @property
    def version(self):
        """Gets the version of this ContainerResp.

        容器镜像版本

        :return: The version of this ContainerResp.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ContainerResp.

        容器镜像版本

        :param version: The version of this ContainerResp.
        :type version: str
        """
        self._version = version

    @property
    def liveness_probe(self):
        """Gets the liveness_probe of this ContainerResp.


        :return: The liveness_probe of this ContainerResp.
        :rtype: :class:`huaweicloudsdkief.v1.Probe`
        """
        return self._liveness_probe

    @liveness_probe.setter
    def liveness_probe(self, liveness_probe):
        """Sets the liveness_probe of this ContainerResp.


        :param liveness_probe: The liveness_probe of this ContainerResp.
        :type liveness_probe: :class:`huaweicloudsdkief.v1.Probe`
        """
        self._liveness_probe = liveness_probe

    @property
    def readiness_probe(self):
        """Gets the readiness_probe of this ContainerResp.


        :return: The readiness_probe of this ContainerResp.
        :rtype: :class:`huaweicloudsdkief.v1.Probe`
        """
        return self._readiness_probe

    @readiness_probe.setter
    def readiness_probe(self, readiness_probe):
        """Sets the readiness_probe of this ContainerResp.


        :param readiness_probe: The readiness_probe of this ContainerResp.
        :type readiness_probe: :class:`huaweicloudsdkief.v1.Probe`
        """
        self._readiness_probe = readiness_probe

    @property
    def ports(self):
        """Gets the ports of this ContainerResp.

        容器端口映射值

        :return: The ports of this ContainerResp.
        :rtype: list[:class:`huaweicloudsdkief.v1.HostContainerPort`]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this ContainerResp.

        容器端口映射值

        :param ports: The ports of this ContainerResp.
        :type ports: list[:class:`huaweicloudsdkief.v1.HostContainerPort`]
        """
        self._ports = ports

    @property
    def resources(self):
        """Gets the resources of this ContainerResp.


        :return: The resources of this ContainerResp.
        :rtype: :class:`huaweicloudsdkief.v1.DeploymentResources`
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ContainerResp.


        :param resources: The resources of this ContainerResp.
        :type resources: :class:`huaweicloudsdkief.v1.DeploymentResources`
        """
        self._resources = resources

    @property
    def volumes(self):
        """Gets the volumes of this ContainerResp.

        卷配置

        :return: The volumes of this ContainerResp.
        :rtype: list[:class:`huaweicloudsdkief.v1.Volumes`]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this ContainerResp.

        卷配置

        :param volumes: The volumes of this ContainerResp.
        :type volumes: list[:class:`huaweicloudsdkief.v1.Volumes`]
        """
        self._volumes = volumes

    @property
    def restarts(self):
        """Gets the restarts of this ContainerResp.

        容器重启次数

        :return: The restarts of this ContainerResp.
        :rtype: int
        """
        return self._restarts

    @restarts.setter
    def restarts(self, restarts):
        """Sets the restarts of this ContainerResp.

        容器重启次数

        :param restarts: The restarts of this ContainerResp.
        :type restarts: int
        """
        self._restarts = restarts

    @property
    def message(self):
        """Gets the message of this ContainerResp.

        容器故障详情

        :return: The message of this ContainerResp.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ContainerResp.

        容器故障详情

        :param message: The message of this ContainerResp.
        :type message: str
        """
        self._message = message

    @property
    def reason(self):
        """Gets the reason of this ContainerResp.

        容器故障原因

        :return: The reason of this ContainerResp.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this ContainerResp.

        容器故障原因

        :param reason: The reason of this ContainerResp.
        :type reason: str
        """
        self._reason = reason

    @property
    def is_ready(self):
        """Gets the is_ready of this ContainerResp.

        健康检查结果

        :return: The is_ready of this ContainerResp.
        :rtype: str
        """
        return self._is_ready

    @is_ready.setter
    def is_ready(self, is_ready):
        """Sets the is_ready of this ContainerResp.

        健康检查结果

        :param is_ready: The is_ready of this ContainerResp.
        :type is_ready: str
        """
        self._is_ready = is_ready

    @property
    def privileged(self):
        """Gets the privileged of this ContainerResp.

        是否启用特权容器，默认值false

        :return: The privileged of this ContainerResp.
        :rtype: bool
        """
        return self._privileged

    @privileged.setter
    def privileged(self, privileged):
        """Sets the privileged of this ContainerResp.

        是否启用特权容器，默认值false

        :param privileged: The privileged of this ContainerResp.
        :type privileged: bool
        """
        self._privileged = privileged

    @property
    def container_id(self):
        """Gets the container_id of this ContainerResp.

        容器ID

        :return: The container_id of this ContainerResp.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        """Sets the container_id of this ContainerResp.

        容器ID

        :param container_id: The container_id of this ContainerResp.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def state(self):
        """Gets the state of this ContainerResp.

        容器状态

        :return: The state of this ContainerResp.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ContainerResp.

        容器状态

        :param state: The state of this ContainerResp.
        :type state: str
        """
        self._state = state

    @property
    def npu_type(self):
        """Gets the npu_type of this ContainerResp.

        NPU类型，支持D310类型和D910类型。 - D310表示D310类型。 - D910表示D910类型。 - 不填表示为D310类型。

        :return: The npu_type of this ContainerResp.
        :rtype: str
        """
        return self._npu_type

    @npu_type.setter
    def npu_type(self, npu_type):
        """Sets the npu_type of this ContainerResp.

        NPU类型，支持D310类型和D910类型。 - D310表示D310类型。 - D910表示D910类型。 - 不填表示为D310类型。

        :param npu_type: The npu_type of this ContainerResp.
        :type npu_type: str
        """
        self._npu_type = npu_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ContainerResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
