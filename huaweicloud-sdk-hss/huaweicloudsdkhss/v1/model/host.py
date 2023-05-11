# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Host:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_id': 'str',
        'host_id': 'str',
        'host_name': 'str',
        'host_ip': 'str',
        'public_ip': 'str',
        'enterprise_project_name': 'str',
        'group_name': 'str',
        'expire_time': 'int',
        'policy_group_name': 'str',
        'host_status': 'str',
        'agent_status': 'str',
        'version': 'str',
        'protect_status': 'str',
        'os_image': 'str',
        'os_type': 'str',
        'os_bit': 'str',
        'detect_result': 'str',
        'risk_port_num': 'int',
        'risk_vul_num': 'int',
        'risk_intrusion_num': 'int',
        'risk_baseline_num': 'int',
        'charging_mode': 'str',
        'resource_id': 'str'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'host_id': 'host_id',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'public_ip': 'public_ip',
        'enterprise_project_name': 'enterprise_project_name',
        'group_name': 'group_name',
        'expire_time': 'expire_time',
        'policy_group_name': 'policy_group_name',
        'host_status': 'host_status',
        'agent_status': 'agent_status',
        'version': 'version',
        'protect_status': 'protect_status',
        'os_image': 'os_image',
        'os_type': 'os_type',
        'os_bit': 'os_bit',
        'detect_result': 'detect_result',
        'risk_port_num': 'risk_port_num',
        'risk_vul_num': 'risk_vul_num',
        'risk_intrusion_num': 'risk_intrusion_num',
        'risk_baseline_num': 'risk_baseline_num',
        'charging_mode': 'charging_mode',
        'resource_id': 'resource_id'
    }

    def __init__(self, agent_id=None, host_id=None, host_name=None, host_ip=None, public_ip=None, enterprise_project_name=None, group_name=None, expire_time=None, policy_group_name=None, host_status=None, agent_status=None, version=None, protect_status=None, os_image=None, os_type=None, os_bit=None, detect_result=None, risk_port_num=None, risk_vul_num=None, risk_intrusion_num=None, risk_baseline_num=None, charging_mode=None, resource_id=None):
        """Host

        The model defined in huaweicloud sdk

        :param agent_id: 云主机id
        :type agent_id: str
        :param host_id: 云主机id
        :type host_id: str
        :param host_name: 云主机名称
        :type host_name: str
        :param host_ip: 云主机私有IP
        :type host_ip: str
        :param public_ip: 云主机公网IP
        :type public_ip: str
        :param enterprise_project_name: 所属企业项目名称
        :type enterprise_project_name: str
        :param group_name: 服务器组名称
        :type group_name: str
        :param expire_time: 服务到期时间
        :type expire_time: int
        :param policy_group_name: 策略组名称
        :type policy_group_name: str
        :param host_status: Agent状态，包含如下4种。   - ACTIVE ：正在运行。   - SHUTOFF ：关机。   - BUILDING ：创建中。   - ERROR ：故障。
        :type host_status: str
        :param agent_status: Agent状态，包含如下3种。   - uninstall ：未注册。   - online ：在线。   - offline ：离线。
        :type agent_status: str
        :param version: 主机开通的版本，包含如下5种输入。   - hss.version.null ：无。   - hss.version.basic ：基础版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。
        :type version: str
        :param protect_status: 防护状态，包含如下2种。 - closed ：关闭。 - opened ：开启。
        :type protect_status: str
        :param os_image: 系统镜像
        :type os_image: str
        :param os_type: 系统类型
        :type os_type: str
        :param os_bit: 操作系统位数
        :type os_bit: str
        :param detect_result: 云主机安全检测结果，包含如下3种。 - undetect ：未检测。 - clean ：无风险。 - risk ：有风险。
        :type detect_result: str
        :param risk_port_num: 资产风险个数
        :type risk_port_num: int
        :param risk_vul_num: 漏洞风险个数
        :type risk_vul_num: int
        :param risk_intrusion_num: 入侵风险个数
        :type risk_intrusion_num: int
        :param risk_baseline_num: 基线风险个数
        :type risk_baseline_num: int
        :param charging_mode: 收费模式，包含如下2种。   - packet_cycle ：包年/包月。   - on_demand ：按需。
        :type charging_mode: str
        :param resource_id: 云服务资源实例ID（UUID）
        :type resource_id: str
        """
        
        

        self._agent_id = None
        self._host_id = None
        self._host_name = None
        self._host_ip = None
        self._public_ip = None
        self._enterprise_project_name = None
        self._group_name = None
        self._expire_time = None
        self._policy_group_name = None
        self._host_status = None
        self._agent_status = None
        self._version = None
        self._protect_status = None
        self._os_image = None
        self._os_type = None
        self._os_bit = None
        self._detect_result = None
        self._risk_port_num = None
        self._risk_vul_num = None
        self._risk_intrusion_num = None
        self._risk_baseline_num = None
        self._charging_mode = None
        self._resource_id = None
        self.discriminator = None

        if agent_id is not None:
            self.agent_id = agent_id
        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if host_ip is not None:
            self.host_ip = host_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if enterprise_project_name is not None:
            self.enterprise_project_name = enterprise_project_name
        if group_name is not None:
            self.group_name = group_name
        if expire_time is not None:
            self.expire_time = expire_time
        if policy_group_name is not None:
            self.policy_group_name = policy_group_name
        if host_status is not None:
            self.host_status = host_status
        if agent_status is not None:
            self.agent_status = agent_status
        if version is not None:
            self.version = version
        if protect_status is not None:
            self.protect_status = protect_status
        if os_image is not None:
            self.os_image = os_image
        if os_type is not None:
            self.os_type = os_type
        if os_bit is not None:
            self.os_bit = os_bit
        if detect_result is not None:
            self.detect_result = detect_result
        if risk_port_num is not None:
            self.risk_port_num = risk_port_num
        if risk_vul_num is not None:
            self.risk_vul_num = risk_vul_num
        if risk_intrusion_num is not None:
            self.risk_intrusion_num = risk_intrusion_num
        if risk_baseline_num is not None:
            self.risk_baseline_num = risk_baseline_num
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if resource_id is not None:
            self.resource_id = resource_id

    @property
    def agent_id(self):
        """Gets the agent_id of this Host.

        云主机id

        :return: The agent_id of this Host.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this Host.

        云主机id

        :param agent_id: The agent_id of this Host.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def host_id(self):
        """Gets the host_id of this Host.

        云主机id

        :return: The host_id of this Host.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this Host.

        云主机id

        :param host_id: The host_id of this Host.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        """Gets the host_name of this Host.

        云主机名称

        :return: The host_name of this Host.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this Host.

        云主机名称

        :param host_name: The host_name of this Host.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        """Gets the host_ip of this Host.

        云主机私有IP

        :return: The host_ip of this Host.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """Sets the host_ip of this Host.

        云主机私有IP

        :param host_ip: The host_ip of this Host.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def public_ip(self):
        """Gets the public_ip of this Host.

        云主机公网IP

        :return: The public_ip of this Host.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this Host.

        云主机公网IP

        :param public_ip: The public_ip of this Host.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def enterprise_project_name(self):
        """Gets the enterprise_project_name of this Host.

        所属企业项目名称

        :return: The enterprise_project_name of this Host.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        """Sets the enterprise_project_name of this Host.

        所属企业项目名称

        :param enterprise_project_name: The enterprise_project_name of this Host.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def group_name(self):
        """Gets the group_name of this Host.

        服务器组名称

        :return: The group_name of this Host.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this Host.

        服务器组名称

        :param group_name: The group_name of this Host.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def expire_time(self):
        """Gets the expire_time of this Host.

        服务到期时间

        :return: The expire_time of this Host.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this Host.

        服务到期时间

        :param expire_time: The expire_time of this Host.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def policy_group_name(self):
        """Gets the policy_group_name of this Host.

        策略组名称

        :return: The policy_group_name of this Host.
        :rtype: str
        """
        return self._policy_group_name

    @policy_group_name.setter
    def policy_group_name(self, policy_group_name):
        """Sets the policy_group_name of this Host.

        策略组名称

        :param policy_group_name: The policy_group_name of this Host.
        :type policy_group_name: str
        """
        self._policy_group_name = policy_group_name

    @property
    def host_status(self):
        """Gets the host_status of this Host.

        Agent状态，包含如下4种。   - ACTIVE ：正在运行。   - SHUTOFF ：关机。   - BUILDING ：创建中。   - ERROR ：故障。

        :return: The host_status of this Host.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        """Sets the host_status of this Host.

        Agent状态，包含如下4种。   - ACTIVE ：正在运行。   - SHUTOFF ：关机。   - BUILDING ：创建中。   - ERROR ：故障。

        :param host_status: The host_status of this Host.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def agent_status(self):
        """Gets the agent_status of this Host.

        Agent状态，包含如下3种。   - uninstall ：未注册。   - online ：在线。   - offline ：离线。

        :return: The agent_status of this Host.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        """Sets the agent_status of this Host.

        Agent状态，包含如下3种。   - uninstall ：未注册。   - online ：在线。   - offline ：离线。

        :param agent_status: The agent_status of this Host.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def version(self):
        """Gets the version of this Host.

        主机开通的版本，包含如下5种输入。   - hss.version.null ：无。   - hss.version.basic ：基础版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。

        :return: The version of this Host.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Host.

        主机开通的版本，包含如下5种输入。   - hss.version.null ：无。   - hss.version.basic ：基础版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。

        :param version: The version of this Host.
        :type version: str
        """
        self._version = version

    @property
    def protect_status(self):
        """Gets the protect_status of this Host.

        防护状态，包含如下2种。 - closed ：关闭。 - opened ：开启。

        :return: The protect_status of this Host.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        """Sets the protect_status of this Host.

        防护状态，包含如下2种。 - closed ：关闭。 - opened ：开启。

        :param protect_status: The protect_status of this Host.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def os_image(self):
        """Gets the os_image of this Host.

        系统镜像

        :return: The os_image of this Host.
        :rtype: str
        """
        return self._os_image

    @os_image.setter
    def os_image(self, os_image):
        """Sets the os_image of this Host.

        系统镜像

        :param os_image: The os_image of this Host.
        :type os_image: str
        """
        self._os_image = os_image

    @property
    def os_type(self):
        """Gets the os_type of this Host.

        系统类型

        :return: The os_type of this Host.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this Host.

        系统类型

        :param os_type: The os_type of this Host.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def os_bit(self):
        """Gets the os_bit of this Host.

        操作系统位数

        :return: The os_bit of this Host.
        :rtype: str
        """
        return self._os_bit

    @os_bit.setter
    def os_bit(self, os_bit):
        """Sets the os_bit of this Host.

        操作系统位数

        :param os_bit: The os_bit of this Host.
        :type os_bit: str
        """
        self._os_bit = os_bit

    @property
    def detect_result(self):
        """Gets the detect_result of this Host.

        云主机安全检测结果，包含如下3种。 - undetect ：未检测。 - clean ：无风险。 - risk ：有风险。

        :return: The detect_result of this Host.
        :rtype: str
        """
        return self._detect_result

    @detect_result.setter
    def detect_result(self, detect_result):
        """Sets the detect_result of this Host.

        云主机安全检测结果，包含如下3种。 - undetect ：未检测。 - clean ：无风险。 - risk ：有风险。

        :param detect_result: The detect_result of this Host.
        :type detect_result: str
        """
        self._detect_result = detect_result

    @property
    def risk_port_num(self):
        """Gets the risk_port_num of this Host.

        资产风险个数

        :return: The risk_port_num of this Host.
        :rtype: int
        """
        return self._risk_port_num

    @risk_port_num.setter
    def risk_port_num(self, risk_port_num):
        """Sets the risk_port_num of this Host.

        资产风险个数

        :param risk_port_num: The risk_port_num of this Host.
        :type risk_port_num: int
        """
        self._risk_port_num = risk_port_num

    @property
    def risk_vul_num(self):
        """Gets the risk_vul_num of this Host.

        漏洞风险个数

        :return: The risk_vul_num of this Host.
        :rtype: int
        """
        return self._risk_vul_num

    @risk_vul_num.setter
    def risk_vul_num(self, risk_vul_num):
        """Sets the risk_vul_num of this Host.

        漏洞风险个数

        :param risk_vul_num: The risk_vul_num of this Host.
        :type risk_vul_num: int
        """
        self._risk_vul_num = risk_vul_num

    @property
    def risk_intrusion_num(self):
        """Gets the risk_intrusion_num of this Host.

        入侵风险个数

        :return: The risk_intrusion_num of this Host.
        :rtype: int
        """
        return self._risk_intrusion_num

    @risk_intrusion_num.setter
    def risk_intrusion_num(self, risk_intrusion_num):
        """Sets the risk_intrusion_num of this Host.

        入侵风险个数

        :param risk_intrusion_num: The risk_intrusion_num of this Host.
        :type risk_intrusion_num: int
        """
        self._risk_intrusion_num = risk_intrusion_num

    @property
    def risk_baseline_num(self):
        """Gets the risk_baseline_num of this Host.

        基线风险个数

        :return: The risk_baseline_num of this Host.
        :rtype: int
        """
        return self._risk_baseline_num

    @risk_baseline_num.setter
    def risk_baseline_num(self, risk_baseline_num):
        """Sets the risk_baseline_num of this Host.

        基线风险个数

        :param risk_baseline_num: The risk_baseline_num of this Host.
        :type risk_baseline_num: int
        """
        self._risk_baseline_num = risk_baseline_num

    @property
    def charging_mode(self):
        """Gets the charging_mode of this Host.

        收费模式，包含如下2种。   - packet_cycle ：包年/包月。   - on_demand ：按需。

        :return: The charging_mode of this Host.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this Host.

        收费模式，包含如下2种。   - packet_cycle ：包年/包月。   - on_demand ：按需。

        :param charging_mode: The charging_mode of this Host.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def resource_id(self):
        """Gets the resource_id of this Host.

        云服务资源实例ID（UUID）

        :return: The resource_id of this Host.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this Host.

        云服务资源实例ID（UUID）

        :param resource_id: The resource_id of this Host.
        :type resource_id: str
        """
        self._resource_id = resource_id

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
        if not isinstance(other, Host):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
