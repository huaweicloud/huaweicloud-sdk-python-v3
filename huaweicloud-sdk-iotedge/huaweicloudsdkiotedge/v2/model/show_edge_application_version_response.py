# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEdgeApplicationVersionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'edge_app_id': 'str',
        'name': 'str',
        'deploy_type': 'str',
        'deploy_multi_instance': 'bool',
        'version': 'str',
        'sdk_version': 'str',
        'description': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'state': 'str',
        'liveness_probe': 'ProbeDTO',
        'readiness_probe': 'ProbeDTO',
        'arch': 'list[str]',
        'command': 'list[str]',
        'args': 'list[str]',
        'container_settings': 'ContainerSettingsDTO',
        'outputs': 'list[str]',
        'inputs': 'list[str]',
        'services': 'list[str]',
        'publish_time': 'str',
        'off_shelf_time': 'str',
        'supplier': 'str',
        'tpl_id': 'str'
    }

    attribute_map = {
        'edge_app_id': 'edge_app_id',
        'name': 'name',
        'deploy_type': 'deploy_type',
        'deploy_multi_instance': 'deploy_multi_instance',
        'version': 'version',
        'sdk_version': 'sdk_version',
        'description': 'description',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'state': 'state',
        'liveness_probe': 'liveness_probe',
        'readiness_probe': 'readiness_probe',
        'arch': 'arch',
        'command': 'command',
        'args': 'args',
        'container_settings': 'container_settings',
        'outputs': 'outputs',
        'inputs': 'inputs',
        'services': 'services',
        'publish_time': 'publish_time',
        'off_shelf_time': 'off_shelf_time',
        'supplier': 'supplier',
        'tpl_id': 'tpl_id'
    }

    def __init__(self, edge_app_id=None, name=None, deploy_type=None, deploy_multi_instance=None, version=None, sdk_version=None, description=None, create_time=None, update_time=None, state=None, liveness_probe=None, readiness_probe=None, arch=None, command=None, args=None, container_settings=None, outputs=None, inputs=None, services=None, publish_time=None, off_shelf_time=None, supplier=None, tpl_id=None):
        """ShowEdgeApplicationVersionResponse

        The model defined in huaweicloud sdk

        :param edge_app_id: 应用ID
        :type edge_app_id: str
        :param name: 应用名称
        :type name: str
        :param deploy_type: 部署类型docker|process
        :type deploy_type: str
        :param deploy_multi_instance: 是否允许部署多实例
        :type deploy_multi_instance: bool
        :param version: 应用版本
        :type version: str
        :param sdk_version: 应用集成的边缘升得快版本
        :type sdk_version: str
        :param description: 应用描述
        :type description: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 最后一次修改时间
        :type update_time: str
        :param state: 应用版本状态
        :type state: str
        :param liveness_probe: 
        :type liveness_probe: :class:`huaweicloudsdkiotedge.v2.ProbeDTO`
        :param readiness_probe: 
        :type readiness_probe: :class:`huaweicloudsdkiotedge.v2.ProbeDTO`
        :param arch: 架构
        :type arch: list[str]
        :param command: 启动命令
        :type command: list[str]
        :param args: 启动参数
        :type args: list[str]
        :param container_settings: 
        :type container_settings: :class:`huaweicloudsdkiotedge.v2.ContainerSettingsDTO`
        :param outputs: 应用输出路由端点
        :type outputs: list[str]
        :param inputs: 应用输入路由
        :type inputs: list[str]
        :param services: 应用实现的服务列表
        :type services: list[str]
        :param publish_time: 发布时间
        :type publish_time: str
        :param off_shelf_time: 下线时间
        :type off_shelf_time: str
        :param supplier: 驱动厂商
        :type supplier: str
        :param tpl_id: 模板id
        :type tpl_id: str
        """
        
        super(ShowEdgeApplicationVersionResponse, self).__init__()

        self._edge_app_id = None
        self._name = None
        self._deploy_type = None
        self._deploy_multi_instance = None
        self._version = None
        self._sdk_version = None
        self._description = None
        self._create_time = None
        self._update_time = None
        self._state = None
        self._liveness_probe = None
        self._readiness_probe = None
        self._arch = None
        self._command = None
        self._args = None
        self._container_settings = None
        self._outputs = None
        self._inputs = None
        self._services = None
        self._publish_time = None
        self._off_shelf_time = None
        self._supplier = None
        self._tpl_id = None
        self.discriminator = None

        if edge_app_id is not None:
            self.edge_app_id = edge_app_id
        if name is not None:
            self.name = name
        if deploy_type is not None:
            self.deploy_type = deploy_type
        if deploy_multi_instance is not None:
            self.deploy_multi_instance = deploy_multi_instance
        if version is not None:
            self.version = version
        if sdk_version is not None:
            self.sdk_version = sdk_version
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if state is not None:
            self.state = state
        if liveness_probe is not None:
            self.liveness_probe = liveness_probe
        if readiness_probe is not None:
            self.readiness_probe = readiness_probe
        if arch is not None:
            self.arch = arch
        if command is not None:
            self.command = command
        if args is not None:
            self.args = args
        if container_settings is not None:
            self.container_settings = container_settings
        if outputs is not None:
            self.outputs = outputs
        if inputs is not None:
            self.inputs = inputs
        if services is not None:
            self.services = services
        if publish_time is not None:
            self.publish_time = publish_time
        if off_shelf_time is not None:
            self.off_shelf_time = off_shelf_time
        if supplier is not None:
            self.supplier = supplier
        if tpl_id is not None:
            self.tpl_id = tpl_id

    @property
    def edge_app_id(self):
        """Gets the edge_app_id of this ShowEdgeApplicationVersionResponse.

        应用ID

        :return: The edge_app_id of this ShowEdgeApplicationVersionResponse.
        :rtype: str
        """
        return self._edge_app_id

    @edge_app_id.setter
    def edge_app_id(self, edge_app_id):
        """Sets the edge_app_id of this ShowEdgeApplicationVersionResponse.

        应用ID

        :param edge_app_id: The edge_app_id of this ShowEdgeApplicationVersionResponse.
        :type edge_app_id: str
        """
        self._edge_app_id = edge_app_id

    @property
    def name(self):
        """Gets the name of this ShowEdgeApplicationVersionResponse.

        应用名称

        :return: The name of this ShowEdgeApplicationVersionResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowEdgeApplicationVersionResponse.

        应用名称

        :param name: The name of this ShowEdgeApplicationVersionResponse.
        :type name: str
        """
        self._name = name

    @property
    def deploy_type(self):
        """Gets the deploy_type of this ShowEdgeApplicationVersionResponse.

        部署类型docker|process

        :return: The deploy_type of this ShowEdgeApplicationVersionResponse.
        :rtype: str
        """
        return self._deploy_type

    @deploy_type.setter
    def deploy_type(self, deploy_type):
        """Sets the deploy_type of this ShowEdgeApplicationVersionResponse.

        部署类型docker|process

        :param deploy_type: The deploy_type of this ShowEdgeApplicationVersionResponse.
        :type deploy_type: str
        """
        self._deploy_type = deploy_type

    @property
    def deploy_multi_instance(self):
        """Gets the deploy_multi_instance of this ShowEdgeApplicationVersionResponse.

        是否允许部署多实例

        :return: The deploy_multi_instance of this ShowEdgeApplicationVersionResponse.
        :rtype: bool
        """
        return self._deploy_multi_instance

    @deploy_multi_instance.setter
    def deploy_multi_instance(self, deploy_multi_instance):
        """Sets the deploy_multi_instance of this ShowEdgeApplicationVersionResponse.

        是否允许部署多实例

        :param deploy_multi_instance: The deploy_multi_instance of this ShowEdgeApplicationVersionResponse.
        :type deploy_multi_instance: bool
        """
        self._deploy_multi_instance = deploy_multi_instance

    @property
    def version(self):
        """Gets the version of this ShowEdgeApplicationVersionResponse.

        应用版本

        :return: The version of this ShowEdgeApplicationVersionResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShowEdgeApplicationVersionResponse.

        应用版本

        :param version: The version of this ShowEdgeApplicationVersionResponse.
        :type version: str
        """
        self._version = version

    @property
    def sdk_version(self):
        """Gets the sdk_version of this ShowEdgeApplicationVersionResponse.

        应用集成的边缘升得快版本

        :return: The sdk_version of this ShowEdgeApplicationVersionResponse.
        :rtype: str
        """
        return self._sdk_version

    @sdk_version.setter
    def sdk_version(self, sdk_version):
        """Sets the sdk_version of this ShowEdgeApplicationVersionResponse.

        应用集成的边缘升得快版本

        :param sdk_version: The sdk_version of this ShowEdgeApplicationVersionResponse.
        :type sdk_version: str
        """
        self._sdk_version = sdk_version

    @property
    def description(self):
        """Gets the description of this ShowEdgeApplicationVersionResponse.

        应用描述

        :return: The description of this ShowEdgeApplicationVersionResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowEdgeApplicationVersionResponse.

        应用描述

        :param description: The description of this ShowEdgeApplicationVersionResponse.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        """Gets the create_time of this ShowEdgeApplicationVersionResponse.

        创建时间

        :return: The create_time of this ShowEdgeApplicationVersionResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowEdgeApplicationVersionResponse.

        创建时间

        :param create_time: The create_time of this ShowEdgeApplicationVersionResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ShowEdgeApplicationVersionResponse.

        最后一次修改时间

        :return: The update_time of this ShowEdgeApplicationVersionResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowEdgeApplicationVersionResponse.

        最后一次修改时间

        :param update_time: The update_time of this ShowEdgeApplicationVersionResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def state(self):
        """Gets the state of this ShowEdgeApplicationVersionResponse.

        应用版本状态

        :return: The state of this ShowEdgeApplicationVersionResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ShowEdgeApplicationVersionResponse.

        应用版本状态

        :param state: The state of this ShowEdgeApplicationVersionResponse.
        :type state: str
        """
        self._state = state

    @property
    def liveness_probe(self):
        """Gets the liveness_probe of this ShowEdgeApplicationVersionResponse.

        :return: The liveness_probe of this ShowEdgeApplicationVersionResponse.
        :rtype: :class:`huaweicloudsdkiotedge.v2.ProbeDTO`
        """
        return self._liveness_probe

    @liveness_probe.setter
    def liveness_probe(self, liveness_probe):
        """Sets the liveness_probe of this ShowEdgeApplicationVersionResponse.

        :param liveness_probe: The liveness_probe of this ShowEdgeApplicationVersionResponse.
        :type liveness_probe: :class:`huaweicloudsdkiotedge.v2.ProbeDTO`
        """
        self._liveness_probe = liveness_probe

    @property
    def readiness_probe(self):
        """Gets the readiness_probe of this ShowEdgeApplicationVersionResponse.

        :return: The readiness_probe of this ShowEdgeApplicationVersionResponse.
        :rtype: :class:`huaweicloudsdkiotedge.v2.ProbeDTO`
        """
        return self._readiness_probe

    @readiness_probe.setter
    def readiness_probe(self, readiness_probe):
        """Sets the readiness_probe of this ShowEdgeApplicationVersionResponse.

        :param readiness_probe: The readiness_probe of this ShowEdgeApplicationVersionResponse.
        :type readiness_probe: :class:`huaweicloudsdkiotedge.v2.ProbeDTO`
        """
        self._readiness_probe = readiness_probe

    @property
    def arch(self):
        """Gets the arch of this ShowEdgeApplicationVersionResponse.

        架构

        :return: The arch of this ShowEdgeApplicationVersionResponse.
        :rtype: list[str]
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this ShowEdgeApplicationVersionResponse.

        架构

        :param arch: The arch of this ShowEdgeApplicationVersionResponse.
        :type arch: list[str]
        """
        self._arch = arch

    @property
    def command(self):
        """Gets the command of this ShowEdgeApplicationVersionResponse.

        启动命令

        :return: The command of this ShowEdgeApplicationVersionResponse.
        :rtype: list[str]
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this ShowEdgeApplicationVersionResponse.

        启动命令

        :param command: The command of this ShowEdgeApplicationVersionResponse.
        :type command: list[str]
        """
        self._command = command

    @property
    def args(self):
        """Gets the args of this ShowEdgeApplicationVersionResponse.

        启动参数

        :return: The args of this ShowEdgeApplicationVersionResponse.
        :rtype: list[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this ShowEdgeApplicationVersionResponse.

        启动参数

        :param args: The args of this ShowEdgeApplicationVersionResponse.
        :type args: list[str]
        """
        self._args = args

    @property
    def container_settings(self):
        """Gets the container_settings of this ShowEdgeApplicationVersionResponse.

        :return: The container_settings of this ShowEdgeApplicationVersionResponse.
        :rtype: :class:`huaweicloudsdkiotedge.v2.ContainerSettingsDTO`
        """
        return self._container_settings

    @container_settings.setter
    def container_settings(self, container_settings):
        """Sets the container_settings of this ShowEdgeApplicationVersionResponse.

        :param container_settings: The container_settings of this ShowEdgeApplicationVersionResponse.
        :type container_settings: :class:`huaweicloudsdkiotedge.v2.ContainerSettingsDTO`
        """
        self._container_settings = container_settings

    @property
    def outputs(self):
        """Gets the outputs of this ShowEdgeApplicationVersionResponse.

        应用输出路由端点

        :return: The outputs of this ShowEdgeApplicationVersionResponse.
        :rtype: list[str]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this ShowEdgeApplicationVersionResponse.

        应用输出路由端点

        :param outputs: The outputs of this ShowEdgeApplicationVersionResponse.
        :type outputs: list[str]
        """
        self._outputs = outputs

    @property
    def inputs(self):
        """Gets the inputs of this ShowEdgeApplicationVersionResponse.

        应用输入路由

        :return: The inputs of this ShowEdgeApplicationVersionResponse.
        :rtype: list[str]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this ShowEdgeApplicationVersionResponse.

        应用输入路由

        :param inputs: The inputs of this ShowEdgeApplicationVersionResponse.
        :type inputs: list[str]
        """
        self._inputs = inputs

    @property
    def services(self):
        """Gets the services of this ShowEdgeApplicationVersionResponse.

        应用实现的服务列表

        :return: The services of this ShowEdgeApplicationVersionResponse.
        :rtype: list[str]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this ShowEdgeApplicationVersionResponse.

        应用实现的服务列表

        :param services: The services of this ShowEdgeApplicationVersionResponse.
        :type services: list[str]
        """
        self._services = services

    @property
    def publish_time(self):
        """Gets the publish_time of this ShowEdgeApplicationVersionResponse.

        发布时间

        :return: The publish_time of this ShowEdgeApplicationVersionResponse.
        :rtype: str
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        """Sets the publish_time of this ShowEdgeApplicationVersionResponse.

        发布时间

        :param publish_time: The publish_time of this ShowEdgeApplicationVersionResponse.
        :type publish_time: str
        """
        self._publish_time = publish_time

    @property
    def off_shelf_time(self):
        """Gets the off_shelf_time of this ShowEdgeApplicationVersionResponse.

        下线时间

        :return: The off_shelf_time of this ShowEdgeApplicationVersionResponse.
        :rtype: str
        """
        return self._off_shelf_time

    @off_shelf_time.setter
    def off_shelf_time(self, off_shelf_time):
        """Sets the off_shelf_time of this ShowEdgeApplicationVersionResponse.

        下线时间

        :param off_shelf_time: The off_shelf_time of this ShowEdgeApplicationVersionResponse.
        :type off_shelf_time: str
        """
        self._off_shelf_time = off_shelf_time

    @property
    def supplier(self):
        """Gets the supplier of this ShowEdgeApplicationVersionResponse.

        驱动厂商

        :return: The supplier of this ShowEdgeApplicationVersionResponse.
        :rtype: str
        """
        return self._supplier

    @supplier.setter
    def supplier(self, supplier):
        """Sets the supplier of this ShowEdgeApplicationVersionResponse.

        驱动厂商

        :param supplier: The supplier of this ShowEdgeApplicationVersionResponse.
        :type supplier: str
        """
        self._supplier = supplier

    @property
    def tpl_id(self):
        """Gets the tpl_id of this ShowEdgeApplicationVersionResponse.

        模板id

        :return: The tpl_id of this ShowEdgeApplicationVersionResponse.
        :rtype: str
        """
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, tpl_id):
        """Sets the tpl_id of this ShowEdgeApplicationVersionResponse.

        模板id

        :param tpl_id: The tpl_id of this ShowEdgeApplicationVersionResponse.
        :type tpl_id: str
        """
        self._tpl_id = tpl_id

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
        if not isinstance(other, ShowEdgeApplicationVersionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
