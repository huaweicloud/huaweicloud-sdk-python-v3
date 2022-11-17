# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScaleScript:

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
        'action_stage': 'str'
    }

    attribute_map = {
        'name': 'name',
        'uri': 'uri',
        'parameters': 'parameters',
        'nodes': 'nodes',
        'active_master': 'active_master',
        'fail_action': 'fail_action',
        'action_stage': 'action_stage'
    }

    def __init__(self, name=None, uri=None, parameters=None, nodes=None, active_master=None, fail_action=None, action_stage=None):
        """ScaleScript

        The model defined in huaweicloud sdk

        :param name: 弹性伸缩自定义自动化脚本的名称，同一个集群的自定义自动化脚本名称不允许相同。  只能由数字、英文字符、空格、中划线和下划线组成，且不能以空格开头。  可输入的字符串长度为1～64个字符。
        :type name: str
        :param uri: 自定义自动化脚本的路径。设置为OBS桶的路径或虚拟机本地的路径。  - OBS桶的路径：直接手动输入脚本路径。示例：s3a://XXX/scale.sh  - 虚拟机本地的路径：用户需要输入正确的脚本路径。脚本所在的路径必须以‘/’开头，以.sh结尾。
        :type uri: str
        :param parameters: 自定义自动化脚本参数。  多个参数间用空格隔开。 可以传入以下系统预定义参数： - ${mrs_scale_node_num}：扩缩容节点数 - ${mrs_scale_type}：扩缩容类型，扩容为scale_out，缩容为scale_in - ${mrs_scale_node_hostnames}：扩缩容的节点主机名称 - ${mrs_scale_node_ips}：扩缩容的节点IP - ${mrs_scale_rule_name}：触发扩缩容的规则名   其他用户自定义参数使用方式与普通shell脚本相同，多个参数中间用空格隔开。
        :type parameters: str
        :param nodes: 自定义自动化脚本所执行的节点组名称（非自定义集群也可使用节点类型，包含Master、Core和Task三种类型）。
        :type nodes: list[str]
        :param active_master: 自定义自动化脚本是否只运行在主Master节点上。  缺省值为false，表示自定义自动化脚本可运行在所有Master节点上。
        :type active_master: bool
        :param fail_action: 自自定义自动化脚本执行失败后，是否继续执行后续脚本和创建集群。  说明：  - 建议您在调试阶段设置为“continue”，无论此自定义自动化脚本是否执行成功，则集群都能继续安装和启动。  - 由于缩容成功无法回滚，因此缩容后执行的脚本“fail_action”必须设置为“continue”。  枚举值： - continue：继续执行后续脚本。 - errorout：终止操作。
        :type fail_action: str
        :param action_stage: 脚本执行时机。  枚举值： - before_scale_out：扩容前 - before_scale_in：缩容前 - after_scale_out：扩容后 - after_scale_in：缩容后
        :type action_stage: str
        """
        
        

        self._name = None
        self._uri = None
        self._parameters = None
        self._nodes = None
        self._active_master = None
        self._fail_action = None
        self._action_stage = None
        self.discriminator = None

        self.name = name
        self.uri = uri
        if parameters is not None:
            self.parameters = parameters
        self.nodes = nodes
        if active_master is not None:
            self.active_master = active_master
        self.fail_action = fail_action
        self.action_stage = action_stage

    @property
    def name(self):
        """Gets the name of this ScaleScript.

        弹性伸缩自定义自动化脚本的名称，同一个集群的自定义自动化脚本名称不允许相同。  只能由数字、英文字符、空格、中划线和下划线组成，且不能以空格开头。  可输入的字符串长度为1～64个字符。

        :return: The name of this ScaleScript.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScaleScript.

        弹性伸缩自定义自动化脚本的名称，同一个集群的自定义自动化脚本名称不允许相同。  只能由数字、英文字符、空格、中划线和下划线组成，且不能以空格开头。  可输入的字符串长度为1～64个字符。

        :param name: The name of this ScaleScript.
        :type name: str
        """
        self._name = name

    @property
    def uri(self):
        """Gets the uri of this ScaleScript.

        自定义自动化脚本的路径。设置为OBS桶的路径或虚拟机本地的路径。  - OBS桶的路径：直接手动输入脚本路径。示例：s3a://XXX/scale.sh  - 虚拟机本地的路径：用户需要输入正确的脚本路径。脚本所在的路径必须以‘/’开头，以.sh结尾。

        :return: The uri of this ScaleScript.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this ScaleScript.

        自定义自动化脚本的路径。设置为OBS桶的路径或虚拟机本地的路径。  - OBS桶的路径：直接手动输入脚本路径。示例：s3a://XXX/scale.sh  - 虚拟机本地的路径：用户需要输入正确的脚本路径。脚本所在的路径必须以‘/’开头，以.sh结尾。

        :param uri: The uri of this ScaleScript.
        :type uri: str
        """
        self._uri = uri

    @property
    def parameters(self):
        """Gets the parameters of this ScaleScript.

        自定义自动化脚本参数。  多个参数间用空格隔开。 可以传入以下系统预定义参数： - ${mrs_scale_node_num}：扩缩容节点数 - ${mrs_scale_type}：扩缩容类型，扩容为scale_out，缩容为scale_in - ${mrs_scale_node_hostnames}：扩缩容的节点主机名称 - ${mrs_scale_node_ips}：扩缩容的节点IP - ${mrs_scale_rule_name}：触发扩缩容的规则名   其他用户自定义参数使用方式与普通shell脚本相同，多个参数中间用空格隔开。

        :return: The parameters of this ScaleScript.
        :rtype: str
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this ScaleScript.

        自定义自动化脚本参数。  多个参数间用空格隔开。 可以传入以下系统预定义参数： - ${mrs_scale_node_num}：扩缩容节点数 - ${mrs_scale_type}：扩缩容类型，扩容为scale_out，缩容为scale_in - ${mrs_scale_node_hostnames}：扩缩容的节点主机名称 - ${mrs_scale_node_ips}：扩缩容的节点IP - ${mrs_scale_rule_name}：触发扩缩容的规则名   其他用户自定义参数使用方式与普通shell脚本相同，多个参数中间用空格隔开。

        :param parameters: The parameters of this ScaleScript.
        :type parameters: str
        """
        self._parameters = parameters

    @property
    def nodes(self):
        """Gets the nodes of this ScaleScript.

        自定义自动化脚本所执行的节点组名称（非自定义集群也可使用节点类型，包含Master、Core和Task三种类型）。

        :return: The nodes of this ScaleScript.
        :rtype: list[str]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this ScaleScript.

        自定义自动化脚本所执行的节点组名称（非自定义集群也可使用节点类型，包含Master、Core和Task三种类型）。

        :param nodes: The nodes of this ScaleScript.
        :type nodes: list[str]
        """
        self._nodes = nodes

    @property
    def active_master(self):
        """Gets the active_master of this ScaleScript.

        自定义自动化脚本是否只运行在主Master节点上。  缺省值为false，表示自定义自动化脚本可运行在所有Master节点上。

        :return: The active_master of this ScaleScript.
        :rtype: bool
        """
        return self._active_master

    @active_master.setter
    def active_master(self, active_master):
        """Sets the active_master of this ScaleScript.

        自定义自动化脚本是否只运行在主Master节点上。  缺省值为false，表示自定义自动化脚本可运行在所有Master节点上。

        :param active_master: The active_master of this ScaleScript.
        :type active_master: bool
        """
        self._active_master = active_master

    @property
    def fail_action(self):
        """Gets the fail_action of this ScaleScript.

        自自定义自动化脚本执行失败后，是否继续执行后续脚本和创建集群。  说明：  - 建议您在调试阶段设置为“continue”，无论此自定义自动化脚本是否执行成功，则集群都能继续安装和启动。  - 由于缩容成功无法回滚，因此缩容后执行的脚本“fail_action”必须设置为“continue”。  枚举值： - continue：继续执行后续脚本。 - errorout：终止操作。

        :return: The fail_action of this ScaleScript.
        :rtype: str
        """
        return self._fail_action

    @fail_action.setter
    def fail_action(self, fail_action):
        """Sets the fail_action of this ScaleScript.

        自自定义自动化脚本执行失败后，是否继续执行后续脚本和创建集群。  说明：  - 建议您在调试阶段设置为“continue”，无论此自定义自动化脚本是否执行成功，则集群都能继续安装和启动。  - 由于缩容成功无法回滚，因此缩容后执行的脚本“fail_action”必须设置为“continue”。  枚举值： - continue：继续执行后续脚本。 - errorout：终止操作。

        :param fail_action: The fail_action of this ScaleScript.
        :type fail_action: str
        """
        self._fail_action = fail_action

    @property
    def action_stage(self):
        """Gets the action_stage of this ScaleScript.

        脚本执行时机。  枚举值： - before_scale_out：扩容前 - before_scale_in：缩容前 - after_scale_out：扩容后 - after_scale_in：缩容后

        :return: The action_stage of this ScaleScript.
        :rtype: str
        """
        return self._action_stage

    @action_stage.setter
    def action_stage(self, action_stage):
        """Sets the action_stage of this ScaleScript.

        脚本执行时机。  枚举值： - before_scale_out：扩容前 - before_scale_in：缩容前 - after_scale_out：扩容后 - after_scale_in：缩容后

        :param action_stage: The action_stage of this ScaleScript.
        :type action_stage: str
        """
        self._action_stage = action_stage

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
        if not isinstance(other, ScaleScript):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
