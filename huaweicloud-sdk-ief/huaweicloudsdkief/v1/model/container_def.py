# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContainerDef:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'image_url': 'str',
        'args': 'list[str]',
        'command': 'list[str]',
        'resources': 'DeploymentResources',
        'envs': 'list[Env]',
        'ports': 'list[HostContainerPortMapping]',
        'privileged': 'bool',
        'run_as_user': 'int',
        'readiness_probe': 'Probe',
        'liveness_probe': 'Probe',
        'version': 'str',
        'volumes': 'list[Volumes]',
        'npu_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'image_url': 'image_url',
        'args': 'args',
        'command': 'command',
        'resources': 'resources',
        'envs': 'envs',
        'ports': 'ports',
        'privileged': 'privileged',
        'run_as_user': 'run_as_user',
        'readiness_probe': 'readiness_probe',
        'liveness_probe': 'liveness_probe',
        'version': 'version',
        'volumes': 'volumes',
        'npu_type': 'npu_type'
    }

    def __init__(self, name=None, image_url=None, args=None, command=None, resources=None, envs=None, ports=None, privileged=None, run_as_user=None, readiness_probe=None, liveness_probe=None, version=None, volumes=None, npu_type=None):
        """ContainerDef

        The model defined in huaweicloud sdk

        :param name: 容器名称，只允许英文小写字母、数字、中划线，最大长度32， 英文小写字母或数字开头和结尾
        :type name: str
        :param image_url: 容器镜像URL
        :type image_url: str
        :param args: 容器启动参数，字符总长度最大为65536
        :type args: list[str]
        :param command: 容器启动命令，字符总长度最大为65536。 command支持使用数组定义多条命令，但在IEF控制台界面只会显示第一条命令。
        :type command: list[str]
        :param resources: 
        :type resources: :class:`huaweicloudsdkief.v1.DeploymentResources`
        :param envs: 环境变量
        :type envs: list[:class:`huaweicloudsdkief.v1.Env`]
        :param ports: 容器端口映射值
        :type ports: list[:class:`huaweicloudsdkief.v1.HostContainerPortMapping`]
        :param privileged: 是否启用特权容器,默认值false
        :type privileged: bool
        :param run_as_user: 容器运行用户ID，输入范围为0~65534的整数
        :type run_as_user: int
        :param readiness_probe: 
        :type readiness_probe: :class:`huaweicloudsdkief.v1.Probe`
        :param liveness_probe: 
        :type liveness_probe: :class:`huaweicloudsdkief.v1.Probe`
        :param version: 容器镜像版本
        :type version: str
        :param volumes: 卷配置
        :type volumes: list[:class:`huaweicloudsdkief.v1.Volumes`]
        :param npu_type: NPU类型，支持D310类型和D910类型。 - D310表示D310类型。 - D910表示D910类型。 - 不填表示为D310类型。
        :type npu_type: str
        """
        
        

        self._name = None
        self._image_url = None
        self._args = None
        self._command = None
        self._resources = None
        self._envs = None
        self._ports = None
        self._privileged = None
        self._run_as_user = None
        self._readiness_probe = None
        self._liveness_probe = None
        self._version = None
        self._volumes = None
        self._npu_type = None
        self.discriminator = None

        self.name = name
        self.image_url = image_url
        if args is not None:
            self.args = args
        if command is not None:
            self.command = command
        if resources is not None:
            self.resources = resources
        if envs is not None:
            self.envs = envs
        if ports is not None:
            self.ports = ports
        if privileged is not None:
            self.privileged = privileged
        if run_as_user is not None:
            self.run_as_user = run_as_user
        if readiness_probe is not None:
            self.readiness_probe = readiness_probe
        if liveness_probe is not None:
            self.liveness_probe = liveness_probe
        if version is not None:
            self.version = version
        if volumes is not None:
            self.volumes = volumes
        if npu_type is not None:
            self.npu_type = npu_type

    @property
    def name(self):
        """Gets the name of this ContainerDef.

        容器名称，只允许英文小写字母、数字、中划线，最大长度32， 英文小写字母或数字开头和结尾

        :return: The name of this ContainerDef.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ContainerDef.

        容器名称，只允许英文小写字母、数字、中划线，最大长度32， 英文小写字母或数字开头和结尾

        :param name: The name of this ContainerDef.
        :type name: str
        """
        self._name = name

    @property
    def image_url(self):
        """Gets the image_url of this ContainerDef.

        容器镜像URL

        :return: The image_url of this ContainerDef.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this ContainerDef.

        容器镜像URL

        :param image_url: The image_url of this ContainerDef.
        :type image_url: str
        """
        self._image_url = image_url

    @property
    def args(self):
        """Gets the args of this ContainerDef.

        容器启动参数，字符总长度最大为65536

        :return: The args of this ContainerDef.
        :rtype: list[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this ContainerDef.

        容器启动参数，字符总长度最大为65536

        :param args: The args of this ContainerDef.
        :type args: list[str]
        """
        self._args = args

    @property
    def command(self):
        """Gets the command of this ContainerDef.

        容器启动命令，字符总长度最大为65536。 command支持使用数组定义多条命令，但在IEF控制台界面只会显示第一条命令。

        :return: The command of this ContainerDef.
        :rtype: list[str]
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this ContainerDef.

        容器启动命令，字符总长度最大为65536。 command支持使用数组定义多条命令，但在IEF控制台界面只会显示第一条命令。

        :param command: The command of this ContainerDef.
        :type command: list[str]
        """
        self._command = command

    @property
    def resources(self):
        """Gets the resources of this ContainerDef.

        :return: The resources of this ContainerDef.
        :rtype: :class:`huaweicloudsdkief.v1.DeploymentResources`
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ContainerDef.

        :param resources: The resources of this ContainerDef.
        :type resources: :class:`huaweicloudsdkief.v1.DeploymentResources`
        """
        self._resources = resources

    @property
    def envs(self):
        """Gets the envs of this ContainerDef.

        环境变量

        :return: The envs of this ContainerDef.
        :rtype: list[:class:`huaweicloudsdkief.v1.Env`]
        """
        return self._envs

    @envs.setter
    def envs(self, envs):
        """Sets the envs of this ContainerDef.

        环境变量

        :param envs: The envs of this ContainerDef.
        :type envs: list[:class:`huaweicloudsdkief.v1.Env`]
        """
        self._envs = envs

    @property
    def ports(self):
        """Gets the ports of this ContainerDef.

        容器端口映射值

        :return: The ports of this ContainerDef.
        :rtype: list[:class:`huaweicloudsdkief.v1.HostContainerPortMapping`]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this ContainerDef.

        容器端口映射值

        :param ports: The ports of this ContainerDef.
        :type ports: list[:class:`huaweicloudsdkief.v1.HostContainerPortMapping`]
        """
        self._ports = ports

    @property
    def privileged(self):
        """Gets the privileged of this ContainerDef.

        是否启用特权容器,默认值false

        :return: The privileged of this ContainerDef.
        :rtype: bool
        """
        return self._privileged

    @privileged.setter
    def privileged(self, privileged):
        """Sets the privileged of this ContainerDef.

        是否启用特权容器,默认值false

        :param privileged: The privileged of this ContainerDef.
        :type privileged: bool
        """
        self._privileged = privileged

    @property
    def run_as_user(self):
        """Gets the run_as_user of this ContainerDef.

        容器运行用户ID，输入范围为0~65534的整数

        :return: The run_as_user of this ContainerDef.
        :rtype: int
        """
        return self._run_as_user

    @run_as_user.setter
    def run_as_user(self, run_as_user):
        """Sets the run_as_user of this ContainerDef.

        容器运行用户ID，输入范围为0~65534的整数

        :param run_as_user: The run_as_user of this ContainerDef.
        :type run_as_user: int
        """
        self._run_as_user = run_as_user

    @property
    def readiness_probe(self):
        """Gets the readiness_probe of this ContainerDef.

        :return: The readiness_probe of this ContainerDef.
        :rtype: :class:`huaweicloudsdkief.v1.Probe`
        """
        return self._readiness_probe

    @readiness_probe.setter
    def readiness_probe(self, readiness_probe):
        """Sets the readiness_probe of this ContainerDef.

        :param readiness_probe: The readiness_probe of this ContainerDef.
        :type readiness_probe: :class:`huaweicloudsdkief.v1.Probe`
        """
        self._readiness_probe = readiness_probe

    @property
    def liveness_probe(self):
        """Gets the liveness_probe of this ContainerDef.

        :return: The liveness_probe of this ContainerDef.
        :rtype: :class:`huaweicloudsdkief.v1.Probe`
        """
        return self._liveness_probe

    @liveness_probe.setter
    def liveness_probe(self, liveness_probe):
        """Sets the liveness_probe of this ContainerDef.

        :param liveness_probe: The liveness_probe of this ContainerDef.
        :type liveness_probe: :class:`huaweicloudsdkief.v1.Probe`
        """
        self._liveness_probe = liveness_probe

    @property
    def version(self):
        """Gets the version of this ContainerDef.

        容器镜像版本

        :return: The version of this ContainerDef.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ContainerDef.

        容器镜像版本

        :param version: The version of this ContainerDef.
        :type version: str
        """
        self._version = version

    @property
    def volumes(self):
        """Gets the volumes of this ContainerDef.

        卷配置

        :return: The volumes of this ContainerDef.
        :rtype: list[:class:`huaweicloudsdkief.v1.Volumes`]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this ContainerDef.

        卷配置

        :param volumes: The volumes of this ContainerDef.
        :type volumes: list[:class:`huaweicloudsdkief.v1.Volumes`]
        """
        self._volumes = volumes

    @property
    def npu_type(self):
        """Gets the npu_type of this ContainerDef.

        NPU类型，支持D310类型和D910类型。 - D310表示D310类型。 - D910表示D910类型。 - 不填表示为D310类型。

        :return: The npu_type of this ContainerDef.
        :rtype: str
        """
        return self._npu_type

    @npu_type.setter
    def npu_type(self, npu_type):
        """Sets the npu_type of this ContainerDef.

        NPU类型，支持D310类型和D910类型。 - D310表示D310类型。 - D910表示D910类型。 - 不填表示为D310类型。

        :param npu_type: The npu_type of this ContainerDef.
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
        if not isinstance(other, ContainerDef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
