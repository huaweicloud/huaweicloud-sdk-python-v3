# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BootstrapScript:

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
        'state': 'str',
        'action_stages': 'list[str]'
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
        'state': 'state',
        'action_stages': 'action_stages'
    }

    def __init__(self, name=None, uri=None, parameters=None, nodes=None, active_master=None, fail_action=None, before_component_start=None, start_time=None, state=None, action_stages=None):
        """BootstrapScript

        The model defined in huaweicloud sdk

        :param name: 引导操作脚本的名称，同一个集群的引导操作脚本名称不允许相同。  只能由数字、英文字符、空格、中划线和下划线组成，且不能以空格开头。  可输入的字符串长度为1～64个字符。
        :type name: str
        :param uri: 引导操作脚本的路径。设置为OBS桶的路径或虚拟机本地的路径。 - OBS桶的路径：直接手动输入脚本路径。例如输入MRS提供的公共样例脚本路径。示例：s3a://bootstrap/presto/presto-install.sh，其中安装dualroles时，presto-install.sh脚本参数为dualroles, 安装worker时，presto-install.sh脚本参数为worker。根据Presto使用习惯，建议您在Active Master节点上安装dualroles，在Core节点上安装worker。 - 虚拟机本地的路径：用户需要输入正确的脚本路径。脚本所在的路径必须以‘/’开头，以.sh结尾。
        :type uri: str
        :param parameters: 引导操作脚本参数。
        :type parameters: str
        :param nodes: 引导操作脚本所执行的节点类型，包含master、core和task三种类型。 说明：节点类型必须为小写字母。
        :type nodes: list[str]
        :param active_master: 引导操作脚本是否只运行在主Master节点上。 缺省值为false，表示引导操作脚本可运行在所有Master节点上。
        :type active_master: bool
        :param fail_action: 引导操作脚本执行失败后，是否继续执行后续脚本和创建集群。  缺省值为errorout,表示终止操作。  说明： 建议您在调试阶段设置为“继续”，无论此引导操作是否执行成功，则集群都能继续安装和启动。  枚举值： - continue：继续执行后续脚本。 - errorout：终止操作。
        :type fail_action: str
        :param before_component_start: 引导操作脚本执行的时间。目前支持“组件启动前”和“组件启动后”两种类型。 缺省值为false，表示引导操作脚本在组件启动后执行。
        :type before_component_start: bool
        :param start_time: 单个引导操作脚本的执行时间。
        :type start_time: int
        :param state: 单个引导操作脚本的运行状态。  - PENDING - IN_PROGRESS - SUCCESS - FAILURE
        :type state: str
        :param action_stages: 选择引导操作脚本执行的时间。 - BEFORE_COMPONENT_FIRST_START: 组件首次启动后 - AFTER_COMPONENT_FIRST_START: 组件首次启动前 - BEFORE_SCALE_IN: 缩容前 - AFTER_SCALE_IN: 缩容后 - BEFORE_SCALE_OUT: 扩容前 - AFTER_SCALE_OUT: 扩容后
        :type action_stages: list[str]
        """
        
        

        self._name = None
        self._uri = None
        self._parameters = None
        self._nodes = None
        self._active_master = None
        self._fail_action = None
        self._before_component_start = None
        self._start_time = None
        self._state = None
        self._action_stages = None
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
        if action_stages is not None:
            self.action_stages = action_stages

    @property
    def name(self):
        """Gets the name of this BootstrapScript.

        引导操作脚本的名称，同一个集群的引导操作脚本名称不允许相同。  只能由数字、英文字符、空格、中划线和下划线组成，且不能以空格开头。  可输入的字符串长度为1～64个字符。

        :return: The name of this BootstrapScript.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BootstrapScript.

        引导操作脚本的名称，同一个集群的引导操作脚本名称不允许相同。  只能由数字、英文字符、空格、中划线和下划线组成，且不能以空格开头。  可输入的字符串长度为1～64个字符。

        :param name: The name of this BootstrapScript.
        :type name: str
        """
        self._name = name

    @property
    def uri(self):
        """Gets the uri of this BootstrapScript.

        引导操作脚本的路径。设置为OBS桶的路径或虚拟机本地的路径。 - OBS桶的路径：直接手动输入脚本路径。例如输入MRS提供的公共样例脚本路径。示例：s3a://bootstrap/presto/presto-install.sh，其中安装dualroles时，presto-install.sh脚本参数为dualroles, 安装worker时，presto-install.sh脚本参数为worker。根据Presto使用习惯，建议您在Active Master节点上安装dualroles，在Core节点上安装worker。 - 虚拟机本地的路径：用户需要输入正确的脚本路径。脚本所在的路径必须以‘/’开头，以.sh结尾。

        :return: The uri of this BootstrapScript.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this BootstrapScript.

        引导操作脚本的路径。设置为OBS桶的路径或虚拟机本地的路径。 - OBS桶的路径：直接手动输入脚本路径。例如输入MRS提供的公共样例脚本路径。示例：s3a://bootstrap/presto/presto-install.sh，其中安装dualroles时，presto-install.sh脚本参数为dualroles, 安装worker时，presto-install.sh脚本参数为worker。根据Presto使用习惯，建议您在Active Master节点上安装dualroles，在Core节点上安装worker。 - 虚拟机本地的路径：用户需要输入正确的脚本路径。脚本所在的路径必须以‘/’开头，以.sh结尾。

        :param uri: The uri of this BootstrapScript.
        :type uri: str
        """
        self._uri = uri

    @property
    def parameters(self):
        """Gets the parameters of this BootstrapScript.

        引导操作脚本参数。

        :return: The parameters of this BootstrapScript.
        :rtype: str
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this BootstrapScript.

        引导操作脚本参数。

        :param parameters: The parameters of this BootstrapScript.
        :type parameters: str
        """
        self._parameters = parameters

    @property
    def nodes(self):
        """Gets the nodes of this BootstrapScript.

        引导操作脚本所执行的节点类型，包含master、core和task三种类型。 说明：节点类型必须为小写字母。

        :return: The nodes of this BootstrapScript.
        :rtype: list[str]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this BootstrapScript.

        引导操作脚本所执行的节点类型，包含master、core和task三种类型。 说明：节点类型必须为小写字母。

        :param nodes: The nodes of this BootstrapScript.
        :type nodes: list[str]
        """
        self._nodes = nodes

    @property
    def active_master(self):
        """Gets the active_master of this BootstrapScript.

        引导操作脚本是否只运行在主Master节点上。 缺省值为false，表示引导操作脚本可运行在所有Master节点上。

        :return: The active_master of this BootstrapScript.
        :rtype: bool
        """
        return self._active_master

    @active_master.setter
    def active_master(self, active_master):
        """Sets the active_master of this BootstrapScript.

        引导操作脚本是否只运行在主Master节点上。 缺省值为false，表示引导操作脚本可运行在所有Master节点上。

        :param active_master: The active_master of this BootstrapScript.
        :type active_master: bool
        """
        self._active_master = active_master

    @property
    def fail_action(self):
        """Gets the fail_action of this BootstrapScript.

        引导操作脚本执行失败后，是否继续执行后续脚本和创建集群。  缺省值为errorout,表示终止操作。  说明： 建议您在调试阶段设置为“继续”，无论此引导操作是否执行成功，则集群都能继续安装和启动。  枚举值： - continue：继续执行后续脚本。 - errorout：终止操作。

        :return: The fail_action of this BootstrapScript.
        :rtype: str
        """
        return self._fail_action

    @fail_action.setter
    def fail_action(self, fail_action):
        """Sets the fail_action of this BootstrapScript.

        引导操作脚本执行失败后，是否继续执行后续脚本和创建集群。  缺省值为errorout,表示终止操作。  说明： 建议您在调试阶段设置为“继续”，无论此引导操作是否执行成功，则集群都能继续安装和启动。  枚举值： - continue：继续执行后续脚本。 - errorout：终止操作。

        :param fail_action: The fail_action of this BootstrapScript.
        :type fail_action: str
        """
        self._fail_action = fail_action

    @property
    def before_component_start(self):
        """Gets the before_component_start of this BootstrapScript.

        引导操作脚本执行的时间。目前支持“组件启动前”和“组件启动后”两种类型。 缺省值为false，表示引导操作脚本在组件启动后执行。

        :return: The before_component_start of this BootstrapScript.
        :rtype: bool
        """
        return self._before_component_start

    @before_component_start.setter
    def before_component_start(self, before_component_start):
        """Sets the before_component_start of this BootstrapScript.

        引导操作脚本执行的时间。目前支持“组件启动前”和“组件启动后”两种类型。 缺省值为false，表示引导操作脚本在组件启动后执行。

        :param before_component_start: The before_component_start of this BootstrapScript.
        :type before_component_start: bool
        """
        self._before_component_start = before_component_start

    @property
    def start_time(self):
        """Gets the start_time of this BootstrapScript.

        单个引导操作脚本的执行时间。

        :return: The start_time of this BootstrapScript.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this BootstrapScript.

        单个引导操作脚本的执行时间。

        :param start_time: The start_time of this BootstrapScript.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def state(self):
        """Gets the state of this BootstrapScript.

        单个引导操作脚本的运行状态。  - PENDING - IN_PROGRESS - SUCCESS - FAILURE

        :return: The state of this BootstrapScript.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this BootstrapScript.

        单个引导操作脚本的运行状态。  - PENDING - IN_PROGRESS - SUCCESS - FAILURE

        :param state: The state of this BootstrapScript.
        :type state: str
        """
        self._state = state

    @property
    def action_stages(self):
        """Gets the action_stages of this BootstrapScript.

        选择引导操作脚本执行的时间。 - BEFORE_COMPONENT_FIRST_START: 组件首次启动后 - AFTER_COMPONENT_FIRST_START: 组件首次启动前 - BEFORE_SCALE_IN: 缩容前 - AFTER_SCALE_IN: 缩容后 - BEFORE_SCALE_OUT: 扩容前 - AFTER_SCALE_OUT: 扩容后

        :return: The action_stages of this BootstrapScript.
        :rtype: list[str]
        """
        return self._action_stages

    @action_stages.setter
    def action_stages(self, action_stages):
        """Sets the action_stages of this BootstrapScript.

        选择引导操作脚本执行的时间。 - BEFORE_COMPONENT_FIRST_START: 组件首次启动后 - AFTER_COMPONENT_FIRST_START: 组件首次启动前 - BEFORE_SCALE_IN: 缩容前 - AFTER_SCALE_IN: 缩容后 - BEFORE_SCALE_OUT: 扩容前 - AFTER_SCALE_OUT: 扩容后

        :param action_stages: The action_stages of this BootstrapScript.
        :type action_stages: list[str]
        """
        self._action_stages = action_stages

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
        if not isinstance(other, BootstrapScript):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
