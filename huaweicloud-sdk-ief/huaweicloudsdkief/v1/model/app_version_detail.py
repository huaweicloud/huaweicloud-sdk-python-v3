# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppVersionDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'version': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'project_id': 'str',
        'image_url': 'str',
        'envs': 'list[Env]',
        'volumes': 'list[Volumes]',
        'configs': 'AppConfigs',
        'resources': 'Resources',
        'arch': 'str',
        'command': 'list[str]',
        'args': 'list[str]',
        'liveness_probe': 'ProbeDetail',
        'readiness_probe': 'ProbeDetail',
        'npu_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'version': 'version',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'project_id': 'project_id',
        'image_url': 'image_url',
        'envs': 'envs',
        'volumes': 'volumes',
        'configs': 'configs',
        'resources': 'resources',
        'arch': 'arch',
        'command': 'command',
        'args': 'args',
        'liveness_probe': 'liveness_probe',
        'readiness_probe': 'readiness_probe',
        'npu_type': 'npu_type'
    }

    def __init__(self, id=None, version=None, created_at=None, updated_at=None, project_id=None, image_url=None, envs=None, volumes=None, configs=None, resources=None, arch=None, command=None, args=None, liveness_probe=None, readiness_probe=None, npu_type=None):
        """AppVersionDetail

        The model defined in huaweicloud sdk

        :param id: 应用版本ID
        :type id: str
        :param version: 应用版本号
        :type version: str
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间 只有更新后才会出现该字段
        :type updated_at: str
        :param project_id: 项目ID
        :type project_id: str
        :param image_url: 镜像存储地址
        :type image_url: str
        :param envs: 环境变量
        :type envs: list[:class:`huaweicloudsdkief.v1.Env`]
        :param volumes: 卷配置
        :type volumes: list[:class:`huaweicloudsdkief.v1.Volumes`]
        :param configs: 
        :type configs: :class:`huaweicloudsdkief.v1.AppConfigs`
        :param resources: 
        :type resources: :class:`huaweicloudsdkief.v1.Resources`
        :param arch: 架构
        :type arch: str
        :param command: 启动命令
        :type command: list[str]
        :param args: 参数
        :type args: list[str]
        :param liveness_probe: 
        :type liveness_probe: :class:`huaweicloudsdkief.v1.ProbeDetail`
        :param readiness_probe: 
        :type readiness_probe: :class:`huaweicloudsdkief.v1.ProbeDetail`
        :param npu_type: NPU芯片类型，可填：D310，D910
        :type npu_type: str
        """
        
        

        self._id = None
        self._version = None
        self._created_at = None
        self._updated_at = None
        self._project_id = None
        self._image_url = None
        self._envs = None
        self._volumes = None
        self._configs = None
        self._resources = None
        self._arch = None
        self._command = None
        self._args = None
        self._liveness_probe = None
        self._readiness_probe = None
        self._npu_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if version is not None:
            self.version = version
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if project_id is not None:
            self.project_id = project_id
        if image_url is not None:
            self.image_url = image_url
        self.envs = envs
        self.volumes = volumes
        if configs is not None:
            self.configs = configs
        if resources is not None:
            self.resources = resources
        if arch is not None:
            self.arch = arch
        if command is not None:
            self.command = command
        if args is not None:
            self.args = args
        if liveness_probe is not None:
            self.liveness_probe = liveness_probe
        if readiness_probe is not None:
            self.readiness_probe = readiness_probe
        if npu_type is not None:
            self.npu_type = npu_type

    @property
    def id(self):
        """Gets the id of this AppVersionDetail.

        应用版本ID

        :return: The id of this AppVersionDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AppVersionDetail.

        应用版本ID

        :param id: The id of this AppVersionDetail.
        :type id: str
        """
        self._id = id

    @property
    def version(self):
        """Gets the version of this AppVersionDetail.

        应用版本号

        :return: The version of this AppVersionDetail.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AppVersionDetail.

        应用版本号

        :param version: The version of this AppVersionDetail.
        :type version: str
        """
        self._version = version

    @property
    def created_at(self):
        """Gets the created_at of this AppVersionDetail.

        创建时间

        :return: The created_at of this AppVersionDetail.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AppVersionDetail.

        创建时间

        :param created_at: The created_at of this AppVersionDetail.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this AppVersionDetail.

        更新时间 只有更新后才会出现该字段

        :return: The updated_at of this AppVersionDetail.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AppVersionDetail.

        更新时间 只有更新后才会出现该字段

        :param updated_at: The updated_at of this AppVersionDetail.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def project_id(self):
        """Gets the project_id of this AppVersionDetail.

        项目ID

        :return: The project_id of this AppVersionDetail.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this AppVersionDetail.

        项目ID

        :param project_id: The project_id of this AppVersionDetail.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def image_url(self):
        """Gets the image_url of this AppVersionDetail.

        镜像存储地址

        :return: The image_url of this AppVersionDetail.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this AppVersionDetail.

        镜像存储地址

        :param image_url: The image_url of this AppVersionDetail.
        :type image_url: str
        """
        self._image_url = image_url

    @property
    def envs(self):
        """Gets the envs of this AppVersionDetail.

        环境变量

        :return: The envs of this AppVersionDetail.
        :rtype: list[:class:`huaweicloudsdkief.v1.Env`]
        """
        return self._envs

    @envs.setter
    def envs(self, envs):
        """Sets the envs of this AppVersionDetail.

        环境变量

        :param envs: The envs of this AppVersionDetail.
        :type envs: list[:class:`huaweicloudsdkief.v1.Env`]
        """
        self._envs = envs

    @property
    def volumes(self):
        """Gets the volumes of this AppVersionDetail.

        卷配置

        :return: The volumes of this AppVersionDetail.
        :rtype: list[:class:`huaweicloudsdkief.v1.Volumes`]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this AppVersionDetail.

        卷配置

        :param volumes: The volumes of this AppVersionDetail.
        :type volumes: list[:class:`huaweicloudsdkief.v1.Volumes`]
        """
        self._volumes = volumes

    @property
    def configs(self):
        """Gets the configs of this AppVersionDetail.

        :return: The configs of this AppVersionDetail.
        :rtype: :class:`huaweicloudsdkief.v1.AppConfigs`
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        """Sets the configs of this AppVersionDetail.

        :param configs: The configs of this AppVersionDetail.
        :type configs: :class:`huaweicloudsdkief.v1.AppConfigs`
        """
        self._configs = configs

    @property
    def resources(self):
        """Gets the resources of this AppVersionDetail.

        :return: The resources of this AppVersionDetail.
        :rtype: :class:`huaweicloudsdkief.v1.Resources`
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this AppVersionDetail.

        :param resources: The resources of this AppVersionDetail.
        :type resources: :class:`huaweicloudsdkief.v1.Resources`
        """
        self._resources = resources

    @property
    def arch(self):
        """Gets the arch of this AppVersionDetail.

        架构

        :return: The arch of this AppVersionDetail.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this AppVersionDetail.

        架构

        :param arch: The arch of this AppVersionDetail.
        :type arch: str
        """
        self._arch = arch

    @property
    def command(self):
        """Gets the command of this AppVersionDetail.

        启动命令

        :return: The command of this AppVersionDetail.
        :rtype: list[str]
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this AppVersionDetail.

        启动命令

        :param command: The command of this AppVersionDetail.
        :type command: list[str]
        """
        self._command = command

    @property
    def args(self):
        """Gets the args of this AppVersionDetail.

        参数

        :return: The args of this AppVersionDetail.
        :rtype: list[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this AppVersionDetail.

        参数

        :param args: The args of this AppVersionDetail.
        :type args: list[str]
        """
        self._args = args

    @property
    def liveness_probe(self):
        """Gets the liveness_probe of this AppVersionDetail.

        :return: The liveness_probe of this AppVersionDetail.
        :rtype: :class:`huaweicloudsdkief.v1.ProbeDetail`
        """
        return self._liveness_probe

    @liveness_probe.setter
    def liveness_probe(self, liveness_probe):
        """Sets the liveness_probe of this AppVersionDetail.

        :param liveness_probe: The liveness_probe of this AppVersionDetail.
        :type liveness_probe: :class:`huaweicloudsdkief.v1.ProbeDetail`
        """
        self._liveness_probe = liveness_probe

    @property
    def readiness_probe(self):
        """Gets the readiness_probe of this AppVersionDetail.

        :return: The readiness_probe of this AppVersionDetail.
        :rtype: :class:`huaweicloudsdkief.v1.ProbeDetail`
        """
        return self._readiness_probe

    @readiness_probe.setter
    def readiness_probe(self, readiness_probe):
        """Sets the readiness_probe of this AppVersionDetail.

        :param readiness_probe: The readiness_probe of this AppVersionDetail.
        :type readiness_probe: :class:`huaweicloudsdkief.v1.ProbeDetail`
        """
        self._readiness_probe = readiness_probe

    @property
    def npu_type(self):
        """Gets the npu_type of this AppVersionDetail.

        NPU芯片类型，可填：D310，D910

        :return: The npu_type of this AppVersionDetail.
        :rtype: str
        """
        return self._npu_type

    @npu_type.setter
    def npu_type(self, npu_type):
        """Sets the npu_type of this AppVersionDetail.

        NPU芯片类型，可填：D310，D910

        :param npu_type: The npu_type of this AppVersionDetail.
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
        if not isinstance(other, AppVersionDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
