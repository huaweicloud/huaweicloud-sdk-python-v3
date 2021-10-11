# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BootstrapScriptResp:


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
        'uri': 'str',
        'parameters': 'str',
        'nodes': 'list[str]',
        'active_master': 'bool',
        'fail_action': 'str',
        'before_component_start': 'bool',
        'start_time': 'int',
        'state': 'str'
    }

    attribute_map = {
        'name': 'name',
        'uri': 'uri',
        'parameters': 'parameters',
        'nodes': 'nodes',
        'active_master': 'active_master',
        'fail_action': 'fail_action',
        'before_component_start': 'before_component_start',
        'start_time': 'start_time',
        'state': 'state'
    }

    def __init__(self, name=None, uri=None, parameters=None, nodes=None, active_master=None, fail_action=None, before_component_start=None, start_time=None, state=None):
        """BootstrapScriptResp - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._uri = None
        self._parameters = None
        self._nodes = None
        self._active_master = None
        self._fail_action = None
        self._before_component_start = None
        self._start_time = None
        self._state = None
        self.discriminator = None

        self.name = name
        self.uri = uri
        if parameters is not None:
            self.parameters = parameters
        self.nodes = nodes
        if active_master is not None:
            self.active_master = active_master
        self.fail_action = fail_action
        if before_component_start is not None:
            self.before_component_start = before_component_start
        if start_time is not None:
            self.start_time = start_time
        if state is not None:
            self.state = state

    @property
    def name(self):
        """Gets the name of this BootstrapScriptResp.

        引导操作脚本的名称，同一个集群的引导操作脚本名称不允许相同。  只能由数字、英文字符、空格、中划线和下划线组成，且不能以空格开头。  可输入的字符串长度为1～64个字符。

        :return: The name of this BootstrapScriptResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BootstrapScriptResp.

        引导操作脚本的名称，同一个集群的引导操作脚本名称不允许相同。  只能由数字、英文字符、空格、中划线和下划线组成，且不能以空格开头。  可输入的字符串长度为1～64个字符。

        :param name: The name of this BootstrapScriptResp.
        :type: str
        """
        self._name = name

    @property
    def uri(self):
        """Gets the uri of this BootstrapScriptResp.

        引导操作脚本的路径。设置为OBS桶的路径或虚拟机本地的路径。 - OBS桶的路径：直接手动输入脚本路径。例如输入MRS提供的公共样例脚本路径。示例：s3a://bootstrap/presto/presto-install.sh，其中安装dualroles时，presto-install.sh脚本参数为dualroles, 安装worker时，presto-install.sh脚本参数为worker。根据Presto使用习惯，建议您在Active Master节点上安装dualroles，在Core节点上安装worker。 - 虚拟机本地的路径：用户需要输入正确的脚本路径。脚本所在的路径必须以‘/’开头，以.sh结尾。

        :return: The uri of this BootstrapScriptResp.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this BootstrapScriptResp.

        引导操作脚本的路径。设置为OBS桶的路径或虚拟机本地的路径。 - OBS桶的路径：直接手动输入脚本路径。例如输入MRS提供的公共样例脚本路径。示例：s3a://bootstrap/presto/presto-install.sh，其中安装dualroles时，presto-install.sh脚本参数为dualroles, 安装worker时，presto-install.sh脚本参数为worker。根据Presto使用习惯，建议您在Active Master节点上安装dualroles，在Core节点上安装worker。 - 虚拟机本地的路径：用户需要输入正确的脚本路径。脚本所在的路径必须以‘/’开头，以.sh结尾。

        :param uri: The uri of this BootstrapScriptResp.
        :type: str
        """
        self._uri = uri

    @property
    def parameters(self):
        """Gets the parameters of this BootstrapScriptResp.

        引导操作脚本参数。

        :return: The parameters of this BootstrapScriptResp.
        :rtype: str
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this BootstrapScriptResp.

        引导操作脚本参数。

        :param parameters: The parameters of this BootstrapScriptResp.
        :type: str
        """
        self._parameters = parameters

    @property
    def nodes(self):
        """Gets the nodes of this BootstrapScriptResp.

        引导操作脚本所执行的节点类型，包含Master、Core和Task三种类型。

        :return: The nodes of this BootstrapScriptResp.
        :rtype: list[str]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this BootstrapScriptResp.

        引导操作脚本所执行的节点类型，包含Master、Core和Task三种类型。

        :param nodes: The nodes of this BootstrapScriptResp.
        :type: list[str]
        """
        self._nodes = nodes

    @property
    def active_master(self):
        """Gets the active_master of this BootstrapScriptResp.

        引导操作脚本是否只运行在主Master节点上。 缺省值为false，表示引导操作脚本可运行在所有Master节点上。

        :return: The active_master of this BootstrapScriptResp.
        :rtype: bool
        """
        return self._active_master

    @active_master.setter
    def active_master(self, active_master):
        """Sets the active_master of this BootstrapScriptResp.

        引导操作脚本是否只运行在主Master节点上。 缺省值为false，表示引导操作脚本可运行在所有Master节点上。

        :param active_master: The active_master of this BootstrapScriptResp.
        :type: bool
        """
        self._active_master = active_master

    @property
    def fail_action(self):
        """Gets the fail_action of this BootstrapScriptResp.

        引导操作脚本执行失败后，是否继续执行后续脚本和创建集群。  缺省值为errorout,表示终止操作。   说明： 建议您在调试阶段设置为“继续”，无论此引导操作是否执行成功，则集群都能继续安装和启动。  枚举值： - continue：继续执行后续脚本。 - errorout：终止操作。

        :return: The fail_action of this BootstrapScriptResp.
        :rtype: str
        """
        return self._fail_action

    @fail_action.setter
    def fail_action(self, fail_action):
        """Sets the fail_action of this BootstrapScriptResp.

        引导操作脚本执行失败后，是否继续执行后续脚本和创建集群。  缺省值为errorout,表示终止操作。   说明： 建议您在调试阶段设置为“继续”，无论此引导操作是否执行成功，则集群都能继续安装和启动。  枚举值： - continue：继续执行后续脚本。 - errorout：终止操作。

        :param fail_action: The fail_action of this BootstrapScriptResp.
        :type: str
        """
        self._fail_action = fail_action

    @property
    def before_component_start(self):
        """Gets the before_component_start of this BootstrapScriptResp.

        引导操作脚本执行的时间。目前支持“组件启动前”和“组件启动后”两种类型。 缺省值为false，表示引导操作脚本在组件启动后执行。

        :return: The before_component_start of this BootstrapScriptResp.
        :rtype: bool
        """
        return self._before_component_start

    @before_component_start.setter
    def before_component_start(self, before_component_start):
        """Sets the before_component_start of this BootstrapScriptResp.

        引导操作脚本执行的时间。目前支持“组件启动前”和“组件启动后”两种类型。 缺省值为false，表示引导操作脚本在组件启动后执行。

        :param before_component_start: The before_component_start of this BootstrapScriptResp.
        :type: bool
        """
        self._before_component_start = before_component_start

    @property
    def start_time(self):
        """Gets the start_time of this BootstrapScriptResp.

        单个引导操作脚本的执行时间。

        :return: The start_time of this BootstrapScriptResp.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this BootstrapScriptResp.

        单个引导操作脚本的执行时间。

        :param start_time: The start_time of this BootstrapScriptResp.
        :type: int
        """
        self._start_time = start_time

    @property
    def state(self):
        """Gets the state of this BootstrapScriptResp.

        单个引导操作脚本的运行状态。 - PENDING - IN_PROGRESS - SUCCESS - FAILURE

        :return: The state of this BootstrapScriptResp.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this BootstrapScriptResp.

        单个引导操作脚本的运行状态。 - PENDING - IN_PROGRESS - SUCCESS - FAILURE

        :param state: The state of this BootstrapScriptResp.
        :type: str
        """
        self._state = state

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
        if not isinstance(other, BootstrapScriptResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
