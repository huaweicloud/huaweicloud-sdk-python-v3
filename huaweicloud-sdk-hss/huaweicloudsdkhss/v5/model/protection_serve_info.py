# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtectionServeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'agent_id': 'str',
        'agent_version': 'str',
        'host_name': 'str',
        'public_ip': 'str',
        'private_ip': 'str',
        'os_type': 'str',
        'rasp_status': 'str',
        'policy_name': 'str',
        'is_friendly_user': 'bool',
        'agent_support_auto_attach': 'bool',
        'agent_status': 'str',
        'auto_attach': 'bool',
        'protect_status': 'str',
        'group_id': 'str',
        'group_name': 'str',
        'protect_event_num': 'int',
        'rasp_port': 'int'
    }

    attribute_map = {
        'host_id': 'host_id',
        'agent_id': 'agent_id',
        'agent_version': 'agent_version',
        'host_name': 'host_name',
        'public_ip': 'public_ip',
        'private_ip': 'private_ip',
        'os_type': 'os_type',
        'rasp_status': 'rasp_status',
        'policy_name': 'policy_name',
        'is_friendly_user': 'is_friendly_user',
        'agent_support_auto_attach': 'agent_support_auto_attach',
        'agent_status': 'agent_status',
        'auto_attach': 'auto_attach',
        'protect_status': 'protect_status',
        'group_id': 'group_id',
        'group_name': 'group_name',
        'protect_event_num': 'protect_event_num',
        'rasp_port': 'rasp_port'
    }

    def __init__(self, host_id=None, agent_id=None, agent_version=None, host_name=None, public_ip=None, private_ip=None, os_type=None, rasp_status=None, policy_name=None, is_friendly_user=None, agent_support_auto_attach=None, agent_status=None, auto_attach=None, protect_status=None, group_id=None, group_name=None, protect_event_num=None, rasp_port=None):
        r"""ProtectionServeInfo

        The model defined in huaweicloud sdk

        :param host_id: 服务器ID
        :type host_id: str
        :param agent_id: Agent ID
        :type agent_id: str
        :param agent_version: Agent版本
        :type agent_version: str
        :param host_name: 服务器名称
        :type host_name: str
        :param public_ip: 弹性ip地址
        :type public_ip: str
        :param private_ip: 私有ip
        :type private_ip: str
        :param os_type: 操作系统类型
        :type os_type: str
        :param rasp_status: 应用防护状态 |- 应用防护状态，包含如下6种。 - 0 ：防护开启中。 - 2 ：防护成功。 - 4 ：防护失败（安装失败）。 - 6 ：未防护。 - 8 ：部分防护。 - 9 ：防护失败。
        :type rasp_status: str
        :param policy_name: 防护策略名称
        :type policy_name: str
        :param is_friendly_user: 是否为友好用户
        :type is_friendly_user: bool
        :param agent_support_auto_attach: agent是否支持动态加载
        :type agent_support_auto_attach: bool
        :param agent_status: Agent状态
        :type agent_status: str
        :param auto_attach: 动态加载是否开启
        :type auto_attach: bool
        :param protect_status: 防护状态 |- agent防护状态，包含如下2种。 - 0 ：关闭。 - 1 ：开启。
        :type protect_status: str
        :param group_id: 服务器组ID
        :type group_id: str
        :param group_name: 服务器组名称
        :type group_name: str
        :param protect_event_num: 防护事件数
        :type protect_event_num: int
        :param rasp_port: RASP端口号
        :type rasp_port: int
        """
        
        

        self._host_id = None
        self._agent_id = None
        self._agent_version = None
        self._host_name = None
        self._public_ip = None
        self._private_ip = None
        self._os_type = None
        self._rasp_status = None
        self._policy_name = None
        self._is_friendly_user = None
        self._agent_support_auto_attach = None
        self._agent_status = None
        self._auto_attach = None
        self._protect_status = None
        self._group_id = None
        self._group_name = None
        self._protect_event_num = None
        self._rasp_port = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if agent_id is not None:
            self.agent_id = agent_id
        if agent_version is not None:
            self.agent_version = agent_version
        if host_name is not None:
            self.host_name = host_name
        if public_ip is not None:
            self.public_ip = public_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if os_type is not None:
            self.os_type = os_type
        if rasp_status is not None:
            self.rasp_status = rasp_status
        if policy_name is not None:
            self.policy_name = policy_name
        if is_friendly_user is not None:
            self.is_friendly_user = is_friendly_user
        if agent_support_auto_attach is not None:
            self.agent_support_auto_attach = agent_support_auto_attach
        if agent_status is not None:
            self.agent_status = agent_status
        if auto_attach is not None:
            self.auto_attach = auto_attach
        if protect_status is not None:
            self.protect_status = protect_status
        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if protect_event_num is not None:
            self.protect_event_num = protect_event_num
        if rasp_port is not None:
            self.rasp_port = rasp_port

    @property
    def host_id(self):
        r"""Gets the host_id of this ProtectionServeInfo.

        服务器ID

        :return: The host_id of this ProtectionServeInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ProtectionServeInfo.

        服务器ID

        :param host_id: The host_id of this ProtectionServeInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def agent_id(self):
        r"""Gets the agent_id of this ProtectionServeInfo.

        Agent ID

        :return: The agent_id of this ProtectionServeInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this ProtectionServeInfo.

        Agent ID

        :param agent_id: The agent_id of this ProtectionServeInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def agent_version(self):
        r"""Gets the agent_version of this ProtectionServeInfo.

        Agent版本

        :return: The agent_version of this ProtectionServeInfo.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        r"""Sets the agent_version of this ProtectionServeInfo.

        Agent版本

        :param agent_version: The agent_version of this ProtectionServeInfo.
        :type agent_version: str
        """
        self._agent_version = agent_version

    @property
    def host_name(self):
        r"""Gets the host_name of this ProtectionServeInfo.

        服务器名称

        :return: The host_name of this ProtectionServeInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ProtectionServeInfo.

        服务器名称

        :param host_name: The host_name of this ProtectionServeInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ProtectionServeInfo.

        弹性ip地址

        :return: The public_ip of this ProtectionServeInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ProtectionServeInfo.

        弹性ip地址

        :param public_ip: The public_ip of this ProtectionServeInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ProtectionServeInfo.

        私有ip

        :return: The private_ip of this ProtectionServeInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ProtectionServeInfo.

        私有ip

        :param private_ip: The private_ip of this ProtectionServeInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def os_type(self):
        r"""Gets the os_type of this ProtectionServeInfo.

        操作系统类型

        :return: The os_type of this ProtectionServeInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ProtectionServeInfo.

        操作系统类型

        :param os_type: The os_type of this ProtectionServeInfo.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def rasp_status(self):
        r"""Gets the rasp_status of this ProtectionServeInfo.

        应用防护状态 |- 应用防护状态，包含如下6种。 - 0 ：防护开启中。 - 2 ：防护成功。 - 4 ：防护失败（安装失败）。 - 6 ：未防护。 - 8 ：部分防护。 - 9 ：防护失败。

        :return: The rasp_status of this ProtectionServeInfo.
        :rtype: str
        """
        return self._rasp_status

    @rasp_status.setter
    def rasp_status(self, rasp_status):
        r"""Sets the rasp_status of this ProtectionServeInfo.

        应用防护状态 |- 应用防护状态，包含如下6种。 - 0 ：防护开启中。 - 2 ：防护成功。 - 4 ：防护失败（安装失败）。 - 6 ：未防护。 - 8 ：部分防护。 - 9 ：防护失败。

        :param rasp_status: The rasp_status of this ProtectionServeInfo.
        :type rasp_status: str
        """
        self._rasp_status = rasp_status

    @property
    def policy_name(self):
        r"""Gets the policy_name of this ProtectionServeInfo.

        防护策略名称

        :return: The policy_name of this ProtectionServeInfo.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this ProtectionServeInfo.

        防护策略名称

        :param policy_name: The policy_name of this ProtectionServeInfo.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def is_friendly_user(self):
        r"""Gets the is_friendly_user of this ProtectionServeInfo.

        是否为友好用户

        :return: The is_friendly_user of this ProtectionServeInfo.
        :rtype: bool
        """
        return self._is_friendly_user

    @is_friendly_user.setter
    def is_friendly_user(self, is_friendly_user):
        r"""Sets the is_friendly_user of this ProtectionServeInfo.

        是否为友好用户

        :param is_friendly_user: The is_friendly_user of this ProtectionServeInfo.
        :type is_friendly_user: bool
        """
        self._is_friendly_user = is_friendly_user

    @property
    def agent_support_auto_attach(self):
        r"""Gets the agent_support_auto_attach of this ProtectionServeInfo.

        agent是否支持动态加载

        :return: The agent_support_auto_attach of this ProtectionServeInfo.
        :rtype: bool
        """
        return self._agent_support_auto_attach

    @agent_support_auto_attach.setter
    def agent_support_auto_attach(self, agent_support_auto_attach):
        r"""Sets the agent_support_auto_attach of this ProtectionServeInfo.

        agent是否支持动态加载

        :param agent_support_auto_attach: The agent_support_auto_attach of this ProtectionServeInfo.
        :type agent_support_auto_attach: bool
        """
        self._agent_support_auto_attach = agent_support_auto_attach

    @property
    def agent_status(self):
        r"""Gets the agent_status of this ProtectionServeInfo.

        Agent状态

        :return: The agent_status of this ProtectionServeInfo.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        r"""Sets the agent_status of this ProtectionServeInfo.

        Agent状态

        :param agent_status: The agent_status of this ProtectionServeInfo.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def auto_attach(self):
        r"""Gets the auto_attach of this ProtectionServeInfo.

        动态加载是否开启

        :return: The auto_attach of this ProtectionServeInfo.
        :rtype: bool
        """
        return self._auto_attach

    @auto_attach.setter
    def auto_attach(self, auto_attach):
        r"""Sets the auto_attach of this ProtectionServeInfo.

        动态加载是否开启

        :param auto_attach: The auto_attach of this ProtectionServeInfo.
        :type auto_attach: bool
        """
        self._auto_attach = auto_attach

    @property
    def protect_status(self):
        r"""Gets the protect_status of this ProtectionServeInfo.

        防护状态 |- agent防护状态，包含如下2种。 - 0 ：关闭。 - 1 ：开启。

        :return: The protect_status of this ProtectionServeInfo.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this ProtectionServeInfo.

        防护状态 |- agent防护状态，包含如下2种。 - 0 ：关闭。 - 1 ：开启。

        :param protect_status: The protect_status of this ProtectionServeInfo.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def group_id(self):
        r"""Gets the group_id of this ProtectionServeInfo.

        服务器组ID

        :return: The group_id of this ProtectionServeInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ProtectionServeInfo.

        服务器组ID

        :param group_id: The group_id of this ProtectionServeInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this ProtectionServeInfo.

        服务器组名称

        :return: The group_name of this ProtectionServeInfo.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ProtectionServeInfo.

        服务器组名称

        :param group_name: The group_name of this ProtectionServeInfo.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def protect_event_num(self):
        r"""Gets the protect_event_num of this ProtectionServeInfo.

        防护事件数

        :return: The protect_event_num of this ProtectionServeInfo.
        :rtype: int
        """
        return self._protect_event_num

    @protect_event_num.setter
    def protect_event_num(self, protect_event_num):
        r"""Sets the protect_event_num of this ProtectionServeInfo.

        防护事件数

        :param protect_event_num: The protect_event_num of this ProtectionServeInfo.
        :type protect_event_num: int
        """
        self._protect_event_num = protect_event_num

    @property
    def rasp_port(self):
        r"""Gets the rasp_port of this ProtectionServeInfo.

        RASP端口号

        :return: The rasp_port of this ProtectionServeInfo.
        :rtype: int
        """
        return self._rasp_port

    @rasp_port.setter
    def rasp_port(self, rasp_port):
        r"""Sets the rasp_port of this ProtectionServeInfo.

        RASP端口号

        :param rasp_port: The rasp_port of this ProtectionServeInfo.
        :type rasp_port: int
        """
        self._rasp_port = rasp_port

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
        if not isinstance(other, ProtectionServeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
