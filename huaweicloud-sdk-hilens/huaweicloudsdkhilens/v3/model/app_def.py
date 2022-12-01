# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppDef:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_docker_login': 'str',
        'app_id': 'str',
        'expire_time': 'int',
        'image_url': 'str',
        'license': 'License',
        'model_key': 'str',
        'app_order_id': 'str',
        'app_url': 'str',
        'channel_limit': 'int',
        'channel_upper_limit': 'int',
        'args': 'list[str]',
        'command': 'list[str]',
        'envs': 'list[Env]',
        'is_modelbox': 'bool',
        'liveness_probe': 'Probe',
        'msgs': 'list[Env]',
        'name': 'str',
        'npu_type': 'str',
        'ports': 'list[HostContainerPortMapping]',
        'privileged': 'bool',
        'readiness_probe': 'Probe',
        'resources': 'ResQuest',
        'version': 'str',
        'volumes': 'list[Volume]'
    }

    attribute_map = {
        'app_docker_login': 'app_docker_login',
        'app_id': 'app_id',
        'expire_time': 'expire_time',
        'image_url': 'image_url',
        'license': 'license',
        'model_key': 'modelKey',
        'app_order_id': 'app_order_id',
        'app_url': 'app_url',
        'channel_limit': 'channel_limit',
        'channel_upper_limit': 'channel_upper_limit',
        'args': 'args',
        'command': 'command',
        'envs': 'envs',
        'is_modelbox': 'is_modelbox',
        'liveness_probe': 'liveness_probe',
        'msgs': 'msgs',
        'name': 'name',
        'npu_type': 'npu_type',
        'ports': 'ports',
        'privileged': 'privileged',
        'readiness_probe': 'readiness_probe',
        'resources': 'resources',
        'version': 'version',
        'volumes': 'volumes'
    }

    def __init__(self, app_docker_login=None, app_id=None, expire_time=None, image_url=None, license=None, model_key=None, app_order_id=None, app_url=None, channel_limit=None, channel_upper_limit=None, args=None, command=None, envs=None, is_modelbox=None, liveness_probe=None, msgs=None, name=None, npu_type=None, ports=None, privileged=None, readiness_probe=None, resources=None, version=None, volumes=None):
        """AppDef

        The model defined in huaweicloud sdk

        :param app_docker_login: 
        :type app_docker_login: str
        :param app_id: 
        :type app_id: str
        :param expire_time: 
        :type expire_time: int
        :param image_url: 
        :type image_url: str
        :param license: 
        :type license: :class:`huaweicloudsdkhilens.v3.License`
        :param model_key: 
        :type model_key: str
        :param app_order_id: app应用的订单ID，技能来源是市场时，如果不填，则自动选择默认订单。
        :type app_order_id: str
        :param app_url: app应用的地址，可以是镜像地址或者OBS地址
        :type app_url: str
        :param channel_limit: 路数限制，添加作业的时候，摄像头和VCN的最大路数不超过该值，范围是0到1000
        :type channel_limit: int
        :param channel_upper_limit: 用户可以指定的路数限制上限，范围是0到1000
        :type channel_upper_limit: int
        :param args: 容器启动参数，字符总长度最大为65536，不允许^#~^$|%&amp;*&lt;&gt;()&#39;\&quot;\\[\\]{}]等特殊字符
        :type args: list[str]
        :param command: 容器启动命令，字符总长度最大为65536。 command支持使用数组定义多条命令，但在IEF控制台界面只会显示第一条命令。不允许^#~^$|%&amp;*&lt;&gt;()&#39;\&quot;\\[\\]{}]等特殊字符
        :type command: list[str]
        :param envs: 环境变量
        :type envs: list[:class:`huaweicloudsdkhilens.v3.Env`]
        :param is_modelbox: 是否是modelbox镜像
        :type is_modelbox: bool
        :param liveness_probe: 
        :type liveness_probe: :class:`huaweicloudsdkhilens.v3.Probe`
        :param msgs: 消息变量
        :type msgs: list[:class:`huaweicloudsdkhilens.v3.Env`]
        :param name: 应用名字，只允许英文小写字母、数字、中划线，最大长度32, 英文小写字母或数字开头和结尾。该名称同时对应技能名称，当不传订单id的时候，默认通过该名称和版本号version字段，选择指定技能版本，进行部署，并选择可用的订单（默认订单优先）扣除份额。
        :type name: str
        :param npu_type: npu类型，支持D310类型和D910类型。D310表示D310类型。  D910表示D910类型。不填表示为D310类型
        :type npu_type: str
        :param ports: 容器端口映射值
        :type ports: list[:class:`huaweicloudsdkhilens.v3.HostContainerPortMapping`]
        :param privileged: 是否启用特权容器,默认值false
        :type privileged: bool
        :param readiness_probe: 
        :type readiness_probe: :class:`huaweicloudsdkhilens.v3.Probe`
        :param resources: 
        :type resources: :class:`huaweicloudsdkhilens.v3.ResQuest`
        :param version: 版本号，长度不操作128，支持大小写数字，下划线，点，中划线
        :type version: str
        :param volumes: 卷配置
        :type volumes: list[:class:`huaweicloudsdkhilens.v3.Volume`]
        """
        
        

        self._app_docker_login = None
        self._app_id = None
        self._expire_time = None
        self._image_url = None
        self._license = None
        self._model_key = None
        self._app_order_id = None
        self._app_url = None
        self._channel_limit = None
        self._channel_upper_limit = None
        self._args = None
        self._command = None
        self._envs = None
        self._is_modelbox = None
        self._liveness_probe = None
        self._msgs = None
        self._name = None
        self._npu_type = None
        self._ports = None
        self._privileged = None
        self._readiness_probe = None
        self._resources = None
        self._version = None
        self._volumes = None
        self.discriminator = None

        if app_docker_login is not None:
            self.app_docker_login = app_docker_login
        if app_id is not None:
            self.app_id = app_id
        if expire_time is not None:
            self.expire_time = expire_time
        if image_url is not None:
            self.image_url = image_url
        if license is not None:
            self.license = license
        if model_key is not None:
            self.model_key = model_key
        if app_order_id is not None:
            self.app_order_id = app_order_id
        if app_url is not None:
            self.app_url = app_url
        if channel_limit is not None:
            self.channel_limit = channel_limit
        if channel_upper_limit is not None:
            self.channel_upper_limit = channel_upper_limit
        if args is not None:
            self.args = args
        if command is not None:
            self.command = command
        if envs is not None:
            self.envs = envs
        if is_modelbox is not None:
            self.is_modelbox = is_modelbox
        if liveness_probe is not None:
            self.liveness_probe = liveness_probe
        if msgs is not None:
            self.msgs = msgs
        if name is not None:
            self.name = name
        if npu_type is not None:
            self.npu_type = npu_type
        if ports is not None:
            self.ports = ports
        if privileged is not None:
            self.privileged = privileged
        if readiness_probe is not None:
            self.readiness_probe = readiness_probe
        if resources is not None:
            self.resources = resources
        if version is not None:
            self.version = version
        if volumes is not None:
            self.volumes = volumes

    @property
    def app_docker_login(self):
        """Gets the app_docker_login of this AppDef.

        :return: The app_docker_login of this AppDef.
        :rtype: str
        """
        return self._app_docker_login

    @app_docker_login.setter
    def app_docker_login(self, app_docker_login):
        """Sets the app_docker_login of this AppDef.

        :param app_docker_login: The app_docker_login of this AppDef.
        :type app_docker_login: str
        """
        self._app_docker_login = app_docker_login

    @property
    def app_id(self):
        """Gets the app_id of this AppDef.

        :return: The app_id of this AppDef.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this AppDef.

        :param app_id: The app_id of this AppDef.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def expire_time(self):
        """Gets the expire_time of this AppDef.

        :return: The expire_time of this AppDef.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this AppDef.

        :param expire_time: The expire_time of this AppDef.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def image_url(self):
        """Gets the image_url of this AppDef.

        :return: The image_url of this AppDef.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this AppDef.

        :param image_url: The image_url of this AppDef.
        :type image_url: str
        """
        self._image_url = image_url

    @property
    def license(self):
        """Gets the license of this AppDef.

        :return: The license of this AppDef.
        :rtype: :class:`huaweicloudsdkhilens.v3.License`
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this AppDef.

        :param license: The license of this AppDef.
        :type license: :class:`huaweicloudsdkhilens.v3.License`
        """
        self._license = license

    @property
    def model_key(self):
        """Gets the model_key of this AppDef.

        :return: The model_key of this AppDef.
        :rtype: str
        """
        return self._model_key

    @model_key.setter
    def model_key(self, model_key):
        """Sets the model_key of this AppDef.

        :param model_key: The model_key of this AppDef.
        :type model_key: str
        """
        self._model_key = model_key

    @property
    def app_order_id(self):
        """Gets the app_order_id of this AppDef.

        app应用的订单ID，技能来源是市场时，如果不填，则自动选择默认订单。

        :return: The app_order_id of this AppDef.
        :rtype: str
        """
        return self._app_order_id

    @app_order_id.setter
    def app_order_id(self, app_order_id):
        """Sets the app_order_id of this AppDef.

        app应用的订单ID，技能来源是市场时，如果不填，则自动选择默认订单。

        :param app_order_id: The app_order_id of this AppDef.
        :type app_order_id: str
        """
        self._app_order_id = app_order_id

    @property
    def app_url(self):
        """Gets the app_url of this AppDef.

        app应用的地址，可以是镜像地址或者OBS地址

        :return: The app_url of this AppDef.
        :rtype: str
        """
        return self._app_url

    @app_url.setter
    def app_url(self, app_url):
        """Sets the app_url of this AppDef.

        app应用的地址，可以是镜像地址或者OBS地址

        :param app_url: The app_url of this AppDef.
        :type app_url: str
        """
        self._app_url = app_url

    @property
    def channel_limit(self):
        """Gets the channel_limit of this AppDef.

        路数限制，添加作业的时候，摄像头和VCN的最大路数不超过该值，范围是0到1000

        :return: The channel_limit of this AppDef.
        :rtype: int
        """
        return self._channel_limit

    @channel_limit.setter
    def channel_limit(self, channel_limit):
        """Sets the channel_limit of this AppDef.

        路数限制，添加作业的时候，摄像头和VCN的最大路数不超过该值，范围是0到1000

        :param channel_limit: The channel_limit of this AppDef.
        :type channel_limit: int
        """
        self._channel_limit = channel_limit

    @property
    def channel_upper_limit(self):
        """Gets the channel_upper_limit of this AppDef.

        用户可以指定的路数限制上限，范围是0到1000

        :return: The channel_upper_limit of this AppDef.
        :rtype: int
        """
        return self._channel_upper_limit

    @channel_upper_limit.setter
    def channel_upper_limit(self, channel_upper_limit):
        """Sets the channel_upper_limit of this AppDef.

        用户可以指定的路数限制上限，范围是0到1000

        :param channel_upper_limit: The channel_upper_limit of this AppDef.
        :type channel_upper_limit: int
        """
        self._channel_upper_limit = channel_upper_limit

    @property
    def args(self):
        """Gets the args of this AppDef.

        容器启动参数，字符总长度最大为65536，不允许^#~^$|%&*<>()'\"\\[\\]{}]等特殊字符

        :return: The args of this AppDef.
        :rtype: list[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this AppDef.

        容器启动参数，字符总长度最大为65536，不允许^#~^$|%&*<>()'\"\\[\\]{}]等特殊字符

        :param args: The args of this AppDef.
        :type args: list[str]
        """
        self._args = args

    @property
    def command(self):
        """Gets the command of this AppDef.

        容器启动命令，字符总长度最大为65536。 command支持使用数组定义多条命令，但在IEF控制台界面只会显示第一条命令。不允许^#~^$|%&*<>()'\"\\[\\]{}]等特殊字符

        :return: The command of this AppDef.
        :rtype: list[str]
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this AppDef.

        容器启动命令，字符总长度最大为65536。 command支持使用数组定义多条命令，但在IEF控制台界面只会显示第一条命令。不允许^#~^$|%&*<>()'\"\\[\\]{}]等特殊字符

        :param command: The command of this AppDef.
        :type command: list[str]
        """
        self._command = command

    @property
    def envs(self):
        """Gets the envs of this AppDef.

        环境变量

        :return: The envs of this AppDef.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.Env`]
        """
        return self._envs

    @envs.setter
    def envs(self, envs):
        """Sets the envs of this AppDef.

        环境变量

        :param envs: The envs of this AppDef.
        :type envs: list[:class:`huaweicloudsdkhilens.v3.Env`]
        """
        self._envs = envs

    @property
    def is_modelbox(self):
        """Gets the is_modelbox of this AppDef.

        是否是modelbox镜像

        :return: The is_modelbox of this AppDef.
        :rtype: bool
        """
        return self._is_modelbox

    @is_modelbox.setter
    def is_modelbox(self, is_modelbox):
        """Sets the is_modelbox of this AppDef.

        是否是modelbox镜像

        :param is_modelbox: The is_modelbox of this AppDef.
        :type is_modelbox: bool
        """
        self._is_modelbox = is_modelbox

    @property
    def liveness_probe(self):
        """Gets the liveness_probe of this AppDef.

        :return: The liveness_probe of this AppDef.
        :rtype: :class:`huaweicloudsdkhilens.v3.Probe`
        """
        return self._liveness_probe

    @liveness_probe.setter
    def liveness_probe(self, liveness_probe):
        """Sets the liveness_probe of this AppDef.

        :param liveness_probe: The liveness_probe of this AppDef.
        :type liveness_probe: :class:`huaweicloudsdkhilens.v3.Probe`
        """
        self._liveness_probe = liveness_probe

    @property
    def msgs(self):
        """Gets the msgs of this AppDef.

        消息变量

        :return: The msgs of this AppDef.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.Env`]
        """
        return self._msgs

    @msgs.setter
    def msgs(self, msgs):
        """Sets the msgs of this AppDef.

        消息变量

        :param msgs: The msgs of this AppDef.
        :type msgs: list[:class:`huaweicloudsdkhilens.v3.Env`]
        """
        self._msgs = msgs

    @property
    def name(self):
        """Gets the name of this AppDef.

        应用名字，只允许英文小写字母、数字、中划线，最大长度32, 英文小写字母或数字开头和结尾。该名称同时对应技能名称，当不传订单id的时候，默认通过该名称和版本号version字段，选择指定技能版本，进行部署，并选择可用的订单（默认订单优先）扣除份额。

        :return: The name of this AppDef.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AppDef.

        应用名字，只允许英文小写字母、数字、中划线，最大长度32, 英文小写字母或数字开头和结尾。该名称同时对应技能名称，当不传订单id的时候，默认通过该名称和版本号version字段，选择指定技能版本，进行部署，并选择可用的订单（默认订单优先）扣除份额。

        :param name: The name of this AppDef.
        :type name: str
        """
        self._name = name

    @property
    def npu_type(self):
        """Gets the npu_type of this AppDef.

        npu类型，支持D310类型和D910类型。D310表示D310类型。  D910表示D910类型。不填表示为D310类型

        :return: The npu_type of this AppDef.
        :rtype: str
        """
        return self._npu_type

    @npu_type.setter
    def npu_type(self, npu_type):
        """Sets the npu_type of this AppDef.

        npu类型，支持D310类型和D910类型。D310表示D310类型。  D910表示D910类型。不填表示为D310类型

        :param npu_type: The npu_type of this AppDef.
        :type npu_type: str
        """
        self._npu_type = npu_type

    @property
    def ports(self):
        """Gets the ports of this AppDef.

        容器端口映射值

        :return: The ports of this AppDef.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.HostContainerPortMapping`]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this AppDef.

        容器端口映射值

        :param ports: The ports of this AppDef.
        :type ports: list[:class:`huaweicloudsdkhilens.v3.HostContainerPortMapping`]
        """
        self._ports = ports

    @property
    def privileged(self):
        """Gets the privileged of this AppDef.

        是否启用特权容器,默认值false

        :return: The privileged of this AppDef.
        :rtype: bool
        """
        return self._privileged

    @privileged.setter
    def privileged(self, privileged):
        """Sets the privileged of this AppDef.

        是否启用特权容器,默认值false

        :param privileged: The privileged of this AppDef.
        :type privileged: bool
        """
        self._privileged = privileged

    @property
    def readiness_probe(self):
        """Gets the readiness_probe of this AppDef.

        :return: The readiness_probe of this AppDef.
        :rtype: :class:`huaweicloudsdkhilens.v3.Probe`
        """
        return self._readiness_probe

    @readiness_probe.setter
    def readiness_probe(self, readiness_probe):
        """Sets the readiness_probe of this AppDef.

        :param readiness_probe: The readiness_probe of this AppDef.
        :type readiness_probe: :class:`huaweicloudsdkhilens.v3.Probe`
        """
        self._readiness_probe = readiness_probe

    @property
    def resources(self):
        """Gets the resources of this AppDef.

        :return: The resources of this AppDef.
        :rtype: :class:`huaweicloudsdkhilens.v3.ResQuest`
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this AppDef.

        :param resources: The resources of this AppDef.
        :type resources: :class:`huaweicloudsdkhilens.v3.ResQuest`
        """
        self._resources = resources

    @property
    def version(self):
        """Gets the version of this AppDef.

        版本号，长度不操作128，支持大小写数字，下划线，点，中划线

        :return: The version of this AppDef.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AppDef.

        版本号，长度不操作128，支持大小写数字，下划线，点，中划线

        :param version: The version of this AppDef.
        :type version: str
        """
        self._version = version

    @property
    def volumes(self):
        """Gets the volumes of this AppDef.

        卷配置

        :return: The volumes of this AppDef.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.Volume`]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this AppDef.

        卷配置

        :param volumes: The volumes of this AppDef.
        :type volumes: list[:class:`huaweicloudsdkhilens.v3.Volume`]
        """
        self._volumes = volumes

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
        if not isinstance(other, AppDef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
