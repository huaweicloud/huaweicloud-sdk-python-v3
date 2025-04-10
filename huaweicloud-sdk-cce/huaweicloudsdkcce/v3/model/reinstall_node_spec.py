# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReinstallNodeSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'os': 'str',
        'login': 'Login',
        'name': 'str',
        'server_config': 'ReinstallServerConfig',
        'volume_config': 'ReinstallVolumeConfig',
        'runtime_config': 'ReinstallRuntimeConfig',
        'k8s_options': 'ReinstallK8sOptionsConfig',
        'lifecycle': 'NodeLifecycleConfig',
        'initialized_conditions': 'list[str]',
        'extend_param': 'ReinstallExtendParam',
        'hostname_config': 'HostnameConfig',
        'security_reinforcement_type': 'str'
    }

    attribute_map = {
        'os': 'os',
        'login': 'login',
        'name': 'name',
        'server_config': 'serverConfig',
        'volume_config': 'volumeConfig',
        'runtime_config': 'runtimeConfig',
        'k8s_options': 'k8sOptions',
        'lifecycle': 'lifecycle',
        'initialized_conditions': 'initializedConditions',
        'extend_param': 'extendParam',
        'hostname_config': 'hostnameConfig',
        'security_reinforcement_type': 'securityReinforcementType'
    }

    def __init__(self, os=None, login=None, name=None, server_config=None, volume_config=None, runtime_config=None, k8s_options=None, lifecycle=None, initialized_conditions=None, extend_param=None, hostname_config=None, security_reinforcement_type=None):
        r"""ReinstallNodeSpec

        The model defined in huaweicloud sdk

        :param os: 操作系统。指定自定义镜像场景将以IMS镜像的实际操作系统版本为准。请选择当前集群支持的操作系统版本，例如EulerOS 2.5、CentOS 7.6、EulerOS 2.8。 
        :type os: str
        :param login: 
        :type login: :class:`huaweicloudsdkcce.v3.Login`
        :param name: 节点名称 &gt; 重装时指定将修改节点名称，且服务器名称会同步修改。默认以服务器当前名称作为节点名称。 &gt; 命名规则：以小写字母开头，由小写字母、数字、中划线(-)组成，长度范围1-56位。
        :type name: str
        :param server_config: 
        :type server_config: :class:`huaweicloudsdkcce.v3.ReinstallServerConfig`
        :param volume_config: 
        :type volume_config: :class:`huaweicloudsdkcce.v3.ReinstallVolumeConfig`
        :param runtime_config: 
        :type runtime_config: :class:`huaweicloudsdkcce.v3.ReinstallRuntimeConfig`
        :param k8s_options: 
        :type k8s_options: :class:`huaweicloudsdkcce.v3.ReinstallK8sOptionsConfig`
        :param lifecycle: 
        :type lifecycle: :class:`huaweicloudsdkcce.v3.NodeLifecycleConfig`
        :param initialized_conditions: 自定义初始化标记。  CCE节点在初始化完成之前，会打上初始化未完成污点（node.cloudprovider.kubernetes.io/uninitialized）防止pod调度到节点上。  cce支持自定义初始化标记，在接收到initializedConditions参数后，会将参数值转换成节点标签，随节点下发，例如：cloudprovider.openvessel.io/inject-initialized-conditions&#x3D;CCEInitial_CustomedInitial。  当节点上设置了此标签，会轮询节点的status.Conditions，查看conditions的type是否存在标记名，如CCEInitial、CustomedInitial标记，如果存在所有传入的标记，且状态为True，认为节点初始化完成，则移除初始化污点。  - 必须以字母、数字组成，长度范围1-20位。 - 标记数量不超过2个 
        :type initialized_conditions: list[str]
        :param extend_param: 
        :type extend_param: :class:`huaweicloudsdkcce.v3.ReinstallExtendParam`
        :param hostname_config: 
        :type hostname_config: :class:`huaweicloudsdkcce.v3.HostnameConfig`
        :param security_reinforcement_type: **参数解释**： 指定节点安全加固类型，当前仅支持HCE2.0镜像等保2.0三级安全加固。 等保加固会对身份鉴别、访问控制、安全审计、入侵防范、恶意代码防范进行检查并加固。详情请参见[Huawei Cloud EulerOS 2.0等保2.0三级版镜像概述](https://support.huaweicloud.com/productdesc-hce/hce_sec_0001.html)。 若未指定此参数，则尝试用原有的值补全。如：原先HCE2.0镜像已配置安全加固，更新节点池时未指定此参数，则仍旧保持安全加固配置，若要取消，需显式指定参数值为\&quot;null\&quot;。 **约束限制**： 不涉及 **取值范围**： 取值范围：[&#39;null&#39;, cybersecurity]; **默认取值**： 不涉及
        :type security_reinforcement_type: str
        """
        
        

        self._os = None
        self._login = None
        self._name = None
        self._server_config = None
        self._volume_config = None
        self._runtime_config = None
        self._k8s_options = None
        self._lifecycle = None
        self._initialized_conditions = None
        self._extend_param = None
        self._hostname_config = None
        self._security_reinforcement_type = None
        self.discriminator = None

        self.os = os
        self.login = login
        if name is not None:
            self.name = name
        if server_config is not None:
            self.server_config = server_config
        if volume_config is not None:
            self.volume_config = volume_config
        if runtime_config is not None:
            self.runtime_config = runtime_config
        if k8s_options is not None:
            self.k8s_options = k8s_options
        if lifecycle is not None:
            self.lifecycle = lifecycle
        if initialized_conditions is not None:
            self.initialized_conditions = initialized_conditions
        if extend_param is not None:
            self.extend_param = extend_param
        if hostname_config is not None:
            self.hostname_config = hostname_config
        if security_reinforcement_type is not None:
            self.security_reinforcement_type = security_reinforcement_type

    @property
    def os(self):
        r"""Gets the os of this ReinstallNodeSpec.

        操作系统。指定自定义镜像场景将以IMS镜像的实际操作系统版本为准。请选择当前集群支持的操作系统版本，例如EulerOS 2.5、CentOS 7.6、EulerOS 2.8。 

        :return: The os of this ReinstallNodeSpec.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        r"""Sets the os of this ReinstallNodeSpec.

        操作系统。指定自定义镜像场景将以IMS镜像的实际操作系统版本为准。请选择当前集群支持的操作系统版本，例如EulerOS 2.5、CentOS 7.6、EulerOS 2.8。 

        :param os: The os of this ReinstallNodeSpec.
        :type os: str
        """
        self._os = os

    @property
    def login(self):
        r"""Gets the login of this ReinstallNodeSpec.

        :return: The login of this ReinstallNodeSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.Login`
        """
        return self._login

    @login.setter
    def login(self, login):
        r"""Sets the login of this ReinstallNodeSpec.

        :param login: The login of this ReinstallNodeSpec.
        :type login: :class:`huaweicloudsdkcce.v3.Login`
        """
        self._login = login

    @property
    def name(self):
        r"""Gets the name of this ReinstallNodeSpec.

        节点名称 > 重装时指定将修改节点名称，且服务器名称会同步修改。默认以服务器当前名称作为节点名称。 > 命名规则：以小写字母开头，由小写字母、数字、中划线(-)组成，长度范围1-56位。

        :return: The name of this ReinstallNodeSpec.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ReinstallNodeSpec.

        节点名称 > 重装时指定将修改节点名称，且服务器名称会同步修改。默认以服务器当前名称作为节点名称。 > 命名规则：以小写字母开头，由小写字母、数字、中划线(-)组成，长度范围1-56位。

        :param name: The name of this ReinstallNodeSpec.
        :type name: str
        """
        self._name = name

    @property
    def server_config(self):
        r"""Gets the server_config of this ReinstallNodeSpec.

        :return: The server_config of this ReinstallNodeSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.ReinstallServerConfig`
        """
        return self._server_config

    @server_config.setter
    def server_config(self, server_config):
        r"""Sets the server_config of this ReinstallNodeSpec.

        :param server_config: The server_config of this ReinstallNodeSpec.
        :type server_config: :class:`huaweicloudsdkcce.v3.ReinstallServerConfig`
        """
        self._server_config = server_config

    @property
    def volume_config(self):
        r"""Gets the volume_config of this ReinstallNodeSpec.

        :return: The volume_config of this ReinstallNodeSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.ReinstallVolumeConfig`
        """
        return self._volume_config

    @volume_config.setter
    def volume_config(self, volume_config):
        r"""Sets the volume_config of this ReinstallNodeSpec.

        :param volume_config: The volume_config of this ReinstallNodeSpec.
        :type volume_config: :class:`huaweicloudsdkcce.v3.ReinstallVolumeConfig`
        """
        self._volume_config = volume_config

    @property
    def runtime_config(self):
        r"""Gets the runtime_config of this ReinstallNodeSpec.

        :return: The runtime_config of this ReinstallNodeSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.ReinstallRuntimeConfig`
        """
        return self._runtime_config

    @runtime_config.setter
    def runtime_config(self, runtime_config):
        r"""Sets the runtime_config of this ReinstallNodeSpec.

        :param runtime_config: The runtime_config of this ReinstallNodeSpec.
        :type runtime_config: :class:`huaweicloudsdkcce.v3.ReinstallRuntimeConfig`
        """
        self._runtime_config = runtime_config

    @property
    def k8s_options(self):
        r"""Gets the k8s_options of this ReinstallNodeSpec.

        :return: The k8s_options of this ReinstallNodeSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.ReinstallK8sOptionsConfig`
        """
        return self._k8s_options

    @k8s_options.setter
    def k8s_options(self, k8s_options):
        r"""Sets the k8s_options of this ReinstallNodeSpec.

        :param k8s_options: The k8s_options of this ReinstallNodeSpec.
        :type k8s_options: :class:`huaweicloudsdkcce.v3.ReinstallK8sOptionsConfig`
        """
        self._k8s_options = k8s_options

    @property
    def lifecycle(self):
        r"""Gets the lifecycle of this ReinstallNodeSpec.

        :return: The lifecycle of this ReinstallNodeSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.NodeLifecycleConfig`
        """
        return self._lifecycle

    @lifecycle.setter
    def lifecycle(self, lifecycle):
        r"""Sets the lifecycle of this ReinstallNodeSpec.

        :param lifecycle: The lifecycle of this ReinstallNodeSpec.
        :type lifecycle: :class:`huaweicloudsdkcce.v3.NodeLifecycleConfig`
        """
        self._lifecycle = lifecycle

    @property
    def initialized_conditions(self):
        r"""Gets the initialized_conditions of this ReinstallNodeSpec.

        自定义初始化标记。  CCE节点在初始化完成之前，会打上初始化未完成污点（node.cloudprovider.kubernetes.io/uninitialized）防止pod调度到节点上。  cce支持自定义初始化标记，在接收到initializedConditions参数后，会将参数值转换成节点标签，随节点下发，例如：cloudprovider.openvessel.io/inject-initialized-conditions=CCEInitial_CustomedInitial。  当节点上设置了此标签，会轮询节点的status.Conditions，查看conditions的type是否存在标记名，如CCEInitial、CustomedInitial标记，如果存在所有传入的标记，且状态为True，认为节点初始化完成，则移除初始化污点。  - 必须以字母、数字组成，长度范围1-20位。 - 标记数量不超过2个 

        :return: The initialized_conditions of this ReinstallNodeSpec.
        :rtype: list[str]
        """
        return self._initialized_conditions

    @initialized_conditions.setter
    def initialized_conditions(self, initialized_conditions):
        r"""Sets the initialized_conditions of this ReinstallNodeSpec.

        自定义初始化标记。  CCE节点在初始化完成之前，会打上初始化未完成污点（node.cloudprovider.kubernetes.io/uninitialized）防止pod调度到节点上。  cce支持自定义初始化标记，在接收到initializedConditions参数后，会将参数值转换成节点标签，随节点下发，例如：cloudprovider.openvessel.io/inject-initialized-conditions=CCEInitial_CustomedInitial。  当节点上设置了此标签，会轮询节点的status.Conditions，查看conditions的type是否存在标记名，如CCEInitial、CustomedInitial标记，如果存在所有传入的标记，且状态为True，认为节点初始化完成，则移除初始化污点。  - 必须以字母、数字组成，长度范围1-20位。 - 标记数量不超过2个 

        :param initialized_conditions: The initialized_conditions of this ReinstallNodeSpec.
        :type initialized_conditions: list[str]
        """
        self._initialized_conditions = initialized_conditions

    @property
    def extend_param(self):
        r"""Gets the extend_param of this ReinstallNodeSpec.

        :return: The extend_param of this ReinstallNodeSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.ReinstallExtendParam`
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        r"""Sets the extend_param of this ReinstallNodeSpec.

        :param extend_param: The extend_param of this ReinstallNodeSpec.
        :type extend_param: :class:`huaweicloudsdkcce.v3.ReinstallExtendParam`
        """
        self._extend_param = extend_param

    @property
    def hostname_config(self):
        r"""Gets the hostname_config of this ReinstallNodeSpec.

        :return: The hostname_config of this ReinstallNodeSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.HostnameConfig`
        """
        return self._hostname_config

    @hostname_config.setter
    def hostname_config(self, hostname_config):
        r"""Sets the hostname_config of this ReinstallNodeSpec.

        :param hostname_config: The hostname_config of this ReinstallNodeSpec.
        :type hostname_config: :class:`huaweicloudsdkcce.v3.HostnameConfig`
        """
        self._hostname_config = hostname_config

    @property
    def security_reinforcement_type(self):
        r"""Gets the security_reinforcement_type of this ReinstallNodeSpec.

        **参数解释**： 指定节点安全加固类型，当前仅支持HCE2.0镜像等保2.0三级安全加固。 等保加固会对身份鉴别、访问控制、安全审计、入侵防范、恶意代码防范进行检查并加固。详情请参见[Huawei Cloud EulerOS 2.0等保2.0三级版镜像概述](https://support.huaweicloud.com/productdesc-hce/hce_sec_0001.html)。 若未指定此参数，则尝试用原有的值补全。如：原先HCE2.0镜像已配置安全加固，更新节点池时未指定此参数，则仍旧保持安全加固配置，若要取消，需显式指定参数值为\"null\"。 **约束限制**： 不涉及 **取值范围**： 取值范围：['null', cybersecurity]; **默认取值**： 不涉及

        :return: The security_reinforcement_type of this ReinstallNodeSpec.
        :rtype: str
        """
        return self._security_reinforcement_type

    @security_reinforcement_type.setter
    def security_reinforcement_type(self, security_reinforcement_type):
        r"""Sets the security_reinforcement_type of this ReinstallNodeSpec.

        **参数解释**： 指定节点安全加固类型，当前仅支持HCE2.0镜像等保2.0三级安全加固。 等保加固会对身份鉴别、访问控制、安全审计、入侵防范、恶意代码防范进行检查并加固。详情请参见[Huawei Cloud EulerOS 2.0等保2.0三级版镜像概述](https://support.huaweicloud.com/productdesc-hce/hce_sec_0001.html)。 若未指定此参数，则尝试用原有的值补全。如：原先HCE2.0镜像已配置安全加固，更新节点池时未指定此参数，则仍旧保持安全加固配置，若要取消，需显式指定参数值为\"null\"。 **约束限制**： 不涉及 **取值范围**： 取值范围：['null', cybersecurity]; **默认取值**： 不涉及

        :param security_reinforcement_type: The security_reinforcement_type of this ReinstallNodeSpec.
        :type security_reinforcement_type: str
        """
        self._security_reinforcement_type = security_reinforcement_type

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
        if not isinstance(other, ReinstallNodeSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
